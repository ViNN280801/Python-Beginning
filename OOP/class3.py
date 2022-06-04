from datetime import datetime


class Player:

    # Properties of class
    __LVL, __HEALTH = 1, 100
    __slots__ = ['__lvl', '__health', '__born']

    # Default Constructor
    def __init__(self):
        self.__health = Player.__HEALTH
        self.__lvl = Player.__LVL
        self.__born = datetime.now()

    # Getter
    def get_lvl(self):
        ''' Returns level of player '''
        return self.__lvl

    # Setter
    def set_lvl(self, numeric):
        ''' Changes level of player '''
        self.__lvl += numeric

    # Using decorators with getter and setter
    # Getter
    @property
    def lvl(self):
        return self.__lvl

    # Getter for health
    @property
    def health(self):
        return self.__health

    # Setter
    @lvl.setter
    def lvl(self, numeric):
        self.__lvl += Player.__typeTest(numeric)
        # Checking of max level
        if self.__lvl >= 100:
            self.__lvl = 100

    # Class method decorator
    # Changes '__LVL' and '__HEALTH'
    @classmethod
    def set_cls_fields(cls, lvl=1, health=100):
        cls.__HEALTH = Player.__typeTest(health)
        cls.__LVL = Player.__typeTest(lvl)

    @staticmethod
    def __typeTest(value):
        # 'isinstance()' funciton checks if 'value' is 'int' 
        if isinstance(value, int):
            return value
        else:
            raise TypeError('Invalid type. Value have to be integer')

    def show(self):
        ''' Shows health and level of current player '''
        print('Health = ' + str(self.health))
        print('Level = ' + str(self.lvl))


player = Player()
# Using default getter and setter
print(player.get_lvl())
player.set_lvl(2)
print(player.get_lvl())
# Using decorators for getter and setter
print(player.lvl)
player.lvl = 5
print(player.lvl)