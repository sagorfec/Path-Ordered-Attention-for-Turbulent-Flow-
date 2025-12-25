# Multiscale Diagnostics for Learning Turbulent Flow Dynamics

This repository contains **reproducible Python code and MATLAB-compatible data**
for generating the figures used in a ScienceDirect / APS-style manuscript on
machine-learned turbulence modeling.

The project provides:
- Multiseed **mean ± std** diagnostics
- Spectral error analysis
- Enstrophy and divergence consistency checks
- Scale-dependent NMSE (large vs small scales)
- Journal-ready PDF figures

---

## Authors

**Authors:**  
[Md. Ifthakhar Khan Sagor]¹*, [Md. Zillur Rahman]², [Partha Mandal]³  

**Affiliations:**  
¹ ² ³ Department of Electrical and Electronics Engineering,  
Faridpur Engineering College,  
Char Kamlapur, Faridpur, 7800, Bangladesh  

**Corresponding Author:**  
*Email:* ifthakhar.eee@fec.edu.bd  
*Phone:* +88-01521-409907  

---

## Repository Structure

```
turbulence_ml_figures_project/
│
├── README.md
├── requirements.txt
├── generate_data.py
├── compute_metrics.py
├── make_figures.py
│
├── data/
│   ├── diag_baseline.mat
│   ├── diag_path.mat
│   └── diag_rope.mat
│
└── figures/
    └── figures_journal.pdf
```

---

## Usage

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. (Optional) Regenerate synthetic data
```bash
python generate_data.py
```

### 3. Generate figures
```bash
python make_figures.py
```

This will reproduce and save them to `figures/`.

---

## Notes for Reviewers

- Diagnostics are averaged over multiple random seeds.
- Shaded regions indicate **±1 standard deviation**.
- Spectral slopes and error growth are consistent with reported findings.
- MATLAB users can load `.mat` files directly without modification.

---

## License

This code is released for **academic and research use**.