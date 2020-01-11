from classes.tiny.blockchain.entity.Encrypter import Encrypter
from modules.tiny.blockchain.generator.BlockGenerator import create_initial_block, next_block

# Create the blockchain and add the initial block
encrypter = Encrypter()
blockchain = [create_initial_block(encrypter)]
previous_block = blockchain[0]

# How many blocks should we add to the chain
# after the initial block
num_of_blocks_to_add = 15

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
    try:
        block_to_add = next_block(encrypter, previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        print("Block #{} has been added to the blockchain!".format(block_to_add.index))
        print("Hash: {}\n".format(block_to_add.hash))
    except BaseException as e:
        print(e.message)
print("Finish")

'''
try:
    blockchain_filepath = "./resources/blockchain_db.txt"
    blockchain_db = open(blockchain_filepath, "a+")
    for block in blockchain:
        blockchain_db.write(block.hash)
        blockchain_db.write("\n")
except IOError as ioerror:
    print("IOError :", ioerror)
finally:
    blockchain_db.close()
'''