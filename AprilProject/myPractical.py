#DEFUALT VALUE IN PYTHON
def gender(sex="unknown"):
    if sex == "m":
        sex = "male"
    elif sex == "f":
        sex = "female"

    print(sex)
gender("f")

def sentence(name = "john", action = "plays", item = "football"):
    print(name , action , item)
sentence()
sentence("mike", "love", "you" )
sentence(name = "wick", action = "hate", item = "fruit")
