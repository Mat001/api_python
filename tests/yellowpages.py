import requests
import time
import unittest


class Yellowpages(unittest.TestCase):

    def setUp(self):

        self.BASE_URL = 'https://accounts.yellowpages.com'
        self.session = requests.Session()

    def test_01(self):
        """POST request for yellowpages login requires full form data and full
        response header to be passed to POST parameters.

        With some websites, only _crsf token is needed, but in this case also full
        header is needed. Not sure how to know what exactly is needed (try/fail).
         Get headres and form data from browser inspector."""

        session = self.session
        base_url = self.BASE_URL

        r = session.get(base_url + '/login', timeout=(10, 10))
        print(r.headers)
        self.assertEqual(200, r.status_code)

        # sign in, get form data format from browser inspector
        form_data = {'_csrf': 'q8kemcGbv557xZ/3oVzfDxQ03v5oia3ZqgCthrDYxN0=',
                     'email': 'gizmo999@zoho.com',
                     'password': 'c8iAy5NwHN7fz84y'}

        header_post = {'Host': 'accounts.yellowpages.com',
             'Connection': 'keep-alive',
             'Content-Length': '106',
             'Cache-Control': 'max-age=0',
             'Origin': 'https://accounts.yellowpages.com',
             'Upgrade-Insecure-Requests': '1',
             'Content-Type': 'application/x-www-form-urlencoded',
             'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, '
                           'like Gecko)' \
                           'Chrome/69.0.3497.100 Safari/537.36',
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                       'image/webp,' \
                       'image/apng,*/*;q=0.8',
             'Referer': 'https://accounts.yellowpages.com/login?next=https%3A%2F'
                        '%2Faccounts.' \
                        'yellowpages.com%2Fdialog%2Foauth&client_id=dd48fffe-acfa-46a2'
                        '-a5c5-' \
                        'c66c30511a8a&response_type=code&app_id=WEB&source=ypu_login'
                        '&vrid=f556dada-' \
                       '3c34-4e07-b38b-5c76461aa45d&merge_history=true',
             'Accept-Encoding': 'gzip, deflate, br',
             'Accept-Language': 'en-US,en;q=0.9',
             'Cookie': 'vrid=f556dada-3c34-4e07-b38b-5c76461aa45d; bucket=ypu%3Aypu%3A'
                       'default; bucketsrc=default; _ga=GA1.2.43547925.1541368298; _'
                       'gid=GA1.2.158707952.1541368298; _fbp=fb.1.1541368297953.1713'
                       '156661; s_cc=true; s_vi=[CS]v1|2DEFB4F5050324C1-4000118700000'
                       'AC9[CE]; optimizelyEndUserId=oeu1541368333067r0.4154815183166'
                       '3804; optimizelySegments=%7B%7D; optimizelyBuckets=%7B%7D; s_'
                       'prop70=November; s_prop71=45; _donotuse_yp_at=NTkzMDI0NzI3CWR'
                       'kNDhmZmZlLWFjZmEtNDZhMi1hNWM1LWM2NmMzMDUxMWE4YQkJYzMzNTAzNTQz'
                       'MTQ5YjUwNTc1MjUwMWUxYTIyYzZjYjQ4NjRmYzZiMzIxMDk4NDg1MTdlOTIxY'
                       'jdjNjg2YTJkYwkOwPvBCQB2pwA%3D.DsD7wQ.k9UwalO0G35ISmoCncdU6vRg'
                       'VAU; optimizelyPendingLogEvents=%5B%5D; _gat=1; s_sq=%5B%5BB%5'
                       'D%5D; _dc_gtm_UA-53369742-1=1; rack.session=BAh7DUkiD3Nlc3Npb2'
                       '5faWQGOgZFVEkiRTU0Njk2M2ZkOTE5Yzc2ZmY0YzNl%0AMDQwODA0YWYyNjZlM'
                       'DM5YjBmNDk3YjdjODQ5NDljNWE0NTE2MjQ2NDFhNDcG%0AOwBGSSIOdGltZXN0'
                       'YW1wBjsARkl1OglUaW1lDZWoHYBFfGfgCjoNbmFub19u%0AdW1pAZI6DW5hbm9'
                       'fZGVuaQY6DXN1Ym1pY3JvIgcUYDoLb2Zmc2V0aQA6CXpv%0AbmVJIghVVEMGOw'
                       'BUSSIJdnJpZAY7AEZJIilmNTU2ZGFkYS0zYzM0LTRlMDct%0AYjM4Yi01Yzc2N'
                       'DYxYWE0NWQGOwBUSSIKZmxhc2gGOwBGewBJIg5zdXBlcnVz%0AZXIGOwBGRkki'
                       'FW9hdXRoX3Nlc3Npb25faWQGOwBGSSIpZjViNWZhY2YtOTVi%0AYi00NTMxLWF'
                       'hYzctNzlkMjZmNzQ5NTk4BjsAVEkiEm1lcmdlX2hpc3RvcnkG%0AOwBGSSIJdH'
                       'J1ZQY7AFRJIg9jc3JmLnRva2VuBjsAVEkiMXE4a2VtY0didjU1%0AN3haLzNvV'
                       'npmRHhRMDN2NW9pYTNacWdDdGhyRFl4TjA9BjsARg%3D%3D%0A--7d6469a9e9'
                       'a76e715f30d7b34cad291488e4a174; s_ppv=sign_in%2C100%2C100%2C12'
                       '94; s_nr=1541368578001'
                    }

        query_params = 'next=https%3A%2F%2Faccounts.yellowpages.com%2Fdialog%2Foauth&' \
              'client_id=dd48fffe-acfa-46a2-a5c5-c66c30511a8a&response_type=code&app_id' \
              '=WEB&source=ypu_login&vrid=f556dada-3c34-4e07-b38b-5c76461aa45d&' \
              'merge_history=true'

        r2 = session.post(base_url + '/login', params= query_params,
                          data=form_data, headers=header_post)
        print(r2.headers)

        self.assertEqual(200, r2.status_code)
        self.assertIn('UserLoggedIn   = true', r2.text)
        self.assertIn('"email":"gizmo999@zoho.com"', r2.text)


        # searcg - implement searching in yellowpages
        # params_search = 'https://www.yellowpages.com/search?search_terms=auto+repair' \
        # u'&geo_location_terms=Pinole%2C+CA'
        #
        # r3 = session.post(base_url + '/search', params=params_search,
        #                   data=form_data, headers=header_post)
        # print(r3.headers)
        #
        # self.assertEqual(200, r3.status_code)



    def shortDescription(self):
        """Utility function to disable displaying docstring in verbose output."""
        return None


if __name__ == '__main__':
    unittest.main(warnings='ignore')
