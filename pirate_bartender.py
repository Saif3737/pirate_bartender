questions =  {"strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"}

ingredients = {"strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]}

new_dict = dict()

def bartender(questions):
    """This asks the questions and answers in boolean form"""
    print("I am your {}").format(bartender.__name__)
    
if __name__ == '__main__':
    print(questions["strong"])
    
import sys
if sys.argv[1] == "yes" or "Yes":
    new_dict["Strong"] = bool(True)
    
    