import re
import requests

url = 'https://www.gushiwen.org/default_{}.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 '
                  '(Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}


def parse_page(url):
    response = requests.get(url, headers=headers)
    text = response.text
    # re.DOTALL表示.
    titles = re.findall('<div class="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
    dynasties = re.findall('<p class="source">.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    authors = re.findall('<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    contents = re.findall('<div class="contson".*?>(.*?)</div>', text, re.DOTALL)
    # print(titles)
    # print(dynasties)
    # print(authors)
    contents = list(map(lambda x: re.sub('<.*?>', '', x).strip(), contents))
    # print(contents)
    # for content in contents:
    #     cont = re.sub('<.*?>', '', content).strip()
    #     print(cont)
    #     print("=" * 20)
    poems = []
    for value in zip(titles, dynasties, authors, contents):
        title, dynasty, author, content = value
        poem = {
            'title': title,
            'dynasty': dynasty,
            'author': author,
            'content': content
        }
        poems.append(poem)

    for value in poems:
        print(value)


def main():
    for i in range(1, 10):
        parse_page(url.format(str(i)))


if __name__ == '__main__':
    main()
