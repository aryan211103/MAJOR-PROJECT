import csv
import pymongo

# Connect to MongoDB (adjust the URI if you're using a remote MongoDB instance)
client = pymongo.MongoClient('mongodb+srv://aryanhirlekar25:k2lWf343NcI8xxOt@cluster0.nk1zh.mongodb.net/?retryWrites=true&w=majority')
db = client['studentdata']  # Replace with your database name
users_collection = db['student']  # Replace with your collection name

# Create a new database (if not already existing) called recommendation_system
db = client["recommendation_system"]

# Create a new collection for modules
modules_collection = db["modules"]

# Path to your CSV file
csv_file_path = 'all_courses_updated_dataset.csv'

# Read the CSV file and insert each row as a document into MongoDB
with open(csv_file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    # Clear the existing collection (optional: in case you're running this multiple times)
    modules_collection.delete_many({})
    
    # Iterate through each row in the CSV and insert it into the MongoDB collection
    for row in csv_reader:
        # Convert the row into a dictionary and insert into the collection
        modules_collection.insert_one({
            "course_name": row['course_name'],
            "module_name": row['module_name'],
            "difficulty_level": row['difficulty_level'],
            "course_level": row['course_level'],  # Beginner, Intermediate, or Expert
            "learning_link": row['link']  # Link to resources
        })

print("Data successfully inserted into MongoDB.")