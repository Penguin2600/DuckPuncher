## Some class that is used all over the place and needs to be patched but not modified
class A(object):
    def __init__(self):
        self.valueOne = 'Dag'
        self.valueTwo = 'Cool'

    # Print first Value
    def print_val(self):
        return "My Values are: %s, %s" % (self.valueOne, self.valueTwo)


#An unbound function that also needs to be patche
def a_func(varone, vartwo):
    b = A()
    b.valueOne = 'fad'
    b.valueTwo = varone
    return b
