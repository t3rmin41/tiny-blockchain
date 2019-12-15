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
        self.encrypter = shifted_dict

    def get_encrypter(self) -> dict:
        return self.encrypter

    def encrypt(self, input: str = ""):
        output = []
        for c in input :
            output.append(self.encrypter.get(c))
        return "".join(output)