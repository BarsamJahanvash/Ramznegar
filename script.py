from random import randint
from time import sleep
import sys

Letters_Dict = {'a': 14, 'b': 16, 'c': 1, 'd': 18, 'e': 23, 'f': 2, 'g': 13, 'h': 6, 'i': 11, 'j': 5, 'k': 19, 'l': 15, 'm': 20, 'n': 3, 'o': 7, 'p': 21, 'q': 4, 'r': 17, 's': 12, 't': 24, 'u': 22, 'v': 8, 'w': 9, 'x': 26, 'y': 10, 'z': 25}


# input = "6 , 11 | 6 , 7 , 9 | 14 , 17 , 23 | 10 , 7 , 22 |"
# # input = "hi how are you"
# input_list = input.split()
# print(input_list)
# # print(input_list)
# words = []
# for i in range(len(input_list)):
#     p = list(Letters_Dict.values())
#     q = list(Letters_Dict.keys())
#     for o in range(26):
#         a = int(p[o])
#         b = (input_list[i])
#         if b != "|":
#             if b != ",":
#                 if a == int(b):
#                     words.append(q[o])
#                     break
            
#         else:
#             words.append(" ")
#             break
# for word in words:
#     print(word,end="")

# code = []
# for i in range(len(input_list)):
#     codeword = ''
#     p = list(Letters_Dict.values())
#     q = list(Letters_Dict.keys())
#     b = input_list[i]
#     for y in range(len(b)):
#         for o in range(26):
#             a = q[o]
#             try:
#                 c = b[y:y+1]
#                 if a == c:
#                     codeword += str(p[o])
#                     if y+1 != len(b):
#                         codeword += " , "
#             except:
#                 pass
#     code.append(codeword)
# for c in code:
#     print(c,end=' | ')



# for i in range(len(input_list[0])):
#     try:
#         print(input_list[0][i:i+1])
#     except:
#         pass

def Decode(inp):
    Letters_Dict = {'a': 14, 'b': 16, 'c': 1, 'd': 18, 'e': 23, 'f': 2, 'g': 13, 'h': 6, 'i': 11, 'j': 5, 'k': 19, 'l': 15, 'm': 20, 'n': 3, 'o': 7, 'p': 21, 'q': 4, 'r': 17, 's': 12, 't': 24, 'u': 22, 'v': 8, 'w': 9, 'x': 26, 'y': 10, 'z': 25}
    input_list = inp.split()
    words = []
    result = ''
    for i in range(len(input_list)):
        p = list(Letters_Dict.values())
        q = list(Letters_Dict.keys())
        for o in range(26):
            a = int(p[o])
            b = (input_list[i])
            if b != "|":
                if b != ",":
                    if a == int(b):
                        words.append(q[o])
                        break
                
            else:
                words.append(" ")
                break
    for word in words:
        # print(word,end="")
        result += word
        result += ""
    return result

def Encode(inp):
    try:
        inp = int(inp)
        return 
    except:
        pass
    Letters_Dict = {'a': 14, 'b': 16, 'c': 1, 'd': 18, 'e': 23, 'f': 2, 'g': 13, 'h': 6, 'i': 11, 'j': 5, 'k': 19, 'l': 15, 'm': 20, 'n': 3, 'o': 7, 'p': 21, 'q': 4, 'r': 17, 's': 12, 't': 24, 'u': 22, 'v': 8, 'w': 9, 'x': 26, 'y': 10, 'z': 25 , "?":"?"}
    inp = inp.lower()
    input_list = inp.split()
    code = []
    result = ''
    for i in range(len(input_list)):
        codeword = ''
        p = list(Letters_Dict.values())
        q = list(Letters_Dict.keys())
        b = input_list[i]
        for y in range(len(b)):
            for o in range(26):
                a = q[o]
                try:
                    c = b[y:y+1]
                    if a == c:
                        codeword += str(p[o])
                        if y+1 != len(b):
                            codeword += " , "
                except:
                    pass
        code.append(codeword)
    for c in code:
        # print(c,end=' | ')
        result += c
        result += " | "
    return result

# while True:
#     print("How Can I Help You?")
#     inp = input("Encoder(e),Decoder(d):")
#     if inp.lower() == "e":
#         inp = input("Enter Your Message:")
#         print(Encode(inp))
#     if inp.lower() == "d":
#         inp = input("Enter Your Code:")
#         print(Decode(inp))
#     sleep(0.25)