import random
class Rand:
    def rand_num(what_to, what):
        result = random.randint(what_to, what)
        return result
    def choose(list):
        result = random.choice(list)
        return result
