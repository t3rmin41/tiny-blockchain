import datetime as date

from modules.tiny.blockchain.entity.Block import Block

def create_initial_block():
    #Manually construct initial block
    return Block(0, date.datetime.now(), "Initial block", "0")

def next_block(last_block: Block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "This is block # " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)
