'''
Дается несколько цифр надо выдать капчу
'''
class CaptchaNums:
    def __init__(self, num):
        self.num = num


    def define_and_run(self):
        if self.num == 0:
            return self.zero()
        if self.num == 1:
            return self.one()
        if self.num == 2:
            return self.two()
        if self.num == 3:
            return self.three()
        if self.num == 4:
            return self.four()
        if self.num == 5:
            return self.five()
        if self.num == 6:
            return self.six()
        if self.num == 7:
            return self.seven()
        if self.num == 8:
            return self.eight()
        if self.num == 9:
            return self.nine()


    def zero(self):
        return '##\n##\n##\n##'
    

    def one(self):
        return '.#\n##\n.#\n.#'
    

    def two(self):
        return '##\n.#\n#.\n##'
    

    def three(self):
        return '##\n.#\n.#\n##'
    

    def four(self):
        return '##\n##\n.#\n.#'
    

    def five(self):
        return '##\n#.\n.#\n##'
    

    def six(self):
        return '.#\n#.\n##\n##'
    

    def seven(self):
        return '##\n.#\n#.\n#.'
    

    def eight(self):
        return '##\n..\n##\n##'
    
    
    def nine(self):
        return '##\n##\n.#\n#.'



def _1_(alpha):
    for i in alpha:
        a.append(_2_(i)[0])
        b.append(_2_(i)[1])
        c.append(_2_(i)[2])
        d.append(_2_(i)[3])


def _2_(i):
    return CaptchaNums(i).define_and_run().split()


a = []
b = []
c = []
d = []


_1_(list(map(int, list(input()))))

print(*a, sep='')
print(*b, sep='')
print(*c, sep='')
print(*d, sep='')
