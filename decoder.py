def decode(str):
    original=""
    for i in range(0,len(str)):
        char=str[i]
        new=ord(char)
        new-=5
        new_char=chr(new)
        original+=new_char
    original=original[::-1]
    return original





sentence=input()
original=decode(sentence)
print(original)