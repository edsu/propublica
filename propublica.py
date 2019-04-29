import json
import requests

class ProPublicaEntity:

    def get(self, url):
        key = open('key.txt').read().strip()
        headers = {"X-API-KEY": key}
        url = "https://api.propublica.org/congress/v1" + url
        data = requests.get(url, headers=headers).json()
        return data['results']


class State(ProPublicaEntity):

    def __init__(self, abbr):
        self.abbr = abbr

    def get_representatives(self):
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

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __repr__(self):
        return self.name

    def get_bills(self):
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

    def __init__(self, title, url, congress):
        self.title = title
        self.url = url
        self.congress = congress

    def __repr__(self):
        return self.title + " <" + self.url + ">"


if __name__ == "__main__":
    main()

