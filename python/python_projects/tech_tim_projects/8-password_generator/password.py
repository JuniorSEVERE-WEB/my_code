#1-Nou pral met import yo
import random # pour trouver des choses aleatoires
import string #pour trouver des listes predefinies de caracteres

#fonksyon ki pral tounen password lan

#2-#fonksyon pou ki chwazi modpass
def generator_password(min_length, numbers = True, characteres_special = True):
    digits = string.digits #tout chif yo ladan
    special = string.punctuation #tout karakte spesyal yo la
    letters = string.ascii_letters #tout alfabe yo la
    
    #3-Otorizasyon karakte
    characteres = letters #modpas lan natireman li gen let
    if numbers: #si li gen nomb
        characteres += digits #varyab karakte yo ap plede akimile chif
    if characteres_special:  #si karakte spesyal egziste
        characteres += special #varyab karakte yo ap plede akimile karakte spesyal
        
    #4-inisyalize tout bagay net avan password lan komanse pran karakte ki pral konstitiye modpass
    pwd = "" #varyab password ki gen pou ramase tout karakte yo
    has_number = False #li pa gen nomb
    has_special = False #li pa gen karakte spesyal
    meets_criteria = False #li poko ranpli krite yo(m panse)
    
    #5-yon bouk ka verifye si modpass lan valid e si li pa two kout
    while not meets_criteria and len(pwd) < min_length: #tanke password lan pa valid e tanke longe password pi piti pase min_length
        new_char = random.choice(characteres)   #nouvo varyab karakte kap pran karakte yo aleatoireman
        pwd += new_char #varyab modpass kap pran tout karakte ki te gen tan rasanble yo
        
        #6-Nou pral gad si diferan karakte yo nan modpass lan
        if new_char in digits:
            has_number = True 
        if new_char in special:
            has_special = True 
            
         #7-nou pral gad si meets_criteria ranpli kondisyon yo ak has yo
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if characteres_special:
            meets_criteria = meets_criteria and has_special
        
    return pwd 

min_length = int(input("Ekri longe ou vle modpass sa stp: "))
has_number = input("siw vle modpass sa gen chif, tape y si non tape nenpot bagay: ").lower() == "y"
has_special = input("Si w vle password lan gen karakte spesyal lan, tape y").lower() == "y"
pwd = generator_password(10, has_number, has_special)
print(pwd)                        
    
    
    
    
    
    
    
    

