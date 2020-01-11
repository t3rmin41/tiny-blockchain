from classes.tiny.blockchain.exception.StringTooLongException import StringTooLongException

class Block:
    def __init__(self, encrypter, index, timestamp, data, previous_hash):
        self.encrypter = encrypter
        self.index = index
        self.timestamp = timestamp
        if len(data) > 255:
            raise StringTooLongException()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.encrypted_block()

    def encrypted_block(self):
        return self.encrypter.encrypt_block(block = self)