from client_ghibli.client import ClientGhibli


class DataManager:
    """
    Data Manager class that handles the Dashboard data.
    """

    def parse_film_id(self, film_id):
        """
        Parse the Film id from the url.

        :param film_id: String, Film id in the Api.

        :return String, parsed string witht he id.
        """

        film_id = film_id.split('/')[-1]

        return film_id

    def match_people_in_movies(self, people_list, movie_map):
        """
        Create Hash Table that maps people with Movies.

        :param people_list: List, People retrieved from the Api.
        :param movie_map: Dict, Mapping dictionary to create a hashing.

        """

        for person in people_list:
            for movie in person.get('films'):
                movie_id = self.parse_film_id(movie)
                if movie_id in movie_map:
                    movie_map[movie_id].append(person)
                else:
                    movie_map.update({movie_id: [person]})

    def get_dashboard_data(self):
        """
        Data Managet that Handle the data for Dashboard.
        """

        movie_map = {}
        client_guibli = ClientGhibli()

        people_list = client_guibli.get_from_api_or_cache(
            endpoint_key='people', cache_timeout=60)
        films_list = client_guibli.get_from_api_or_cache(
            endpoint_key='films', cache_timeout=60)


        if people_list.get('data') and films_list.get('data'):
            people_list = people_list.get('data')
            films_list = films_list.get('data')

            self.match_people_in_movies(people_list, movie_map)

            for item in films_list:

                item.update(
                    {
                        'people': movie_map[
                            item.get('id')] if item.get('id') in movie_map else []
                    }
                )

            return films_list
