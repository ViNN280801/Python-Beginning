from class1 import Verification_v1
import tkinter


filename_ = 'filename'

# Following initializing of class accompanied by inheritance


class Verification_v2(Verification_v1):
    # Overriding default constructor
    def __init__(self, login, psswd, age):
        super().__init__(login, psswd)
        self.__save_to_file(filename_)
        self.age = age

    # Extending opportunities of class by inheritance
    def show(self):
        ''' Returnds login and password in a tuple '''
        return self.login, self.psswd

    # Overriding saving to file funciton
    # Making this function private
    def __save_to_file(self, filename):
        ''' Checks login for availibility. Writes new user to file '''
        # Opening file in default mode
        with open(filename) as file:
            # Reading all lines from file with 'for' loop
            for line in file:
                # If user with this login is already exists -> raise error
                if f'{self.login}, {self.psswd}\n' in line:
                    raise ValueError('User with this login already exists')
        # If there is no such user -> saving to file new user
        super().save_to_file(filename)

# Creating simple window app


class My_app(tkinter.Tk):
    # Default constructor
    def __init__(self):
        ''' Initializing tkinter.Tk constructor '''
        tkinter.Tk.__init__(self)
        self.geometry('400x400')
        self.setUI()

    def setUI(self):
        ''' Creates button '''
        tkinter.Button(self, text='OK').pack()


# x = Verification_v2('login', 'D@N#ASDd34f32!@ed', 21)

# Illustrative example of polymorphism
class A:
    def a(self):
        print('A')

class B:
    def b(self):
        print('B')

class C(B):
    def a(self):
        print('C')

class D(C, A):
    def a(self):
        super(C, self).a()
        # __mro__ it is an algorithm which search methods from inherited classes
        print(self.__class__.__mro__)

D().a()