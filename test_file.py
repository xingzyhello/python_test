import os
import sys
import binhex
import binascii


def file_txt_ascii_hex_handle(file_path_src,file_path_des,num_char=0):
    f_size = os.path.getsize(file_path_src)
    print(" 文件 {0} 的大小：{1} 字节 ".format(file_path_src,f_size))

    if file_path_src == file_path_des :
        print(" 必须是两个不同的文件 ");print(" 执行完成 ")
        return None

    f_src = open(file_path_src,mode = 'rt')
    f_des = open(file_path_des,mode = 'wt')

    l_ascii_hex = ('0','1','2','3','4','5','6','7','8','9','a','A','b','B','c','C','d','D','e','E','f','F')
    count_right_data = 0
    count_err_data = 0
    while True:
        f_data = f_src.read(1)
        if f_data:
            if f_data in l_ascii_hex:
                f_des.write(f_data)
                count_right_data += 1
                if num_char > 0:
                    if (count_right_data % num_char) == 0:
                        f_des.write("\r\n")
            else:
                count_err_data += 1
        else:
            print(" 执行完成 ")
            print(" 符合条件的数据的字节数：{0} ".format(count_right_data))
            print(" 不符合条件的数据的字节数：{0} ".format(count_err_data))

            break

    f_src.close()
    f_des.close()

    return


def file_ascii_hex_to_hex(file_path_src,file_path_des):
    f_size = os.path.getsize(file_path_src)
    print("文件 {0} 的大小：{1} 字节".format(file_path_src,f_size))

    if file_path_src == file_path_des :
        print(" 必须是两个不同的文件 ");print(" 执行完成 ")
        return None

    f_src = open(file_path_src,mode = 'rt')
    f_des = open(file_path_des,mode = 'wb')

    l_ascii_hex_base48 = ('0','1','2','3','4','5','6','7','8','9')
    l_ascii_hex_base65 = ('A','B','C','D','E','F')
    l_ascii_hex_base97 = ('a','b','c','d','e','f')

    count_right_data = 0
    count_err_data = 0

    while True:
        str_data = f_src.read(2)
        length = len(str_data)
        if length == 2:
            # if str_data[0] in l_ascii_hex_base97 :
            #     hex_h = ord(str_data[0]) - 97 + 10
            # elif str_data[0] in l_ascii_hex_base65 :
            #     hex_h = ord(str_data[0]) - 65 + 10
            # elif str_data[0] in l_ascii_hex_base48 :
            #     hex_h = ord(str_data[0]) - 48
            # else :
            #     print(" ERROR DATA : {0}".format(str_data[0]))
            #     break
            #
            # if str_data[1] in l_ascii_hex_base97 :
            #     hex_l = ord(str_data[1]) - 97 + 10
            # elif str_data[1] in l_ascii_hex_base65 :
            #     hex_l = ord(str_data[1]) - 65 + 10
            # elif str_data[1] in l_ascii_hex_base48 :
            #     hex_l = ord(str_data[1]) - 48
            # else :
            #     print(" ERROR DATA : {0}".format(str_data[1]))
            #     break

            # if hex_h >= 16 :
            #     print('*' * 10)
            # if hex_l >= 16 :
            #     print('*' * 20)
            # hex_data = (hex_h << 4) | (hex_l & 0x0F)
            # f_char = binhex(str_data)
            f_char = binascii.a2b_hex(str_data)
            print(f_char)
            # hex_data &= 0xFF
            # f_char = chr(hex_data).encode('hex')
            # f_char = hex(hex_data)
            # f_char = f_char[2:]
            # hex_data.bit_length()

            # print((len(f_char)))
            f_char = f_char.encode()
            # print(f_char.encode())
            if len(f_char) > 1 :
                print('*'*10)
                # print(hex_data)
                print(len(f_char))
                print(f_char)
            f_des.write(f_char)

            count_right_data += 1


        else:
            print(" 执行完成 ")
            print(" 符合条件的数据的字节数：{0} ".format(count_right_data))
            print(" 不符合条件的数据的字节数：{0} ".format(count_err_data))

            break

    f_src.close()
    f_des.close()

    return


# C:\Users\xingzy\Desktop\111.txt
# f_path_src = input("输入文件文件路径和名称：")
# f_path_des = input("输入文件文件路径和名称：")
f_path_src = 'C:\\Users\\xingzy\\Desktop\\111.txt'
f_path_des = 'C:\\Users\\xingzy\\Desktop\\112.txt'
f_path_des_1 = 'C:\\Users\\xingzy\\Desktop\\113.txt'

file_txt_ascii_hex_handle(f_path_src,f_path_des,num_char=0)

file_ascii_hex_to_hex(f_path_des,f_path_des_1)
# help(hex)
# help(binhex)
# tt=322
# tem='%d' %tt
# print(tem)
# help(str.encode)
# help(chr)
# help(os.write)

