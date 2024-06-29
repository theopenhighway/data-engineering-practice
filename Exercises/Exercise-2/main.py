import requests
import pandas as pd
from bs4 import BeautifulSoup


parent_dir = "C:\\Users\\milo\\personal projects\\data-engineering-practice\\Exercises\\Exercise-2\\"


def find_filename(soup, date):
    for i in range(3,10):
        tr = soup.find_all('tr')[i]
        date_time = tr.find_all('td')[1]
        
        if date_time.get_text(strip=True) == date:
            filename_attribute = tr.find_all('td')[0].find('a')
            return filename_attribute.get_text()
    
    return None

def download_csv(uri,filename):
    query_parameters = {"downloadformat": "csv"}

    try:
        response = requests.get(uri, params=query_parameters)
    except requests.exceptions.HTTPError as e:
        print(e.response.text)
        return
    
    path_to_zip_file = parent_dir + filename

    with open(path_to_zip_file, mode="wb") as file:
        file.write(response.content)
    
    print("%s sucessfully downloaded" % filename)

def csv_to_pandas(filename):
    df = pd.read_csv(filename)
    print(df.loc[df['HourlyDryBulbTemperature'].idxmax()])

def main():
    # your code here
    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    date = "2024-01-19 09:53"
    filename = find_filename(soup, date)

    download_link = url + filename

    download_csv(download_link, filename)
    csv_to_pandas(filename)


if __name__ == "__main__":
    main()
