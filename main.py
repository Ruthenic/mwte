import readchar
import os
import sys
def clearscreen(): 
    if os.name == 'nt': 
        os.system('cls') 
    else: 
        os.system('clear') 
try:
    filename = sys.argv[1]
except:
    filename = ''
text = []
if not filename == "":
    with open(filename) as f:
        for line in f:
            text.append(list(line))
else:
    text.append([])
#text = [['T', 'e', 's', 't'], ['T', 'e', 's', 't'], ['T', 'e', 's', 't']]
cx,cy = 0,0
while True:
    dx,dy = 0,0
    for i in text:
        for c in i:
            if dx == cx and dy == cy:
                print("\033[107m\033[30m" + c + "\033[0m\033[0m", end="")
            else:
                print(c, end="")
            if cx == len(i) and dy == cy and dx == len(i)-1:
                print("\033[107m" + " " + "\033[0m", end="")
            dx+=1
        dx=0
        dy+=1
        print("")
    char = readchar.readkey()
    #print(char)
    if char == '\x11':
        exit()
    elif char == readchar.key.UP:
        cy-=1
        if cy<0:
            cy=0
    elif char == readchar.key.DOWN:
        cy+=1
        if cy>len(text)-1:
            cy=len(text)-1
    elif char == readchar.key.LEFT:
        cx-=1
        if cx<0 and cy>=0:
            cy-=1
            cx=len(text[cy])
    elif char == readchar.key.RIGHT:
        try:
            cx+=1
            if cx>len(text[cy]) and cy<=len(text):
                cy+=1
                cx=0
                #cx=len(text[cy])
        except:
            cx-=1
    elif char == readchar.key.BACKSPACE:
        if len(text[cy]) == 0:
            text.pop(cy)
            cy-=1
            try:
                cx=len(text[cy])+1
            except:
                cx=0
        elif cx == 0:
            try:
                cx=len(text[cy-1])+1
            except:
                cx=0
            for i in text[cy]:
                try:
                    text[cy-1].append(i)
                except:
                    pass
            cy-=1
        else:
            try:
                text[cy].pop(cx)
            except:
                text[cy].pop(cx-1)
        cx-=1
    elif char == readchar.key.ENTER:
        text.insert(cy+1, [])
        cy+=1
    elif char == readchar.key.CTRL_S:
        if filename == '':
            filename = input("Filename: ")
        with open(filename, "w") as f:
            for i in text:
                teng = ""
                for let in i:
                    teng+=let
                teng+="\n"
                f.write(teng)
    else:
        text[cy].insert(cx, char)
        cx+=1
    if cy>=len(text):
        cy-=1
        cx=len(text[cy]) #assume that if cursor x is exceeding buffer length, cx will need to be reset
    if cy<0:
        cy+=1
        cx=0 #assume that if cursor x is exceeding buffer length, cx will need to be reset
    if len(text) == 0:
        text.append([])
    clearscreen()
    print(cx,cy)
