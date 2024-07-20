from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import sys
sys.setrecursionlimit(10000)


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

    def parse_elements(self):
        operation = []

        element = ''
        for char in self.register:
            if char not in ['/','*','-','+', '%']:
                element += char
            else:
                operation.append(element)
                element = ''
                operation.append(char)

        operation.append(element)
        return operation

    def perform_operation(self, operation: list):
        operation_length = len(operation)

        if operation_length == 1:
            return operation[0]

        for i, element in enumerate(operation):
            if element == '*':
                if (i + 1) >= operation_length or i == 0:
                    operation.pop(i)
                    return self.perform_operation(operation)
                
                operation[i] = float(operation[i-1]) * float(operation[i+1])
                operation.pop(i+1)
                operation.pop(i-1)
                return self.perform_operation(operation)
        

        for i, element in enumerate(operation):
            if element == '/':
                if (i + 1) >= operation_length or i == 0:
                    operation.pop(i)
                    return self.perform_operation(operation)
                
                operation[i] = float(operation[i-1]) / float(operation[i+1])
                operation.pop(i+1)
                operation.pop(i-1)
                return self.perform_operation(operation)


        for i, element in enumerate(operation):
            if element == '%':
                operation[i] = float(operation[i-1]) / 100
                operation.pop(i-1)
                return self.perform_operation(operation)

        for i, element in enumerate(operation):
            if element == '-':
                if (i + 1) >= operation_length:
                    operation.pop(i)
                    return self.perform_operation(operation)
                
                if i == 0:
                    operation.pop(i)
                    operation[i+1] = operation[i+1] + '-'
                    return self.perform_operation(operation)
                
                operation[i] = float(operation[i-1]) - float(operation[i+1])
                operation.pop(i+1)
                operation.pop(i-1)
                return self.perform_operation(operation)


        for i, element in enumerate(operation):
            if element == '+':
                if (i + 1) >= operation_length:
                    operation.pop(i)
                    return self.perform_operation(operation)
                
                operation[i] = float(operation[i-1]) + float(operation[i+1])
                operation.pop(i+1)
                operation.pop(i-1)
                return self.perform_operation(operation)


    def calculate(self):
        operation = self.parse_elements()
        result = str(self.perform_operation(operation))
        self.update_register(result)
        self.update_input()



    def button_click(self, value):
        if value == 'X':
            value = '*'
        
        self.register += value
        self.sanitize_register()
        self.update_input()
