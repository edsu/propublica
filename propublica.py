import json
import requests

class ProPublicaEntity:
    """
    A base class for interacting with the ProPublica API by sending the key with
    all HTTP requests.
    """

    def get(self, url):
        """
        Perform an HTTP GET request and return the JSON data in the response.
        """
        key = open('key.txt').read().strip()
        headers = {"X-API-KEY": key}
        url = "https://api.propublica.org/congress/v1" + url
        data = requests.get(url, headers=headers).json()
        return data['results']


class State(ProPublicaEntity):
    """
    A class for representing a state in the United States Congress.
    """

    def __init__(self, abbr):
        """
        The constructor which you must give a valid state abbreviation: e.g. md.
        """
        self.abbr = abbr

    def get_representatives(self):
        """
        Returns a list of Representative objects for the state.
        """
        reps = []
        for member in self.get("/members/house/md/current.json"):
            reps.append(
                Representative(
                    name=member['name'],
                    id=member['id']
                )
            )
        return reps

class Representative(ProPublicaEntity):
    """
    A class for members of the House of Representatives.
    """

    def __init__(self, name, id):
        """
        The constructor which takes a name and a ProPublica identifier as 
        arguments.
        """
        self.name = name
        self.id = id

    def __repr__(self):
        return self.name

    def get_bills(self):
        """
        Returns a list of bills that the representative has introduced.
        """
        bills = []
        bill_data = self.get('/members/' + self.id + '/bills/introduced')
        for bill in bill_data[0]['bills']:
            bills.append(
                Bill(
                    title=bill['title'],
                    url=bill['congressdotgov_url'],
                    congress=bill['congress']
                )
            )
        return bills


class Bill(ProPublicaEntity):
    """
    A class for a House of Representatives bill.
    """

    def __init__(self, title, url, congress):
        """
        You must construct a Bill by passing in its title, its url and the
        congress it belongs to (e.g. 116)
        """
        self.title = title
        self.url = url
        self.congress = congress

    def __repr__(self):
        return self.title + " <" + self.url + ">"

