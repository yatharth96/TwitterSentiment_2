from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
import sys

#Enter twitter app credentials here
CONSUMER_KEY=""
CONSUMER_SECRET=""
ACESS_TOKEN=""
ACCESS_TOKEN_SECRET=""

class listener(StreamListener):    
    def on_data(self,data):
        
        tweet=data.split('''"text":"''')[1].split('''","source"''')[0]
        print tweet
        print "============================================================================="
        fh=open("twitterdata.csv",'a')
        fh.write(tweet)
        fh.write('\n')
        fh.write("======================================================================================")
        fh.write("\n")         
        fh.close()
        return True
        
    def on_error(self,status):
        print status

auth=OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

# Enter the tag/tags you want to search tweets about
try:
    twitterStream=Stream(auth,listener())
    twitterStream.filter(track=["<Enter tags here>"],languages=["en"])
except KeyboardInterrupt:
    print "Terminated by user"
    print "All tweets saved to :",os.path.join(os.getcwd(),'twitterdata.csv')
    sys.exit()
