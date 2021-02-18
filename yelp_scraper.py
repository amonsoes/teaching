import bs4
import requests
import argparse

'''
Start script with: python3 yelp_scraper.py --loc=Vienna --typ=Restaurants
'''

def perform_request(url, params):
    req = requests.get(url, params=params)
    return req

def extract_results(soup):
    
    title = soup.head.text
    div_results_class = 'mainAttributes__09f24__26-vh arrange-unit__09f24__1gZC1 arrange-unit-fill__09f24__O6JFU border-color--default__09f24__R1nRO'
    divs = [i for i in soup.find_all('div', class_=div_results_class)]
    titles = [res.find('h4').text for res in divs]
    base_url = 'https://www.yelp.de'
    links = [base_url+res.find('a', href=True)['href'] for res in divs]
    ratings = [res.find('div',{'aria-label':True})['aria-label'] for res in divs]
    
    print(title,'\n\n')
    for title, rating, link in zip(titles, ratings, links):
        print(f'\nTitle: {title}\nRating: {rating}\nLink: {link}\n\n')


if __name__ == '__main__':
    
    def main(loc, typ):
        params = {
            'find_loc' : loc,
            'find_desc' : typ
            }
        url = 'https://www.yelp.de/search'
        req = perform_request(url, params)

        soup = bs4.BeautifulSoup(req.text, 'html.parser')

        extract_results(soup)
    
    