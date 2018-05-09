import mock
from tornado.web import Application
import route.charges as ch
from tornado.testing import AsyncHTTPTestCase
from urllib import urlencode


class ChargeTest(AsyncHTTPTestCase):
    def get_app(self):
        return Application([("/charges", ch.PayHandler)])

    def test_pay_charge(self):
        post_data = {
            "ch_id": "ch_zbLCXPSS0uLS",
            "env_name": "dev",
            "live_key": "sk_live_vjfr9084iP8KO"
        }
        with mock.patch.object(ch.PayHandler, 'get_current_user'):
            path = "/charges"
            response = self.fetch(path, method='POST', body=urlencode(post_data))
        self.assertEqual(response.code, 200)
        self.assertTrue('env_name' in response.body)
