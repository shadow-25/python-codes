def encode(sen):
    code=""
    code_1=sen[::-1] #reverse the string

    for i in range(0,len(code_1)):
        char=code_1[i]
        new=ord(char)
        new+=5
        new_char=chr(new)
        code+=new_char
    return code
# def salt(str):#imcomplete
#     sal_1=['a','z','1','.','\'','"',' ','8','?','#']
#     new_str=list(str)
#     return code

sentence=input()
code=encode(sentence)
print(code)