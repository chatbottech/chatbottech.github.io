"""
Prototype of search algorithm.

No logic proving. Implements estimation of probable states from
preconditions.

Tree format: {'action': (precondition_set, postcondition_set)}
"""


TREE = {
    # What would you like?
    # First of all you have to want to know what the user would like
    # This means there is a reward in your exploration tree for knowing that
    # Also, we don't know what we want
    'say(want(i, know(i, what(like(you)))))': ({'want(i, know(i, what(like(you))))'}, {'know(you, want(i, know(i, what(like(you)))))'}),

    # Or treat questions differently
    'say(what(like(you)))': (set(), {}),

    # Generally:
    'say(X)': ({'X'}, {'know(you, X)'}),
    
    # I want apples
    # In order to say you want something, you have to want it
    # If someone asked you what you would like, they have an answer now
    'say(want(i, basket(apples)))': ({'want(i, basket(apples))'}, {'know(you, want(i, basket(apples)))'}),

    # In order to add apples to the basket, they have to not already be in there
    # After adding them, you still want apples
    'add(basket(apples))': ({'~basket(apples)'}, {'basket(apples)'}),
}

# You are rewarded if there's nothing you want that you don't have
REWARD = {'want(basket(apples)) & basket(apples)', '~want(basket(apples)) & ~basket(apples)'}
