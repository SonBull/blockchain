# Initialising genesis block and our blockchain as empty list
MINING_REWARD = 10

genesis_block = {'previous_hash': '', 'index': 0, 'transaction': []}
blockchain = [genesis_block]
open_transactions = []
owner = 'Chris'
participants = {'Chris'}


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transaction'] if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transaction'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']

def add_transaction(recipient, sender=owner, amount = 1.0):
    """ Append a new value as well as the last blockchain value 
    to the blockchain.

    Arguments:
        :sender: the sender of the coins.
        :recipient: the receipient of the coins.
        :amount: the amount of coins sent with the transaction
    """
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    # get the last element in the blockchain
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    # Reward the owner of the blockchain with coins, when mining a block.
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    # [:] copies the whole list, otherwise you only copy by reference.
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transaction': copied_transactions
    }
    blockchain.append(block)
    return True


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
    """ Verify the current blockchain and return True if it's valid, False otherwise"""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True
    
waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new Block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('h: Manipulate the blockchain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print('Added transaction')
        else:
            print('Transaction failed')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_element()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'h':
        # Make sure that you don´t try to hack the blockchain if its empty.
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 100.0}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Invalid Input! Please pick a value from the list!')
    if not verify_chain():
        print_blockchain_element()
        print('Blockchain not valid!')
        # Break out of the loop
        break
    print(get_balance('Chris'))
else: 
    print('User left!')

print('Done!')
