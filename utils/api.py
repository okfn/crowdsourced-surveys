import os
import requests
import json
import ipdb
# from oauthlib.oauth2 import LegacyApplicationClient
# from requests_oauthlib import OAuth2Session


class ApiWrapper:

    path = '/api'
    namespace = 'v3'

    def __init__(self):
        self.config()
        return

    # ---------------------------------------------
    # Utility methods

    def config(self):
        """ Configure the instance
        """
        self.api_url = '{}{}/{}'.format(
            os.getenv('PLATFORM_URL'),
            self.path,
            self.namespace
        )
        self.api_username = os.environ.get('PLATFORM_USERNAME')
        self.api_password = os.environ.get('PLATFORM_PASSWORD')
        self.api_secret = os.environ.get('PLATFORM_SECRET')
        self.api_client_id = 'ushahidiui'
        self.api_scope = 'users posts media forms api tags savedsearches sets stats layers config messages notifications webhooks contacts roles permissions csv tos dataproviders'
        self.api_token = None

    def test(self):
        """ Pings the API, returns HTTP status
        """
        url = '%s' % os.getenv('PLATFORM_URL')
        return requests.get(url)


    def get_token(self):
        """ Log in and get an authentication token, store it and return it
        """
        url = '{}/oauth/token'.format(os.getenv('PLATFORM_URL'))

        params = {
            "client_id": self.api_client_id,
            "client_secret": self.api_secret,
            "grant_type": "password",
            "password": self.api_password,
            "scope": "posts media forms api tags savedsearches sets users stats layers config messages notifications webhooks contacts roles permissions csv tos dataproviders",
            "username": self.api_username,
        }
        res = requests.post(url, data=params)
        # self.session = OAuth2Session(client=LegacyApplicationClient(
        #     client_id=self.api_client_id, scope=self.api_scope
        # ))
        # token = self.session.fetch_token(
        #     token_url=url,
        #     username=self.api_username,
        #     password=self.api_password,
        #     client_id=self.api_client_id,
        #     client_secret=self.api_secret
        # )
        # self.api_token = token
        self.api_token = res.json()['access_token']
        return self.api_token

    def make_request(self, url, data={}, method='GET'):
        """ Make an authorized request to the API
        """
        token = self.api_token
        headers = {
            'Authorization': 'Bearer %s' % token
        }
        if method == 'POST':
            return requests.post(url, headers=headers, data=data)
        elif method == 'PUT':
            return requests.put(url, headers=headers, data=data)
        elif method == 'DELETE':
            return requests.delete(url, headers=headers)
        else:
            return requests.get(url, headers=headers)

    def authenticated(function):
        def wrapper(self, *args, **kwargs):
            if self.api_token is None:
                self.get_token()
            return function(self, *args, **kwargs)
        return wrapper

    def validated(function):
        def wrapper(self, *args, **kwargs):
            res = function(self, *args, **kwargs)
            if res.status_code == requests.codes.ok:
                return res.json()
            else:
                return False
        return wrapper

    @authenticated
    def toggle_private(self):
        """ This method is a work around the broken client UI: toggle the "private" setting for the site
        """

        status = self.make_request('%s/config/site/site_private' % self.api_url).json()['private']
        data = json.dumps({"private": not status})

        res = self.make_request('%s/config/site/site_private' % self.api_url, data=data, method='PUT')
        print(res.text)

    # ---------------------------------------------
    # CRUD methods

    @authenticated
    def get_user(self):
        """ Get the currently logged in user
        """
        res = self.make_request('{}/users/me'.format(self.api_url))
        print(res.text)

    @authenticated
    @validated
    def create_form(self, data, verbose=True):
        """ Create a new form
        """
        res = self.make_request(url='{}/forms'.format(self.api_url),
                                data=json.dumps(data),
                                method='POST')
        if verbose:
            print(res.text)
        return res

    @authenticated
    @validated
    def create_stage(self, form_id, data, verbose=True):

        data['form_id'] = form_id
        data['formId'] = form_id
        res = self.make_request(
            url='{}/forms/{}/stages'.format(self.api_url, form_id),
            data=json.dumps(data),
            method="POST"
        )
        if verbose:
            print(res.text)
        return res

    @authenticated
    @validated
    def create_attribute(self, form_id, stage_id, data, verbose=True):

        data['form_stage_id'] = stage_id
        res = self.make_request(
            url='{}/forms/{}/attributes'.format(self.api_url, form_id),
            data=json.dumps(data),
            method="POST"
        )
        if verbose:
            print(res.text)
        return res

    @authenticated
    @validated
    def delete_form(self, id):
        res = self.make_request('{}/forms/{}'.format(self.api_url, id),
                                method='DELETE')
        return res

    def submit_response(self, survey_id, response):
        """ Send a response for an existing survey
        """
        return
