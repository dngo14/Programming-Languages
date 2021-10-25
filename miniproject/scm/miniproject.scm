#!/usr/local/dept/bin/mzscheme
#lang scheme/base

(require racket/system)

(define intromessage (lambda ()
    (display "You will be given a prompt, where you must enter the prompt as quickly and as accurate as possible\n\n")))

(define prompt (lambda ()
  (let ((n (random-integer 11)))
    (cond [(equal? n 0) "I had never seen a house on fire before, so, one evening when I heard fire engines, I ran towards the sound.\n"]
          [(equal? n 1) "Last month a grand exhibition was held in our city. My friends and I went to see it in the evening.\n"]
          [(equal? n 2) "He is no James Bond; his name is Roger Moore. The irony of the situation wasn't lost on anyone in the room.\n"]
          [(equal? n 3) "He is no James Bond; his name is Roger Moore. The irony of the situation wasn't lost on anyone in the room.\n"]
          [(equal? n 4) "She sat in the darkened room waiting. It was now a standoff. He had the power to put her in the room, but not the 
          power to make her repent. It wasn't fair and no matter how long she had to endure the darkness, she wouldn't change her attitude. 
          At three years old, Sandy's stubborn personality had already bloomed into full view.\n"]
          [(equal? n 5) "There are only three ways to make this work. The first is to let me take care of everything. 
          The second is for you to take care of everything. The third is to split everything 50 / 50. I think the last 
          option is the most preferable, but I'm certain it'll also mean the end of our marriage.\n"]
          [(equal? n 6) "I haven't bailed on writing. Look, I'm generating a random paragraph at this very moment in an attempt to get my 
          writing back on track. I am making an effort. I will start writing consistently again!\n"]
          [(equal? n 7) "She reached her goal, exhausted. Even more chilling to her was that the euphoria that she thought she'd feel 
          upon reaching it wasn't there. Something wasn't right. Was this the only feeling she'd have for over five years of hard work?\n"]
          [(equal? n 8) "She considered the birds to be her friends. She'd put out food for them each morning and then she'd watch as 
          they came to the feeders to gorge themselves for the day. She wondered what they would do if something ever happened to her. 
          Would they miss the meals she provided if she failed to put out the food one morning?\n"]
          [(equal? n 9) "There was no time. He ran out of the door without half the stuff he needed for work, but it didn't matter. 
          He was late and if he didn't make this meeting on time, someone's life may be in danger.\n"]
          [(equal? n 10) "He had done everything right. There had been no mistakes throughout the entire process. It had been perfection and he 
          knew it without a doubt, but the results still stared back at him with the fact that he had lost.\n"]
          [else "The lone lamp post of the one-street town flickered, not quite dead but definitely on its way out. Suitcase by her side, 
          she paid no heed to the light, the street or the town. A car was coming down the street and with her arm outstretched and thumb in the air, she had a plan.\n"]))))

(define userinput '())
(define displayprompt "")

(define (slist->string slst)
  (cond ((empty? slst) "")
        ((empty? (rest slst)) (symbol->string (first slst)))
        (else (string-append (symbol->string (first slst))
                             " "
                             (slist->string (rest slst))))))

(define userfunction
  (lambda ()
    (let loop ((input (read)))
      (if (string? input)
          (begin (set! userinput (append userinput (list input)))
                 (loop))
          'done
          ))
          ))

(define checkerrors 
  (lambda (userinput prompt)
   (display "hi")
  ))

(define main (lambda ()
(intromessage)
(set! displayprompt (prompt))
(display displayprompt)
(userfunction)
))
(main)

(define main2 
(lambda()
  
))

(main2)