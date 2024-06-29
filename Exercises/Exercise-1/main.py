import requests
import os

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def create_directory(dir):
    parent_dir = "C:\\Users\\milo\\personal projects\\data-engineering-practice\\Exercises\\"
    path = os.path.join(parent_dir, dir)

    if not os.path.exists(path):
        try:
            os.mkdir(path)
            print("Directory '%s' created" % dir)
        except OSError as error:
            print("error:" %  error)

def main():
    dir = "downloads"

    create_directory(dir)
    # your code here
    pass


if __name__ == "__main__":
    main()
