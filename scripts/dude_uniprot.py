import json

dude_chembl = {
    'AKT1': ['CHEMBL4282'],
    'CP3A4': ['CHEMBL340'],
    'GCR': ['CHEMBL2034'],
    'HIVPR': ['CHEMBL243'],
    'HIVRT': ['CHEMBL247'],
    'KIF11': ['CHEMBL4581']
}

with open('../data/dude_chembl_ids.json', 'w') as f:
    json.dump(dude_chembl, f)

