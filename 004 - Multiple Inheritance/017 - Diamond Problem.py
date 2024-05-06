class A:
    def show(self):
        print("This is A")

class B(A):
    def show(self):
        print("This is B")

class C(A):
    def show(self):
        print("This is C")

class D(B, C):
    pass

object = D()
object.show()
help(object)