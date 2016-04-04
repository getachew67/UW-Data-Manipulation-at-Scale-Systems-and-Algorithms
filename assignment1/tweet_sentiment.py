import sys
import json
from pprint import pprint
import unicodedata



def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores=tweetscores={}
    for line in sent_file:
	term, score= line.split("\t")
    	scores[term]=int(score)
    for line in tweet_file:
	line=line.strip()
	tweet=json.loads(line)
	if tweet.has_key('text')=='True':
		tweetsplit=tweet['text'].split()
    		for term in scores:
			for i in tweetsplit:
				if str(i.encode('ascii','ignore'))==str(term):
					tweetscores[term]=scores[term]
				else:
					tweetscores[term]=0
    for term in tweetscores:
	print term+' '+str(tweetscores[term])


if __name__ == '__main__':
    main()
