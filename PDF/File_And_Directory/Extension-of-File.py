import os

parts = os.path.splitext("image.jpg")
print(parts)

extension = parts[1]
print(extension)

extension2 = os.path.splitext("text.pdf")[1]
print(extension2)