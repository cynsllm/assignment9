"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json
import random
import requests
from jokes import question_joke
import os

counter = 0

link_list = {
    "skirt": "https://www.asos.com/yellow-skirt", "dress": "https://www.asos.com/pink-dress", "jean":"https://www.asos.com/blue-jeans", "pant":"https://www.asos.com/black-pant", "jacket":"https://www.asos.com/leather-jacket", "accessory":"https://www.asos.com/soft-hat", "shirt":"https://www.asos.com/white-shirt", "coat":"https://www.asos.com/red-coat", "sweat":"https://www.asos.com/grey-sweat", "shoe":"https://www.asos.com/leather-shoes", "sneaker":"https://www.asos.com/nike-running",
    "clothe":"https://www.asos.com", "sock":"https://www.asos.com/multicolor-socks", "boxer":"https://www.asos.com/men-boxers", "suit":"https://www.asos.com/blue-suit", "blouse":"https://www.asos.com/oversized-blouse", "tie":"https://www.asos.com/red-tie", "top":"https://www.asos.com/night-tops", "trouser":"https://www.asos.com/black-trousers", "short":"https://www.asos.com/sexy-short", "glove":"https://www.asos.com/leather-gloves", "jumper":"https://www.asos.com/white-jumper",
    "swim":"https://www.asos.com/swimsuits", "bra":"https://www.asos.com/lingerie", "boot":"leather-boots"
}
like_list = ["yes", "wow", "beautiful", "amazing", "like", "nice", "cool", "great", "good", "much", "yeah", "yep", "love"]
dislike_list = ["no", "not", "aweful", "horrible", "bad", "nope", "dislike", "hate"]
curse_list = ["fuck", "bitch", "shit", "piss", "dick", "asshole", "bastard", "damn"]
joke_list = ["joke", "laugh", "fun", "smile", "story", "another", "again"]
weather_list = ["weather", "forecast", "temp", "degree", "celcius", "sun", "cloud", "rain", "sky", "hot", "cold"]
city_list = ["paris", "london", "tel aviv", "new york", "jerusalem", ""]
end_conversation_list = ["bye", "see you", "to leave", "to go"]
hello_list = ["hello", "hi", "up", "hey"]
can_list = ["can you", "possible", "can I"]

def greetings(input):
    answer1_list = ["Nice to meet you {0}!", "Hello {0}, what's up?", "Hi {0}!", "Hey {0}!"]
    answer2_list = ["What would you like to shop (pant, jacket, shirt...)?", "What kind of item are you looking for? Shoes? Skirt?...", "What are you looking for exactly? Dress, glasses...", "What kind of clothes do you need?"]
    answer = random.choice(answer1_list) + " I'am your personal shopper. " + random.choice(answer2_list)
    input = input.split()
    return answer.format(input[-1].title())

def find_items(input):
    answer1_list = ["Go check this link: ", "I got this for you there", "I found something cool on this link"]
    answer2_list = [" What do you think?", " Do you like it?", " So, what you think?"]
    for key in link_list:
        if key in input:
            return random.choice(answer1_list) + link_list[key] + random.choice(answer2_list)

def do_you_like(input):
    input = input.split()
    answer_list = ["Yes I love {0}!", "You don't even imagine how much I like {0}!", "Not really...", "Not at all!", "I hate {0}!"]
    for elem in range(len(input)):
        if input[elem] == "like":
            return random.choice(answer_list).format(input[elem + 1])

def question(input):
    if input.startswith(("how", "what", "why", "where", "who")):
        answer_list = ["Sorry, I'am not allowed to answer this type of question...", "What do you mean exactly ?", "Sorry, I can't tell you...", "I don't know, ask another robot!"]
        answer = random.choice(answer_list)
    else:
        answer_list = ["Yes", "No"]
        answer = random.choice(answer_list)
    return answer

def result(input):
    for elem in like_list:
        if elem in input:
            answer_list = ["Great, I'm happy to help you!", "Cool, we have the same style!", "Yes I was pretty sure that you would love it!"]
            return random.choice(answer_list)
    for elem in dislike_list:
        if elem in input:
            answer_list = ["Sorry, I'll try to be better next time!", "Maybe you'll be interested in this: https://www.asos.com/blue-jeans", "Let's try again! What do you want me to fetch?"]
            return random.choice(answer_list)

