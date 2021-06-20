This repository contains the code and data for the paper 'Learning from Docked Ligands: Ligand-Based Features Rescue Structure-Based Scoring Functions When Trained On Docked Poses' (10.26434/chemrxiv.13637756.v1).

- Data - binding affinity data, computed features, and other inputs.
- Results - predicted binding affinity values, computed correlation coefficients, and other outputs.
- Figures - figures generated for the paper/SI.
- Notebooks - calculations were run in Jupyter notebooks. Note that some calculations, such as computation of PLEC fingerprints, are quite intensive - do not expect to be able to run thme in five minutes on a laptop!
- Scripts - scripts used to access ChEMBL and and compute ligand Tanimoto similarity.

Due to their large size, files under ./data are tracked by git-lfs. To clone the repository including these files, you'll need to install [git-lfs](https://git-lfs.github.com/). You can then clone the repository as usual by running git clone.

### Data sets

There are two data sets used in this paper - the PDBbind Refined Set and our Updated DUD-E Diverse Subset. The latter consists of six targets taken from the DUD-E Diverse Subset - AKT1, CP3A4, GCR, HIVPR, HIVRT and KIF11 - with ligands and binding affinity data for each target extracted from ChEMBL version 25. We have made this data set available so that others can use it their own experiments. The following files provided in the /data/ directory:

\<target\>_\<chembl_id>_extracted_data.csv - ligand binding data extracted from ChEMBL version 25 for \<target\>; \<chembl_id\> denotes the ChEMBL target ID used to query the database.<\br>
\<target\>\_KI\_clean.csv - binding affinity values (in pK units) for the ligands of \<target\>, indexed by ligand ChEMBL ID.<\br>
\<target\>\_KI\_docked\_features.json - Python dictionary containing RF-Score v3 features computed using docked poses of the ligands of \<target\>. Keys are of the form \<ligand chembl id\>\_\<docked pose number\>.<\br>
\<target\>\_KI\_rdkit\_descriptors.json - Python dictionary containing RDKit 2D molecular descriptors computed for the ligands of \<target\>. Keys are ligand ChEMBL IDs.<\br>

These files are used by the notebook 'dud-e\_chembl.ipynb' to produce the results presented in Table 5.

We have also made the docked poses used to compute these features freely available on Figshare: https://doi.org/10.6084/m9.figshare.13713226.v1

