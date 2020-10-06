f = open("terms.txt", "r")
li = list(f)
li = [i.replace('\n', '') for i in li]

while 1:
    word = input("enter word: ")
    a = 1
    for i in li:
        if i in word or word in i:
            a = 0
            print('Present')
            break
    if(a == 1):
        print("Abscent")
