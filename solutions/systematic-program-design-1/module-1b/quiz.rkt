
(require 2htdp/image)

;; Image, Image -> Boolean
;; takes two images and returns true when first is larger than the second
(check-expect
 (larger? (rectangle 30 50 "solid" "red") (rectangle 20 30 "solid" "red"))
 (> (* 30 50) (* 20 30))
 )

(check-expect
 (larger? (rectangle 20 30 "solid" "red") (rectangle 30 50 "solid" "red"))
 (> (* 20 30) (* 30 50))
 )

(check-expect
 (larger? (rectangle 20 20 "solid" "red") (rectangle 20 20 "solid" "red"))
 false
 )


;(define (larger? image-a image-b) false) ; stub

;(define (larger? image-a image-b)
;    (... image-a image-b))               ; template

(define (larger? image-a image-b)
  (> (* (image-width image-a) (image-height image-a)) (* (image-width image-b) (image-height image-b)))
)
