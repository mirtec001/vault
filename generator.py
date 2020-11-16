import random

class Generator:
    def __init__(self, length, numbers, special_characters):
        self.length = length
        self.numbers = numbers
        self.special_characters = special_characters
        self.alphabet = ['a','b','c','d','e','f','g','h',
                         'i','j','k','l','m','n','o','p',
                         'q','r','s','t','i','v','w','x',
                         'y','z']
        self.specials = ['!','@','#','$','%','^','&','*',
                         '(',')','-','_','=','+','[',']',
                         '{','}','\\','|',';',':','\'','\"',
                         ',','.','<','>','/','?']

    def get_special_characters(self):
        return self.specials[random.randint(0, len(self.specials) - 1)]

    def get_letter(self):
        return self.alphabet[random.randint(0, len(self.alphabet) - 1)]

    def gen_pass(self):

        pass_string = ""

        for _ in range(self.length):
            if self.special_characters == 'y':
                letter_number_special = random.randint(0, 2)
                if letter_number_special == 0:
                    to_upper = random.randint(0, 1)
                    if to_upper == 0:
                        pass_string += self.get_letter().upper()
                    else:
                        pass_string += self.get_letter()
                if letter_number_special == 1:
                    pass_string += str(random.randint(0, 9))
                if letter_number_special == 2:
                    pass_string += str(self.get_special_characters())
            else:
                letter_number = random.randint(0, 1)
                if letter_number == 0:
                    to_upper = random.randint(0, 1)
                    if to_upper:
                        pass_string += self.get_letter().upper()
                    else:
                        pass_string == self.get_letter()
                if letter_number_special == 1:
                    pass_string += str(random.randint(0, 9))

        return pass_string
