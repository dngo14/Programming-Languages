(lambda (x) (+ x x))
((lambda (x) (+ x x)) (* 3 4))
(let ([double (lambda (x) (+ x x))])
  (list (double (* 3 4))
        (double (/ 99 11))
        (double (- 2 7))))
(let ([f (lambda x x)])
  (f 1 2 3 4))
	
(lambda (x)
  (cons x (f x y)))
(define double-any
  (lambda (f x)
    (f x x)))
(define cadr
  (lambda (x)
    (car (cdr x))))
(define abs
  (lambda (n)
    (if (< n 0)
        (- 0 n)
        n)))
(define abs
  (lambda (n)
    (if (>= n 0)
        n
        (- 0 n))))
(define reciprocal
  (lambda (n)
    (if (= n 0)
        "oops!"
        (/ 1 n))))
(define reciprocal
  (lambda (n)
    (and (not (= n 0))
         (/ 1 n))))
(define sign
  (lambda (n)
    (if (< n 0)
        -1
        (if (> n 0)
            +1
            0))))
(sign -88.3)
(define income-tax
  (lambda (income)
    (cond
      [(<= income 10000) (* income .05)]
      [(<= income 20000) (+ (* (- income 10000) .08) 500.00)]
      [(<= income 30000) (+ (* (- income 20000) .13) 1300.00)]
      [else (+ (* (- income 30000) .21) 2600.00)])))