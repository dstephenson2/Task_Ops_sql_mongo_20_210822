from flask import Flask, request, jsonify
import pymongo # pip install pymongo

# create an app
app = Flask(__name__)

# create and establish a connection with mongo
client = pymongo.MongoClient("mongodb+srv://FSDS_mongodb:FSDS_mongo_db@cluster0.fhmxaie.mongodb.net/?retryWrites=true&w=majority")

# create a database i.e a folder, inside this database ull have a table i.e. a file, which will carry actual data
database = client['task4ops']
# create a collection(table) inside this database, the way we create tables, procedures in mysql; collection is bunch of documents/data
collection = database["taskcollection"] # only once we insert data the database will be created in mongo, else though we run the command at this point it will not be created

@app.route("/insert/mongo" , methods=['POST'])
def insert():
    if (request.method == 'POST'):
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name:number})
        return jsonify(str('Inserted Successfully'))


if __name__ == '__main__':
    app.run(port=5001) # already sql.py is running on 5000, hence postman is throwing an error