from __future__ import division
import sys
import json
from collections import defaultdict
import operator

def extract (tweet):
		try:
			country=tweet['place']['country'].encode('ascii','ignore')
			return country
		except:
			return None
def main():
	sent_file= open(sys.argv[1])
	tweet_file= open(sys.argv[2])
	tweets=[]
	scores=finalscores=happiness={}
	statesscores=numberoftweets=defaultdict(int)
	maxno=0
	for line in sent_file:
		term, score= line.split("\t")
    		scores[term]=int(score)
	for line in tweet_file:
		line=line.strip()
		tweets.append(json.loads(line))
	for tweet in tweets:
		if extract(tweet):
			country=extract(tweet)
			if country=='United States':
				place=tweet['place']['full_name'].encode('ascii','ignore')			
				state=place.split(',')[1]
				if len(state)==3:				
					text=tweet['text'].encode('ascii','ignore')	
					for word in text.split():
						for term in scores:				
							if word == term:
								statesscores[state]+=int(scores[term])
							else:
								statesscores[state]+=0
			
					numberoftweets[state]+=1						
			
	for state in statesscores:
			happiness[state]=(statesscores[state]/numberoftweets[state])
			if happiness[state]>maxno:
				maxno=happiness[state]
				maxstate=state
	print maxstate	
					
				
	
			

if __name__ == '__main__':
    	main()
