;Excercise 2.1
 (define power
    (lambda (base n)
        (cond ((or (= base 1) (= n 0)) 1)
        (else (* base (power base (- n 1)))))))

;Excercise 2.3
(define square
    (lambda (n)
        (cond 
        [(= n 0) 0]
        [(= n 1) 1]
        [else (+ (square (- n 2))
        (- (* 4 n) 4))]
        )))

;Excercise 2.4
(define square
    (lambda (n)
        (if (= n 0)
            0
            (if (even? n)
                (*(square (/ n 2))
                4)
                (+ (square (- n 1))
                (- (+ n n) 1))))))

;Excercise 2.5
(define multiply
    (lambda (a b)
    (cond
    [(= b 0) 0]
    [else (+ (multiply a (- b 1)) a)]
    )))

;Excercise 2.17
(define presents-on-day
    (lambda (n)
        (if (= n 1)
        1
        (+ n (presents-on-day (- n 1))))))

(define presents-through-day
    (lambda (n)
        (if (= n 1) 1
        (+ (presents-on-day n) (presents-through-day (- n 1))
    ))))