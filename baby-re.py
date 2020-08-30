#!/usr/bin/env python3

hex_list = ["594234427B425448", "3448545F5633525F", "455F5354", "7D5A"] #hex from debugger
flag_list = []
for i in hex_list:
        to_ascii = bytes.fromhex(i).decode('utf-8')
        rev_str = ''.join(reversed(to_ascii))
        flag_list.append(rev_str)
final_flag = ''.join(flag_list)
print(final_flag)

