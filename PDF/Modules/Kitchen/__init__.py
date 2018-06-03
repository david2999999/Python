# Then create a file in Kitchen called _init__.py (this
# name has to be the same name as the method in a class that you ’ ve seen already, and note that it has two
# underscores before and after the name). This file is the hint that tells Python that this is a package
# directory, and not just a directory with Python files in it. This is important because it ensures that you
# know you ’ re responsible for maintaining this and controlling its behavior. This file has a lot of control
# over how the package is going to be used, because unlike a module, when a package is imported, every
# file in the directory isn ’ t immediately imported and evaluated. Instead, the _init__.py file is
# evaluated, and here you can specify which files are used and how they ’ re used!