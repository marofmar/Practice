import torch

num_entries = 5000
db = torch.rand(num_entries) >0.5 # 0,1 # DEBUG:



# 1. remove an entry function
def rmv_ent(db, n):
    b = torch.cat([db[:n], db[n+1:]])
    return # BUG:

# 2. iterate through whole database
def rmv_db(db):
    tmp = []
    for i in range(len(db)):
        tmp.append(rmv_ent(db, i))
    return tmp


# 3. merge above two functions together
def create_db_and_parallels(n_entries):
    db = torch.rand(n_entries)>0.5
    pds = rmv_db(db)

    return db, pds
