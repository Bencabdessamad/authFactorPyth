from pyotp import TOTP 
# generate a secret key for the user 
secret = TOTP.random_base32()
# generate a qr code that can be scanned by the ysers mobile app
qr_code= TOTP(secret).provistioning_uri("username@example.ma")
#verify a code entered by the yser 
user_code = input("Enter code from your mobile app")
totp = TOTP(user_code);
if totp.verify(user_code):
    print("Verified")
else:
    print("Failed")