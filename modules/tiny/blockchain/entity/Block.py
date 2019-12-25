#import modules.tiny.blockchain.entity.Encrypter as Encrypter
from modules.tiny.blockchain.entity.Encrypter import Encrypter

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.encrypted_block()

    def encrypted_block(self):
        data_string = str(str(self.index) +
                          str(self.timestamp) +
                          str(self.data) +
                          str(self.previous_hash))
        return Encrypter.Instance().encrypt(input = data_string)