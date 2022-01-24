module parameters

! This module contains all the modifiable parameters for 
! the suite of ps f90 files.

 !Domain grid dimensions:
integer,parameter:: nx=512, ny=64

 !Domain width in x and limits in y:
double precision,parameter:: ellx=51200d0
double precision,parameter:: ymin=0.d0,ymax=6400d0

 !Simulation duration and data save interval:
double precision,parameter:: tsim=900.d0,tgsave=10.d0
 
 !Hyperviscosity parameters:
integer,parameter:: nnu=3
double precision,parameter:: prediss=10.d0
! Damping rate is prediss*zeta_rms*(k/k_max)^(2*nnu) on wavenumber
! k where k_max is the maximum x or y wavenumber and zeta_rms is
! the rms vorticity. Note: nnu = 3 and prediss = 10 are recommended.

end module