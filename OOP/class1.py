# User verification
class Verification_v1:
    # Default constructor
    def __init__(self, login, psswd):
        self.login = login
        self.psswd = psswd
        self.__lenPsswd()

    # Checking of password length
    def __lenPsswd(self):
        ''' Checks length of password '''
        if len(self.psswd) < 8:
            raise ValueError(
                'Unreliable password. (Minimal length of password is 8 symbols)')

    # Saving all changes to a file
    def save_to_file(self, filename):
        ''' Writing users to a file in following template: login, password '''
        with open(filename, 'a') as file:
            file.write(f'{self.login}, {self.psswd}\n')
