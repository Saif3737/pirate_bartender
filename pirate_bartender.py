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

answers = {"strong": None, "salty": None, "bitter": None, "sweet": None, "fruity": None}

def bartender(questions):
    """This asks the questions and answers in boolean form"""
    print("I am your {}").format(bartender.__name__)
    
if __name__ == '__main__':
    print("Please answer the following questions by entering yes or no for each one by entering yes or no in order following the questions")
    
if raw_input(questions["salty"]) == "yes":
    answers["salty"] = bool(True)

else:
    answers["salty"] = bool(False)

if raw_input(questions["strong"]) == "yes":
    answers["strong"] = bool(True)

else:
    answers["strong"] = bool(False)

if raw_input(questions["bitter"]) == "yes":
     answers["bitter"] = bool(True)

else:
    answers["bitter"] = bool(False)
    
if raw_input(questions["sweet"]) == "yes":
     answers["sweet"] = bool(True)

else:
    answers["sweet"] = bool(False)
    
if raw_input(questions["fruity"]) == "yes":
     answers["fruity"] = bool(True)

else:
    answers["fruity"] = bool(False)
    
print(answers)

import random

def construct(questions):
    "This {} your drink".format(construct.__name__)
    list_1 = []
    if __name__ == '__main__':
    
        list_1 = []
        if answers["salty"] == bool(True):
            list_1.append(random.choice(ingredients["salty"]))
        if answers["sweet"] == bool(True):
            list_1.append(random.choice(ingredients["sweet"]))
        if answers["bitter"] == bool(True):
            list_1.append(random.choice(ingredients["bitter"]))
        if answers["fruity"] == bool(True):
            list_1.append(random.choice(ingredients["fruity"]))
        if answers["strong"] == bool(True):
            list_1.append(random.choice(ingredients["strong"]))
        return list_1
    print("here's the drink")
    for ingredients in list_1:
        print("The drink's ingredients are {}").format(ingredients.__name__)
        
    
        

    
    


        
        
    
    

    
    
    
    
    



    




    
    
    
    

    
