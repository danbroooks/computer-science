
;
; PROBLEM:
;
; Write a function that consumes two numbers and produces the larger of the two.
;


(define (maximum a b)
  (if (> a b) a b)
)

(maximum 3 3)

(maximum 7 42)

(maximum 106 78)