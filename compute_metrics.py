"""
Metric definitions used in the manuscript.
"""
import numpy as np

def nmse(u_pred, u_true):
    err = u_pred-u_true
    return np.sum(err**2)/(np.sum(u_true**2)+1e-12)

def correlation(u_pred, u_true):
    a=u_pred.ravel(); b=u_true.ravel()
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)+1e-12)

def divergence(u,dx):
    ux,uy=u[...,0],u[...,1]
    return ((np.roll(ux,-1,0)-np.roll(ux,1,0)) +
            (np.roll(uy,-1,1)-np.roll(uy,1,1)))/(2*dx)

def enstrophy(u,dx):
    ux,uy=u[...,0],u[...,1]
    dvx=(np.roll(uy,-1,0)-np.roll(uy,1,0))/(2*dx)
    duy=(np.roll(ux,-1,1)-np.roll(ux,1,1))/(2*dx)
    omega=dvx-duy
    return 0.5*np.mean(omega**2)