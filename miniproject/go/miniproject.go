package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strings"
	"time"
)

type Prompts struct {
	prompt1, prompt2, prompt3, prompt4, prompt5, prompt6, prompt7, prompt8, prompt9, prompt10,
	prompt11, prompt12, prompt13, prompt14, prompt15, prompt16, prompt17, prompt18, prompt19, prompt20 string
}

func (prompts *Prompts) randomprompt() string {
	var sliceofprompts []string
	sliceofprompts = append(sliceofprompts, prompts.prompt1, prompts.prompt2, prompts.prompt3, prompts.prompt4,
		prompts.prompt5, prompts.prompt6, prompts.prompt7, prompts.prompt8, prompts.prompt9, prompts.prompt10, prompts.prompt11,
		prompts.prompt12, prompts.prompt13, prompts.prompt14, prompts.prompt15, prompts.prompt16, prompts.prompt17, prompts.prompt18,
		prompts.prompt19, prompts.prompt20)

	rand.Seed(time.Now().UnixNano())
	index := rand.Intn(len(sliceofprompts))
	returnprompt := sliceofprompts[index]
	return returnprompt
}

type Errors struct {
	listpromptwords []string
	listuserwords   []string
	errors          int
	correctentries  int
}

func (errors *Errors) finderrors(prompt string, user string) (int, int) {
	promptwords := strings.Split(prompt, " ")
	userwords := strings.Split(user, " ")

	removelast := len(userwords) - 1
	stringlength := userwords[removelast]
	userwords[removelast] = stringlength[:len(stringlength)-1]

	errors.listpromptwords = promptwords
	errors.listuserwords = userwords

	for index, _ := range errors.listuserwords {
		if index <= len(errors.listuserwords) {
			if errors.listpromptwords[index] == errors.listuserwords[index] {
				errors.correctentries += 1
				continue
			} else {
				errors.errors += 1
			}
		} else {
			if errors.listpromptwords[index] == errors.listuserwords[index] {
				if errors.listpromptwords[index+1] == errors.listuserwords[index+1] && errors.listpromptwords[index-1] == errors.listuserwords[index-1] {
					errors.correctentries += 1
					continue
				} else {
					errors.errors += 1
				}
			} else {
				errors.errors += 1
			}
		}
	}
	return errors.errors, errors.correctentries
}

func (errors *Errors) typingspeed(userinput string, time float64) (float64, float64) {
	characters := (strings.Split(userinput, ""))
	characters = characters[:len(characters)-1]
	characterscount := float64(len(characters))
	grosswpm := (characterscount / 5) / time
	netwpm := ((characterscount / 5) - float64(errors.errors)) / time

	grosswpm *= 100
	netwpm *= 100

	return grosswpm, netwpm

}

func typingaccuracy(correctentries int, prompt string) float64 {
	promptedit := strings.Split(prompt, " ")
	promptedit = promptedit[:len(promptedit)-1]
	promptlength := float64(len(promptedit))

	accuracy := 100 * (float64(correctentries-1) / promptlength)

	return accuracy
}

type Words struct {
	listofwords []string
}

func (words *Words) chooserandomword() string {
	rand.Seed(time.Now().UnixNano())
	index := rand.Intn(len(words.listofwords))

	return words.listofwords[index]
}

const time_in_seconds = 60

var score int

func userinput(word *Words, time *time.Timer) {
	errors := 0
	score = 0

	for {
		outputword := word.chooserandomword()
		fmt.Println(outputword)
		var userword string
		fmt.Scanln(&userword)

		if userword == outputword {
			score += 1
			fmt.Println("Score:", score, "Errors:", errors)
		} else {
			errors += 1
			fmt.Println("Score:", score, "Errors:", errors)
		}
	}
}

