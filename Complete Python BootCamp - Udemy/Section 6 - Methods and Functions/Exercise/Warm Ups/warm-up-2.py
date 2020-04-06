# Write a function that takes a two-word string and returns True if both words begins with the same letter
# Example:
#       animal_crackers('Levelheaded Llama') --> True
#       animal_crackers('Crazy Kangaroo') --> False
def animal_crackers(text):
    word_list = text.lower().split()
    return word_list[0][0] == word_list[1][0]

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
print(animal_crackers('Crazy cat'))