class Alga:

    beindított_telepek= 0

    def __init__(self, minta="A"):

        if type(minta) == self.__class__:
            self.telep= minta.telep[:]
        else:
            self.telep= list(minta)

        self.generáció= 0
        self.__class__.beindított_telepek+= 1


    def szabály(self, egyed):

        if egyed == "A":
            return ["A","B"]

        elif egyed == "B":
            return ["A"]

        return [egyed]


    def növekedés(self, n=1):

        for i in range(n):

            újtelep= []
            for e in self.telep:
                újtelep.extend(self.szabály(e))

            self.telep= újtelep

        self.generáció+= n


    def info(self):
        return f"Típus: {self.__class__.__name__}, " \
               f"méret: {len(self.telep)}, generáció: {self.generáció}"

    @classmethod
    def telepszám(cls):
        return cls.beindított_telepek

    def __call__(self, n=1):

        self.növekedés(n)
        return self.generáció, len(self.telep)

    def __str__(self):

        if self.__len__() <= 40:
            return "".join(self.telep)
        else:
            return "".join(self.telep[:15]+["..."]+self.telep[-15:])

    def __len__(self):
        return len(self.telep)

    def __repr__(self):
        s= "".join(self.telep)
        return f"{self.__class__.__name__}('{s}')"

    def __eq__(self, másik):
        return self.telep == másik.telep # lexikografikus

    def __lt__(self, másik):
        return self.telep < másik.telep # lexikografikus

    def __bool__(self):
        return self.generáció>0

    def __add__(self, másik):
        szumalg= self.__class__()
        #szumalg= self.__init__()
        szumalg.telep= self.telep + másik.telep
        return szumalg

    def __getitem__(self, index):

        if type(index) == slice:
            minta= "".join(self.telep[index])
            return self.__class__(minta)

        return self.telep[index]

    def __setitem__(self, index, s):
        self.telep[index]= s