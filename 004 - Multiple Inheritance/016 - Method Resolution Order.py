class A:
    def show(self):
        print("This is A")

class B:
    def show(self):
        print("This is B")

class C(A,B):
    def show(self):
        print("This is C")

object = C()
object.show()