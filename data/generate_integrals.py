"""Generate the molecular integral data used by 3_Chemistry.ipynb.

This is the only part of the tutorial that needs PySCF. The output file
(h2_sto3g.npz, about 5 kB) ships with the repository so that participants do not
have to install a quantum chemistry package during the session.

    pip install pyscf
    python generate_integrals.py

For each geometry it stores, in the Hartree-Fock molecular orbital basis:

    h1     (M, M)          one-electron integrals h_pq
    eri    (M, M, M, M)    two-electron integrals (pq|rs), chemists' notation
    e_nuc                  nuclear repulsion energy
    e_hf                   restricted Hartree-Fock energy   (reference)
    e_fci                  full configuration interaction   (exact in this basis)

Everything is in Hartree; bond lengths are in Angstrom.
"""

import numpy as np
from pyscf import gto, scf, fci, ao2mo


def molecular_integrals(atom, basis="sto-3g"):
    """Run RHF + FCI and return the integrals in the MO basis."""
    mol = gto.M(atom=atom, basis=basis, unit="Angstrom", verbose=0)
    mf = scf.RHF(mol).run()

    c = mf.mo_coeff
    h1 = c.T @ mf.get_hcore() @ c
    eri = ao2mo.restore(1, ao2mo.kernel(mol, c), c.shape[1])

    e_fci = fci.FCI(mf).kernel()[0]
    return h1, eri, mol.energy_nuc(), mf.e_tot, e_fci


def main(path="h2_sto3g.npz"):
    # Dense sampling around equilibrium, coarser out towards dissociation.
    # 0.735 A is included explicitly: it is the STO-3G equilibrium bond length
    # and the geometry the notebook uses by default.
    bond_lengths = np.unique(np.round(np.concatenate([
        np.arange(0.30, 1.60, 0.05),
        np.arange(1.60, 3.05, 0.10),
        [0.735],
    ]), 4))

    h1s, eris, e_nucs, e_hfs, e_fcis = [], [], [], [], []
    for r in bond_lengths:
        h1, eri, e_nuc, e_hf, e_fci = molecular_integrals(f"H 0 0 0; H 0 0 {r}")
        h1s.append(h1)
        eris.append(eri)
        e_nucs.append(e_nuc)
        e_hfs.append(e_hf)
        e_fcis.append(e_fci)

    np.savez_compressed(
        path,
        bond_lengths=bond_lengths,
        h1=np.array(h1s),
        eri=np.array(eris),
        e_nuc=np.array(e_nucs),
        e_hf=np.array(e_hfs),
        e_fci=np.array(e_fcis),
    )

    i = int(np.argmin(e_fcis))
    print(f"wrote {path}: {len(bond_lengths)} geometries, "
          f"{bond_lengths[0]}-{bond_lengths[-1]} A")
    print(f"  minimum FCI energy {e_fcis[i]:.6f} Ha at R = {bond_lengths[i]} A")


if __name__ == "__main__":
    main()
