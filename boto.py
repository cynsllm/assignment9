"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json
import random
import requests
import enchant
import enchant
d = enchant.Dict("en_US")
from test import check_word
import re
from jokes import question_joke
counter = 0

#import webbrowser
#webbrowser.open("https://www.asos.com/bariano/bariano-tiered-fishtail-mesh-maxi-dress-in-navy/prd/10419456?clr=navy&SearchQuery=&cid=8799&gridcolumn=1&gridrow=1&gridsize=4&pge=1&pgesize=72&totalstyles=7085")

link_list = {"skirt": "https://www.asos.com/yellow-skirt", "dress": "https://www.asos.com/pink-dress", "jean":"https://www.asos.com/blue-jeans", "pant":"https://www.asos.com/black-pant", "jacket":"https://www.asos.com/leather-jacket", "accessory":"https://www.asos.com/soft-hat", "shirt":"https://www.asos.com/white-shirt", "coat":"https://www.asos.com/red-coat", "sweat":"https://www.asos.com/grey-sweat", "shoe":"https://www.asos.com/leather-shoes", "sneaker":"https://www.asos.com/nike-running",
                 "clothe":"https://www.asos.com", "sock":"https://www.asos.com/multicolor-socks", "boxer":"https://www.asos.com/men-boxers", "suit":"https://www.asos.com/blue-suit", "blouse":"https://www.asos.com/oversized-blouse", "tie":"https://www.asos.com/red-tie", "top":"https://www.asos.com/night-tops", "trouser":"https://www.asos.com/black-trousers", "short":"https://www.asos.com/sexy-short", "glove":"https://www.asos.com/leather-gloves", "jumper":"https://www.asos.com/white-jumper",
                 "swim":"https://www.asos.com/swimsuits", "bra":"https://www.asos.com/lingerie", "boot":"leather-boots"}
like_list = ["yes", "wow", "beautiful", "amazing", "like", "nice", "cool", "great", "good", "much", "yeah", "yep", "love"]
dislike_list = ["no", "not", "aweful", "horrible", "bad", "nope", "dislike", "hate"]
curse_list = ["fuck", "bitch", "shit", "piss", "dick", "asshole", "bastard", "damn"]
joke_list = ["joke", "laugh", "fun", "smile", "story", "another", "again"]
weather_list = ["weather", "forecast", "temp", "degree", "celcius", "sun", "cloud", "rain", "sky", "hot", "cold"]
city_list = ["paris", "london", "tel aviv", "new york", "jerusalem"]
end_conversation_words = ["bye", "see you", "to leave", "to go"]
hello_list = ["hello", "hi", "up", "hey"]




def greetings(input):
    greeting_list = ["Nice to meet you {0}!", "Hello {0}, what's up?", "Hi {0}!"]
    shop_list = ["What would you like to shop (pant, jacket, shirt...)?", "What kind of item are you looking for? Shoes? Skirt?...", "What are you looking for exactly? Dress, glasses...", "What kind of clothe do you need?"]
    greeting = random.choice(greeting_list) + " I'am your personal shopper. " + random.choice(shop_list)
    input = input.lower()
    input = input.split()
    return greeting.format(input[-1].title())


def find_items(input):
    list = ["Go check this link ", "I got this for you ", "I found something cool "]
    link_list = {"skirt": "https://www.asos.com/yellow-skirt", "dress": "https://www.asos.com/pink-dress", "jean":"https://www.asos.com/blue-jeans", "pant":"https://www.asos.com/black-pant", "jacket":"https://www.asos.com/leather-jacket", "accessory":"https://www.asos.com/soft-hat", "shirt":"https://www.asos.com/white-shirt", "coat":"https://www.asos.com/red-coat", "sweat":"https://www.asos.com/grey-sweat", "shoe":"https://www.asos.com/leather-shoes", "sneaker":"https://www.asos.com/nike-running",
                 "clothe":"https://www.asos.com", "sock":"https://www.asos.com/multicolor-socks", "boxer":"https://www.asos.com/men-boxers", "suit":"https://www.asos.com/blue-suit", "blouse":"https://www.asos.com/oversized-blouse", "tie":"https://www.asos.com/red-tie", "top":"https://www.asos.com/night-tops", "trouser":"https://www.asos.com/black-trousers", "short":"https://www.asos.com/sexy-short", "glove":"https://www.asos.com/leather-gloves", "jumper":"https://www.asos.com/white-jumper",
                 "swim":"https://www.asos.com/swimsuits", "bra":"https://www.asos.com/lingerie", "boot":"leather-boots"}
    result = [" what do you think?", " Do you like it?"]
    for key in link_list:
        if key in input:
            return random.choice(list) + link_list[key] + random.choice(result)


