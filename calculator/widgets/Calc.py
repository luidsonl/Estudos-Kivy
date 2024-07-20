from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import re


class Calc(BoxLayout):
    Builder.load_file('./screens/Calc.kv')

    register = ''

    def update_input(self):
        self.ids.calc_input.text = self.register

    def update_register(self, text):
        self.register = text

    def sanitize_register(self):
        sanitized_register = []

        for i, char in enumerate(self.register):
            if i == 0:
                if char in ['0','1','2','3','4','5','6','7','8','9','-']:
                    sanitized_register += char
                continue

            if char in['0','1','2','3','4','5','6','7','8','9']:
                if sanitized_register[-1] =='%':
                    continue
                sanitized_register += char
                continue

            if char in ['.', '%']:
                flag = True
                for i, s_char in enumerate(sanitized_register):
                    if s_char in ['.','/','*','-','+', '%']:
                        flag = False
                    if s_char in ['0','1','2','3','4','5','6','7','8','9']:
                        if sanitized_register[i-1] in ['/','*','-','+']:
                            flag = True

                if flag:
                    sanitized_register += char
                    continue


            if (sanitized_register[-1] in ['/','*','-','+', '.'] and char in ['/','*','-','+']):
                sanitized_register[-1] = char
                continue
            
            if char in ['/','*','-','+']:
                sanitized_register += char
                continue
        
        self.register = ''.join(sanitized_register)
            


    def validate_input(self, instance, text):
            self.update_register(text)
            self.sanitize_register()
            self.update_input()


    def clear(self):
        self.register = ''
        self.update_input()

    def back(self):
        self.register = self.register[:-1]
        self.update_input()

    def button_click(self, value):
        if value == 'X':
            value = '*'
        
        self.register += value
        self.sanitize_register()
        self.update_input()
