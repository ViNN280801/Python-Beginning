# Object - unit of information in memory
# Instance - specific object of class
# Class - instruction of creating objects certain type
# Method - function of class
# Fields and properties - variables in a class
# Attributes - all names in a class: variables and methods

# Initializing class 'Wallet'
class Wallet:
    # Constructor of object
    def __init__(self, currency, name='Unknown'):
        ''' Assigning default variables '''
        # __money is a private variable
        if currency not in ('USD', 'EUR', 'RUB'):
            raise ValueError(
                'Currency error. Specified currency is unavalible')
        self.__money = 0.00
        self.currency = currency
        self.name = name

    def add_money(self, money_to_add):
        ''' Adding money on a balance. Returns how much money will be added '''
        self.__money += money_to_add
        return money_to_add

    def spend_money(self, money_to_spend):
        ''' Spending money from balance. Returns how much money will be spent '''
        if self.__money < money_to_spend:
            print('Insufficient funds')
        else:
            self.__money -= money_to_spend
        return money_to_spend

    def transfer_money(self, dest_wallet, money_to_transfer):
        ''' Transfers money from one wallet to another '''
        # Checkig if money to transfer is bigger value than money which we have on a balance
        if money_to_transfer > self.__money:
            print('Insufficient funds')
        else:
            # Taking away from this wallet
            self.__money -= money_to_transfer
            # Adding to another wallet
            dest_wallet.__money += money_to_transfer

    def balance(self):
        ''' Returns how much money is in the wallet '''
        return self.__money

    # Destructor
    def __del__(self):
        print('Wallet has been removed')


# Initializing instances of class 'Wallet'
wallet_1 = Wallet('USD')
wallet_2 = Wallet('EUR', 'Bill')

# Can't access to '__money' field
wallet_1.__money = 100
print('wallet_1: ' + str(wallet_1.balance()))
print('wallet_2: ' + str(wallet_2.balance()))

wallet_2.add_money(40)
wallet_1.spend_money(1000)
print('\nwallet_1: ' + str(wallet_1.balance()))
print('wallet_2: ' + str(wallet_2.balance()))

wallet_2.transfer_money(wallet_1, 20)
print('\nwallet_1: ' + str(wallet_1.balance()))
print('wallet_2: ' + str(wallet_2.balance()))
