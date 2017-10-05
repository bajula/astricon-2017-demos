from credentials import Credentials
import pyotp

class OTPProvider():
    def __init__(self):
        self.totp = pyotp.TOTP(Credentials.AUTHENTICATOR_KEY)

    def current_token(self):
        return self.totp.now()

if __name__ == '__main__':
    otp_provider = OTPProvider()
    print(otp_provider.current_token())