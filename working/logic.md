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
 - Do you sell milk?
   - I want to know if milk is for sale
   - want(i, know(i, sell(milk))).
 - Do you sell salt?
 - I'd like some cheese
   - I'd like there to be cheese in the basket
   - want(i, basket(cheese)).
 - Have you added cheese to the basket?
   - I want to know if there is cheese in the basket
   - want(i, know(i, basket(cheese))).
 - What's in the basket?
   - I want to know the items that are in the basket
 - Actually I don't want milk
   - I want there to not be milk in the basket
   - want(i, ~basket(milk)).

Possible replies:
 - We sell milk, cheese and bread
 - Yes, we sell milk
 - No, we don't sell salt
 - Ok, I've added cheese to the basket
 - Yes, there is cheese in the basket
 - There is milk and cheese in the basket
 - There is nothing in the basket
 - Ok, I've removed milk from the basket
 - There is no milk in the basket


Knowledge

sell(milk).
sell(cheese).
sell(bread).
~sell(salt).

Initial state

~basket(milk).
~basket(cheese).
~basket(bread).
