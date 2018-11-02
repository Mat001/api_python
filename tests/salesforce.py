"""
Goal: Automating sales opportunity creation process and testing it.
An opportunity in Salesforce has different types and stages – this test tries
to automate creation of different permutations.

Use Salesforce API to create a new opportunities and validate they were created.
1. Authenticate/authorize access to API (create dev account first)
2. Use auth token to access test endpoint once authenticated.
3. Create new opportunity and validate it

I used the following steps:
- Get the payload from Salesforce API workbench
- Create an opportunity of type new business
- Create/select a stage for the opportunity: Qualification/ Meeting Scheduled/
Proposal or Price Quote/Negotiation or Review
- Create a new account

TASK (coding)
- Write a POST call passing the JSON Payload as a request 
- Assert the status code of 201 received
- Validate that the opportunity has been created 
- GET the Opportunity created
- Assert Status code 
- Parse the JSON and Assert the opportunities created for each of them for each stage
and opportunity type and account

Using curl:
curl -d "grant_type=password" -d "client_id=my_remote_access_consumer_key" -d
"client_secret=my_remote_access_consumer_secret" -d "username=dustin@example.com"
 -d "password=my_password+security_token"
 https://ap1.salesforce.com/services/oauth2/token

Salesforce API docs://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/
api_rest/quickstart_oauth.htm
"""
import requests
import unittest
import json


class Salesforce(unittest.TestCase):

    def setUp(self):
        self.BASE_URL = 'https://ap1.salesforce.com'

        client_secret = 'to_be_inserted'
        password = 'to_be_inserted'

        credentials = {
            'grant_type': 'password',
            'client_id': '3MVG9zlTNB8o8BA28oKeNIRrpUToEFXXhdqfDXdKbeCiQA6.cWLPXnM845we_Hpuef_9bOoFHA1aRRFqRzuLx',
            'client_secret': client_secret,
            'username': 'mpx2@mpx2.com',
            'password': password
        }

        auth = requests.post(self.BASE_URL + '/services/oauth2/token',
                             data=credentials,
                             timeout=(10, 10))

        resp = auth.json()
        print('AUTH: ', resp)
        self.assertEqual(auth.status_code, 200)

        # need session here to store access_token for each subsequent request (or cookie)
        self.session = requests.session()
        self.header = {
            'Authorization': resp['token_type'] + ' ' + resp['access_token'],
            'content-type': 'application/json'
        }

    def test_01_qualification_opportunity(self):
        print("Salesforce")

        session = self.session
        header = self.header

        payload = {
            "Name": "new business 11",
            "StageName": "Qualification / Meeting Scheduled/ Proposal",
            "CloseDate": "2019-01-01",
            "Amount": 1001,
        }

        # Write a POST call passing the JSON Payload as a request
        # needed to use json.payload instead of data=payload
        post_opport = session.post(
            'https://ap1.salesforce.com/services/data/v43.0/sobjects/Opportunity/',
            data=json.dumps(payload),
            headers=header,
            timeout=(10, 10))

        opport_response = post_opport.json()
        print('OPP: ', opport_response)

        # Assert the status code of 201 received
        self.assertEqual(post_opport.status_code, 201)
        self.assertIsNotNone(opport_response['id'])
        self.assertTrue(opport_response['success'])

        # Validate that the opportunity has been created:
        # GET the Opportunity created
        # Assert Status code
        id = opport_response['id']
        get_created_opport = session.get(
            'https://ap1.salesforce.com/services/data/v43.0/sobjects/Opportunity/' + id,
            headers=header,
            timeout=(10, 10))

        opp_resp = get_created_opport.json()
        print(opp_resp)

        self.assertEqual(get_created_opport.status_code, 200)
        self.assertEqual(opp_resp['Id'], id)
        self.assertEqual(opp_resp['Name'], 'new business 11')
        self.assertEqual(opp_resp['attributes']['type'], 'Opportunity')
        self.assertEqual(opp_resp['StageName'],
                         'Qualification / Meeting Scheduled/ Proposal')

    def test_02_price_quote_opportunity(self):
        # Parse the JSON and Assert the opportunities created for each of them
        # for each stage and opportunity type and account.

        session = self.session
        header = self.header

        payload = {
            "Name": "new business 22",
            "StageName": "Price Quote / Negotiation",
            "CloseDate": "2019-02-02",
            "Amount": 1002,
        }

        post_opport = session.post(
            self.BASE_URL + '/services/data/v43.0/sobjects/Opportunity/',
            data=json.dumps(payload),
            headers=header,
            timeout=(10, 10))

        opport_response = post_opport.json()
        # print(opport_response)

        # Assert the status code of 201 received
        self.assertEqual(post_opport.status_code, 201)
        self.assertIsNotNone(opport_response['id'])
        self.assertTrue(opport_response['success'])

        # Validate that the opportunity has been created:
        # GET the Opportunity created, Assert Status code
        id = opport_response['id']
        get_created_opport = session.get(
            'https://ap1.salesforce.com/services/data/v43.0/sobjects/Opportunity/' + id,
            headers=header,
            timeout=(10, 10))

        opp_resp = get_created_opport.json()
        print(opp_resp)

        self.assertEqual(get_created_opport.status_code, 200)
        self.assertEqual(opp_resp['Id'], id)
        self.assertEqual(opp_resp['Name'], 'new business 22')
        self.assertEqual(opp_resp['attributes']['type'], 'Opportunity')
        self.assertEqual(opp_resp['StageName'], 'Price Quote / Negotiation')

    def test_03_review_opportunity(self):
        # Parse the JSON and Assert the opportunities created for each of them
        # for each stage and opportunity type and account

        session = self.session
        header = self.header

        payload = {
            "Name": "new business 33",
            "StageName": "Review",
            "CloseDate": "2019-03-03",
            "Amount": 1003,
        }

        post_opport = session.post(
            self.BASE_URL + '/services/data/v43.0/sobjects/Opportunity/',
            data=json.dumps(payload),
            headers=header,
            timeout=(10, 10))

        opport_response = post_opport.json()
        # print(opport_response)

        # Assert the status code of 201 received
        self.assertEqual(post_opport.status_code, 201)
        self.assertIsNotNone(opport_response['id'])
        self.assertTrue(opport_response['success'])

        # Validate that the opportunity has been created:
        # GET the Opportunity created
        # Assert Status code
        id = opport_response['id']
        get_created_opport = session.get(
            'https://ap1.salesforce.com/services/data/v43.0/sobjects/Opportunity/' + id,
            headers=header,
            timeout=(10, 10))

        opp_resp = get_created_opport.json()
        print(opp_resp)

        self.assertEqual(get_created_opport.status_code, 200)
        self.assertEqual(opp_resp['Id'], id)
        self.assertEqual(opp_resp['Name'], 'new business 33')
        self.assertEqual(opp_resp['attributes']['type'], 'Opportunity')
        self.assertEqual(opp_resp['StageName'], 'Review')

    def tearDown(self):
        print('----------------------------------------------------')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
