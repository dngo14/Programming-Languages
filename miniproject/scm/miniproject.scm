(define intromessage (lambda ()
    (display "\nYou will be given a prompt where you must enter the prompt as quickly and as accurate as possible.\n\nPlease wrap your input with quotations (\") or the program will not run properly!\n\nPress ENTER to Continue\n")))

(define prompt (lambda ()
  (let ((n (random-integer 11)))
    (cond [(equal? n 0) "I had never seen a house on fire before, so, one evening when I heard fire engines, I ran towards the sound."]

          [(equal? n 1) "Last month a grand exhibition was held in our city. My friends and I went to see it in the evening."]

          [(equal? n 2) "He is no James Bond; his name is Roger Moore. The irony of the situation wasn't lost on anyone in the room."]

          [(equal? n 3) "He is no James Bond; his name is Roger Moore. The irony of the situation wasn't lost on anyone in the room."]

          [(equal? n 4) "She sat in the darkened room waiting. It was now a standoff. He had the power to put her in the room, but not 
          the power to make her repent. It wasn't fair and no matter how long she had to endure the darkness, she wouldn't change her attitude. 
          At three years old, Sandy's stubborn personality had already bloomed into full view."]

          [(equal? n 5) "There are only three ways to make this work. The first is to let me take care of everything. The second is for you to 
          take care of everything. The third is to split everything 50 / 50. I think the last option is the most preferable, but I'm certain it'll also mean the end of our marriage."]
          [(equal? n 6) "I haven't bailed on writing. Look, I'm generating a random paragraph at this very moment in an attempt to get my 
          writing back on track. I am making an effort. I will start writing consistently again!"]

          [(equal? n 7) "She reached her goal, exhausted. Even more chilling to her was that the euphoria that she thought she'd feel 
          upon reaching it wasn't there. Something wasn't right. Was this the only feeling she'd have for over five years of hard work?"]

          [(equal? n 8) "She considered the birds to be her friends. She'd put out food for them each morning and then she'd watch as 
          they came to the feeders to gorge themselves for the day. She wondered what they would do if something ever happened to her. 
          Would they miss the meals she provided if she failed to put out the food one morning?"]

          [(equal? n 9) "There was no time. He ran out of the door without half the stuff he needed for work, but it didn't matter. 
          He was late and if he didn't make this meeting on time, someone's life may be in danger."]

          [(equal? n 10) "He had done everything right. There had been no mistakes throughout the entire process. It had been perfection 
          and he knew it without a doubt, but the results still stared back at him with the fact that he had lost."]

          [(equal? n 11) "He looked at the sand. Picking up a handful, he wondered how many grains were in his hand. 
          Hundreds of thousands? 'Not enough,' the said under his breath. I need more."]

          [(equal? n 12) "Twenty-five stars were neatly placed on the piece of paper. There was room for five more stars 
          but they would be difficult ones to earn. It had taken years to earn the first twenty-five, and they were considered the 'easy' ones."]

          [(equal? n 13) "It's always good to bring a slower friend with you on a hike. If you happen to come across bears, 
          the whole group doesn't have to worry. Only the slowest in the group do. That was the lesson they were about to 
          learn that day."]

          [(equal? n 14) "She didn't understand how changed worked. When she looked at today compared to yesterday, there was 
          nothing that she could see that was different. Yet, when she looked at today compared to last year, she couldn't see 
          how anything was ever the same."]

          [(equal? n 15) "The clowns had taken over. And yes, they were literally clowns. Over 100 had appeared out of a 
          small VW bug that had been driven up to the bank. Now they were all inside and had taken it over."]

          [(equal? n 16) "It was going to rain. The weather forecast didn't say that, but the steel plate in his hip 
          did. He had learned over the years to trust his hip over the weatherman. It was going to rain, so he better 
          get outside and prepare."]

          [(equal? n 17) "Sometimes it's just better not to be seen. That's how Harry had always lived his life. 
          He prided himself as being the fly on the wall and the fae that blended into the crowd. That's why he 
          was so shocked that she noticed him."]

          [(equal? n 18) "I'm going to hire professional help tomorrow. I can't handle this anymore. She 
          fell over the coffee table and now there is blood in her catheter. This is much more than I ever signed up to do."]

          [(equal? n 19) "It probably seemed trivial to most people, but it mattered to Tracey. 
          She wasn't sure why it mattered so much to her, but she understood deep within her being that it mattered to 
          her. So for the 365th day in a row, Tracey sat down to eat pancakes for breakfast."]

          [(equal? n 20) "The lone lamp post of the one-street town flickered, not quite dead but definitely on its way out. 
          Suitcase by her side, she paid no heed to the light, the street or the town. A car was coming down 
          the street and with her arm outstretched and thumb in the air, she had a plan."]

          [else "The lone lamp post of the one-street town flickered, not quite dead but definitely on its way out. Suitcase by her 
          side, she paid no heed to the light, the street or the town. A car was coming down the street and with her arm outstretched and thumb in the air, she had a plan."]))))

(define userinput '())
(define displayprompt "")
(define splituser)
(define splitprompt)
(define numberprompt)
(define numberuser)

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

(define member?
  (lambda (a lat)
    (cond
      ((null? lat) #f)
      (else (or (eq? (car lat) a) ; changed eq? to equal? 
                (member? a (cdr lat)))))))

(define intersect
  (lambda (set1 set2)
    (cond
      ((null? set1)(quote ()))
      ((member (car set1) set2)
       (cons (car set1)
             (intersect (cdr set1) set2)))
      (else (intersect (cdr set1) set2)))))

(define howMany 
  (lambda (list)
   (define (iter numSoFar restOfList)
      (if (null? restOfList)  
          numSoFar
          (iter (+ numSoFar 1) (cdr restOfList))
      )
   )
   (iter 0 list)
))


(define main (lambda ()
(intromessage)
(read)
(set! displayprompt (prompt))
(display displayprompt)
(userfunction)
(set! splituser (map string (string->list (car userinput))))
(set! splitprompt (map string (string->list displayprompt)))

(define numberprompt (howMany splitprompt))
(define numberuser (howMany splituser))
(define percentcorrect (* (/ numberuser numberprompt) 100))
(display "You Are ")
(display percentcorrect)
(display "% Correct")

))
(main)