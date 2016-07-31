# TwitterSentiment_2
Sentimental analysis of twitter data

### Version
 - Python 2.7.x

### Requirements
 - Tweepy (```$pip install tweepy ```)
 - Twitter app [credentials](https://apps.twitter.com)

### Usage
1. Run getdata.py to gather twitter feeds in *twitterdata.csv*
2. Hit **Ctrl+C** when you wish to stop gather more data.
3. Place the *positive-words.txt* and *negative-words.txt* in **same directory** as of *main.py*
4. Run main.py for sentimental analysis of gathered data.

### Features
 - Cleans the data before analysing.
 - Removes repeated tweets/words.
