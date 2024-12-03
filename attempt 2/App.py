from flask import Flask, render_template, request, jsonify
import csv
import random
import json

app = Flask(__name__)

# Load the questions from the JSON file
with open('questions.json') as json_file:
    question_db = json.load(json_file)

@app.route('/get_questions', methods=['GET'])
def get_questions():
    course_interest = request.args.get('course')
    if course_interest in question_db:
        questions = []
        for level in ['beginner', 'intermediate', 'expert']:
            questions.extend(question_db[course_interest].get(level, []))
        return jsonify(questions)
    return jsonify([]), 404

# Function to determine the user's skill level based on the score
def determine_skill_level(score):
    if score <= 2:
        return "beginner"
    elif 3 <= score <= 5:
        return "intermediate"
    else:
        return "expert"
    
def recommend_modules(course_interest, skill_level, csv_file='all_courses_updated_dataset.csv'):
    recommended_modules = []

    # Log the course and skill level
    print(f"Recommending modules for course: {course_interest}, Skill Level: {skill_level}")

    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Ensure the course name matches the user's selected course
            if course_interest.lower() in row['course_name'].lower():
                # Log each module being checked
                # print(f"Checking module: {row['course_name']} with difficulty: {row['difficulty_level']}")
                print(skill_level,row['course_level'])
                # Adjust filtering logic based on skill level and difficulty
                if skill_level == 'beginner' and row['course_level'].lower() == 'beginner'  and row['difficulty_level'] in ['Easy', 'Medium', 'Hard']:
                    print(f"Matched for beginner: {row}")
                    recommended_modules.append({ 
                        'module_name': row['module_name'],
                        'difficulty': row['difficulty_level'],
                        'link': row['link']
                    })
                elif skill_level == 'intermediate' and row['difficulty_level'] in ['Medium', 'Hard']:
                    print(f"Matched for intermediate: {row}")
                    recommended_modules.append({
                        'module_name': row['module_name'],
                        'difficulty': row['difficulty_level'],
                        'link': row['link']
                    })
                elif skill_level == 'expert' and row['difficulty_level'] == 'Hard':
                    print(f"Matched for expert: {row}")
                    recommended_modules.append({
                        'module_name': row['module_name'],
                        'difficulty': row['difficulty_level'],
                        'link': row['link']
                    })

    # Log the final recommended modules
    print(f"Recommended modules: {recommended_modules}")

    return recommended_modules

# Route to handle quiz submission and return skill level + recommendations
@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    data = request.get_json()
    course_interest = data['course']
    user_answers = data['answers']

    # Calculate the user's score
    score = sum(1 for answer in user_answers if answer['user_option'] == answer['correct_option'])

    # Determine the user's skill level based on the score
    skill_level = determine_skill_level(score)

    # Get recommended modules based on the course interest and skill level
    recommended = recommend_modules(course_interest, skill_level)
    
    # Return the skill level, score, and recommended modules to the frontend
    return jsonify({
        'skill_level': skill_level,
        'recommended_modules': recommended,
        'score': score
    })
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)