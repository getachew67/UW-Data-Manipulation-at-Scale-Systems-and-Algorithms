import operator
import sys
import json

def main():
	tweet_file= open(sys.argv[1])
	tweets=dtext=topten=[]
	sortedtext={}	
	for line in tweet_file:
		line=line.strip()
		tweet=json.loads(line)
		if tweet.has_key('entities'):
			if tweet['entities']['hashtags']!=[]:
				for i in tweet['entities']["hashtags"]:				
					dtext.append((i['text']))
	for i in dtext:
		if i in sortedtext:
			sortedtext[i]+=1
		else:
			sortedtext[i]=1
	topten=sorted(sortedtext.items(), key=operator.itemgetter(1))			
	topten=topten[0:10]
	for i in topten:
		print str(i[0].encode('ascii','ignore'))+' ' +str(i[1])
					
				
	
			

if __name__ == '__main__':
    	main()
