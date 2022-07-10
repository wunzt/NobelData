# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 7/10/2022
# Description: Creates a dictionary of nobel prize data from a .json file and returns a sorted list of surnames
#               of winners for a given year and category.

import json


class NobelData:
    """Creates a dictionary of nobel prize data from a .json file and returns a sorted list of surnames of winners
    for a given year and category."""

    def __init__(self):
        """Initializes a dictionary of nobel prize data from a .json file."""
        with open("nobels.json", "r") as infile:
            nobel_data = json.load(infile)

        self._nobel_data = nobel_data

    def search_nobel(self, year, category):
        """Returns a sorted list of surnames of winners for a given year and category."""
        winners = []

        for val in self._nobel_data["prizes"]:
            if year == self._nobel_data["prizes"][0]["year"] and category == self._nobel_data["prizes"][1]["category"]:
                winners.append(self._nobel_data["prizes"][0]["laureates"][2]["surname"])

        winners.sort()

        return winners



nd = NobelData()
nd.search_nobel("2001", "economics")