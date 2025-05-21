'''
Tests in Pytest
'''
from app import app


def test_client():
    '''
    Makes a request and checks the message received is the same
    '''
    response = app.test_client().get('/test')
    assert response.status_code == 200
    assert response.json['message'] == "Hello, World!"


def test_experience():
    '''
    Add a new experience and then get all experiences. 
    
    Check that it returns the new experience in that list
    '''
    example_experience = {
        "title": "Software Developer",
        "company": "A Cooler Company",
        "start_date": "October 2022",
        "end_date": "Present",
        "description": "Writing JavaScript Code",
        "logo": "example-logo.png"
    }

    item_id = app.test_client().post('/resume/experience',
                                     json=example_experience).json['id']
    response = app.test_client().get('/resume/experience')
    assert response.json[item_id] == example_experience


def test_education():
    '''
    Test the /resume/education POST and GET endpoints.

    - Ensure an empty payload returns a 400 error.
    - Ensure missing required fields return a 400 error.
    - Successfully add a valid education entry.
    - Confirm the entry is correctly returned via GET.
    '''
    empty_education = {}
    missing_education = {
        "course": "Engineering",
        "school": "NYU",
        "end_date": "August 2024",
        "grade": "86%",
        "logo": "example-logo.png"
    }
    example_education = {
        "course": "Engineering",
        "school": "NYU",
        "start_date": "October 2022",
        "end_date": "August 2024",
        "grade": "86%",
        "logo": "example-logo.png"
    }

    client = app.test_client()

    # Test empty payload:
    response = client.post('/resume/education', json=empty_education)
    assert response.status_code == 400
    assert response.json['error'] == "No data provided"

    # Test missing field:
    response = client.post('/resume/education', json=missing_education)
    assert response.status_code == 400
    assert response.json['error'] == "Missing required fields"

    # Test valid education:
    response = client.post('/resume/education', json=example_education)
    assert response.status_code == 201
    item_id = response.json['id']
    assert isinstance(item_id, int)
    assert item_id == 1

    # Test retrieval:
    # TODO: The GET endpoint needs to be implemented in `app.py` for this to pass. # pylint: disable=fixme
    response = client.get('/resume/education')
    assert response.status_code == 200
    assert response.json[item_id] == example_education

def test_skill():
    '''
    Add a new skill and then get all skills. 
    
    Check that it returns the new skill in that list
    '''
    example_skill = {
        "name": "JavaScript",
        "proficiency": "2-4 years",
        "logo": "example-logo.png"
    }

    item_id = app.test_client().post('/resume/skill',
                                     json=example_skill).json['id']

    response = app.test_client().get('/resume/skill')
    assert response.json[item_id] == example_skill
