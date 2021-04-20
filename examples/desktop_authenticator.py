# Example of generating authenticating codes using guard module
# To use is you have to obtain 'shared_secret' and 'identity_secret'
# From your Steamguard file

from pysteam.guard import generate_confirmation_key, generate_one_time_code
shared_secret = ''
identity_secret = ''

one_time_authentication_code = generate_one_time_code(shared_secret)
print(one_time_authentication_code)

confirmation_key = generate_confirmation_key(identity_secret, 'conf')
print(confirmation_key)