from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem
from rdkit import RDLogger
RDLogger.DisableLog('rdApp.*')

import json
import sys

if __name__=='__main__':
    pdbbind_dir = sys.argv[1]
    training_set_file = sys.argv[2]
    test_set_file = sys.argv[3]
    with open(training_set_file) as f:
        training_set = [line.strip() for line in f]
    with open(test_set_file) as f:
        test_set = [line.strip() for line in f]

    mols_to_load = training_set.extend(test_set)

    mols = {}
    fingerprints = {}
    for pdb in mols_to_load:
        sdf = f'{pdbbind_dir}/{pdb}/{pdb}_ligand.sdf'
        mol = next(Chem.SDMolSupplier(sdf))
        if mol is None:
            mol2 = f'{pdbbind_dir}/{pdb}/{pdb}_ligand.mol2'
            mol = Chem.MolFromMol2File(mol2)
        mols[pdb] = mol
        fingerprints[pdb] = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=2048)

    tanimoto_similarity = {}

    for pdb_test in test_set:
        tanimoto_similarity[pdb_test] = {}
        for pdb_train in training_set:
            tanimoto_similarity[pdb_test][pdb_train] = DataStructs.FingerprintSimilarity(fingerprints[pdb_test], fingerprints[pdb_train])
    with open('../data/ligand_tanimoto_similarity.json') as f:
        json.dump(tanimoto_similarity, f)