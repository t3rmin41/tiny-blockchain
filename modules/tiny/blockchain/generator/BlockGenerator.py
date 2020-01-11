import datetime as date
from classes.tiny.blockchain.entity.Block import Block

def digits_sum(large_int):
    sum = 0
    while large_int > 9:
        sum += large_int % 10
        large_int = large_int // 10
    sum += large_int
    return sum

def create_initial_block(encrypter):
    #Manually construct initial block
    now = date.datetime.utcnow()
    timestamp = (now.year // 100, now.year % 100, now.month, now.day, now.hour, now.minute, now.second, digits_sum(now.microsecond))
    return Block(encrypter, 0, timestamp, "Initial block", "0")

def next_block(encrypter, last_block: Block):
    this_index = last_block.index + 1
    now = date.datetime.utcnow()
    # Timestamp as a tuple: E.g. (20,19,12,28,13,0,1) -> 2019-12-28 13:00:01
    this_timestamp = (now.year // 100, now.year % 100, now.month, now.day, now.hour, now.minute, now.second, digits_sum(now.microsecond))
    '''
    too_long_string = []
    for i in range(0, 265):
        too_long_string.append('a')
    this_data = str(too_long_string)
    '''
    this_data = "This is block # " + str(this_index)
    this_hash = last_block.hash
    return Block(encrypter, this_index, this_timestamp, this_data, this_hash)
