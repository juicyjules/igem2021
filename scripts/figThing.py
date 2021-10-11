from bs4 import BeautifulSoup
def loadShit():
    stuff = parseRes()
    #print(stuff)
    thing  = open("results2.html",'r').read()
    root = BeautifulSoup(thing,"html.parser")
    figures = root.find_all(class_="figure")
    for figure,lol in zip(figures,stuff):
        s =  f'<span class="phat">{lol[0]}</span>{lol[1]}'
        ss = BeautifulSoup(s,"html.parser")
        ps = figure.find("p")
        ps.contents = []
        ps.append(ss)
        print(ps)
        #print(figure.find("p"))
    with open("results.out.html","w") as t:
        t.write(str(root))
def parseRes():
    f = open("results","r")
    lines = f.readlines()
    xd = []
    for i in range(len(lines)//2):
        xd.append((lines[2*i],lines[2*i+1]))
    return xd
if __name__=="__main__":
    loadShit()