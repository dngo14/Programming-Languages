#imports
import time
import random
import threading

def prompts(): #function to choose a random prompt
    prompt1 = "I had never seen a house on fire before, so, one evening when I heard fire engines, I ran towards the sound"
 
    prompt2 = "Last month a grand exhibition was held in our city. My friends and I went to see it in the evening."

    prompt3 = "He is no James Bond; his name is Roger Moore. The irony of the situation wasn't lost on anyone in the room."

    prompt4 = "The lone lamp post of the one-street town flickered, not quite dead but definitely on its way out. Suitcase by her side, she paid no heed to the light, the street or the town. A car was coming down the street and with her arm outstretched and thumb in the air, she had a plan."

    prompt5 = "She sat in the darkened room waiting. It was now a standoff. He had the power to put her in the room, but not the power to make her repent. It wasn't fair and no matter how long she had to endure the darkness, she wouldn't change her attitude. At three years old, Sandy's stubborn personality had already bloomed into full view."

    prompt6 = "There are only three ways to make this work. The first is to let me take care of everything. The second is for you to take care of everything. The third is to split everything 50 / 50. I think the last option is the most preferable, but I'm certain it'll also mean the end of our marriage."

    prompt7 = "I haven't bailed on writing. Look, I'm generating a random paragraph at this very moment in an attempt to get my writing back on track. I am making an effort. I will start writing consistently again!"

    prompt8 = "She reached her goal, exhausted. Even more chilling to her was that the euphoria that she thought she'd feel upon reaching it wasn't there. Something wasn't right. Was this the only feeling she'd have for over five years of hard work?"

    prompt9 = "She considered the birds to be her friends. She'd put out food for them each morning and then she'd watch as they came to the feeders to gorge themselves for the day. She wondered what they would do if something ever happened to her. Would they miss the meals she provided if she failed to put out the food one morning?"

    prompt10 = "There was no time. He ran out of the door without half the stuff he needed for work, but it didn't matter. He was late and if he didn't make this meeting on time, someone's life may be in danger."

    prompt11 = "He had done everything right. There had been no mistakes throughout the entire process. It had been perfection and he knew it without a doubt, but the results still stared back at him with the fact that he had lost."

    prompt12 = "He looked at the sand. Picking up a handful, he wondered how many grains were in his hand. Hundreds of thousands? 'Not enough,' the said under his breath. I need more."

    prompt13 = "Twenty-five stars were neatly placed on the piece of paper. There was room for five more stars but they would be difficult ones to earn. It had taken years to earn the first twenty-five, and they were considered the 'easy' ones."

    prompt14 = "It's always good to bring a slower friend with you on a hike. If you happen to come across bears, the whole group doesn't have to worry. Only the slowest in the group do. That was the lesson they were about to learn that day."

    prompt15 = "She didn't understand how changed worked. When she looked at today compared to yesterday, there was nothing that she could see that was different. Yet, when she looked at today compared to last year, she couldn't see how anything was ever the same."

    prompt16 = "The clowns had taken over. And yes, they were literally clowns. Over 100 had appeared out of a small VW bug that had been driven up to the bank. Now they were all inside and had taken it over."

    prompt17 = "It was going to rain. The weather forecast didn't say that, but the steel plate in his hip did. He had learned over the years to trust his hip over the weatherman. It was going to rain, so he better get outside and prepare."

    prompt18 = "Sometimes it's just better not to be seen. That's how Harry had always lived his life. He prided himself as being the fly on the wall and the fae that blended into the crowd. That's why he was so shocked that she noticed him."

    prompt19 = "I'm going to hire professional help tomorrow. I can't handle this anymore. She fell over the coffee table and now there is blood in her catheter. This is much more than I ever signed up to do."

    prompt20 = "It probably seemed trivial to most people, but it mattered to Tracey. She wasn't sure why it mattered so much to her, but she understood deep within her being that it mattered to her. So for the 365th day in a row, Tracey sat down to eat pancakes for breakfast."


    listofprompts = [prompt1, prompt2, prompt3, prompt4, prompt5, prompt6, prompt7, prompt8, prompt9, prompt10,
    prompt11, prompt12, prompt13, prompt14, prompt15, prompt16, prompt17, prompt18, prompt19, prompt20]
    x = random.choice(listofprompts)

    return x

