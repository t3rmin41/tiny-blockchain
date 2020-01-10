import datetime as date
from modules.tiny.blockchain.entity.Block import Block

datetime_format = "%Y-%m-$d %H:%M:%S.%s"

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
    # Timestamp as a tuple? E.g. (20,19,12,28,13,0,1) -> 2019-12-28 13:00:01
    now = date.datetime.utcnow()
    this_timestamp = (now.year // 100, now.year % 100, now.month, now.day, now.hour, now.minute, now.second, digits_sum(now.microsecond))
    this_data = "This is block # " + str(this_index)
    this_hash = last_block.hash
    return Block(encrypter, this_index, this_timestamp, this_data, this_hash)
