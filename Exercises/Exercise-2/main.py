import requests
import pandas
from bs4 import BeautifulSoup

def find_filename(soup, date):
    for i in range(3,10):
        tr = soup.find_all('tr')[i]
        date_time = tr.find_all('td')[1]
        
        if date_time.get_text(strip=True) == date:
            filename_attribute = tr.find_all('td')[0].find('a')
            return filename_attribute.get_text()
    
    return None

def download_csv(url):
    pass

def csv_to_pandas():
    pass

def main():
    # your code here
    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    date = "2024-01-19 09:53"
    filename = find_filename(soup, date)

    download_link = url + filename

    download_csv(download_link)


if __name__ == "__main__":
    main()
