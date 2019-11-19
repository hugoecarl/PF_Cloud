import pymongo

connection = pymongo.MongoClient('localhost', 27017)

database = connection['mydb_1']

collection = database['mycol_1']

data = {
        'title': u'Hugo Carl',
        'description': u'Programa Python',
        'done': False
    }
data1 = {
        'title': u'Gabriel M',
        'description': u'Banco de dados SQL',
        'done': False
    }

collection.insert_one(data)
collection.insert_one(data1)

for i in collection.find({}):
    print(i)
