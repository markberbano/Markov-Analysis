import random

def process_file(filename):
#Formats the text so that punctuation is removed, lower-case, and readable
	fp=open(filename)
	newtext=[]
	for line in fp:
		line=line.replace('-',' ')
		for word in line.split():
			word=word.strip(string.punctuation + string.whitespace)
			word=word.lower()
			newtext.append(word)
	
	return(newtext)

def markov():
#Generates a dictionary with every prefix combination in the text and all the suffix
#options in a list
	markovdict={}
	prefix=''
	prefix_num=2
	newtext=process_file('testtext.txt')
	
	for i in range(len(newtext)):
		if i<len(newtext)-2:
			prefix=newtext[i]+' '+newtext[i+1]
			suffix=newtext[i+2]
			if prefix in markovdict:
				markovdict[prefix].append(suffix)
			
			else:
				markovdict[prefix]=[]
				markovdict[prefix].append(suffix)
				
	return(markovdict)