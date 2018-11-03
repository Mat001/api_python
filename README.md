## API mini test framework in Python.

Demonstration of API calls/tests on a test website and on real Salesforce API

### Instructions to run

1. ###### Prerequisites
    
    `install pipenv`

2. ###### Run tests
    
    `python -W ignore -m unittest discover -v`

Things to improve:
- to use a better API with a database to be able to test patching, updating and deleting
- Docker is optional, doesn't add value at the moment as test logs are only visible 
inside the container (logs) 
