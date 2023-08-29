#!/usr/bin/env python
// command: python3 hex_str_to_c_array.py string
import sys

def hex_to_c_array(hex_string):
    byte_array = bytes.fromhex(hex_string)
    c_array = "{\n"
    for i in range(0, len(byte_array), 8):
        chunk = byte_array[i:i+8]
        c_array += "    " + ", ".join(["0x{:02x}".format(byte) for byte in chunk]) + ",\n"
    c_array += "};"
    return c_array

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python hex_to_c_array.py <hexadecimal_string>")
        sys.exit(1)
    
    hex_string = sys.argv[1]
    c_array = hex_to_c_array(hex_string)
    print("C Array Format:")
    print(c_array)
