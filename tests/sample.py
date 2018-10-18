# TODO use this site to test against: https://reqres.in/

# TODO implement POLLING - for requests/responses that take longer
# https://pypi.org/project/polling/
# https://medium.com/@justiniso/using-the-polling-module-in-python-87052d7da4d9
# maybe polling is built in in requests already?
# you want to poll if resource is not yet available (otherwise response will be 404)


# TODO ADD UNITTEST CLASS SUITE


import requests
import json

BASE_URL = 'https://reqres.in'


##############################################
# GET - get
##############################################
def get():
    print('# ===================================')
    print('# GET')
    print('# ===================================')
    params = {'page': 2}
    response1 = requests.get(BASE_URL + '/api/users', params=params, timeout=(10, 10))
    pretty = json.dumps(response1.json(), indent=4)     # a string
    print(pretty)


get()

##############################################
# POST - create
##############################################
def post():
    """ Required to post/create:

        1. resource - endpoint (/api/users)
        2. payload (data to post)
        3. use POST method
        4. response should be 201
        5. expected response should be known - see json file below

    Expected response:
    {
        "name": "morpheus",
        "job": "leader",
        "id": "299",
        "createdAt": "2018-10-17T20:58:54.814Z"
    }"""
    print('# ===================================')
    print('# POST')
    print('# ===================================')

    payload = {
        "name": "morpheusx",
        "job": "leader"
    }

    post_new = requests.post(BASE_URL + '/api/users', data=payload, timeout=(10, 10))  # payload is json, but it gets automatically converted into dict here
    print(post_new.status_code)
    print(json.dumps(post_new.json(), indent=4))
    d = post_new.json()

    assert d['name'] == payload['name']
    assert d['job'] == payload['job']

    # TODO test that new is different from previous - test site may not be able to provide for that
    #   assert that original list of user didn't include new entry
    #   assert current list of users includes new entry


post()

##############################################
# PUT - update
##############################################
def put():
    """
    Expected response:
    {
    "name": "morpheus",
    "job": "zion resident",
    "updatedAt": "2018-10-17T21:33:30.161Z"
    }"""
    print('# ===================================')
    print('# PUT')
    print('# ===================================')

    payload = {
        "name": "morpheusx",
        "job": "zion resident"
    }

    post_new = requests.put(BASE_URL + '/api/users/2', data=payload, timeout=(10, 10))  # payload is json, but it gets automatically converted into dict here
    print(post_new.status_code)
    print(json.dumps(post_new.json(), indent=4))
    d = post_new.json()

    assert d['name'] == payload['name']
    assert d['job'] == payload['job']

    # TODO test that new is different from previous - test site may not be able to provide for that
    #   assert that original user has old "job"
    #   assert current user has "new" job


put()

##############################################
# PATCH - update
##############################################
"""body = json.dumps({u"body": u"Sounds great! I'll get right on it once I feed my cat."})
>>> url = u"https://api.github.com/repos/requests/requests/issues/comments/5804413"

>>> r = requests.patch(url=url, data=body, auth=auth)"""
def patch():
    """
    Expected response:
    {
    "name": "morpheus",
    "job": "zion resident_patched",
    "updatedAt": "2018-10-17T21:33:30.161Z"
    }"""
    print('# ===================================')
    print('# PATCH')
    print('# ===================================')


    payload = {
        "name": "morpheusx",
        "job": "zion resident_patched"
    }

    post_new = requests.put(BASE_URL + '/api/users/2', data=payload, timeout=(10, 10))  # payload is json, but it gets automatically converted into dict here
    print(post_new.status_code)
    print(json.dumps(post_new.json(), indent=4))
    d = post_new.json()

    assert d['name'] == payload['name']
    assert d['job'] == payload['job']

    # TODO test that new is different from previous - test site may not be able to provide for that
    #   assert that original user has old "job"
    #   assert current user has "new" job


patch()




##############################################
# DELETE - delete
##############################################
def delete():
    print('# ===================================')
    print('# DELETE')
    print('# ===================================')

    remove = requests.delete(BASE_URL + '/api/users/2', timeout=(10, 10))  # payload is json, but it gets automatically converted into dict here
    print(remove.status_code)

    assert remove.status_code == 204
    # TODO assert deleted entry is no longer in the original data

delete()


##############################################
# AUTHENTICATION - BASIC POST CREDENTIALS
##############################################
def auth1():
    """Expected response:
    {
    "token": "QpwL5tke4Pnpja7X"
    }
    """

    print('# ===================================')
    print('# POST - BASIC AUTHENTICATION')
    print('# ===================================')

    credentials = {
        "email": "sydney@fife",
        "password": "pistol"
    }

    authentication = requests.post(BASE_URL + '/api/register', data=credentials, timeout=(10, 10))
    print(authentication.status_code)
    print(json.dumps(authentication.json(), indent=4))
    d = authentication.json()

    # assert d['name'] == payload['name']


auth1()

##############################################
# AUTHENTICATION - USING REQUESTS'HTTPBasicAuth
##############################################
def auth2():
    """Expected response:
    {
    "token": "QpwL5tke4Pnpja7X"
    }
    """
    import re

    print('# ===================================')
    print('# POST - BASIC AUTHENTICATION')
    print('# ===================================')

    # create a session object, we need to persist data over two pages(?)
    session = requests.session()

    # get login page text
    page = session.get('https://opensource-demo.orangehrmlive.com/', timeout=(10,10))
    print(page.status_code)

    # search for csrf token
    p = re.search('_csrf_token" value="(.*)" id="csrf_', page.text)
    token = p.group(1)
    print('token: ', token)

    # get form data from browser inspector
    form_data = {
                '_csrf_token': token,
                'actionID': "",
                'hdnUserTimeZoneOffset': '-7',
                'Submit': 'LOGIN',
                'txtPassword': 'admin123',
                'txtUsername': 'Admin'
    }

    # login (using form data)
    next = session.post('https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials', data=form_data, timeout=(10, 10))
    print(next.status_code)

    # confirm we are on next page - logged in by verifying Logout link exists on page
    p2 = re.search('<li><a href="/index.php/auth/logout">(.*)</a></li>', next.text)
    logout = p2.group(1)

    if logout == 'Logout':
        print('We successfully loged in.')
    else:
        print('Login unsuccessful.')


auth2()






























