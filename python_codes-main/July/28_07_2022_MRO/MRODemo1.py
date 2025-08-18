
class Parent1(object):

    def __init__(self):
        print("Parent1 Constructor")

class Parent2(object):
    
    def __init__(self):
        print("Parent2 Constructor")

class Child(Parent1, Parent2):

    def __init__(self):
        print("Child Constructor")

obj = Child()
