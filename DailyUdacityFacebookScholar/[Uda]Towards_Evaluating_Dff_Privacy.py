'''
Does the output of a query 'leaking' privacy?
- whether the output of a query changes when we remove someone from the dataset?
'''
def create_db_and_parallels(n_entries):
    db = torch.rand(n_entries)>0.5
    pds = rmv_db(db)

    return db, pds


db, pdbs = create_db_and_parallels(5000)

def query(db):
    return db.float().mean()

full_db_result = query(db) # return the (sum of the 1's/5000)

sensitivity = 0
for pdb in pdbs: # for each parallel database which has been removed one entry by each
    pdb_result = query(pdb)
    db_distance = torch.abs(pdb_result - full_db_result)

    if (db_distance > sensitivity):
        sensitivity = db_distance


# above, calculating the max value into a function format

def cal_sensitivity(query, n = 1000):

    db, pdbs = create_db_and_parallels(n)
    full_db_result = query(db)

    sensitivity = 0
    for pdb in pdbs:
        pdb_result = query(pdb)
        db_distance = torch.abs(pdb_result-full_db_result)
        if(db_distance > sensitivity):
            sensitivity = db_distance

    return sensitivity
