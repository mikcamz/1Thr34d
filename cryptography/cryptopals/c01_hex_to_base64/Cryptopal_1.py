import base64

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"  # Hex representation of "Hello World"

# Convert hex string to bytes
bytes_data = bytes.fromhex(hex_string)

# Encode bytes to Base64
base64_bytes = base64.b64encode(bytes_data)

# Decode Base64 bytes to a string
base64_string = base64_bytes.decode("utf-8")

print(f"Hex string: {hex_string}")
print(f"Base64 string: {base64_string}")
