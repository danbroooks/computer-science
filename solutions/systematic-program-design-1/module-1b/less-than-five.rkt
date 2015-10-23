
;
; PROBLEM:
;
; DESIGN function that consumes a string and determines whether its length is
; less than 5.  Follow the HtDF recipe and leave behind commented out versions
; of the stub and template.
;


;; String -> Boolean
;; takes String str and returns true if its length is less than 5
(check-expect (short? "hi") true)
(check-expect (short? "ciao") true)
(check-expect (short? "hello") false)
(check-expect (short? "goodbye") false)

;(define (short? str) false) ; stub

;(define (short? str)         ; template
;  (... str))

(define (short? str)
  (> 5 (string-length str))
)
