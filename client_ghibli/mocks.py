FILMS_MOCK_SUCCESS = [
    {
        "id": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
        "title": "Castle in the Sky",
        "description": ("The orphan Sheeta inherited a mysterious crystal "
        "that links her to the mythical sky-kingdom of Laputa. With the help of "
        "resourceful Pazu and a rollicking band of sky pirates, she makes her way "
        "to the ruins of the once-great civilization. Sheeta and Pazu must outwit "
        "the evil Muska, who plans to use Laputa's science to make himself "
        "ruler of the world."),
        "director": "Hayao Miyazaki",
        "producer": "Isao Takahata",
        "release_date": "1986",
        "rt_score": "95"
    },
    {
        "id": "12cfb892-aac0-4c5b-94af-521852e46d6a",
        "title": "Grave of the Fireflies",
        "description": ("In the latter part of World War II, a boy and his sister, "
        "orphaned when their mother is killed in the firebombing of Tokyo, "
        "are left to survive on their own in what remains of civilian life in "
        "Japan. The plot follows this boy and his sister as they do their best to "
        "survive in the Japanese countryside, battling hunger, prejudice, and "
        "pride in their own quiet, personal battle."),
        "director": "Isao Takahata",
        "producer": "Toru Hara",
        "release_date": "1988",
        "rt_score": "97"
    }
]

PEOPLE_MOCK_SUCCESS = [
    {
        "id": "ba924631-068e-4436-b6de-f3283fa848f0",
        "name": "Ashitaka",
        "gender": "male",
        "age": "late teens",
        "eye_color": "brown",
        "hair_color": "brown",
        "films": ["https://ghibliapi.herokuapp.com/films/12cfb892-aac0-4c5b-94af-521852e46d6a"],
        "species": "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
        "url": "https://ghibliapi.herokuapp.com/people/ba924631-068e-4436-b6de-f3283fa848f0"
    },
    {
        "id": "030555b3-4c92-4fce-93fb-e70c3ae3df8b",
        "name": "Yakul",
        "age": "Unknown",
        "gender": "male",
        "eye_color": "Grey",
        "hair_color": "Brown",
        "films": ["https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"],
        "species": "https://ghibliapi.herokuapp.com/species/6bc92fdd-b0f4-4286-ad71-1f99fb4a0d1e",
        "url": "https://ghibliapi.herokuapp.com/people/030555b3-4c92-4fce-93fb-e70c3ae3df8b"
    }
]


class MockClientGhibli(object):

    def get_from_api_or_cache(
        self, endpoint_key, raise_exception=False, cache_timeout=0, **kwargs):

        response = {}

        if endpoint_key == 'films':
            response = {
                'data': FILMS_MOCK_SUCCESS,
                'error': []
            }
        elif endpoint_key == 'people':
            response =  {
                'data': PEOPLE_MOCK_SUCCESS,
                'error': []
            }
        
        return response
