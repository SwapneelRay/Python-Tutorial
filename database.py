import dbm

db = dbm.open('caption','c')

db['cblogo.png'] = 'logo photo new'

for key in db:
    print(key,db[key])
    
db.close()