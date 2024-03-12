from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

def parse():
    url = 'https://pepper.ru/'
    page = requests.get(url, headers={'User-Agent': UserAgent().chrome})
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
    blocktitle = soup.findAll('a', class_='cept-tt thread-link linkPlain thread-title--list js-thread-title')
    blockdegrees = soup.findAll('span', class_ = ['cept-vote-temp vote-temp vote-temp--hot', 'cept-vote-temp vote-temp vote-temp--burn', 'space--h-2 text--b'])
    titles = []
    degreesinput = []
    degreesoutput = []
    links = []
    for data in blocktitle:
        titles.append(data.get('title'))
    for data in blockdegrees:
        degreesinput.append(data.string)
    for data in blocktitle:
        links.append(data.get('href'))
    for line in degreesinput:
        if line == "Горячо!":
            continue
        line = line.replace('\n', '').replace('\t', '')
        degreesoutput.append(line)
    for l,b,a in zip(titles, degreesoutput, links):
        print("Название: ",l,"Градусы: ", b,"Ссылка: ", a)
    print(len(links))

