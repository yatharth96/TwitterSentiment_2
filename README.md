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

### License
List of positive and negative words taken from [Opinion Mining, Sentiment Analysis, and Opinion Spam Detection](https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html).

*Research Paper* - Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
      Proceedings of the ACM SIGKDD International Conference on Knowledge 
      Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
       Washington, USA
