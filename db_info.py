from pymongo import MongoClient

config={
    "host":"localhost",
    "port":27017,
    "username":"",
    "password":""
}

class Connection:
    def __new__(cls, database):
        connection=MongoClient(**config)
        return connection[database]
    
#Above via URL => https://obikastanya.medium.com/flask-mongodb-validate-your-data-using-json-schema-178f7e676df5