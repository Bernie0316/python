import random
def main():
    # 1 computer starts executing the sentences.py program by calling the main function.
    quantity = 1
    tense = "past"
    # 2 While executing the main function, the computer calls the make_sentence function.
    # 7 Finally, the computer executes the print function.
    print(f"{make_sentence(quantity, tense)}.")
    quantity = 2
    tense = "present"
    print(f"{make_sentence(quantity, tense)}.")
    quantity = 1
    tense = "future"
    print(f"{make_sentence(quantity, tense)}.")
    quantity = 2
    tense = "past"
    print(f"{make_sentence(quantity, tense)}.")
    quantity = 1
    tense = "present"
    print(f"{make_sentence(quantity, tense)}.")
    quantity = 2
    tense = "past"
    print(f"{make_sentence(quantity, tense)}.")
    pass

def make_sentence(quantity, tense):
    # 3 While executing the make_sentence function, /
    # 3 the computer calls the get_determiner, get_noun, get_verb, and get_prepositional_phrase functions.
    determiner = get_determiner(quantity) 
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    # 3 get_prepositional_phrase functions.
    prepositional_phrase = get_prepositional_phrase(quantity)
    prepositional_phrase_2 = get_prepositional_phrase(quantity)

    # 6 Then, the computer executes the str.capitalize method.
    sentence = f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase} {prepositional_phrase_2}"
    return sentence

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    # 4 While executing the get_prepositional_phrase function, /
    # the computer calls the get_preposition, get_determiner, and get_noun functions.
    get_preposition() 
    get_determiner(quantity)
    get_noun(quantity)
    prepositional_phrase = f'{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}'
    return prepositional_phrase

# 5 While executing each of the get_determiner, get_noun, get_verb, and get_preposition functions, /
# the computer calls the random.choice function.
def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]  
    noun = random.choice(nouns)      
    return noun

def get_verb(quantity, tense):
    if tense.lower() == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    if tense.lower() == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    if tense.lower() == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    if tense.lower() == "future": 
        verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]  
    verb = random.choice(verbs)    
    return verb

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition
main()

"""
Within your make_sentence function add another 
call to get_prepositional_phrase so that each sentence includes two prepositional phrases like this:
    One girl across one cat talked for the car.
    A bird near the rabbit drinks off one child.
    The child under the cat will run on the car.
    Some dogs without a cat drank above many rabbits.
    Some children from a bird laugh at many dogs.
    Some rabbits behind one man will talk about some cats.

    Write a function named get_adjective 
and call it in your make_sentence function to add an adjective to the sentences produced by your program. 
Does it make sense to call get_adjective in your get_prepositional_phrase function?

Write a function named get_adverb 
and call it in your make_sentence function to add an adverb to the sentences produced by your program.

{Determiner} {adjective} {noun} {prepositional_phrase} {adverb} {verb} 
{determiner} {adjective} {noun} {prepositional_phrase}.

Such as these sentences:
    The red birds in the air quickly ate some fast fish in the water.
    The busy bird with a car sweetly drank many smart rabbits by one boy.
    One dinky boy near the dog calmly grew some tall children across a cat.
"""







    