'''
Flask Application
'''
from flask import Flask, jsonify, request
from models import Experience, Education, Skill

app = Flask(__name__)

data = {
    "experience": [
        Experience("Software Developer",
                   "A Cool Company",
                   "October 2022",
                   "Present",
                   "Writing Python Code",
                   "example-logo.png")
    ],
    "education": [
        Education("Computer Science",
                  "University of Tech",
                  "September 2019",
                  "July 2022",
                  "80%",
                  "example-logo.png")
    ],
    "skill": [
        Skill("Python",
              "1-2 Years",
              "example-logo.png")
    ]
}


@app.route('/test')
def hello_world():
    '''
    Returns a JSON test message
    '''
    return jsonify({"message": "Hello, World!"})


@app.route('/resume/experience', methods=['GET', 'POST'])
def experience():
    '''
    Handle experience requests
    '''
    if request.method == 'GET':
        return jsonify(data['experience'])

    if request.method == 'POST':
        experience_data = request.get_json()
        new_experience = Experience(
            experience_data['title'],
            experience_data['company'],
            experience_data['start_date'],
            experience_data['end_date'],
            experience_data['description'],
            experience_data['logo']
        )
        data['experience'].append(new_experience)
        return jsonify({"index": len(data['experience']) - 1}), 201

    return jsonify({"error": "Method not allowed"}), 405

@app.route('/resume/experience/<int:index>', methods=['GET'])
def get_experience_by_index(index):
    '''
    Get a specific experience by index
    '''
    try:
        experience = data['experience'][index]
        return jsonify(experience)
    except IndexError:
        return jsonify({"error": "Experience not found"}), 404

@app.route('/resume/education', methods=['GET', 'POST'])
def education():
    '''
    Handles education requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})


@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})
