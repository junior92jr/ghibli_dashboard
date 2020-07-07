import mock
from mock import patch

from django.test import TestCase

from client_ghibli.client import ClientGhibli
from client_ghibli.mocks import MockClientGhibli

from .utils import DataManger


class DashboardTest(TestCase):
    
    @patch.object(
        ClientGhibli, 'get_from_api_or_cache', 
        MockClientGhibli.get_from_api_or_cache)
    def test_success_response(self):

        manager = DataManger()

        response = manager.get_dashboard_data()

        self.assertIsNotNone(response)

    def test_error_response(self):
        """
        TODO: Unit test to check when there are errors in the Api.
        """
        pass