func main() {

	fmt.Println("Type SpeedTest to play typing speed test game\nType TimedWord to play timed typing word game:")
	var gamemode string
	fmt.Scanln(&gamemode)

	if gamemode == "TimedWord" {
		listofwords := []string{"hello", "computer", "Daniel", "Software", "Keyboard", "WiFi", "remote", "robot",
			"camera", "baker", "laptop", "Tech Guy", "Olaf", "Skoglund", "Holland", "Larson", "Ellingson",
			"water", "microwave", "whiteboard", "science", "Python", "C++", "Go", "Java", "Javascript",
			"HTML", "CSS", "RGB", "lamp", "coding", "headphones", "earbuds", "mouse", "pencil", "pen"}
		words := Words{listofwords}

		timer := time.NewTimer(time.Second * time_in_seconds)

		defer timer.Stop()

		fmt.Println("START")

		go userinput(&words, timer)
		{
			<-timer.C
			fmt.Printf("Congratulations! Your final score is %d after %d seconds.", score, time_in_seconds)
		}
	} else if gamemode == "SpeedTest" {
		prompts := Prompts{"I had never seen a house on fire before, so, one evening when I heard fire engines, I ran towards the sound.",
			"Last month a grand exhibition was held in our city. My friends and I went to see it in the evening.",
			"He is no James Bond; his name is Roger Moore. The irony of the situation wasn't lost on anyone in the room.",
			"The lone lamp post of the one-street town flickered, not quite dead but definitely on its way out. Suitcase by her side, she paid no heed to the light, the street or the town. A car was coming down the street and with her arm outstretched and thumb in the air, she had a plan.",
			"She sat in the darkened room waiting. It was now a standoff. He had the power to put her in the room, but not the power to make her repent. It wasn't fair and no matter how long she had to endure the darkness, she wouldn't change her attitude. At three years old, Sandy's stubborn personality had already bloomed into full view.",
			"There are only three ways to make this work. The first is to let me take care of everything. The second is for you to take care of everything. The third is to split everything 50 / 50. I think the last option is the most preferable, but I'm certain it'll also mean the end of our marriage.",
			"I haven't bailed on writing. Look, I'm generating a random paragraph at this very moment in an attempt to get my writing back on track. I am making an effort. I will start writing consistently again!",
			"She reached her goal, exhausted. Even more chilling to her was that the euphoria that she thought she'd feel upon reaching it wasn't there. Something wasn't right. Was this the only feeling she'd have for over five years of hard work?",
			"She considered the birds to be her friends. She'd put out food for them each morning and then she'd watch as they came to the feeders to gorge themselves for the day. She wondered what they would do if something ever happened to her. Would they miss the meals she provided if she failed to put out the food one morning?",
			"There was no time. He ran out of the door without half the stuff he needed for work, but it didn't matter. He was late and if he didn't make this meeting on time, someone's life may be in danger.",
			"He had done everything right. There had been no mistakes throughout the entire process. It had been perfection and he knew it without a doubt, but the results still stared back at him with the fact that he had lost.",
			"He looked at the sand. Picking up a handful, he wondered how many grains were in his hand. Hundreds of thousands? 'Not enough,' the said under his breath. I need more.",
			"Twenty-five stars were neatly placed on the piece of paper. There was room for five more stars but they would be difficult ones to earn. It had taken years to earn the first twenty-five, and they were considered the 'easy' ones.",
			"It's always good to bring a slower friend with you on a hike. If you happen to come across bears, the whole group doesn't have to worry. Only the slowest in the group do. That was the lesson they were about to learn that day.",
			"She didn't understand how changed worked. When she looked at today compared to yesterday, there was nothing that she could see that was different. Yet, when she looked at today compared to last year, she couldn't see how anything was ever the same.",
			"The clowns had taken over. And yes, they were literally clowns. Over 100 had appeared out of a small VW bug that had been driven up to the bank. Now they were all inside and had taken it over.",
			"It was going to rain. The weather forecast didn't say that, but the steel plate in his hip did. He had learned over the years to trust his hip over the weatherman. It was going to rain, so he better get outside and prepare.",
			"Sometimes it's just better not to be seen. That's how Harry had always lived his life. He prided himself as being the fly on the wall and the fae that blended into the crowd. That's why he was so shocked that she noticed him.",
			"I'm going to hire professional help tomorrow. I can't handle this anymore. She fell over the coffee table and now there is blood in her catheter. This is much more than I ever signed up to do.",
			"It probably seemed trivial to most people, but it mattered to Tracey. She wasn't sure why it mattered so much to her, but she understood deep within her being that it mattered to her. So for the 365th day in a row, Tracey sat down to eat pancakes for breakfast."}

		start := time.Now()

		prompt := prompts.randomprompt()
		fmt.Println(prompt)

		reader := bufio.NewReader(os.Stdin)
		var userinput string
		userinput, _ = reader.ReadString('\n')

		end := float64(time.Since(start) / time.Second)

		errors := Errors{nil, nil, 0, 0}

		errorcount, correctcount := errors.finderrors(prompt, userinput)
		grosswpm, netwpm := errors.typingspeed(userinput, end)
		accuracy := typingaccuracy(correctcount, prompt)

		fmt.Println("Overview\nYou had", errorcount, "errors\nAccuracy: ", accuracy, "%\nNetWPM: ", netwpm, "\nGrossWPM: ", grosswpm)
	} else {
		fmt.Println("That is not an input, try again")
	}
}
