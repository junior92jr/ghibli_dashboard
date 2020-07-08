import logging
import requests
import hashlib
import urllib

from django.conf import settings
from django.core.cache import cache

from .constants import (
    STUDIOGHIBLI_ENDPOINTS, 
    STUDIOGHIBLI_PROTOCOL, 
    STUDIOGHIBLI_BASE_URL,
)

logger = logging.getLogger(__name__)


class ClientGhibli:
    """
    Client for Ghibli API.
    """

    def __init__(self):
        """
        Initializer of the Class.
        """

        self.__protocol = STUDIOGHIBLI_PROTOCOL
        self.__base_url = STUDIOGHIBLI_BASE_URL

        self.__endpoint = '{protocol}://{base_url}'.format(
            protocol=self.__protocol,
            base_url=self.__base_url,
        )

    def __get_method(self, url):
        """
        Method Get to retrieve in the API.

        :param url: Url to be used to perform the request.
        
        :return Dictionary with the information from the API.
        """

        response = {
            'data': [], 
            'errors': []
        } 

        api_response = requests.get(url)

        if api_response and api_response.status_code == 200:
            api_response = api_response.json()
            response.update({'data': api_response})
        else:
            response['errors'].append(api_response.content)

        return response

    def get_from_api_or_cache(
        self, endpoint_key, raise_exception=False, cache_timeout=0, **kwargs):
        """
        Method that retrieve data from the API or from the File System Cache.

        :param endpoint_key: String, indicate which endpoint to be used.
        :param raise_exception: Boolean, indicate to raise an error.
        :param cache_timeout: Integer, Valid lifetime for stored response in cache.
        :param kwargs: Dict, additional params.

        :return Dict, response with data and errors.
        """

        url = '{endpoint}{films_endpoint}'.format(
            endpoint=self.__endpoint, 
            films_endpoint=STUDIOGHIBLI_ENDPOINTS[endpoint_key]
        )

        # TODO: Using kwargs for hanlding query params.

        cache_key = 'client_ghibli_get_{endpoint_key}_{sha1_key}'.format(
            endpoint_key=endpoint_key, 
            sha1_key=hashlib.sha1(url.encode('utf-8')).hexdigest())
        
        try:
            if cache_timeout != 0 and cache.get(cache_key) is not None:
                response = cache.get(cache_key)
            else:
                response = self.__get_method(url)

                if cache_timeout != 0:
                    cache.set(cache_key, response, cache_timeout)
        
        except Exception as err:
            # TODO: Improving error handling for API.
            logger.error('Error with the endpoint')
            if raise_exception:
                raise err
            pass
            
        return response
