import modules.tiny.blockchain.entity.Block as Block
from modules.tiny.blockchain.generator.BlockGenerator import digits_sum

class Encrypter:
    def __init__(self):
        ascii_capitals_in_number = range(65, 90)
        ascii_lowercase_in_number = range(97, 122)
        encryption_dict = dict()
        for i in ascii_capitals_in_number:
            encryption_dict[chr(i)] = chr(i + 1)
        encryption_dict['Z'] = 'A'
        '''
        for i in ascii_lowercase_in_number:
            encryption_dict[chr(i)] = chr(i + 1)
        encryption_dict['z'] = 'a'
        numbers = range(0, 10)
        for i in range(0, 10):
           encryption_dict[str(i)] = str(numbers[-i])
        encryption_dict[" "] = "_"
        encryption_dict["#"] = "@"
        '''
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
        data_char_list = []
        block_data = block.data
        for char in block_data :
            data_char_list.append(ord(char))
        # simply hash as sha() both first part (index and timestamp) and data part - that will be
        # harder way - implement Fowler-Noll-Vo algorithm (simple, effective yet non-toy)
        '''
        block_data_length = len(block.data)
        if (block_data_length <= 255) :
            while block_data_length < 100000000 :
                block_data = block_data * factor
        else:
            while block_data_length > 1
        '''
        return result
