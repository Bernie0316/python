import random
# 01 Using VS Code, create a new file, import the random module at the top of the file, and save the file as sentences.py
# 02 Copy and paste the following get_determiner function into your program.
def main():
    quantity = 1
    tense = "past"
    print(f"a. {make_sentence(quantity, tense)}")
    quantity = 1
    tense = "present"
    print(f"b. {make_sentence(quantity, tense)}")
    quantity = 1
    tense = "future"
    print(f"c. {make_sentence(quantity, tense)}")
    quantity = 2
    tense = "past"
    print(f"d. {make_sentence(quantity, tense)}")
    quantity = 2
    tense = "present"
    print(f"e. {make_sentence(quantity, tense)}")
    quantity = 3
    tense = "past"
    print(f"f. {make_sentence(quantity, tense)}")
    pass

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word.capitalize()

# 03 Use the get_determiner function as an example to help you write the get_noun function./
#  The get_noun function must have the following header and /
# fulfill the requirements of the following documentation string.

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]  
    noun = random.choice(nouns)      
    return noun

# 04 Use the get_determiner function as an example to help you write the get_verb function./
#  The get_verb function must have the following header and /
# fulfill the requirements of the following documentation string.
def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense.lower() == "past":
        verb = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    if tense.lower() == "present" and quantity == 1:
        verb = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    if tense.lower() == "present" and quantity != 1:
        verb = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    if tense.lower() == "future": 
        verb = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]  
    verb = random.choice(verb)                 
    return verb

# 05 Write a function named make_sentence with the following header and documentation string. /
# Your make_sentence function must call your/
#  get_determiner, get_noun, and get_verb function once each and build and return a sentence. /
# Your make_sentence function must capitalize the first letter of the sentence and end it with a period (.).
def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """   
    determiner = get_determiner(quantity) 
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    sentence = f"{determiner} {noun} {verb}"
    return sentence
main()
    