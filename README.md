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
| `3_Ising.ipynb`     | The transverse-field Ising model: $\mathbb{Z}_2$ symmetry and spontaneous symmetry breaking, the exact free-fermion solution via Jordan–Wigner, the Hamiltonian Variational Ansatz, VQE across a quantum phase transition, and entanglement entropy at criticality | 90–100 min |
| `4_Chemistry.ipynb` | Where the Hamiltonian comes from: molecular integrals, second quantisation, the Jordan–Wigner transformation, $\mathbb{Z}_2$ symmetry tapering, problem-inspired ansätze, and the H$_2$ dissociation curve | 90 min |

Notebooks 3 and 4 are self-contained but assumes notebooks 1 and 2 have been covered. It is
aimed at physics students and expects familiarity with second quantisation at the level
of an undergraduate quantum mechanics course; no prior quantum chemistry is assumed.

Exercises are marked `YOUR CODE HERE` and each is followed by a cell marked
`# Solution`.

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
