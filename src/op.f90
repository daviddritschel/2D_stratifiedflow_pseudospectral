module parameters

! This module contains all the modifiable parameters for 
! the suite of ps f90 files.

 !Domain grid dimensions:
integer,parameter:: nx=N_X,ny=N_Y

 !Domain width in x and limits in y:
double precision,parameter:: ellx=L_X
double precision,parameter:: ymin=Y_MIN,ymax=Y_MAX

 !Simulation duration and data save interval:
double precision,parameter:: tsim=T_SIM,tgsave=T_GSAVE
 
 !Hyperviscosity parameters:
integer,parameter:: nnu=N_NU
double precision,parameter:: prediss=PRE_DISS
! Damping rate is prediss*zeta_rms*(k/k_max)^(2*nnu) on wavenumber
! k where k_max is the maximum x or y wavenumber and zeta_rms is
! the rms vorticity. Note: nnu = 3 and prediss = 10 are recommended.

end module
