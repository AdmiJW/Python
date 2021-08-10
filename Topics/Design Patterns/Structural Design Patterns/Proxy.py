
class ATM_Machine:
    def __init__(self, cash):
        self._cash = cash

    def get_cash(self):
        return self._cash

    def add_cash(self, amt):
        self._cash += amt


# Note that instead of creating a proxy class, we can put the proxy functionality
# in the ATM_Machine itself via decorators (or inheritance)
class ATM_Proxy:
    def __init__(self):
        self._machine = ATM_Machine(1000)
        self._isAccessed = False

    def access_atm(self):
        if self._isAccessed:
            print("The ATM is being accessed!")
            return None
        else:
            self._isAccessed = True
            return self._machine

    def release_atm(self):
        self._isAccessed = False



if __name__ == '__main__':
    proxy = ATM_Proxy()
    # Say now User1 wants to access the atm
    user1ATM = proxy.access_atm()
    print( user1ATM.get_cash() )
    user1ATM.add_cash(2000)

    # If User1 is not done using ATM, User2 cannot access
    user2ATM = proxy.access_atm()

    # Now User1 is done, release atm
    proxy.release_atm()

    # Now finally User2 can use
    user2ATM = proxy.access_atm()
    print( user2ATM.get_cash() )
