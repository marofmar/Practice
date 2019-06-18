# flip two coins: generaate 1/0

# report both the true query and noised query for database size 10, 100, 1000, 10,000

def create_db_and_parallels(n_entries):
    db = torch.rand(n_entries)>0.5
    pds = rmv_db(db)
    return db, pds

def query(db):
    true_result = torch.mean(db.float())
    first_coin_flip = (torch.rand(len(db))>0.5).float()
    second_coin_flip = (torch.rand(len(db))>0.5).float()
    augmented_db = db.float()*first_coin_flip + (1-first_coin_flip)*second_coin_flip
    private_result = torch.mean(augmented_db.float())
    true_result = torch.mean(augmented_db.float()) * 2 -0.5

    return private_result, true_result

db, pdbs = create_db_and_parallels(1000)
private_result, ture_result = query(db)
print("With Noise: ", private_result)
print("Without Noise: ", true_result)

db, pdbs = create_db_and_parallels(100000)
private_result, ture_result = query(db)
print("With Noise: ", private_result)
print("Without Noise: ", true_result)
