import requests
import json
import unittest


class ApiTests(unittest.TestCase):

    def setUp(self):
        # no authentication required, API is fully open to public
        self.BASE_URL = 'https://api.openaq.org/v1'

    def test_01_get(self):
        print('# GET')
        params = {'country': 'SI'}
        # r = requests.get('https://musicdemons.com/api/v1/person', timeout=(10, 10))
        # r = requests.get('https://musicdemons.com/api/v1/login', timeout=(10, 10))
        r = requests.get('https://musicdemons.com/api/v1/register', timeout=(10, 10))
        self.assertEqual(r.status_code, 200)

        result = r.json()
        print(result)
        # ljubljana_location = result['results'][0]['location']
        # self.assertTrue(ljubljana_location.startswith('Ljubljana Be'), msg="Location doesn't start with Ljubljana Be")

    def tearDown(self):
        print('----------------------------------------------------')


if __name__ == '__main__':
    unittest.main(warnings='ignore')