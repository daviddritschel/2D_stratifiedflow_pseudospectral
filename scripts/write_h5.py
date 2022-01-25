import h5py
import numpy as np
import os
from ps_config import nx, ny, ellx, ymin, ymax

print(nx, ny, ellx, ymin, ymax)
exit()

params = {
    'nx':   256,
    'ny':   384,
    'ellx': 1000.0,
    'ymin': 0.0,
    'ymax': 1500
}

nx = int(params['nx'])
ny = int(params['ny'])

#-----------------------------------------------------------------
# Open ene.asc file in one directory to get time between frames:
in_file=open('evolution/ecomp.asc','r')
time, ekin, epot, etot = np.loadtxt(in_file,dtype=float,unpack=True)
in_file.close()
nt = len(time)

dset = {
    'bb': 'buoyancy',
    'zz': 'vorticity'
}

N = nx * (ny + 1)

h5file = h5py.File('ps_fields.hdf5', 'w')

h5file.attrs['nsteps'] = nt

box = h5file.create_group('box')
box.attrs['extent'] = (params['ellx'], params['ymax'] - params['ymin'])
box.attrs['origin'] = (-params['ellx'] * 0.5, params['ymin'])
box.attrs['ncells'] = (np.int32(nx), np.int32(ny))

for frame in range(nt):
    group = h5file.create_group('step#' + str(frame).zfill(10))

    for field in ['bb', 'zz']:
        fname = os.path.join('evolution', field + '.r4')

        in_file = open(fname,'r')
        raw_array = np.fromfile(in_file,dtype=np.float32)
        in_file.close()

        Z = np.empty([nx, ny+1])
        Z = raw_array[frame*(N+1)+1:(frame+1)*(N+1)].reshape(nx, ny+1)

        group[dset[field]] = np.float64(Z.copy())

h5file.close()