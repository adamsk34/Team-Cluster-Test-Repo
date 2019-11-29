# import twitter
import json
import glob
import csv
import os
import datetime

files = glob.glob("./city_tweets/*.json")

uk_hour_diff = 6

uk_date_str = "2019_11_29"

folder_to_save = "./tweets_csv/no_date_overlap2/" + uk_date_str + "/"


def main():

    for file_path in files:
        with open(file_path, "r") as file:

            twitterJson = json.load(file)

            file_name = file_path.split('/')[2]

            city, party, leader = getCityAndQuery(file_name)

            if not os.path.exists(folder_to_save):
                os.makedirs(folder_to_save)

            file_to_save = "./tweets_csv/no_date_overlap2/" + \
                uk_date_str + "/" + city + ".csv"

            data = []

            print(file_to_save)

            if "statuses" in twitterJson.keys():

                for item in twitterJson["statuses"]:

                    tweet = item["text"]
                    tweet_time = item["created_at"]

                    row = {
                        "city": city,
                        "party": party,
                        "leader": leader,
                        "tweet": tweet,
                        "tweet_time": tweet_time
                    }

                    if isDate(tweet_time, uk_date_str):
                        data.append(row)

            writeInCsv(file_to_save, data)


def isDate(tweet_time, date):
    date_str = "Nov " + date[-2:]

    return date_str in tweet_time


def writeInCsv(file_to_save: str,  data: list) -> None:

    with open(file_to_save, 'a') as csvFile:
        fields = ['city', 'party', 'leader', 'tweet', 'tweet_time']
        writer = csv.DictWriter(csvFile, delimiter=',',
                                lineterminator='\n', fieldnames=fields)

        fileEmpty = os.stat(file_to_save).st_size == 0

        if fileEmpty:
            writer.writeheader()

        writer.writerows(data)

    print("writing completed")

    csvFile.close()


def getCityAndQuery(file_name: str) -> tuple:

    splited_file_name = file_name.split('_')

    city = splited_file_name[0]
    party = splited_file_name[2] if splited_file_name[1] == "party" else ""
    leader = splited_file_name[2] if splited_file_name[1] == "leader" else ""

    return (city, party, leader)


if __name__ == '__main__':
    main()
