import classes.tiny.blockchain.entity.Block as Block
import hashlib as hasher
from modules.tiny.blockchain.generator.BlockGenerator import digits_sum

class Encrypter:
    def __init__(self):
        ascii_capitals_in_number = range(65, 90)
        encryption_dict = dict()
        for i in ascii_capitals_in_number:
            encryption_dict[chr(i)] = chr(i + 1)
        encryption_dict['Z'] = 'A'
        self.encrypter_dict = encryption_dict

    def get_encrypter_dict(self) -> dict:
        return self.encrypter_dict

    def encrypt_string(self, input: str = ""):
        return "".join(self.get_encrypter_dict()[key] if key in self.get_encrypter_dict() else key for key in input)

    def encrypt_block(self, block: Block) -> str: #values passed to function are passed by reference, not by value like in Java
        result: str
        block_index = block.index
        ascii_uppercase_start_code = 65
        ascii_uppercase_end_code = 90
        # hash index
        if ascii_uppercase_start_code <= block_index + ascii_uppercase_start_code <= ascii_uppercase_end_code :
            result = self.get_encrypter_dict()[chr(block_index + ascii_uppercase_start_code)]
        else:
            while block_index + ascii_uppercase_start_code > ascii_uppercase_end_code :
                block_index = digits_sum(block_index)
            result = self.get_encrypter_dict()[chr(block_index + ascii_uppercase_start_code)]
        # hash timestamp
        for date_part in block.timestamp :
            if date_part + ascii_uppercase_start_code <= ascii_uppercase_end_code :
                result += self.get_encrypter_dict()[chr(date_part + ascii_uppercase_start_code)]
            else:
                while date_part + ascii_uppercase_start_code > ascii_uppercase_end_code:
                    date_part = digits_sum(date_part)
                result += self.get_encrypter_dict()[chr(date_part + ascii_uppercase_start_code)]
        # hash data field
        sha = hasher.sha256()
        sha.update(str(result).encode('utf-8') + str(block.previous_hash).encode('utf-8'))
        #return result
        return sha.hexdigest()
