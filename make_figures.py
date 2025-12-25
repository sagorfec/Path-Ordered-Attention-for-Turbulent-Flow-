"""
Generate journal-ready figures from diagnostic .mat files.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from matplotlib.backends.backend_pdf import PdfPages

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman','Times','DejaVu Serif']

files = {
    "Baseline":"data/diag_baseline.mat",
    "PaTH":"data/diag_path.mat",
    "RoPE":"data/diag_rope.mat"
}

metrics={}
for k,v in files.items():
    metrics[k]=loadmat(v)

t = np.arange(len(metrics["Baseline"]["nmse_mean"].squeeze())) * float(metrics["Baseline"]["dt"])

with PdfPages("figures/figures_journal.pdf") as pdf:
    # NMSE
    fig,ax=plt.subplots(figsize=(8,4.5))
    for k in metrics:
        m=metrics[k]["nmse_mean"].squeeze()
        s=metrics[k]["nmse_std"].squeeze()
        ax.plot(t,m,label=k); ax.fill_between(t,m-s,m+s,alpha=0.25)
    ax.set_xlabel("time"); ax.set_ylabel("NMSE"); ax.grid(); ax.legend()
    pdf.savefig(fig); plt.close(fig)

    # Correlation
    fig,ax=plt.subplots(figsize=(8,4.5))
    for k in metrics:
        m=metrics[k]["rho_mean"].squeeze()
        s=metrics[k]["rho_std"].squeeze()
        ax.plot(t,m,label=k); ax.fill_between(t,m-s,m+s,alpha=0.25)
    ax.set_xlabel("time"); ax.set_ylabel("ρ(t)"); ax.grid(); ax.legend()
    pdf.savefig(fig); plt.close(fig)

print("Figures written to figures/figures_journal.pdf")