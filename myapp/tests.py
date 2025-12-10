from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['testdb.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = Options()
        opts.binary_location = "/usr/bin/firefox-esr"
        cls.selenium = WebDriver(options=opts)
        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))

        self.assertEqual(self.selenium.title, "Log in | Django site admin")

        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys('admin')
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys('admin123')

        self.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()

        self.assertEqual(self.selenium.title, "Site administration | Django site admin")
