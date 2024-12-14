from bitcoin import *

# Generate private key
private_key = random_key()
print("Private Key:", private_key)

# Generate public key
public_key = privtopub(private_key)

# Generate Bitcoin address
address = pubtoaddr(public_key)
print("Bitcoin Address:", address)
