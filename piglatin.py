Vowels = "AEIOU"

mystr = "RHYTHM"

index=0
cluster = ""

if(mystr[index] in Vowels):
    print(mystr+"WAY")
else:
    while index<len(mystr) and (not mystr[index] in Vowels):
        
        cluster = cluster+ mystr[index] 
        index=index+1
    print(mystr[index:]+cluster+"AY")

        

   
    
