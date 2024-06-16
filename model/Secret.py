import secrets
import string
class Secret:
    def generateRandString(self,length):
        alphabet = string.ascii_letters + string.digits
        rdString = ''.join(secrets.choice(alphabet) for i in range(length))
        return rdString