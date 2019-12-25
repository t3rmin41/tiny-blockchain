from modules.tiny.blockchain.entity.Singleton import Singleton

@Singleton
class Encrypter:
    def __init__(self):
        ascii_capitals_in_number = range(65, 90)
        ascii_lowercase_in_number = range(97, 122)
        shifted_dict = dict()
        for i in ascii_capitals_in_number:
            shifted_dict[chr(i)] = chr(i + 1)
        shifted_dict['Z'] = 'A'
        for i in ascii_lowercase_in_number:
            shifted_dict[chr(i)] = chr(i + 1)
        shifted_dict['z'] = 'a'
        numbers = range(0, 10)
        for i in range(0, 10):
            shifted_dict[str(i)] = str(numbers[-i])
        shifted_dict[" "] = "_"
        shifted_dict["#"] = "@"
        self.encrypter_dict = shifted_dict

    @staticmethod
    def get_encrypter_dict() -> dict:
        return Encrypter.Instance().encrypter_dict

    @staticmethod
    def encrypt(input: str = ""):
        return "".join(Encrypter.Instance().get_encrypter_dict()[key] if key in Encrypter.Instance().get_encrypter_dict() else key for key in input)