#Variables
key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key2_key1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_key3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_key1_key3_key2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

#Converting from hex to bytes
key1_ord = [o for o in bytes.fromhex(key1)]
key2_key3_ord = [o for o in bytes.fromhex(key2_key3)]
flag_key1_key3_key2_ord = [o for o in bytes.fromhex(flag_key1_key3_key2)]


flag_key1_ord = [
    o_f132 ^ o23 for (o_f132, o23) in zip(flag_key1_key3_key2_ord, key2_key3_ord)
]
flag_ord = [o_f1 ^ o1 for (o_f1, o1) in zip(flag_key1_ord, key1_ord)]


print("".join(chr(o) for o in flag_ord))

