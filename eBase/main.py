from db import db_lower

class eBase:

    def __init__(self):
        pass

    def encrypt(self, text_to_encrypt):
        self.text_to_encrypt = text_to_encrypt
        for output in db_lower:
            print(output)
        # output = text_to_encrypt.replace(self.text_to_encrypt, db_lower)
        # print(f"OutPut -> {output}")

eBase().encrypt("h")