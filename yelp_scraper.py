import bs4
import requests
import argparse


def perform_request(url, params):
    req = requests.get(url, params=params)
    return req

def extract_results(soup):
    
    title = soup.head.text
    div_results_class = 'mainAttributes__09f24__26-vh arrange-unit__09f24__3IxLD arrange-unit-fill__09f24__1v_h4 border-color--default__09f24__1eOdn'
    divs = [i for i in soup.find_all('div', class_=div_results_class)]
    titles = [res.find('h4').text for res in divs]
    base_url = 'https://www.yelp.de'
    links = [base_url+res.find('a', href=True)['href'] for res in divs]
    ratings = [res.find('div',{'aria-label':True})['aria-label'] for res in divs]
    
    print(title,'\n\n')
    for title, rating, link in zip(titles, ratings, links):
        print(f'\nTitle: {title}\nRating: {rating}\nLink: {link}\n\n')


if __name__ == '__main__':
    
    # build a parser object

    parser = argparse.ArgumentParser()

    # add your arguments. "--" makes them optional, without them they are positional
    # type specifies how the program should interpret the input (as string, int, bool, float)
    # if type=str, python will call the str() method on whatever input you passed in
    # 'help' expects a string, which will be displayed if the user wants help in CLI

    parser.add_argument('--loc', type=str, help='set the location you want to query')
    parser.add_argument('--typ', type=str, help='set which kinds of businessess you want to query')

    # parse the args. all arguments will be available through this arg object

    args = parser.parse_args() # '' is only needed in jupyter notebooks

    # now you can use the input passed trough the args in the CLI like that:
    # args.loc
    # args.typ
        
    params = {
        'find_loc' : args.loc,
        'find_desc' : args.typ
        }
    url = 'https://www.yelp.de/search'
    req = perform_request(url, params)

    soup = bs4.BeautifulSoup(req.text, 'html.parser')

    extract_results(soup)
    
    