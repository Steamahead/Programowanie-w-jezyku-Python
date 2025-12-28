from typing import List
import requests
import argparse

URL_API = 'https://api.openbrewerydb.org/v1/breweries'

class Brewery:
    def __init__(self, name: str, city: str, state: str, brewery_type: str):
        self.name = name
        self.city = city
        self.state = state
        self.brewery_type = brewery_type

    def __str__(self):
        return f"Browar: {self.name} | Miasto: {self.city} ({self.state}) | Typ: {self.brewery_type}"


def get_breweries_from_api(city: str | None) -> list:
    if city is not None:
        return requests.get(f'{URL_API}?by_city={city}&per_page=20').json()

    return requests.get(f'{URL_API}?per_page=20').json()


def brewery_factory(breweries: list) -> List[Brewery]:
    brewery_objects = []
    for item in breweries:
        new_brewery = Brewery(
            name=item.get('name', 'Brak nazwy'),
            city=item.get('city', 'Nieznane'),
            state=item.get('state', 'Nieznane'),
            brewery_type=item.get('brewery_type', 'Nieznany')
        )
        brewery_objects.append(new_brewery)
    return brewery_objects


def get_args():
    parser = argparse.ArgumentParser(description='Pobieranie listy browarów')
    parser.add_argument('-c', '--city', help='Filter brewery by city', required=False)
    return vars(parser.parse_args())


def main():
    args = get_args()
    raw_data = get_breweries_from_api(city=args['city'])
    breweries_list = brewery_factory(raw_data)

    if not breweries_list:
        print("Nie znaleziono browarów.")
    else:
        for brewery in breweries_list:
            print(brewery)


if __name__ == '__main__':
    main()