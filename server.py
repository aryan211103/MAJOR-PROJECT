from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from bson import ObjectId  # Used for handling MongoDB ObjectIDs
from flask_cors import CORS  # To handle CORS issues

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Connect to MongoDB Atlas
client = MongoClient('mongodb+srv://aryanhirlekar25:k2lWf343NcI8xxOt@cluster0.nk1zh.mongodb.net/?retryWrites=true&w=majority')
db = client['studentdata']  # Replace with your database name
users_collection = db['student']  # Replace with your collection name

# Route to render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and insert data into MongoDB
@app.route('/submit', methods=['POST'])
def create_user():
    try:
        # Get the data from the request body (JSON format)
        new_user = request.json
        
        # Insert the new user data into MongoDB
        users_collection.insert_one(new_user)
        
        return jsonify({'message': 'User Created'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all users and display on the webpage
@app.route('/view-data', methods=['GET'])
def view_data():
    try:
        users = list(users_collection.find())
        for user in users:
            user['_id'] = str(user['_id'])  # Convert ObjectId to string for JSON serialization
        return render_template('view_data.html', users=users)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask server
if __name__ == '__main__':
    app.run(port=5000, debug=True)
