



;; hear("Do you sell cheese?", is(sell(cheese))).
;; hear("I'd like some salt,", want(basket(salt))).
;; hear("Is there cheese in the basket?", is(basket(cheese))).
;; hear("Actually, I don't want milk.", not(want(basket(milk)))).
;; hear("What's in the basket?", what(basket)).

;; say("Yes, we sell cheese.", sell(milk)).
;; say("Ok, I've added salt to the basket", basket(salt)).
;; say("The basket is empty.", nothing(basket)).

;; basket(milk) :- after(add_to_basket(milk)).
;; not(basket(milk)) :- before(add_to_basket(milk)).

;; % What about generalisations?

;; % either
;; basket(X) :- after(add_to_basket(X)).

(hear "Do you sell cheese?" (is (sell cheese)))
