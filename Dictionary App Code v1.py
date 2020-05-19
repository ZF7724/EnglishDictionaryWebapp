import json
import difflib
from difflib import SequenceMatcher as SM
from difflib import get_close_matches as GCM




data=json.load(open("data.json",'r'))

def define(word):
    
    word=word.lower()
    
    if word in data:
        definition=data[word]
        return definition
    
    elif word.title() in data:
        definition=data[word.title()]
        return definition
    
    elif word.upper() in data:
        definition=data[word.upper()]
        return definition
    
    
    elif len(GCM(word.title(),data.keys(),cutoff=0.8))>0 :
        correction=input("Did you mean %s instead? Enter Y if yes, or N if no: " % GCM(word.title(),data.keys(),cutoff=0.8)[0])
        
        correction=correction.upper()
        
        if correction=="Y":
            return data[GCM(word.title(),data.keys(),cutoff=0.8)[0]]
            
        elif correction=="N":
            return "Word does not exist. Please double check word."
            
        else:
            return "We did not understand your entry."
            
    
    
    elif len(GCM(word.upper(),data.keys(),cutoff=0.8))>0 :
        correction=input("Did you mean %s instead? Enter Y if yes, or N if no: " % GCM(word.upper(),data.keys(),cutoff=0.8)[0])
        
        correction=correction.upper()
        
        if correction=="Y":
            return data[GCM(word.upper(),data.keys(),cutoff=0.8)[0]]
            
        elif correction=="N":
            return "Word does not exist. Please double check word."
            
        else:
            return "We did not understand your entry."
    
    
       
    
    elif len(GCM(word,data.keys(),cutoff=0.8))>0 :
        correction=input("Did you mean %s instead? Enter Y if yes, or N if no: " % GCM(word,data.keys(),cutoff=0.8)[0])
        
        correction=correction.upper()
        
        if correction=="Y":
            return data[GCM(word,data.keys(),cutoff=0.8)[0]]
            
        elif correction=="N":
            return "Word does not exist. Please double check word."
            
        else:
            return "We did not understand your entry."
            
            


def main():
    
    word=input("Enter a word: ")
    
    Definition=define(word)
    
    if type(Definition)==list:
        
        for words in Definition:
            print(words)
    
    else:
        print(Definition)
    
            
            

main()
