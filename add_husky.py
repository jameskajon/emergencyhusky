import json, pprint, requests, sys, argparse
from bs4 import BeautifulSoup


if sys.version_info < (3, 7):
    # 3.7 required for dictionary order. can be hardcoded if need to use older version
    sys.exit("error: this script requires Python 3.7 or greater.")


# with open("huskies.js", 'r') as j:
#      js_content = j.read()
#
# json_content = js_content[js_content.find('[') : js_content.find(']') + 1]
# print(json_content)
# data = json.loads(json_content)
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scrape the info from the given url and produce an js object.')
    parser.add_argument("url", type=str, help='the url to scrape data from')
    args = parser.parse_args()
    # url = 'https://www.flickr.com/photos/43089317@N04/8024806200'
    url = args.url

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    # photo_soup = soup.find("span", {class: "facade-of-protection-neue"})
    # TODO: get high res version from the zoom div
    photo_soup = soup.select_one('div.view.photo-well-media-scrappy-view.requiredToShowOnServer img.main-photo')

    print(photo_soup)
    if photo_soup:
        print(photo_soup.get('alt'))
        print(photo_soup.get('src'))
        text = photo_soup.get('alt')
        link = photo_soup.get('src')

        image = {}
        image["url"] = url
        image["title"] = text + ", on Flickr"
        image["imageUrl"] = link
        image["imageAlt"] = text.split("by")[0].strip()

        print("{")
        for k, v in image.items():
            print('\t"{}": "{}",'.format(k, v))
        print("},")



