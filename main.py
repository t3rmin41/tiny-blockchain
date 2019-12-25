from modules.tiny.blockchain.generator.BlockGenerator import create_initial_block, next_block

# Create the blockchain and add the initial block
blockchain = [create_initial_block()]
previous_block = blockchain[0]

# How many blocks should we add to the chain
# after the initial block
num_of_blocks_to_add = 20

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    # Tell everyone about it!
    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))

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