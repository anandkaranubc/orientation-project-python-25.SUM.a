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
        return jsonify()

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

@app.route('/resume/education', methods=['GET', 'POST'])
def education():
    """
    Handle GET and POST requests for education entries.

    Returns
    -------
    Response
        JSON response containing all education entries (GET) or the index of a new entry (POST).
    """
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        content = request.json
        if not content:
            return jsonify({"error": "No data provided"}), 400
        if not all(key in content for key in ['course', 'school', 'start_date', 'end_date', 'grade', 'logo']):
            return jsonify({"error": "Missing required fields"}), 400
        new_education = Education(
            content['course'],
            content['school'],
            content['start_date'],
            content['end_date'],
            content['grade'],
            content['logo']
        )
        data['education'].append(new_education)
        return jsonify({"id": len(data['education']) - 1}), 201

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
