
;
; PROBLEM:
;
; Use the How to Design Functions (HtDF) recipe to design a function that consumes an image,
; and appears to put a box around it. Note that you can do this by creating an "outline"
; rectangle that is bigger than the image, and then using overlay to put it on top of the image.
; For example:
;
; (boxify (ellipse 60 30 "solid" "red")) should produce .
;
; Remember, when we say DESIGN, we mean follow the recipe.
;
; Leave behind commented out versions of the stub and template.
;


(require 2htdp/image)

; Image -> Image
; takes an image and returns the same image with a border box added around it
(check-expect (image-width (boxify (ellipse 60 30 "solid" "red"))) 60)
(check-expect (image-height (boxify (ellipse 60 30 "solid" "red"))) 30)

; (define (boxify img) (square 30 "solid" "red"))      ; stub

;(define (boxify img)         ; template
;  (... img))

(define (boxify img)
  (overlay
    img (rectangle (image-width img) (image-height img) "outline" "black")
  )
)
