#imports
import time
import random

def prompts(): #function to choose a randome prompt
    prompt1 =" I had never seen a house on fire before, so, one evening when I heard fire engines"\
    #"with loud alarm bells rushing past my house. I quickly ran out and, a few streets away, joined a large"\
    #"crowd of people. We could see the fire only from a distance because the police would not allow any one near the building on fire"\
    #"What a terrible scene I saw that day! Huge flames of fire were coming out of each floor, and black and thick smoke spread all around."\
    #"Four fire engines were engaged and the firemen in their uniform were playing the hose on various parts of the building."\
    #"Then the tall ladders of the fire engine were stretched upwards. Some firemen climbed up with hoses in their hands."\
    #"The continuous flooding brought the fire under control but the building was completely destroyed."

    prompt2 = "Last month a grand exhibition was held in our city. My friends and I went to see it in evening."\
    #"Our first impression on entering the grounds was that whole thing looked like a fairyland. The vast space was"\
    #"decorated in magnificent, bright and purple colour and lit up with countless lights. Men, women and children were"\
    #"moving from corner to corner, admiring the beauty of all kinds of stalls set up. These stalls were like small shops."\
    #"While the stalls made a very interesting sight, what attracted us most was the Children's Corner in the exhibition."\
    #"The Children's Corner was crowded with boys and girls. All types of amusements could be seen here. Children and some grown-ups"\
    #"were enjoying the giant wheel, wooden hoses, dodge-cars, railway train and other things. I too had my share of fun with my friends"\
    #"and returned home after enjoying a most delightful evening."

    listofprompts = [prompt1, prompt2]

    x = random.choice(listofprompts)
    return x

def finderrors(prompt, userinput): #function to find errors
    errors = 0

    promptwords = prompt.split()
    userwords = userinput.split()

def elapsedtime(start, end): #function to find elapsed time
    time = (end - start)
    return time

def typingspeed(userinput, errors, time): #function to find typing speed
    characters = len(list(userinput))
    grosswpm = (characters/5)/time
    netwpm = ((characters/5)-errors)/time
    print(characters)

#def typingaccuracy(): #function to find percent accuracy

    

if __name__ == '__main__':
    prompt = prompts()
    input("To start, press enter: ")
    print(prompt)
    start = time.time()
    userinput = input()
    end = time.time()

    usertime = elapsedtime(start, end)
    errors = finderrors(prompt, userinput)
    typingspeed(userinput, errors, usertime)
    
    
    
    print(usertime)
    print (userinput)
