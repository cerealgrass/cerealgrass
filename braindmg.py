# WORD UNSCRAMBLE CODE
import random
words = [
    "skibidi", "sigma", "gyatt", "munting", "hawktuah", 
    "edging", "gooning", "kneesurgery", "rizzler", "thickofit",
    "amogus", "miaw", "spitonthatthang", "gyatt", "costcoguys",  
    "mango", "thosewhoknow", "balkan", "friesinthebag", "ginger", 
    "talktuah", "diddyoil", "drakesnake", "negativeaura", "epstein", 
    "chillguy", "gimmemymoney", "trump2024", "trollface", "alphabeta"
]
# choose a word randomly
word = random.choice(words)

#split this into characters in a list
cl = list(word)

# shuffle the items in a list
random.shuffle(cl)

# put the list back into a string
s = ''
for c in cl:
    s = s + c + ' '

# while true
while True:
#display the word
    print ("/n&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print ("can you rizz this gyatt?")
    print (s)
# options Type 1 to scramble again, 2 to guess, 3 to give up:
    o = input("1 to rescramble 2 to answer and 3 to give up like a beta")
# if option 1
    if o == "1": 
        random.shuffle(cl)
        s = ''
        for x in cl:
            s+= x + " "
# elif option 2
    elif o == "2":
        gu = input("what is your word")
        if gu == word:
            print("correct! {} was the word!".format(word))
            break
        else:
            print ("WRONG")
# elif option 3
    elif o == "3":
        print("you gave up and lost every last drop of aura you had")
        break
    elif o == "i know":
        print ("consulting the book of skibidishanti you see all past,present and future possibilities of words")
        print (words)
    else:
        print("no idea what you just typed in, read the damn instructions")

# # else invalid
