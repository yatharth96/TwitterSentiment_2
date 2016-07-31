#Run getdata.py first.
import re
f=open('twitterdata.csv','r')
wordlist=[]
lines=f.readlines()
f.close()
print len(lines)
for line in lines:
    content=re.sub('https:.*\S?','',line).split()
    for words in content:
        if words.startswith('\\')==True or words.isdigit() or len(words)<4:
            continue
        else:
            wordlist.append(words)
wordset=set(wordlist)
positiveDB=open("positive-words.txt",'r').read().split('\n')
negativeDB=open("negative-words.txt",'r').read().split('\n')
sent,pos,neg=0,0,0
for word in wordset:
    if word in positiveDB:
        pos+=1
        sent+=1
        continue
    if word in negativeDB:
        neg+=1
        sent-=1
print "Overall Sentimental Score: ",sent
print "Positive Sentimental Score: ",pos
print "Negative Sentimental Score: ",neg
