import json, pprint, requests
from bs4 import BeautifulSoup

with open("huskies.js", 'r') as j:
     js_content = j.read()

json_content = js_content[js_content.find('[') : js_content.find(']') + 1]
print(json_content)
data = json.loads(json_content)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)

url = 'https://www.flickr.com/photos/43089317@N04/8024806200'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
# photos = soup.find("span", {class: "facade-of-protection-neue"})
photos = soup.select_one('div.view.photo-well-media-scrappy-view.requiredToShowOnServer img.main-photo')

print(photos)
print(photos.get('alt'))
print(photos.get('src'))




