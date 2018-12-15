import enchant

d = enchant.Dict("en_US")
def check_word(input):
    if d.check(input) == False:
        return "yes"
    else:
        return "mistake"
#print(check_word("HELLO"))


import re
test = "é&àçr"
def reg(test):
    if re.match(r"[A-Za-z]*", test):
        print('Yes')
    else:
        print("nope")
reg(test)

def find_item(input):
    link_list = {"skirt": "https://www.asos.com/yellow-skirt", "dress": "https://www.asos.com/pink-dress",
                 "jean": "https://www.asos.com/blue-jeans", "pant": "https://www.asos.com/black-pant",
                 "jacket": "https://www.asos.com/leather-jacket", "accessory": "https://www.asos.com/soft-hat",
                 "shirt": "https://www.asos.com/white-shirt", "coat": "https://www.asos.com/red-coat",
                 "sweat": "https://www.asos.com/grey-sweat", "shoe": "https://www.asos.com/leather-shoes",
                 "sneaker": "https://www.asos.com/nike-running",
                 "clothe": "https://www.asos.com", "sock": "https://www.asos.com/multicolor-socks",
                 "boxer": "https://www.asos.com/men-boxers", "suit": "https://www.asos.com/blue-suit",
                 "blouse": "https://www.asos.com/oversized-blouse", "tie": "https://www.asos.com/red-tie",
                 "top": "https://www.asos.com/night-tops", "trouser": "https://www.asos.com/black-trousers",
                 "short": "https://www.asos.com/sexy-short", "glove": "https://www.asos.com/leather-gloves",
                 "jumper": "https://www.asos.com/white-jumper",
                 "swim": "https://www.asos.com/swimsuits", "bra": "https://www.asos.com/lingerie",
                 "boot": "leather-boots"}
    for key in link_list:
        if key in input:
            return link_list[key]
print(find_item("sock"))