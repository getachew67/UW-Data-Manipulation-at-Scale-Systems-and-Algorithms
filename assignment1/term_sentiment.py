import sys
import json
from pprint import pprint
import unicodedata

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores=newterms=newscores={}
    tweets=[]
    for line in sent_file:
	term, score= line.split("\t")
    	scores[term]=int(score)
    for line in tweet_file:
	line=line.strip()
	tweets.append(json.loads(line))
    for tweet in tweets:
	if 'text' in tweet:
		tweetsplit=tweet['text'].split()
		for i in tweetsplit:
			if not scores.has_key(i):
				newterms[i]=0
    pos=neg=1
    for term in newterms:
	for tweet in tweets:
		if 'text' in tweet:
		 	if tweet['text'].find(term)>=0:
				tweetsplit=tweet['text'].split()
				for i in tweetsplit:
					if scores.has_key(i):
						if scores[i]>=0:
							pos+=scores[i]
						else:
							neg+=scores[i]
	if(pos+neg)==0:
		newterms[term]=0
	else:
		newterms[term]= (pos-neg)/(pos+neg)
	pos=neg=1
	print term + ' ' + str(newterms[term])
	
		
		


if __name__ == '__main__':
    main()
