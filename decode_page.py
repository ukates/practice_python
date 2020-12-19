import requests
from bs4 import BeautifulSoup

base_url = "https://kentuckysportsradio.com"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')

post_list = soup.find(class_='fl-post-feed')

titles = post_list.find_all('strong')


file_name = input('What would you like the name of the file to be: ')

with open(file_name + ".txt", 'w') as open_file:
    for title in titles:
        headline = title.contents[0]
        open_file.write(headline + '\n')

with open(file_name + ".txt", 'r') as open_file:
    all_text = open_file.read()
    print(all_text)

open_file.close()
