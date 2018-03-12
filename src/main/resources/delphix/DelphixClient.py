#
# Copyright 2018 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import requests
import json


class DelphixClient:

    def __init__(self, server):
        self.server = server
        self.cookies = self.get_session()

    def get_session(self):
        print('- open session on {0}'.format(self.server['url']))
        headers = {'Content-type': 'application/json'}
        data = {
            "type": "APISession",
            "version": {
                "type": "APIVersion",
                "major": 1,
                "minor": 8,
                "micro": 2
            }
        }

        r = requests.post('{0}/resources/json/delphix/session'.format(self.server['url']),
                          headers=headers,
                          data=json.dumps(data))
        return r.cookies

    def _login(self):
        print('- login')
        headers = {'Content-type': 'application/json'}
        data = {
            "type": "LoginRequest",
            "username": self.server['username'],
            "password": self.server['password'],
        }
        r = requests.post('{0}/resources/json/delphix/login'.format(self.server['url']),
                          headers=headers,
                          cookies=self.cookies,
                          data=json.dumps(data))

        if self._response_ok(r):
            print("- Authenticated ! ")
        else:
            raise self._response_error(r)
        return r.text

    def _logout(self):
        print('- logout')
        headers = {'Content-type': 'application/json'}
        requests.post('{0}/resources/json/delphix/logout'.format(self.server['url']),
                      headers=headers,
                      cookies=self.cookies)

    def _get_params(self, vdb):
        result = {'ref': 'NOT_FOUND', 'cont': 'NOT_FOUND', 'vsrc': 'NOT_FOUND'}
        print('- get params')
        headers = {'Content-type': 'application/json'}

        r = requests.get('{0}/resources/json/delphix/database'.format(self.server['url']),
                         headers=headers,
                         cookies=self.cookies)

        for db in r.json()['result']:
            if db['name'] == vdb:
                result['ref'] = db['reference']
                result['cont'] = db['provisionContainer']

        r = requests.get('{0}/resources/json/delphix/source'.format(self.server['url']),
                         headers=headers,
                         cookies=self.cookies)

        for db in r.json()['result']:
            if db['name'] == vdb:
                result['vsrc'] = db['reference']

        print('- database reference {ref}'.format(**result))
        print('- database provisionContainer {cont}'.format(**result))
        print('- source reference {vsrc}'.format(**result))
        return result

    def _refresh(self, vdb):
        parameters = self._get_params(vdb=vdb)
        print("- refresh ")
        headers = {'Content-type': 'application/json'}
        data = {
            "type": "OracleRefreshParameters",
            "timeflowPointParameters": {
                "type": "TimeflowPointSemantic",
                "container": parameters['cont'],
                "location": "LATEST_SNAPSHOT"
            }
        }

        r = requests.post(
            '{0}/resources/json/delphix/database/{1}/refresh'.format(self.server['url'], parameters['ref']),
            headers=headers,
            cookies=self.cookies,
            data=json.dumps(data))
        if self._response_ok(r):
            print("- Job    {0}".format(r.json()['job']))
            print("- Action {0}".format(r.json()['action']))
            return {'job': r.json()['job'], 'action': r.json()['action']}
        else:
            raise self._response_error(r)

    def _rewind(self, vdb):
        parameters = self._get_params(vdb=vdb)
        print("- rewind ")
        headers = {'Content-type': 'application/json'}
        data = {
            "type": "OracleRollbackParameters",
            "timeflowPointParameters": {
                "type": "TimeflowPointSemantic",
                "container": parameters['ref'],
                "location": "LATEST_SNAPSHOT"
            }
        }

        r = requests.post(
            '{0}/resources/json/delphix/database/{1}/rollback'.format(self.server['url'], parameters['ref']),
            headers=headers,
            cookies=self.cookies,
            data=json.dumps(data))
        if self._response_ok(r):
            print("- Job    {0}".format(r.json()['job']))
            print("- Action {0}".format(r.json()['action']))
            return {'job': r.json()['job'], 'action': r.json()['action']}
        else:
            raise self._response_error(r)

    def _snapshot(self, vdb):
        parameters = self._get_params(vdb=vdb)
        print("- snapshot ")
        headers = {'Content-type': 'application/json'}
        data = {
            "type": "OracleSyncParameters"
        }

        r = requests.post(
            '{0}/resources/json/delphix/database/{1}/sync'.format(self.server['url'], parameters['ref']),
            headers=headers,
            cookies=self.cookies,
            data=json.dumps(data))

        if self._response_ok(r):
            print("- Job    {0}".format(r.json()['job']))
            print("- Action {0}".format(r.json()['action']))
            return {'job': r.json()['job'], 'action': r.json()['action']}
        else:
            raise self._response_error(r)

    def _response_ok(self, r):
        return r.status_code == 200 and r.json()['type'] == 'OKResult'

    def _response_error(self, r):
        return Exception(r.text)

    def refresh(self, vdb):
        self._login()
        print("- Refresh {0} with Delphix".format(vdb))
        result = self._refresh(vdb)
        self._logout()
        return result

    def snapshot(self, vdb):
        self._login()
        print("- Snapshot {0} with Delphix".format(vdb))
        result = self._snapshot(vdb)
        self._logout()
        return result

    def rewind(self, vdb):
        self._login()
        print("- Rewind {0} with Delphix".format(vdb))
        result = self._rewind(vdb)
        self._logout()
        return result
