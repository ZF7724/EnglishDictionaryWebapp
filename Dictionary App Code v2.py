import mysql.connector
import difflib
from difflib import SequenceMatcher as SM
from difflib import get_close_matches as GCM



connect=mysql.connector.connect(
        
        user="***********",
        password="********",
        host="***********",
        database="*************"
        
        
        )

def Convert(tup, di): 
    for a, b in tup: 
        di.setdefault(a, []).append(b) 
    return di 
    

def define(word):
    
    Cursor=connect.cursor()
    
    Query=Cursor.execute("SELECT * FROM Dictionary")
    
    Result=Cursor.fetchall()
    
    dictionary={}
    
    Result=Convert(Result,dictionary)
    

    
    if word in Result:
        definition=Result[word]
        return definition
    
    elif word.upper() in Result:
        definition=Result[word.upper()]
        return definition
    
    elif word.title() in Result:
        definition=Result[word.title()]
        return definition
    
        
    elif len(GCM(word,Result.keys(),cutoff=0.8))>0 :
        correction=input("Did you mean %s instead? Enter Y if yes, or N if no: " % GCM(word,Result.keys(),cutoff=0.8)[0])
        
        correction=correction.upper()
        
        if correction=="Y":
            return Result[GCM(word,Result.keys(),cutoff=0.8)[0]]
            
        elif correction=="N":
            return "Word does not exist. Please double check word."
            
        else:
            return "We did not understand your entry."
        

    
def main():
    
    word=input("Enter a word: ")
    definition=define(word)
    print(definition)
        
main()
        
        

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
















