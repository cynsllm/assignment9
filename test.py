import enchant
d = enchant.Dict("en_US")
if d.check("hellorg fnjks fhdzjk") is True:
    print("english")
else:
    print("not english")