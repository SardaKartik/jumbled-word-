"""
there are two player in the game 
player 2 has some word in the mind 
he will write the shuffle word 
and the player 1 has to guess the actual word is 
if he is able to this 
he will get the point 
who will get more point is the winner of the game
"""
import random

def choose():
    list=["rainbow","science","programming","acquaintance","similarity","database","player","condition","genius","reverse","name","word","answer","difficult","xylophone","water","stories","boat","theory","digital","snide","supercilious","implicit","authentic","pronounce","pronunciation","confident","expression","english","attention","categories","low","problematic","micro","sustainable","make","asking","golden","saying","make","consistently"]
    pick=random.choice(list)
    return pick

def jumblepicked_word(word):
    jumbled_word="".join(random.sample(word,len(word)))
    """cannot understand this function properly"""
    return jumbled_word

def thank(p1name,p2name,pp1,pp2):
    print(p1name," your score is ",pp1)
    print(p2name," your score is ",pp2)
    if pp1>pp2:
        print(p1name," is winner ")
    elif pp2>pp1:
        print(p2name," is winner ")
    else :
        print("wow match drawn")
    print("thank for playing ")
    print("have a niced day ")



def play():
    p1name=input("player 1 pls enter your name ")
    p2name=input("player 2 you have to input your name ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        
        #computer task 
        picked_word=choose()
        # create the question 
        qn=jumblepicked_word(picked_word)
        print(qn)
        # for player 1
        if turn%2==0:
            print(p1name," this is your turn ")
            ans=input("what is on my mind ")
            if ans==picked_word :
                pp1=pp1+1
                print(p1name," your score is ",pp1)
            else :
                print("better luck next time the word is ",picked_word)
        # for player 2
        else :
            print(p2name," this is your turn ")
            ans=input("what is on my mind ")
            if ans==picked_word :
                pp2=pp2+1
                print(p2name," your score is ",pp2)
            else :
                print("better luck next time the word is ",picked_word)
        c=int(input("press 1 for continue and 0 to quit: "))
        if c==0 :
                thank(p1name,p2name,pp1,pp2)
                break
        turn=turn+1

play()
