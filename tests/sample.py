# use this site to test against: https://reqres.in/

# TODO implement POLLING - for requests/responses that take longer - however polling is already included in timeout param in requests no?

import requests
import json
import unittest

class ApiTests(unittest.TestCase):

    def setUp(self):
        self.BASE_URL = 'https://reqres.in'

    ##############################################
    # GET - get
    ##############################################
    def test_01_get(self):
        print('# GET')
        params = {'page': 2}
        r = requests.get(self.BASE_URL + '/api/users', params=params, timeout=(10, 10))
        print(r.json())
        # pretty = json.dumps(r.json(), indent=4)     # a string
        # print(pretty)
        assert r.status_code == 200


    ##############################################
    # POST - create
    ##############################################
    def test_02_post(self):
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
        print('# POST')

        payload = {
            "name": "morpheusx",
            "job": "leader"
        }

        post_new = requests.post(self.BASE_URL + '/api/users', data=payload, timeout=(10, 10))  # payload is json, but it gets automatically converted into dict here
        print(post_new.status_code)
        print(post_new.json())
        d = post_new.json()

        assert post_new.status_code == 201
        assert d['name'] == payload['name']
        assert d['job'] == payload['job']

        # TODO test that new is different from previous - test site may not be able to provide for that
        #   assert that original list of user didn't include new entry
        #   assert current list of users includes new entry


    ##############################################
    # PUT - update
    ##############################################
    def test_03_put(self):
        """
        Expected response:
        {
        "name": "morpheus",
        "job": "zion resident",
        "updatedAt": "2018-10-17T21:33:30.161Z"
        }"""
        print('# PUT')

        payload = {
            "name": "morpheusx",
            "job": "zion resident"
        }

        update = requests.put(self.BASE_URL + '/api/users/2', data=payload, timeout=(10, 10))  # payload is json, but it gets automatically converted into dict here
        print(update.status_code)
        print(update.json())
        d = update.json()

        assert update.status_code == 200
        assert d['name'] == payload['name']
        assert d['job'] == payload['job']

        # TODO test that new is different from previous - test site may not be able to provide for that
        #   assert that original user has old "job"
        #   assert current user has "new" job


    ##############################################
    # PATCH - update
    ##############################################
    def test_04_patch(self):
        """
        Expected response:
        {
        "name": "morpheus",
        "job": "zion resident_patched",
        "updatedAt": "2018-10-17T21:33:30.161Z"
        }"""
        print('# PATCH')

        payload = {
            "name": "morpheusx",
            "job": "zion resident_patched"
        }

        patch = requests.put(self.BASE_URL + '/api/users/2', data=payload, timeout=(10, 10))
        print(patch.status_code)
        print(patch.json())
        d = patch.json()

        assert patch.status_code == 200
        assert d['name'] == payload['name']
        assert d['job'] == payload['job']

        # TODO test that new is different from previous - test site may not be able to provide for that
        #   assert that original user has old "job"
        #   assert current user has "new" job


    ##############################################
    # DELETE - delete
    ##############################################
    def test_05_delete(self):
        print('# DELETE')

        remove = requests.delete(self.BASE_URL + '/api/users/2', timeout=(10, 10))
        print(remove.status_code)

        assert remove.status_code == 204
        # TODO assert deleted entry is no longer in the original data


    ##############################################
    # AUTHENTICATION - BASIC POST CREDENTIALS
    ##############################################
    def test_06_auth1(self):
        """Expected response:
        {
        "token": "QpwL5tke4Pnpja7X"
        }
        """

        print('# POST - BASIC AUTH/ POST CREDENTIALS')

        credentials = {
            "email": "sydney@fife",
            "password": "pistol"
        }

        authentication = requests.post(self.BASE_URL + '/api/register', data=credentials, timeout=(10, 10))
        print(authentication.status_code)
        print(authentication.json())
        d = authentication.json()

        assert authentication.status_code == 201
        assert d['token'] == 'QpwL5tke4Pnpja7X'


    ##############################################
    # AUTHENTICATION - USING DYNAMICALLY GENERATED CSRF TOKEN, by scraping it
    ##############################################
    def test_07_auth2(self):
        """Expected response:
        {
        "token": "QpwL5tke4Pnpja7X"
        }
        """
        import re

        print('# POST - AUTHENTICATION/ SCRAPING TOKEN')

        # create a session object, we need to persist data over two pages(?)
        session = requests.session()

        # get login page text
        page = session.get('https://opensource-demo.orangehrmlive.com/', timeout=(10,10))
        print('Login page', page.status_code)

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
        print('Login', next.status_code)

        # confirm we are on next page - logged in by verifying Logout link exists on page
        p2 = re.search('<li><a href="/index.php/auth/logout">(.*)</a></li>', next.text)
        logout = p2.group(1)

        if logout == 'Logout':
            print('Successfully loged in.')
        else:
            print('Login unsuccessful.')

        assert next.status_code == 200
        assert logout == 'Logout'


    ##############################################
    # AUTHENTICATION - USING REQUESTS'HTTPBasicAuth
    ##############################################


    ##############################################
    # AUTHENTICATION - OAuth1
    ##############################################


    ##############################################
    # DELAYED RESPONSE
    ##############################################
    def test_08_delayed_response(self):
        print('# DELAYED RESPONSE')

        params = {'delay': 3}
        r = requests.get(self.BASE_URL + '/api/users', params=params, timeout=(10, 10))
        print(r.status_code)
        print(r.json())
        assert r.status_code == 200


    def tearDown(self):
        print('----------------------------------------------------')


if __name__ == '__main__':
    unittest.main(warnings='ignore')















