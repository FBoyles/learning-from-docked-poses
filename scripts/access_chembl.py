import json
import sqlite3
import pandas as pd

connection = sqlite3.connect("/home/fergus/chembl_25/chembl_25_sqlite/chembl_25.db")
print("Connected to db")

cursor = connection.cursor()

with open('../data/dude_chembl_ids.json') as f:
    dude_chembl_ids = json.load(f)

for target in dude_chembl_ids:

    print(target)

    for i in dude_chembl_ids[target]:
        print(i)

        qtext = f"""
        SELECT
          activities.standard_value            AS standard_value,
          activities.data_validity_comment     AS data_validity_comment,
          activities.potential_duplicate       AS potential_duplicate,
          assays.confidence_score              AS confidence_score,
          compound_structures.canonical_smiles AS canonical_smiles,
          molecule_dictionary.chembl_id        AS chembl_id
        FROM activities
          JOIN assays ON activities.assay_id = assays.assay_id
          JOIN target_dictionary ON assays.tid = target_dictionary.tid
          JOIN target_components ON target_dictionary.tid = target_components.tid
          JOIN component_class ON target_components.component_id = component_class.component_id
          JOIN protein_family_classification ON component_class.protein_class_id = protein_family_classification.protein_class_id
          JOIN molecule_dictionary ON activities.molregno = molecule_dictionary.molregno
          JOIN molecule_hierarchy ON molecule_dictionary.molregno = molecule_hierarchy.molregno
          JOIN compound_structures ON molecule_hierarchy.parent_molregno = compound_structures.molregno
        WHERE activities.standard_units = 'nM' AND
              activities.standard_type = 'Ki' AND
              activities.standard_relation = '=' AND
              target_dictionary.target_type = 'SINGLE PROTEIN' AND
              target_dictionary.chembl_id = '{i}'
        """

        print("Executing query")
        cursor.execute(qtext)
        print("Query executed")

        print("Getting data")
        results = cursor.fetchall()
        print("Got data")

        names = list(map(lambda x: x[0], cursor.description))
        all_data = pd.DataFrame(results, columns=names)

        all_data.to_csv(f"../data/{target}_{i}_extracted_chembl_data.csv")

cursor.close()

connection.close()
