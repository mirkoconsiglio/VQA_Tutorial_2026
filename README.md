# QALYPSO VQA LECTURES

A tutorial on variational quantum algorithms (VQAs), which leverage both quantum and
classical resources to solve optimisation problems.

We walk through the Variational Quantum Eigensolver and use it to determine the
ground-state energy of the hydrogen molecule, then map out the full dissociation curve
of H$_2$ on a simulator.

## Contents

| Notebook            | Topic | Approx. time |
|---------------------|---|---|
| `1_Intro.ipynb`     | Complexity classes, the NISQ era, and the four modules of a VQA: objective function, parametrised circuit, measurement, classical optimiser | 45 min |
| `2_VQE.ipynb`       | Building a working VQE on a two-qubit Hamiltonian, convergence, comparing optimisers | 45 min |
| `3_Ising.ipynb` | The transverse-field Ising model: $\mathbb{Z}_2$ symmetry and spontaneous symmetry breaking, the exact free-fermion solution via Jordan–Wigner, the Hamiltonian Variational Ansatz, VQE across a quantum phase transition, and entanglement entropy at criticality | 95–105 min |
| `4_Chemistry.ipynb` | Where the Hamiltonian comes from: molecular integrals, second quantisation, the Jordan–Wigner transformation, $\mathbb{Z}_2$ symmetry tapering, problem-inspired ansätze, and the H$_2$ dissociation curve | 90 min |
 

### What notebook 3 covers
 
1. **The model.** Ferromagnetic coupling against a transverse field, and the two limits it interpolates between.
2. **Symmetry.** $[\hat H, \prod_j \hat X_j] = 0$, and why the finite-size ground state is a cat state rather than a symmetry-broken one. The doublet splitting is shown to vanish exponentially with $N$.
3. **Exact solution.** Jordan–Wigner run in the opposite direction to the usual quantum-chemistry use: spins to fermions, where the model becomes free. Includes the parity term on the closing bond of the ring and the two momentum sectors it produces. The diagonalisation is then set out in four steps — expand the brackets, Fourier transform, reduce each momentum pair to a two-level problem, fill the ground state. The dispersion $\varepsilon_k = 2J\sqrt{1+g^2-2g\cos k}$ is quoted rather than derived, with references for anyone who wants the algebra, and then verified against exact diagonalisation to machine precision.
4. **Hamiltonian Variational Ansatz.** $2p$ parameters, symmetry-preserving by construction. Students find numerically that it becomes exact at $p = N/2$, and the light-cone argument for why.
5. **VQE across the transition.** The central result: at $p=2$ on 8 spins the energy error at criticality is under 3%, which looks respectable, while the order parameter is wrong by a factor of 16. Energy is local and forgiving; correlations are not.
6. **Entanglement.** The $\ln 2$ plateau of the cat state, the peak at criticality, and a fit that recovers the Ising CFT central charge $c = 1/2$ to about a percent.
Notebook 3 assumes notebooks 1 and 2 have been covered. It is aimed at physics students
and expects second quantisation at the level of an undergraduate quantum mechanics
course. Section 3 is the longest at roughly 30 minutes; section 6 is the natural one to
drop if you are running short of time.

### What notebook 4 covers

1. **Electronic structure.** Born-Oppenheimer, STO-3G, and what the one- and two-electron integrals are. Loads them from the shipped .npz, so nobody installs PySCF during your session.
2. **Second quantisation.** The anticommutation relations doing the work of antisymmetry.
3. **Jordan-Wigner.** Students implement a_p as Pauli strings, then assemble the 15-term four-qubit Hamiltonian. Exercise 1 is verifying {a_p, a_q†} = δ_pq numerically. The payoff: the lowest eigenvalue matches FCI to 1.3×10⁻¹⁵ Ha.
4. **Symmetry tapering.** Exercise 2 confirms [H, Z₀Z₁] = 0, then Bravyi-style tapering to two qubits, still exact.
5. **Problem-inspired ansatz.** The ground state lives in span{|00⟩,|11⟩}, so Ry(θ) plus a CNOT is exact. One parameter, so you can plot the entire cost landscape, which is a nice foil for the barren-plateau figure in notebook 1.
6. **Dissociation curve.** Rebuild the Hamiltonian at each of 42 bond lengths, warm-start from the previous geometry, plot against HF and FCI with an error panel.
 
### Exercises and solutions
 
Places for participants to write code are marked `YOUR CODE HERE`. Each is followed by a
worked solution in a **collapsed cell**: it shows up as a thin clickable bar, and
expands when clicked. The code inside stays fully runnable while hidden.
 
This uses the standard `jupyter.source_hidden` cell metadata, which JupyterLab and
Notebook 7 (what `pip install notebook` gives you) understand natively. No extension is
needed. The classic Notebook 6 interface ignores it and will show the solutions
expanded, so run the tutorial in Notebook 7 or Lab.
 
Every solution cell also carries a `solution` tag, so you can strip them out completely
for a handout version:
 
```bash
jupyter nbconvert --to notebook \
  --TagRemovePreprocessor.enabled=True \
  --TagRemovePreprocessor.remove_cell_tags solution \
  3_Ising.ipynb --output 3_Ising_exercises.ipynb
```
 
Everything runs on a laptop with no data files and no external downloads: the model is
defined by two numbers. The longest cell is the parameter sweep in section 5, at roughly
half a minute.
 
## Installing these notebooks
 
1. Go to the directory you want to download the repository on using the terminal.
2. You can run `git clone https://github.com/mirkoconsiglio/VQA_tutorial.git` in your
   specified directory.
3. Then `cd VQA_tutorial`.
4. Create a virtual environment using either `virtualenv VQA_tutorial` or
   `conda create --name VQA_tutorial python=3.12` if you have Conda installed.
5. If you installed with `virtualenv` then run `source VQA_tutorial/bin/activate`, or
   `conda activate VQA_tutorial` if you used Conda.
6. Then run `pip install -r requirements.txt`.
7. Run `jupyter notebook` in your terminal.
Run the version-check cell at the top of `1_Intro.ipynb` to confirm the install worked.

## Data

For notebook 4: `data/h2_sto3g.npz` holds the one- and two-electron integrals for H$_2$ in the STO-3G
basis at 42 bond lengths from 0.3 to 3.0 Å, together with Hartree–Fock and full
configuration interaction reference energies. It is about 5 kB and ships with the
repository, so participants do not need to install a quantum chemistry package.

To regenerate it, or to produce data for a different molecule or basis:

```bash
pip install pyscf
cd data && python generate_integrals.py
```
