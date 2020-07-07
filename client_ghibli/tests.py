import mock
from mock import patch

from django.test import TestCase

from .client import ClientGhibli
from .mocks import FILMS_MOCK_SUCCESS


class ClientGhibliCase(TestCase):

    def test_response_content_is_not_null(self):
        with patch('requests.get') as mock_request:

            mock_request.return_value.status_code = 200
            mock_request.return_value.content = FILMS_MOCK_SUCCESS

            client = ClientGhibli()
            response = client.get_from_api_or_cache('films')

            self.assertIsNotNone(response)

    def test_response_content_is_empty(self):
        """
        TODO: Basically Define more cases in order to get all possible errors
        """
        pass

    def test_response_content_with_error(self):
        """
        TODO: Basically Define more cases in order to get all possible errors
        """
        pass
