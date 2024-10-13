from alga import Alga

class Sierpinski(Alga):

    beindított_telepek= 0

    def __init__(self, minta= "A", név= ""):

        self.név= név
        #Alga.__init__(self, minta)
        super().__init__(minta)

    def szabály(self, egyed):
        # A --> B−A−B, B --> A+B+A

        if egyed == "A":
            return list("B-A-B")

        elif egyed == "B":
            return list("A+B+A")

        return [egyed]