#!/usr/bin/env python

import argparse
import h5py
import numpy as np
import os
from ps_config import nx, ny, ellx, ymin, ymax

ev_dir = ''
saveas = ''

try:
    parser = argparse.ArgumentParser(description="Generate H5 output file.")

    required = parser.add_argument_group('required arguments')

    parser.add_argument("--evolution-dir",
                        type=str,
                        required=True,
                        help="evolution directory")

    parser.add_argument("--saveas",
                        type=str,
                        required=True,
                        help="name of file to be saved")

    args = parser.parse_args()

    ev_dir = args.evolution_dir
    saveas = args.saveas
except Exception as ex:
    print(ex)

print("Parameters from parameters.f90:")
print("nx   = ", nx)
print("ny   = ", ny)
print("ellx = ", ellx)
print("ymin = ", ymin)
print("ymax = ", ymax)

#-----------------------------------------------------------------
# Open ene.asc file in one directory to get time between frames:
in_file=open(os.path.join(ev_dir, 'ecomp.asc'),'r')
time, ekin, epot, etot = np.loadtxt(in_file,dtype=float,unpack=True)
in_file.close()
nt = len(time)

dset = {
    'bb': 'buoyancy',
    'zz': 'vorticity'
}

N = nx * (ny + 1)

h5file = h5py.File(saveas + '.hdf5', 'w')

dt = h5py.string_dtype('ascii', 6)

h5file.attrs.create("output_type", r"fields", dtype=dt, shape=1)

h5file.attrs['nsteps'] = [nt]

box = h5file.create_group('box')
box.attrs['extent'] = (ellx, ymax - ymin)
box.attrs['origin'] = (-ellx * 0.5, ymin)
box.attrs['ncells'] = (np.int32(nx), np.int32(ny))

for frame in range(nt):
    group = h5file.create_group('step#' + str(frame).zfill(10))

    group.attrs['t'] = time[frame]

    for field in ['bb', 'zz']:
        fname = os.path.join(ev_dir, field + '.r4')

        in_file = open(fname,'r')
        raw_array = np.fromfile(in_file,dtype=np.float32)
        in_file.close()

        Z = np.empty([nx, ny+1])
        Z = raw_array[frame*(N+1)+1:(frame+1)*(N+1)].reshape(nx, ny+1)

        group[dset[field]] = np.float64(Z.copy())

h5file.close()
