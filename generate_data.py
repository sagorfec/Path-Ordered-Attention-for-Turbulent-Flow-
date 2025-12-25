"""
Generate synthetic divergence-free velocity fields and prediction rollouts.
Outputs MATLAB-compatible .mat files.
"""
import numpy as np
from scipy.io import savemat

nx = ny = 64
nt = 200
Ntest = 8
dt = 0.01
L = 2*np.pi
dx = L/nx
kf = 4

def divergence_free_field():
    psi = np.random.randn(nx, ny)
    u = np.zeros((nx, ny, 2))
    u[...,0] = (np.roll(psi,-1,1)-np.roll(psi,1,1))/(2*dx)
    u[...,1] =-(np.roll(psi,-1,0)-np.roll(psi,1,0))/(2*dx)
    return u

u_true = np.zeros((nx,ny,nt,Ntest,2))
u_pred = np.zeros_like(u_true)

for n in range(Ntest):
    u0 = divergence_free_field()
    for t in range(nt):
        phase = 0.15*t
        u_true[:,:,t,n,0] = np.cos(phase)*u0[...,0] - np.sin(phase)*u0[...,1]
        u_true[:,:,t,n,1] = np.sin(phase)*u0[...,0] + np.cos(phase)*u0[...,1]
        growth = 0.02 + 0.0008*t
        noise = growth*np.random.randn(nx,ny,2)
        u_pred[:,:,t,n,:] = u_true[:,:,t,n,:] + noise

savemat("data/sim_predictions.mat", {
    "u_true":u_true,"u_pred":u_pred,
    "dt":dt,"dx":dx,"L":L,"kf":kf
}, do_compression=True)

print("Synthetic data saved to data/sim_predictions.mat")