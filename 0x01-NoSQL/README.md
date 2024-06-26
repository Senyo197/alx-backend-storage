# 0x01. NoSQL

wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org
...
sudo service mongod status
mongod start/running, process 3627
mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
 
pip3 install pymongo
python3
import pymongo
pymongo.__version__
'3.10.1'
Potential issue if documents creation doesn’t work or this error: Data directory /data/db not found., terminating (source and source)

sudo mkdir -p /data/db
Or if /etc/init.d/mongod is missing, please find here an example of the file:

## 0. List all databases
mandatory
Write a script that lists all databases in MongoDB.
  
## 1. Create a database
mandatory
Write a script that creates or uses the database my_db:

## 2. Insert document
mandatory
Write a script that inserts a document in the collection school:

The document must have one attribute name with value “Holberton school”
The database name will be passed as option of mongo command
  
## 3. All documents
mandatory
Write a script that lists all documents in the collection school:

The database name will be passed as option of mongo command
  
## 4. All matches
mandatory
Write a script that lists all documents with name="Holberton school" in the collection school:

The database name will be passed as option of mongo command
  
## 5. Count
mandatory
Write a script that displays the number of documents in the collection school:

The database name will be passed as option of mongo command
  
## 6. Update
mandatory
Write a script that adds a new attribute to a document in the collection school:

The script should update only document with name="Holberton school" (all of them)
The update should add the attribute address with the value “972 Mission street”
The database name will be passed as option of mongo command
  
## 7. Delete by match
mandatory
Write a script that deletes all documents with name="Holberton school" in the collection school:

The database name will be passed as option of mongo command
  
## 8. List all documents in Python
mandatory
Write a Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
  
## 9. Insert a document in Python
mandatory
Write a Python function that inserts a new document in a collection based on kwargs:

Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
Returns the new _id
  
## 10. Change school topics
mandatory
Write a Python function that changes all topics of a school document based on the name:

Prototype: def update_topics(mongo_collection, name, topics):
mongo_collection will be the pymongo collection object
name (string) will be the school name to update
topics (list of strings) will be the list of topics approached in the school
  
## 11. Where can I learn Python?
mandatory
Write a Python function that returns the list of school having a specific topic:

Prototype: def schools_by_topic(mongo_collection, topic):
mongo_collection will be the pymongo collection object

## 12. Log stats
mandatory
Write a Python script that provides some stats about Nginx logs stored in MongoDB:

- Database: logs
- Collection: nginx
Display (same as the example):
- first line: x logs where x is the number of documents in this collection
	- second line: Methods:
		- 5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it’s a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
You can use this dump as data sample: dump.zip

The output of your script must be exactly the same as the example
