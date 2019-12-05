Version:3.0

To compile the code:
```
javac Sentimental.java
```

To run the code:
```
java Sentimental
```

Sentimental.java reads the raw tweets from the path `tweets_csv/no_date_overlap/`
and writes the Sentimental .csv files in the following path `SENTIMENTAL_DATA/`

Sentimental.java has been tested on Windows 10 and Linux Mint 19.1.

Functions:

(I) public static float calculateSentiment(String tweet, HashMap<String, Integer> afinn_hash_map )

Parameters: calculateSentiment fucntion requires 2 parameters where the 1st one is the tweets which is in String 
and the 2nd one is a HashMap containing the AFINN-111 values where the key is the word (String) and
the value is the corresponding sentiment value (int).

Discription:The function takes a String i.e. a tweet and assigns a Sentiment value by searching each word or 
upto 3 words as a key in the HashMap and summing up the value and dividing it with the length of the tweet 

Return: The funtion returns a float value

Example: 
The function gets the following tweet "I can't stand the person because he cheated in the exam" and the AFINN-111
HashMap. To assign a weighted sentiment value to the tweet with the following steps:

1) Search each word in the AFINN-111 HashMap and get the sum of the value
KEY         : VALUE (as in the AFINN-111 HashMap)
can't stand : -3
cheated     : -3

The sum of the value =  -6

2) Divide the sum with the length of the tweet to assign the weighted sentiment value
The length of the tweet (number of words) = 11
The weighted sentiment value = (-6)/11 = -0.5454545455

Note: We divide the sum by the length of the tweet as we want to give a proper weight to the sentiment value

(II) public static boolean isClean(String city, String party, String leader)

Parameters: isClean function requires 3 parameters (Strings) where the 1st is the name of the city, 
2nd is the name of the party and the 3rd is the name of the leader.

Discription: This function takes the 3 strings and compare it with the city, party name and political leader
which we need, allowing us to clean the data so that we can avoide noise as splitting the tweet.csv files
lead to the sentimental.csv having uncessary data.

Returns: The function returns true if the data is clean. 

(III) Main function

In the main function there are 2 try catch. 1st try catch reads the AFINN-111.csv file and creates a 
hash map.
2nd try catch reads the tweet.csv files and write a corresponding sentiment.csv file where it writes the following columns
City, Party and Sentiment Value. 