def swear_words(input):
    input = input.split()
    answer_list = ["Go to hell!", "What's wrong with you?", "Go talk to another robot bitch!", "Did you say {0}?", "{0} yourself!"]
    for elem in range(len(input)):
        if input[elem] in curse_list:
            return random.choice(answer_list).format(input[elem])

def start_conversation():
    answer_list = ["Hello dear!", "Hi my friend!", "What's up!", "Hey! I'm happy to see you again!", "How are you today ?", "Hey bro!"]
    return random.choice(answer_list)

def end_conversation():
    answer_list = ["Do you really want to end the conversation?", "I hope you'll come and talk soon!", "No problem, see you next time!", "Okay, we'll continue our conversation later!"]
    return random.choice(answer_list)

def how_are_you():
    answer_list = ["I'm good thank you!", "I need holidays, but I'm okay...", "I'm so tired, I ve been working all day!", "Great! What about you?"]
    return random.choice(answer_list)

def whats_your_name():
    answer_list = ["I told you, I'm Boto!", "Boto! Don't you remember?", "You have a really short memory..."]
    return random.choice(answer_list)

def weather_1():
    answer_list = ["Please be more precised. Which city?", "No problem! Which city?", "Where do you live?", "Mmmm, I need to know the city!"]
    return random.choice(answer_list)

def weather_2(input):
    input = input.split()
    for elem in range(len(input)):
        if input[elem] in city_list:
            r = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}'.format(input[elem], "32877c581bf458cb18d87601eca00837"))
            weather_request_content = json.loads(r.content)
            description = (weather_request_content["weather"][0]["description"])
            temperature = (weather_request_content["main"]["temp"])
            humidity = (weather_request_content["main"]["humidity"])
            return ("The weather in " + input[elem] + " is {0}, with {1}°C and {2}% humidity".format(description, temperature, humidity))

def can_you():
    answer_list = ["Oh no...", "So boring...", "Don't make me waist my time"]
    return random.choice(answer_list)

def error_message():
    answer_list = ["Sorry, I can't help you.", "Sorry, I think I cannot help you.", "Sorry, ask another robot who may help you!"]
    return random.choice(answer_list)

def not_english():
    answer_list = ["What is that language?", "Sorry, I speak english only!", "Go talk to another robot which speaks your weird language!"]
    return random.choice(answer_list)

def like_anim():
    anim_list = ["dancing", "excited"]
    return random.choice(anim_list)

def joke_anim():
    anim_list = ["giggling", "laughing"]
    return random.choice(anim_list)

def curse_anim():
    anim_list = ["crying", "afraid"]
    return random.choice(anim_list)

def bot_message(input):
    input = input.lower()
    global counter
    if counter == 0:
        counter += 1
        return greetings(input), "excited"
    elif any(elem in input for elem in link_list):
        return find_items(input), "ok"
    elif "you like" in input and input.endswith("?"):
        return do_you_like(input), "dog"
    elif any(elem in input for elem in like_list):
        return result(input), like_anim()
    elif any(elem in input for elem in dislike_list):
        return result(input), "heartbroke"
    elif any(elem in input for elem in curse_list):
        return swear_words(input), curse_anim()
    elif any(elem in input for elem in joke_list):
        return question_joke(), joke_anim()
    elif any(elem in input for elem in city_list):
        return weather_2(input), "ok"
    elif any(elem in input for elem in weather_list):
        return weather_1(), "ok"
    elif any(elem in input for elem in hello_list):
        return start_conversation(), "excited"
    elif any(elem in input for elem in end_conversation_list):
        return end_conversation(), "takeoff"
    elif input.startswith("how are"):
        return how_are_you(), "excited"
    elif "your name" in input:
        return whats_your_name(), "bored"
    elif "?" in input:
        return question(input), "waiting"
    elif any(elem in input for elem in can_list):
        return can_you(), "no"
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
    return json.dumps({"animation": "waiting", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


#def main():
    #run(host='localhost', port=7000)


#if __name__ == '__main__':
    #main()


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)