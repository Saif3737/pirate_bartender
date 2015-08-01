import random

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
    
    

def construct(questions):
    "This {} your drink".format(construct.__name__)
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
        
if __name__ == '__main__':
    print("Please answer the following questions by entering yes or no for each one by entering yes or no in order following the questions")
    
    for question in questions:
        answers[question] = raw_input(questions[question]) == "yes"  
        
    print("Here is your drink, it is a combination of {}").format(', '.join(construct(questions)))
        
        
    
        

    
    


        
        
    
    

    
    
    
    
    



    




    
    
    
    

    
