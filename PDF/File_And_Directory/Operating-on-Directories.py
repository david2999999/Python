import os
import shutil

# Creating an empty directory is even easier than creating a file. Just call os.mkdir . The parent directory
# must exist, however. The following will raise an exception if the parent directory C:\photos\zoo does
# not exist
os.mkdir("C:\\photos\\zoo\\snakes")


# You can create the parent directory itself using os.mkdir , but the easy way out is instead to use
# os.makedirs , which creates missing parent directories. For example, the following will create
# C:\photos and C:\photos\zoo , if necessary
os.makedirs("C:\\photos\\zoo\\snakes")

# This removes only the snakes subdirectory.
os.rmdir("C:\\photos\\zoo\\snakes")

# There is a way to remove a directory even when it contains other files and subdirectories. The function
# shutil.rmtree does this. Be careful, however; if you make a programming or typing mistake and pass
# the wrong path to this function, you could delete a whole bunch of files before you even know what ’ s
# going on! For instance, this will delete your entire photo collection — zoo, snakes, and all
shutil.rmtree("C:\\photos")