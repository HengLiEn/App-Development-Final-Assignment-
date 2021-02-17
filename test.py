import shelve
# db = shelve.open('GoFit.db', 'r')
# freq_dict = db['freq']
# db.close()

db = shelve.open('GoFit.db','c')
db['Review']={}
db.close()


