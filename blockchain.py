# Initialising our blockchain as empty list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value 
    to the blockchain.

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1])
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) 
    as a float. """
    user_input = float(input('Your Transaction Amount please: '))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_element():
    # Output Blockchain
    for block in blockchain:
        print('Outputting Block')
        print(block)


while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_element()
    elif user_choice == 'q':
        break
    else:
        print('Invalid Input! Please pick a value from the list!')

print('Done!')
