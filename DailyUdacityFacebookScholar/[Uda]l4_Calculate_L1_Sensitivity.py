# Project3
'''
- Create the query() function
- Create 10 databases of size 10
- Query each database with a threshold of 5 (calculate sensitivity)
- Print out the sensitivity of each database
'''
def create_db_and_parallels(n_entries):
    db = torch.rand(n_entries)>0.5
    pds = rmv_db(db)
    return db, pds

def query(db, threshold = 5):
    return (db.sum() > threshold).float()


db, pdb = create_db_and_parallels(10)

def sensitivity(query, n = 1000):

    db, pdbs = create_db_and_parallels(n)
    full_db_result = query(db)

    sensitivity = 0
    for pdb in pdbs:
        pdb_result = query(pdb)
        db_distance = torch.abs(pdb_result-full_db_result)
        if(db_distance > sensitivity):
            sensitivity = db_distance

    return sensitivity

for i in range(len(pdb)):
    sen_f = sensitivity(query, n= 10)
    print(sens_f)
