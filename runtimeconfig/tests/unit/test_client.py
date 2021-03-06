# Copyright 2016 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import mock


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


class TestClient(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.runtimeconfig.client import Client

        return Client

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_wo_client_info(self):
        from google.cloud._http import ClientInfo
        from google.cloud.runtimeconfig._http import Connection

        PROJECT = "PROJECT"
        http = object()
        creds = _make_credentials()

        client = self._make_one(project=PROJECT, credentials=creds, _http=http)
        self.assertIsInstance(client._connection, Connection)
        self.assertIs(client._credentials, creds)
        self.assertIs(client._http_internal, http)
        self.assertIsInstance(client._connection._client_info, ClientInfo)

    def test_ctor_w_client_info(self):
        from google.cloud._http import ClientInfo
        from google.cloud.runtimeconfig._http import Connection

        PROJECT = "PROJECT"
        http = object()
        creds = _make_credentials()
        client_info = ClientInfo()

        client = self._make_one(
            project=PROJECT, credentials=creds, _http=http, client_info=client_info
        )
        self.assertIsInstance(client._connection, Connection)
        self.assertIs(client._credentials, creds)
        self.assertIs(client._http_internal, http)
        self.assertIs(client._connection._client_info, client_info)

    def test_config(self):
        PROJECT = "PROJECT"
        CONFIG_NAME = "config_name"
        creds = _make_credentials()

        client = self._make_one(project=PROJECT, credentials=creds)
        new_config = client.config(CONFIG_NAME)
        self.assertEqual(new_config.name, CONFIG_NAME)
        self.assertIs(new_config._client, client)
        self.assertEqual(new_config.project, PROJECT)
        self.assertEqual(
            new_config.full_name, "projects/%s/configs/%s" % (PROJECT, CONFIG_NAME)
        )
        self.assertFalse(new_config.description)
