import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.*;

/*
 * Version:2.0
 * Note: RAW_DATA folder should have the B1-B12 folders containing raw data and SENTIMENT_DATA folder should have B1-B12 folders which should be empty
 * Please refer README.txt for documentation
 */
public class Sentimental {

  public static void main(String[] args) {

    /************************************************************************************************
     * **********READS THE AFINN-111.CSV AND CREATS A HASH MAP WHERE THE WORD IS THE
     * KEY*************** *****************AND THE CORESSPONDING SENTIMENTAL VALUE
     * IS THE VALUE************************
     * *********************************************************************************************
     */

    HashMap<String, Integer> afinn_hash_map = new HashMap<String, Integer>();

    try {

      FileReader fileRdr = new FileReader("AFINN-111.csv");

      // Open a BufferedReader.
      BufferedReader inFile = new BufferedReader(fileRdr);

      // Read the file line-by-line
      String line;
      do {
        line = inFile.readLine();
        if (line != null) {

          String[] afinn = line.split(",");
          String word = afinn[0];
          int sentimentValue = Integer.parseInt(afinn[1]);
          afinn_hash_map.put(word, sentimentValue);
        }
      } while (line != null);
      inFile.close();
    } // try
    catch (IOException e) {

      System.out.println("Failed to read the data file" + e.getMessage());

    } // catch

    /**********************************************************************************************
     * *******************************************************************************************
     * *******************************************************************************************
     * *******************************************************************************************
     */

    /************************************************************************************************
     * **********READS THE city.CSV AND CREATS ANOTHER FILE NAMED
     * citySentiment.CSV*************** **********WHERE THE tweet OF THE city.CSV IS
     * REPLACED WITH ITS CORRESPONDINGVALUE******************
     * *******************************SENTIMENTAL VALUE.
     * ************************************************ *********NOTE: DOWNLOAD THE
     * RAW_DATA AND SENTIMENT_DATA FOLDER TO DESKTOP AND RUN THE CODE***************
     * *********************************************************************************************
     */

    String[] city = { "aberdeen", "belfast", "birmingham", "cardiff", "derry", "edinburgh", "glasgow", "lisburn",
        "liverpool", "london", "newport", "swansea" };
    int batches = 12;
    int date = 18;

    for (int b = 1; b < batches + 1; b++) {
      for (int c = 0; c < city.length; c++) {

        try {
          String path = System.getProperty("user.dir");

          FileReader fileRdr_2 = new FileReader(
              path + "\\tweets_csv\\no_date_overlap\\2019_11_" + date + "\\" + city[c] + ".csv");
          new File(path + "\\SENTIMENT_DATA\\B" + b).mkdirs();
          PrintWriter outFile = new PrintWriter(
              new FileWriter(path + "\\SENTIMENT_DATA\\B" + b + "\\" + city[c] + "Sentiment.csv"));
          outFile.println("City," + "Party," + "Leader," + "Sentiment Value");
          // Open a BufferedReader.
          BufferedReader inFile_2 = new BufferedReader(fileRdr_2);

          // Read the file line-by-line
          String line_2;
          line_2 = inFile_2.readLine();
          while (line_2 != null) {
            line_2 = inFile_2.readLine();
            if (line_2 != null) {
              String[] data = line_2.split(",");
              if (data.length > 3) {
                String longTweet = "";
                for (int i = 3; i < data.length; i++) {
                  if (i == data.length) {
                    longTweet = (longTweet + data[i] + " ");
                  } // if
                  else {
                    longTweet = (longTweet + data[i]);
                  } // else
                } // for
                float sentimentValue = calculateSentiment(longTweet, afinn_hash_map);
                if (isClean(data[0], data[1], data[2])) {
                  outFile.println(data[0] + "," + data[1] + "," + data[2] + "," + sentimentValue); // city party
                }
              } // if
            } // if
          } // while
          outFile.close();
          inFile_2.close();
        } // try
        catch (IOException e) {

          System.out.println("Failed to read the data file" + e.getMessage());

        } // catch

        /**********************************************************************************************
         * *******************************************************************************************
         * *******************************************************************************************
         * *******************************************************************************************
         */
      } // for changing city
      date++;
    } // for changing directory
  }// main

  /*
   * Gives a sentimental value to each tweet by adding each words value from the
   * AFINN-111.csv file and dividing the value with the length of the tweet (no.
   * of words) so that we can give proper weight to the tweet.
   */
  public static float calculateSentiment(String tweet, HashMap<String, Integer> afinn_hash_map) {
    float result = 0;
    tweet.toLowerCase();
    String[] tweetSplit = tweet.split("\\s+");

    for (int i = 0; i < tweetSplit.length; i++) {
      if (afinn_hash_map.containsKey(tweetSplit[i])) {
        result += afinn_hash_map.get(tweetSplit[i]);
      } // if
      else if ((i < tweetSplit.length - 1) && (afinn_hash_map.containsKey(tweetSplit[i] + " " + tweetSplit[i + 1]))) {
        result += afinn_hash_map.get(tweetSplit[i] + " " + tweetSplit[i + 1]);
      } // elseif
      else if ((i < tweetSplit.length - 2)
          && (afinn_hash_map.containsKey(tweetSplit[i] + " " + tweetSplit[i + 1] + " " + tweetSplit[i + 2]))) {
        result += afinn_hash_map.get(tweetSplit[i] + " " + tweetSplit[i + 1] + " " + tweetSplit[i + 2]);
      } // elseif

    } // for
    result = result / (tweetSplit.length);
    return result;
  }// calculateSentiment

  public static boolean isClean(String city, String party, String leader) {

    boolean resultCity = false;
    boolean resultParty = false;
    boolean resultLeader = false;

    String[] citys = { "aberdeen", "belfast", "birmingham", "cardiff", "derry", "edinburgh", "glasgow", "lisburn",
        "liverpool", "london", "newport", "swansea" };
    String[] parties = { "", "Brexit-Party", "Conservative-Party", "Labour-Party", "Liberal-Democrats" };
    String[] leaders = { "", "Jeremy-Corbyn", "Boris-Johnson", "Jo-Swinson", "Nigel-Farage" };

    for (int i = 0; i < citys.length; i++) {

      if (city.contentEquals(citys[i])) {
        resultCity = true;
      }
    }

    for (int j = 0; j < parties.length; j++) {

      if (party.contentEquals(parties[j])) {
        resultParty = true;
      }
    }

    for (int k = 0; k < leaders.length; k++) {

      if (leader.contentEquals(leaders[k])) {
        resultLeader = true;
      }
    }

    return (resultCity && resultParty && resultLeader);
  }// isClean

}// Sentimental