def finderrors(prompt, userinput): #function to find errors
    promptwords = prompt.split()
    userwords = userinput.split()
    errors = 0
    correctentries = 0
    for index in range(len(userwords)):
        if index in (0, len(userwords)-1):
            if userwords[index] == promptwords[index]:
                correctentries+=1
                continue
            else:
                errors+=1
        else:
            if userwords[index] == promptwords[index]:
                if (userwords[index+1] == promptwords[index+1]) & (userwords[index-1] == promptwords[index-1]):
                    correctentries+=1
                    continue
                else:
                    errors+=1
            else:
                errors+=1

    promptspaces = promptwords.count(" ")
    userspaces = userwords.count(" ")
    spaceerrors = abs(promptspaces - userspaces)
    errors += spaceerrors

    return errors, correctentries

        
def elapsedtime(start, end): #function to find elapsed time
    time = (end - start)

    return time

def typingspeed(userinput, errors, time): #function to find typing speed
    characters = len(list(userinput))
    grosswpm = (characters/5)/time
    netwpm = ((characters/5)-errors)/time
    netwpm*=100
    grosswpm*=100

    return netwpm, grosswpm

def typingaccuracy(correctentries, prompt): #function to find percent accuracy
    promptlength = len(prompt.split())
    accuracy = 100*(correctentries/promptlength)
    
    return accuracy

# Code for random word generator

def words(): #Get a random word
    listofwords = ["hello", "computer", "Daniel", "Software", "Keyboard", "WiFi", "remote", "robot",
    "camera", "baker", "laptop", "Tech Guy", "Olaf", "Skoglund", "Holland", "Larson", "Ellingson",
    "water", "microwave", "whiteboard", "science", "Python", "C++", "Go", "Java", "Javascript",
    "HTML", "CSS", "RGB", "lamp", "coding", "headphones", "earbuds", "mouse", "pencil", "pen"]

    x = random.choice(listofwords)

    return x

score = 0
errors = 0

def checkwords(userword, word): #check if the user typed the right answer and display time left
    global score
    global errors
    global my_timer

    if (userword == word):
        score = score+1
        print("score: {}".format(score), my_timer, "seconds left")
    else:
        errors+=1
        print("score: {}".format(score), my_timer, "seconds left")


def timer(): #starts the timer
    global my_timer
    my_timer = 60
    while my_timer > 0:
        time.sleep(1)
        my_timer -= 1

def usertype(): #gets user input
    while my_timer > 0:
        word = words()
        print(word)
        userword = input()
        checkwords(userword, word)

    print("IN 60 SECONDS\nFinal Score: {}\nErrors: {}\n".format(score, errors))


    
def main(): #main function of the game
    input("TO START, PRESS ENTER\n")
    gamemode = input("Type SpeedTest to play typing speed test game\
    \nType TimedWord to play timed typing word game\n:  ")

    if (gamemode == "SpeedTest"):
        print("Starting Speed Test")
        prompt = prompts()
        print(prompt)
        start = time.time()
        userinput = input()
        end = time.time()

        usertime = elapsedtime(start, end)
        errors, correctentries = finderrors(prompt, userinput)
        netwpm, grosswpm = typingspeed(userinput, errors, usertime)
        accuracy = typingaccuracy(correctentries, prompt)
        
        print("You had {} errors\nAccuracy: {}%\nNetWPM: {}\nGrossWPM: {}\nTime: {} seconds".format(errors, round(accuracy,2), round(netwpm,2), round(grosswpm,2), round(usertime,2)))
    elif (gamemode == "TimedWord"):
        print("Starting Timed Word Game")
        thread1 = threading.Thread(target=timer)
        thread2 = threading.Thread(target=usertype)
        thread1.start()
        thread2.start()


    else:
        print("That is not an input, try again")

if __name__ == '__main__':
    main()