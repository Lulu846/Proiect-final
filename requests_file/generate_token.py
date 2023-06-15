import time

import requests as requests
from selenium.webdriver.common.by import By
from requests_file.browser import Browser


class Generate_token(Browser):
    CLIENT_ID = "20824dd7c2cd46c892a3c787a7e02d96"
    CLIENT_SECRET = "fc2f0ab71fba40d28abba69a73c857ae"
    RESPONSE_TYPE= "code"
    ENCODED_REDIRECT_URI = "http%3A%2F%2Ftestitluluapp"
    REDIRECT_URI = "http://testitluluapp"
    SCOPE = "ugc-image-upload user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-follow-modify user-follow-read user-read-playback-position user-top-read user-read-recently-played user-library-modify user-library-read user-read-email user-read-private"
    HOST = "https://accounts.spotify.com"
    USERNAME = (By.ID,"login-username")
    PASSSWORD = (By.ID,"login-password")
    LOG_IN_BUTTON =(By.ID,"login-button")
    AGREE_BUTTON = (By.CLASS_NAME,"jWBSO")
    GRANT_TYPE = "authorization_code"

    def create_authorize_endpoint(self):
        endpoint = self.HOST + "/authorize?client_id=" + self.CLIENT_ID+"&response_type="+self.RESPONSE_TYPE+"&redirect_uri="+self.ENCODED_REDIRECT_URI+"&scope="+self.SCOPE
        return endpoint

    def load_endpoint(self):
        self.chrome.get(self.create_authorize_endpoint())

    def login_to_spotify(self):
        self.chrome.find_element(*self.USERNAME).send_keys("maniu.raluca@gmail.com")
        self.chrome.find_element(*self.PASSSWORD).send_keys("packard1981")
        self.chrome.find_element(*self.LOG_IN_BUTTON).click()

    def authorize_login(self):
        self.chrome.find_element(*self.AGREE_BUTTON).click()

    def get_code(self):
        url = self.chrome.current_url
        code = url[url.index("=")+1:]
        return code

    def get_token(self):
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
                "redirect_uri": self.REDIRECT_URI,
                "client_id": self.CLIENT_ID,
                "client_secret":self.CLIENT_SECRET,
                "code":self.get_code(),
                "grant_type":self.GRANT_TYPE
                }
        response = requests.post(self.HOST + "/api/token", data=data, headers=header)
        time.sleep(3)
        return response.json()["access_token"]

    def authorization(self):
        self.create_authorize_endpoint()
        self.load_endpoint()
        self.login_to_spotify()
        try:
            self.authorize_login()
        except:
            self.get_code()
        return f"Bearer {self.get_token()}"