def main():
    # Python has a very simple way of letting you make decisions. The reserved word for decision making is
    # if , and it is followed by a test for the truth of a condition, and the test is ended with a colon, so you ’ ll
    # see it referred to here as if ... : . It can be used with anything that evaluates to True or False to say
    # “ if something is true, do what follows ” :
    if 1 > 2:
        print("No it is not")

    if 2 > 1:
        print("Yes, It is")

    omelet_ingredients = {
        "egg" : 2,
        "mushrooom" : 5,
        "pepper" : 1,
        "cheese" : 1,
        "milk" : 1
    }

    fridge_content = {
        "egg" : 10,
        "mushroom" : 20,
        "pepper" : 3,
        "cheese" : 2,
        "tomato" : 4,
        "milk" : 15
    }

    have_ingredients = [False]

    if fridge_content["egg"] > omelet_ingredients["egg"] :
        have_ingredients[0] = True

    have_ingredients.append("egg")

    print(have_ingredients)

    # After a condition is tested with an if ...: and there is an additional level of indentation, Python will
    # continue to evaluate the rest of the code that you ’ ve placed in the indentation. If the first if ...: isn ’ t
    # true, none of the code below it will be evaluated — it would be skipped entirely.
    # However, if the first if ...: statement is true, the second one at the same level will be evaluated. The
    # outcome of a comparison only determines whether the indented code beneath it will be run. Code at
    # the same level, or above, won ’ t be stopped without something special happening, such as an error or
    # another condition that would prevent the program from continuing to run.
    if fridge_content["mushroom"] > omelet_ingredients["mushrooom"]:
        if have_ingredients[0] == False :
            have_ingredients[0] = True
        have_ingredients.append("mushroom")

    print(have_ingredients)




if __name__ == "__main__":
    main()