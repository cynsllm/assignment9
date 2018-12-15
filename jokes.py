import random


def question_joke():
    dict = {
        "How do you keep a French person from crashing your party?": 'Put a sign up that says "no nudity"',
        "Why do French People eat snails?": "Because they don't like fast food!",
        "How does every French joke start?": "By looking over your shoulder.",
        "What is the Guillotine?": "A French chopping centre.",
        "Which ghost was president of France?": "Charles de Ghoul.",
        "Where do fruits go on vacation?": "Pear-is.",
        "Whats the difference between a smart Frenchman and a unicorn?": "Nothing, they're both fictional characters",
        "Did you hear about the Frenchman who jumped into the river in Paris?": "He was declared to be in Seine.",
        "Did you hear about the winner of the French beauty contest?": "Me neither.",
        "What do you call an Frenchman in the knockout stages of the World Cup?": "A Referee.",
        "Why wasn't Jesus born in France?": "He couldn't find 3 wise men or a virgin.",
        "What do you call a Frenchman advancing on Baghdad?": "A salesman.",
        "Where can you find 60,100,000 French jokes?": "In France. Did you hear about the brave Frenchman? Oh you didn't. Well don't feel bad no one else has either.",
        "How do you brainwash a Frenchman?": "Fill his underpants with water.",
        "Did you hear about the French Army rifle sold on ebay?": 'The only description under the picture of it was "Nie gefeuert, einmal fallen gelessen" This is German for "never fired, dropped once"',
        "How do you kill a Frenchman?": "Slam the toilet seat down when he's getting a drink.",
        "How did the French react to German reunification?": "They put up speed bumps at the borders to slow down the panzers.",
        "What do you call a man who only needs body armor on his back?": "Jacques Chirac",
        "What is the other way to spell the name of the French president?": "Jacques ChIraq.",
        "Which is the most biggest rope?": "Europe",
        "What is the French national anthem?": "We surrender.",
        "What does a frog in Paris eat?": "French Flies.",
        "What's the best place to hide your money?": "Under a Frenchman's soap.",
        "What do you do if you drive over a Frenchman?": "Reverse!",
        "Why don't they have fireworks at Euro Disney?": "Because every time they shoot them off, the French try to surrender.",
        "The American military wears combat boots. What does the French military wear?": "Track shoes.",
        "How do you sink a French battleship?": "Put it in water.",
        "Whats in the middle of Paris?": "R.",
        "Why is the French Prime Minister never seen in the morning?": "Becasue he is pm not am!",
        "What do French recruits learn in basic training?": "How to surrender in 17 different languages.",
        "How do French tanks work?": "They have one forward gear and six reverse ones.",
        "Why don't the French eat M&M candies?": "They're too hard to peel."
    }
    joke = random.choice(list(dict))
    return joke + " " + dict[joke]



