# Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald

# def old_macdonald(name):
#     first_letter = name[0]
#     in_between = name[1: 3]
#     fourth_letter = name[3]
#     rest = name[4:]
#     return first_letter.upper() + in_between + fourth_letter.upper() + rest

def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()

print(old_macdonald('macdonald'))