from modules.tiny.blockchain.entity.Encrypter import Encrypter

# Create blockchain but instead of proposed here https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b
# hashlib use own decrypter with simply shifted letters by 1 position and numbers reversed

inputString1 = "crazy"
print("Encrypted '", inputString1, "' string : ", sep="", end="")
print(Encrypter().encrypt(inputString1))

inputString2 = "Outstanding 0123"
print("Encrypted '", inputString2, "' string : ", sep="", end="")
print(Encrypter().encrypt(inputString2))