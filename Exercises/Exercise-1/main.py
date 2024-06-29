import requests
import os
import zipfile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

parent_dir = "C:\\Users\\milo\\personal projects\\data-engineering-practice\\Exercises\\"

def create_directory(dir):
    path = os.path.join(parent_dir, dir)

    if not os.path.exists(path):
        try:
            os.mkdir(path)
            print("Directory '%s' created" % dir)
            return
        except OSError as error:
            print("error: %s" %  error)
            return
    
    print("Directory '%s' already exists" % dir)

def download_files(uri):
    query_parameters = {"downloadformat": "zip"}

    try:
        response = requests.get(uri, params=query_parameters)
    except requests.exceptions.HTTPError as e:
        print(e.response.text)
        return
    
    with open("gdp_by_country.zip", mode="wb") as file:
        file.write(response.content)
    
    
def unzip_files(filename):
    path_to_zip_file = parent_dir + "\\downloads\\" + filename
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(path_to_zip_file)

def main():
    dir = "downloads"

    create_directory(dir)
    # for uri in download_uris:
    #     download_files(uri)



if __name__ == "__main__":
    main()
