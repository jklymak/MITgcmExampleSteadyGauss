
import numpy as np
import matplotlib.pyplot as plt
from shutil import copy
from os import mkdir
import os

def lininc(n, Dx, dx0):
  a =(Dx-n*dx0)*2./n/(n+1)
  dx = dx0 + np.arange(1., n+1., 1.)*a
  return dx

Fr = 0.13
H = 2000.
h0 = 500.
om = 2 * np.pi/12.42/3600.
N0 = 5.2e-3
u0 = Fr*N0*h0

outdir = f'../runs/RunFr{int(10_000 * Fr):03d}'

# These must match ../code/SIZE.h
ny = 1
nx = 4*20
nz = 25

# y direction:
dy = 1000
# x direction
xt = 410e3

nmid = 50
dx0 = 300.
nleft = int((nx-nmid)/2)
print(nleft)
nright = int((nx-nmid)/2)
dx = np.zeros(nx)
dxleft = np.flipud(lininc(nleft,200.e3,dx0))
dxright = lininc(nright,200.e3,dx0)
dx[0:nleft]=dxleft
dx[(nleft):(nleft+nmid)]=dx0
dx[(nleft+nmid):]=dxright
x = np.cumsum(dx)
x = x - x[int(np.floor(nx/2))]

## set up output directory
## Copy some other files
import shutil

if os.path.exists(outdir+'.bak'):
  shutil.rmtree(outdir+'.bak')
if os.path.exists(outdir):
  shutil.move(outdir, outdir+'.bak')

os.mkdir(outdir)
os.mkdir(outdir+'/input')
os.mkdir(outdir+'/input/figs')
os.mkdir(outdir+'/indata')
os.mkdir(outdir+'/build')

shutil.copy('data', outdir+'/input/data')
shutil.copy('eedata', outdir + '/input/')
shutil.copy('data.kl10', outdir+'/input/')
shutil.copy('data.mnc', outdir+'/input/')
shutil.copy('data.obcs', outdir+'/input/')
shutil.copy('data.diagnostics', outdir+'/input/')
shutil.copy('data.pkg', outdir+'/input/data.pkg')
shutil.copy('gendata.py', outdir+'/input/')
shutil.copy('../build/mitgcmuv', outdir+'/build')
shutil.copy('../build/Makefile', outdir+'/build/Makefile')
# also store these.  They are small and helpful to document what we did
for nm in {'code','build_options','analysis'}:
    to_path = outdir+'/'+nm
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree('../'+nm, outdir+'/'+nm)

with open(outdir + "/indata/delXvar.bin", "wb") as f:
    dx.tofile(f)
f.close()
# plot
if True:
    fig, ax = plt.subplots()
    ax.plot(x/1000., dx)
    ax.set_xlim([-10, 10])
    fig.savefig(outdir + '/input/figs/dx.pdf')

# topo
sigma = 4000. # m

topo = 1500 * np.exp(-x*x/(sigma**2))-1500+h0
#topo = h0*exp(-x*x/(3000**2))
topo[topo<0.]=0.
topo=-H+topo
topo[topo<-H]=-H

# plot
if True:
    fig, ax = plt.subplots()
    ax.plot(x/1.e3,topo)
    # xlim([-20.,20.])
    fig.savefig(outdir + '/input/figs/topo.pdf')

with open(outdir+"/indata/topo.bin", "wb") as f:
	topo.tofile(f)

# dz:
# dz is from the surface down (right?).  Its saved as positive.
dz = np.zeros(nz)+H/nz
with open(outdir+"/indata/delZvar.bin", "wb") as f:
	dz.tofile(f)

# temperature profile...
g=9.8
alpha = 2e-4
T0 = 28 + np.cumsum(N0**2/g/alpha*(-dz))
with open(outdir+"/indata/TRef.bin", "wb") as f:
  T0.tofile(f)

# save T0 over whole domain
TT0 = np.tile(T0, nx).T

with open(outdir+"/indata/T0.bin", "wb") as f:
	TT0.tofile(f)


z = np. cumsum(dz)
# plot:
if True:
    fig, ax = plt.subplots()
    ax.plot(T0,z)
    fig.savefig(outdir+'/input/figs/TO.pdf')

# Forcing for boundaries
dt=3720.
time = np.arange(0, 12.*3720, dt)

om = 2 * np.pi / 12.40 / 3600;
uw = u0+0.*time
ue = u0+0.*time
# plot:
if True:
    fig, ax = plt.subplots()
    ax.plot(time/3600./12.4,ue,label='Ue')
    ax.plot(time/3600/12.4,uw,label='Uw')
    ax.legend()
    ax.set_xlabel('t/T')
    ax.set_ylabel('Vel')
    ax.set_title('%d' % time[-1])
    fig.savefig(outdir+'/input/figs/Vels.pdf')

# try time,nz,ny...
uen = np.zeros((np.shape(time)[0], nz, ny))
for j in range(0, ny):
  for i in range(0, nz):
    uen[:, i, j] = ue
#print(uen)

uwn = np.zeros((np.shape(time)[0], nz, ny))
for j in range(0, ny):
  for i in range(0, nz):
    uwn[:, i, j] = uw
#print(uwn)

with open(outdir+"/indata/Ue.bin", "wb") as f:
  uen.tofile(f)

with open(outdir+"/indata/Uw.bin", "wb") as f:
  uwn.tofile(f)

t = np.zeros((np.shape(time)[0], nz, ny))
for j in range(0,ny):
  for i in range(0,nz):
	  for k in range(0, np.shape(time)[0]):
	    t[k, i, j] = T0[i]
with open(outdir+"/indata/Te.bin", "wb") as f:
	t.tofile(f)
f.close()
with open(outdir+"/indata/Tw.bin", "wb") as f:
	t.tofile(f)
f.close()

