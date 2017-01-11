from numpy import *
from scipy import *
from pylab import *
from shutil import copy
from os import mkdir

def lininc(n,Dx,dx0):
  a=(Dx-n*dx0)*2./n/(n+1)
  print a
  dx = dx0+arange(1.,n+1.,1.)*a
  return dx

Fr=0.13/6.
H = 2000.
h0=500.
om = 2.*pi/12.42/3600.
N0=5.2e-3
u0=Fr*N0*h0


outdir='dataHs%04d' % (10000*Fr)
try:
  mkdir(outdir)
except:
  print outdir+' Exists'
copy('gendata.py',outdir)

ny = 1
nx = 8*188
nz = 200


# y direction:
dy = 1000

# x direction
xt = 410e3

nmid = 100.
dx0=50.
nleft = (nx-nmid)/2
nright = (nx-nmid)/2
dx = zeros(nx)
dxleft = flipud(lininc(nleft,200.e3,dx0))
dxright = lininc(nright,200.e3,dx0)
dx[0:nleft]=dxleft
dx[(nleft):(nleft+nmid)]=dx0
dx[(nleft+nmid):]=dxright
x=cumsum(dx)
x = x-x[nx/2]

with open(outdir+"/delXvar", "wb") as f:
	dx.tofile(f)
f.close()
plot(x/1000.,dx)
xlim([-10,10])
savefig(outdir+'/dx.pdf')

# topo
sigma = 10000. # m

topo = 1500*exp(-x*x/(sigma**2))-1500+h0
#topo = h0*exp(-x*x/(3000**2))
print shape(topo)
topo[topo<0.]=0.
topo=-H+topo
topo[topo<-H]=-H
clf()
plot(x/1.e3,topo)
xlim([-20.,20.])
savefig(outdir+'/topo.pdf')


with open(outdir+"/topo.bin", "wb") as f:
	topo.tofile(f)
f.close()
# dz:
# dz is from the surface down (right?).  Its saved as positive.

dz=zeros(nz)+H/nz

with open(outdir+"/delZvar", "wb") as f:
	dz.tofile(f)
f.close()

# temperature profile...
g=9.8
alpha = 2e-4
T0 = 28+cumsum(N0**2/g/alpha*(-dz))

with open(outdir+"/TRef.bin", "wb") as f:
	T0.tofile(f)
f.close()
z=cumsum(dz)

clf()
plot(T0,z)
savefig(outdir+'/TO.pdf')

print u0

# Forcing for boundaries
dt=1240.
time = arange(0,12.*12.4*3600.-100.,dt)
print shape(time)
om = 2*pi/12.40/3600;
print u0
uw = u0*sin(om*time)
a=pow(tanh((time)/3600./10.),1.)
a=a/max(a);
uw=uw*a
uw[0]=0.
uw[-1]=0.
uw[-2]=0.
uw[-3]=0.

g = 9.81
cbt = sqrt(g*H)
timee=time-(x[-14]-x[14])/cbt;
ue = u0*sin(om*(timee))
#a=(tanh((timee)/3600./5.))
a=a/max(a)
ue=ue*a
ue[-1]=0.
ue[0]=0.
ue[-1]=0.
ue[-2]=0.
ue[-3]=0.
clf()
plot(time/3600./12.4,ue,label='Ue')
plot(time/3600/12.4,uw,label='Uw')
legend()
xlabel('t/T')
ylabel('Vel')
title('%d' % time[-1])
savefig(outdir+'/Vels.pdf')
print shape(time)
print time[-1]+dt

# try time,nz,ny...

uen=zeros((shape(time)[0],nz,ny))
for j in range(0,ny):
  for i in range(0,nz):
    uen[:,i,j]=ue
print shape(uen)

uwn=zeros((shape(time)[0],nz,ny))
print shape(uwn)
for j in range(0,ny):
  for i in range(0,nz):
    uwn[:,i,j]=uw
print shape(uen)
          
with open(outdir+"/Ue%04d.obcs" % (Fr*10000), "wb") as f:
  uen.tofile(f)

with open(outdir+"/Uw%04d.obcs" % (Fr*10000), "wb") as f:
  uwn.tofile(f)



t=zeros((shape(time)[0],nz,ny))
for j in range(0,ny):
	for i in range(0,nz):
		for k in range(0,shape(time)[0]):
			t[k,i,j]=T0[i]
print shape(t)
with open(outdir+"/Te.obcs", "wb") as f:
	t.tofile(f)
f.close()
with open(outdir+"/Tw.obcs", "wb") as f:
	t.tofile(f)
f.close()

###  Make data.obcs and put into this directory....
with  open("data.obcs0100") as fin:
  with open(outdir+"/data.obcs", "wt") as fout:
    for line in fin:
      fout.write( line.replace('0100', '%04d'% (Fr*10000)) )
fin.close()
fout.close()

## Copy some other files
import shutil 

shutil.copy('dataHy5', outdir+'/data')
shutil.copy('eedata', outdir)
shutil.copy('data.pp81', outdir)
shutil.copy('data.diagnostics', outdir)
shutil.copy('data.pkgKL', outdir+'/data.pkg')
