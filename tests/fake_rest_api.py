import requests
import time
import unittest


class ApiTests(unittest.TestCase):

    def setUp(self):
        """no authentication required, API is fully open to public"""

        self.BASE_URL = 'https://fakerestapi.azurewebsites.net'

    def test_01_get_activities(self):
        """Each activity should have the following keys: ID, Title, DueDate, Completed"""

        base_url = self.BASE_URL
        r = requests.get(base_url + '/api/Activities', timeout=(10, 10))
        result = r.json()

        self.assertEqual(r.status_code, 200)

        # using generator for memory efficiency because list of items can be large
        gen = (activity for activity in result)
        for i in gen:
            self.assertEqual(list(i.keys()), ['ID', 'Title', 'DueDate', 'Completed'])

    def test_02_add_activities(self):
        """Add activity. Test fails because API doesn't store newly added activities."""

        base_url = self.BASE_URL

        # always pass python dict here. Any conversion happens in the step after
        data = {
            "ID": 333,
            "Title": "Activity X",
            "DueDate": "2018-10-27T17:06:04.909Z",
            "Completed": True
        }

        headers = {'Content-type': 'application/json'}
        r = requests.post(base_url + '/api/Activities', headers=headers, data=data,
                          timeout=(10, 10))

        self.assertEqual(r.status_code, 200)

        r = requests.get(base_url + '/api/Activities', timeout=(10, 10))
        last_act = r.json().pop()

        # verify posted activity and last appended activity are the same
        # fails, because API doesn't save new entries to DB
        self.assertNotEqual(data, last_act)

    def test_03_titles_of_first_five_activities(self):
        """Assert titles of first five activities contain correct title (word
        'Activity'), generated in the previous test."""

        base_url = self.BASE_URL
        r = requests.get(base_url + '/api/Activities', timeout=(10, 10))

        self.assertEqual(r.status_code, 200)

        result = r.json()
        activities_generator = (el for ind, el in enumerate(result) if el['ID'] < 5)
        for activity in activities_generator:
            # titles should contain "Activity" and number
            self.assertTrue(
                activity['Title'] in ['Activity 1', 'Activity 2', 'Activity 3',
                                      'Activity 4', 'Activity 5'])

    def test_04_timestamp_in_ascending_order(self):
        """Take timestamps of first five activities. Compare times between two requests
        one second apart."""

        base_url = self.BASE_URL
        r1 = requests.get(base_url + '/api/Activities/1', timeout=(10, 10))
        time.sleep(1)
        r2 = requests.get(base_url + '/api/Activities/2', timeout=(10, 10))

        self.assertEqual(r1.status_code, 200)
        self.assertEqual(r2.status_code, 200)

        result1 = r1.json()
        result2 = r2.json()

        self.assertLess(result1['DueDate'], result2['DueDate'])

    def test_05_confirm_activity_values(self):
        """Validate different properties in an activity."""

        base_url = self.BASE_URL
        r = requests.get(base_url + '/api/Activities/1', timeout=(10, 10))
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(result['ID'], 1)
        self.assertEqual(result['Title'], 'Activity 1')
        self.assertFalse(result['Completed'])

    def shortDescription(self):
        """Utility function to disable displaying docstring in verbose output."""
        return None


if __name__ == '__main__':
    unittest.main(warnings='ignore')
