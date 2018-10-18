#
# Copyright 2018 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from delphixpy.delphix_engine import DelphixEngine
from delphixpy.exceptions import RequestError
from delphixpy.exceptions import JobError
from delphixpy.exceptions import HttpError
from delphixpy import job_context
from delphixpy.web import job
from delphixpy.web import system

from delphix.lib.DlpxException import DlpxException
from delphix.lib.DxLogging import print_debug
from delphix.lib.DxLogging import print_info

VERSION = 'v.0.2.09'

class DelphixSession(object):
    """
    Class to get the configuration and returns an Delphix authentication
    object
    """

    def __init__(self):
        self.server_session = None
        self.dlpx_engines = {}
        self.jobs = {}

    def __getitem__(self, key):
        return self.data[key]

    @staticmethod
    def create(config):
        sess = DelphixSession()
        sess.dlpx_engines[config['hostname']] = config
        sess.serversess(config['ip_address'], config['username'], config['password'])
        return sess

    def serversess(self, f_engine_address, f_engine_username,
                   f_engine_password, f_engine_namespace='DOMAIN'):
        """
        Method to setup the session with the Virtualization Engine

        f_engine_address: The Virtualization Engine's address (IP/DNS Name)
        f_engine_username: Username to authenticate
        f_engine_password: User's password
        f_engine_namespace: Namespace to use for this session. Default: DOMAIN
        """

#        if use_https:
#            if hasattr(ssl, '_create_unverified_context'):
#                ssl._create_default_https_context = \
#                    ssl._create_unverified_context

        if f_engine_password:
            self.server_session = DelphixEngine(f_engine_address,
                                                f_engine_username,
                                                f_engine_password,
                                                f_engine_namespace)
        elif f_engine_password is None:
            self.server_session = DelphixEngine(f_engine_address,
                                                f_engine_username,
                                                None, f_engine_namespace)