def question(input):
    if input.lower().startswith(("how", "what", "why", "where", "who")):
        answer_list = ["Sorry, I'am not allowed to answer this type of question...", "I don't understand please ask again", "What do you mean exactly ?", "Sorry, I can't tell you...", "I don't know, ask another robot!"]
        answer = random.choice(answer_list)
    else:
        answer_list = ["yes", "no"]
        answer = random.choice(answer_list)
    return answer


def result(input):
    for elem in like_list:
        if elem in input:
            list = ["Great, I'm happy to help you!", "Cool, we have the same style!", "Yessss I was pretty sure that you would love it"]
            return random.choice(list)
    for elem in dislike_list:
        if elem in input:
            list = ["Sorry, I'll try to be better next time!", "Maybe you'll be interested in this: XXXX"]
            return random.choice(list)
    return "i don't know"

def swear_words():
    return "you have a problem ?"

def start_conversation():
    answer_list = ["Hello dear!", "Hi my friend!", "What's up!", "Hey! I'm happy to see you again!", "How are you today ?", "Hey bro!"]
    return random.choice(answer_list)

def end_conversation():
    end_conversation_list = ["Do you really want to end the conversation?", "I hope you'll come and talk soon!", "No problem, see you next time!", "Okay, we'll continue our conversation later!"]
    end_conversation = random.choice(end_conversation_list)
    return end_conversation

def how_are_you():
    answer_list = ["I'm good thank you!", "I need holidays, but I'm okay...", "I'm so tired, I ve been working all day!", "Great! What about you?"]
    return random.choice(answer_list)

def whats_your_name():
    answer_list = ["I told you, I'm Boto!", "My name is Boto but you can call me Bouskoutou", "Boto! Don't you remember?", "You have a really short memory..."]
    return random.choice(answer_list)

def do_you_like(input):
    input = input.split()
    answer_list = ["Yes I love {0}!", "You don't even imagine how much I like {0}!", "Not really...", "Not at all!", "I hate {0}!"]
    for elem in range(len(input)):
        if input[elem] == "like":
            return random.choice(answer_list).format(input[elem + 1])

def weather_1():
    return "Which city?"

def weather_2(input):
    city_of_interest = input
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}'.format(city_of_interest, "32877c581bf458cb18d87601eca00837"))
    weather_request_content = json.loads(r.content)
    city_temp = (weather_request_content['main']['temp'])
    city_humidity = (weather_request_content['main']['humidity'])
    weather_desc = (weather_request_content['weather'][0]['description'])
    return (weather_desc, city_temp, city_humidity)

def error_message():
    return "sorry i can't help you"

def bot_message(input):
    global counter
    if counter == 0:
        counter += 1
        return greetings(input), "excited"
    elif any(elem in input for elem in link_list):
        return find_items(input), "crying"
    elif "you like" in input and input.lower().endswith("?"):
        return do_you_like(input), "no"
    elif any(elem in input for elem in like_list):
        return result(input), "dog"
    elif any(elem in input for elem in dislike_list):
        return result(input), "dancing"
    elif any(elem in input for elem in curse_list):
        return swear_words(), "ok"
    elif any(elem in input for elem in joke_list):
        return question_joke(), "giggling"
    elif any(elem in input for elem in hello_list):
        return start_conversation(), "excited"
    elif any(elem in input for elem in end_conversation_words):
        return end_conversation(), "no"
    elif input.lower().startswith("how are"):
        return how_are_you(), "excited"
    elif "your name" in input:
        return whats_your_name(), "dancing"
    elif "?" in input:
        return question(input), "ok"
    elif any(elem in input for elem in weather_list):
        return weather_1(), "dog"
    elif any(elem in input for elem in city_list):
        return weather_2(input), "heartbroke"
    else:
        return error_message(), "confused"


@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    (user_message, animation) = bot_message(user_message)
    return json.dumps({"animation": animation, "msg": user_message})


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()
