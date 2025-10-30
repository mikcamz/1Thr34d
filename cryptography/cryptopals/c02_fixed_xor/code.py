hex_string = (
    "1c0111001f010100061a024b53535009181c"  # Hex representation of "Hello World"
)
hex_string_to_xor = "686974207468652062756c6c277320657965"
# Convert hex string to bytes
bytes_data = bytes.fromhex(hex_string)

# for each byte a from hex string and b from string to xor
# we xor them and zip into a bytestring 

bytes_data = bytes(a ^ b for a, b in zip(bytes_data, bytes.fromhex(hex_string_to_xor)))

# then we decode
print(bytes_data.hex())
