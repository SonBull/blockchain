# Initialising genesis block and our blockchain as empty list
genesis_block = {'previous_hash': '', 'index': 0, 'transaction': []}
blockchain = [genesis_block]
open_transactions = []
owner = 'Chris'


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount = 1.0):
    """ Append a new value as well as the last blockchain value 
    to the blockchain.

    Arguments:
        :sender: the sender of the coins.
        :recipient: the receipient of the coins.
        :amount: the amount of coins sent with the transaction
    """
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)


def mine_block():
    # get the last element in the blockchain
    last_block = blockchain[-1]
    hashed_block = ''
    for key in last_block:
        value = last_block[key]
        hashed_block = hashed_block + str(value)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transaction': open_transactions
    }
    blockchain.append(block)


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) 
    as a float. """
    tx_recipient = input('Enter the receipient of the transaction: ')
    tx_amount = float(input('Your Transaction Amount please: '))
    # return tupel (data structure)
    return (tx_recipient, tx_amount)


def get_user_choice():
    """ Small Function to get the user choice """
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_element():
    # Output Blockchain
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)

def verify_chain():

    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
    return is_valid 

waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new Block')
    print('3: Output the blockchain blocks')
    print('h: Manipulate the blockchain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_element()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2] 
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Invalid Input! Please pick a value from the list!')
    # if not verify_chain():
    #     print_blockchain_element()
    #     print('Blockchain not valid!')
    #     break
else: 
    print('User left!')

print('Done!')
