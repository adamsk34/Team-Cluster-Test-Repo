import json
import glob
import csv
import os
import datetime


# file location
files = glob.glob("./city_tweets/*" + str(datetime.date.today()) + ".json")


# Getting UK Time
uk_hour_diff = 6
uk_date = datetime.datetime.now() + datetime.timedelta(hours=uk_hour_diff)
uk_date_str = str(uk_date.year) + "_" + str(uk_date.month) + "_" + str(uk_date.day)


# Folder location to save the csv file
folder_to_save = "./tweets_csv/" + uk_date_str + "/"


def main():

    # Reading each files in the folder
    for file_path in files:
        with open(file_path, "r") as file:

            # Loading the JSON file
            twitterJson = json.load(file)

            # Getting the file name
            file_name = file_path.split('/')[2]

            city, party, leader = getCityAndQuery(file_name)

            if not os.path.exists(folder_to_save):
                os.makedirs(folder_to_save)
            
            # Creating a csv file location for each city
            file_to_save = "./tweets_csv/" + uk_date_str + "/" + city + ".csv"

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

                    data.append(row)

            writeInCsv(file_to_save, data)


#  Writing the csv file
def writeInCsv(file_to_save: str,  data: list) -> None:

    with open(file_to_save, 'a') as csvFile:
        fields = ['city', 'party', 'leader', 'tweet', 'tweet_time']
        writer = csv.DictWriter(csvFile, delimiter=',', lineterminator='\n', fieldnames=fields)

        fileEmpty = os.stat(file_to_save).st_size == 0

        if fileEmpty:
            writer.writeheader()

        writer.writerows(data)

    print("writing completed")

    csvFile.close()

# Extracting the city name, party, and leader from the file name.
def getCityAndQuery(file_name: str) -> tuple:

    splited_file_name = file_name.split('_')

    city = splited_file_name[0]
    party = splited_file_name[2] if splited_file_name[1] == "party" else ""
    leader = splited_file_name[2] if splited_file_name[1] == "leader" else ""

    return (city, party, leader)


if __name__ == '__main__':
    main()
