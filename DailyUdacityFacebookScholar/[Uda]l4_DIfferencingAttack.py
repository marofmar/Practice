# Project: Perform a Differncing Attack on Row 10
def create_db_and_parallels(n_entries):
    db = torch.rand(n_entries)>0.5
    pds = rmv_db(db)
    return db, pds

db, _ = create_db_and_parallels(100)
pdb = get_paralle_db(db, remove_index = 10)

# differencing attack using sum query
sum(db) - sum(pdb)
# differencing attack using mean query
(sum(db).float()/len(db)) - (sum(pdb).float()/len(pdb))
# differencing attack using threshold
(sum(db).float()>49)-(sum(pdb).float()>49)
