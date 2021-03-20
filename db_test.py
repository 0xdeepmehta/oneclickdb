from pymongo import MongoClient 
from pymongo import ReturnDocument 
    
# Create a pymongo client 
client = MongoClient('localhost', 27017) 
  
# Get the database instance 
db = client['test_lol'] 
  
# Create a collection 
doc = db['Student'] 

doc.insert_one({'name': 'Raju'})
print("lol")
print(doc.find_one_and_update({'name':"Raju"}, { '$set': { "Branch" : 'pop'} })) 
