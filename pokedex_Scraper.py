import requests
import lxml
import re
from bs4 import BeautifulSoup
from google_images_download import google_images_download


def main():
    getImage("pokemon scarlet")


def scrapePokedex():
    """
    Function that scraps the a website for pokedex information
    Will write to a file
    """
    result = requests.get(
        "https://www.nintendolife.com/guides/pokemon-scarlet-and-violet-pokedex-complete-paldea-pokedex-all-pokemon-locations"
    )
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    table = soup.find("table")
    pokedex = []
    for row in table.findAll("tr"):
        # Source for html tag removal
        # https://medium.com/@jorlugaqui/how-to-strip-html-tags-from-a-string-in-python-7cb81a2bbf44
        clean = re.compile("<.*?>")
        rows = []
        for col in row.contents:
            newRow = re.sub(clean, "", str(col))
            rows.append(newRow + ".")
        pokedex.append(rows)
    pokedex[0] = ["pokedex_id", "pokemon_name", "location"]
    with open("pokedex.txt", "w") as f:
        for lines in pokedex:
            for entry in lines:
                f.write(entry + " ")

            f.write("\n")


# def getImage(query):
#     response = google_images_download.googleimagesdownload()
#     args = {
#         "keywords": "dog",
#         "limit": 2,
#         "print_urls": False,
#     }
#     arguments = {
#         "keywords": "Polar bears,baloons,Beaches",
#         "limit": 20,
#         "print_urls": True,
#         "raw_google_data": True,
#     }
#     try:
#         paths = response.download(arguments)
#         print(paths)
#     except FileNotFoundError:
#         print("Image not found")


if __name__ == "__main__":
    main()
