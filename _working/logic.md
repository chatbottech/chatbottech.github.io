Ideas for implementing a probabilistic logic reasoning system
=============================================================

Shopping example
----------------


We can buy three things: milk, cheese and bread.

Possibilities:
 - The user could want no items, one, or two items or all three items.
 - The basket can contain any combination of items (at most one of each for now)
 - We need to get to a point where the user is satisfied
 

Possible queries:
 - What do you sell?
   - I want to know the items that are for sale
   - want(i, know(i, all(X, sell(X)))).
   - want(i, know(i, items-for-sale)).
   - what(sell).
   - want(i, know(i, what(sell))).
 - Do you sell milk?
   - I want to know if milk is for sale
   - want(i, know(i, sell(milk))).
   - whether(sell(milk)).  [whether is question semantics defined by Karttunen 77]
   - want(i, know(i, whether(sell(milk)))).
 - Do you sell salt?
 - I'd like some cheese
   - I'd like there to be cheese in the basket
   - want(i, basket(cheese)).
 - Have you added cheese to the basket?
   - I want to know if there is cheese in the basket
   - want(i, know(i, basket(cheese))).
   - whether(basket(cheese)).
   - want(i, know(i, whether(basket(cheese)))).
 - What's in the basket?
   - I want to know the items that are in the basket
   - what(basket).
   - want(i, know(i, what(basket))).
 - Actually I don't want milk
   - I want there to not be milk in the basket
   - want(i, ~basket(milk)).
 - I don't want to know what's in the basket
   - ~want(i, know(i, what(basket))).

Actions:
 - _add milk to basket_
   - Precondition: ~basket(milk).
   - Postcondition: basket(milk).

Possible replies:
 - We sell milk, cheese and bread
    - sell(milk) & sell(cheese) & sell(bread).
 - Yes, we sell milk
    - sell(milk).
 - No, we don't sell salt
    - ~sell(salt).
 - Ok, I've added cheese to the basket
    - basket(cheese).
 - Yes, there is cheese in the basket
    - basket(cheese).
 - There is milk and cheese in the basket
    - basket(cheese) & basket(milk).
 - There is nothing in the basket
    - basket(empty).
 - Ok, I've removed milk from the basket
    - ~basket(milk).
 - There is no milk in the basket
    - ~basket(milk).


Knowledge

sell(milk).
sell(cheese).
sell(bread).
~sell(salt).

Initial state

~basket(milk).
~basket(cheese).
~basket(bread).
