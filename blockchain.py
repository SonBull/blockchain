#This is the first attempt of creating a blockchain with Python. 
#Initialising empty list.
blockchain = []

#defining function to get the latest element in the list
def get_last_blockchain_value():
    return blockchain[-1]

#defining function to append a new element to the list
def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])
#user driven input of blockchain values.
tx_amount = float(input('Your Transaction Amount please: '))
add_value(tx_amount)

tx_amount = float(input('Your Transaction Amount please: '))
add_value(tx_amount, get_last_blockchain_value())

tx_amount = float(input('Your Transaction Amount please: '))
add_value(tx_amount, get_last_blockchain_value())
#printing the blockchain
print(blockchain)