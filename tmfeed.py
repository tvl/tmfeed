#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from termcolor import colored
import click
import sys

url = 'https://tmfeed.ru/{}'

@click.group()
def cli():
        pass

@cli.command(help='Get best posts for day.')
def day():
    main(url.format('popular/day/'))

@cli.command(help='Get best posts for week.')
def week():
    main(url.format('popular/week/'))

@cli.command(help='Get best posts for month')
def month():
    main(url.format('popular/month/'))

@cli.command(help='Get all latest posts.')
def all():
    main(url.format('all/'))

def main(url):
    response = requests.get(url)
    if not response.status_code == 200:
        print('Ошибка ({}) {}'.format(response.status_code, url))
        sys.exit(1)
    html = response.content
    soup = BeautifulSoup(html,'html.parser')
    print('{} (via tmfeed CLI)'.format(soup.html.head.title.text))
    for link in soup.find_all('li', 'tm-post'):
        post = link.find_all('div')
        print(post[0].a.text, end=' ')
        print(colored(post[0].span.text, 'cyan'))
        print(colored(post[1].a.text), 'blue')
        print(colored(post[1].a['href'] , 'green'), end=' ')
        print(colored('{}'.format(post[3].find_all('div')[0].text), 'cyan'))
    print('2006 — 2018 «TM»')
if __name__ == "__main__":
        cli()
