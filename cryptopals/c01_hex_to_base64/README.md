the challenge is pretty straight forward!

Decode the string from hex to b base64

This is my flow, Hex -> Bytes -> binary -> Base64

SO my first approach would be the raw code

WE have 1 hex character from 1 to 15 which is 4 bits to represent. But base64 use the 6 bits of the binary, means that we have to use 2 character from the hex format, convert it into binaries, then split 6 digits (in binary format each) and convert to base64

example:

hex (492) -> binary(0100 | 1001 | 0010 ) -> (010010 | 010010 ) -> decimal (18 | 18) -> base64(SS)

A-Za-z+/= is range from 0 to 63 in decimal

That is the theory. But we can use the built in function to solve !
