#!/bin/python
from bs4 import BeautifulSoup
import sys
import wikifoo
folder = ""
def getSkel():
    skel = open("skeleton.html",'r').read()
    soup = BeautifulSoup(skel,"html.parser")
    return soup
def log(msg, lvl):
    info = ["*","+","-"]
    print("["+info[lvl]+"] "+msg)
def setActive(root,name):
    menus = root.findAll(class_="nav-item dropdown")+root.findAll(class_="nav-item dropdown nav-reactor")
    drops = root.findAll(attrs={"class":"dropdown-item"}) +root.findAll(attrs={"class":"dropdown-item nav-reactor"})
    links = root.findAll(attrs={"class":"nav-item"}) +root.findAll(attrs={"class":"nav-item nav-reactor"})
    for link in links:
        if (link.get_text().strip()) == name:
            link["class"]+=["active"]
            log("Made Navigation active...",1)
    for menu in menus:
        drops = menu.findAll(attrs={"class":"dropdown-item"})
        for drop in drops:
            if (drop.get_text().strip()) == name:
                drop["class"]+=["active"]
                menu["class"]+=["active"]
                log("Made Navigation active...",1)
def generate(name):
    root = getSkel()
    log("Generating Site "+name+"...",0)
    setActive(root,name)
    heading = root.find(class_="photo-wrapper").find("h1")
    heading.string = name
    log("Replacing Heading...",1)
    headerImage =root.find(class_="header-photo")
    headerImage["src"] = headerImage["src"].replace("safety.jpg",name.lower()+".jpg")
    log("Replacing Headerphoto...",1)
    with open(folder+name.lower()+".html","w") as file:
        file.write(str(root))
def replaceNav(name):
    file=name.lower()+".html"
    log("Loaded up "+name.lower()+".html...",1)
    skel = open("nav.html",'r').read()
    nav = BeautifulSoup(skel,"html.parser")
    setActive(nav,name)
    f = open(file,'r').read()
    x = BeautifulSoup(f,"html.parser")
    z = x.find("nav")
    z.contents = nav.find("nav").contents
    log("Replaced Nav...",1)
    with open(file,"w") as t:
        t.write(str(x))
    log("File written...",1)
def generateTextContent(name,headings,content):
    file=name.lower()+".html"
    log("Loaded up "+name+"...",0)
    f = open(file,'r').read()
    x = BeautifulSoup(f,"html.parser")
    z = x.find(class_="content")
    z.contents=[]
    scrollspy = '<div class="scroll-spy"><div class="spy-list" id="spy"></div></div>'
    ss = BeautifulSoup(scrollspy,"html.parser")
    ssd = ss.find(class_="spy-list")
    textcontent = '<div class="text-content"></div>'
    tc = BeautifulSoup(textcontent,"html.parser")
    tcd = tc.find(class_="text-content")
    tcd = tc.find(class_="text-content")
    for i in range(len(content)):
        log("Generating Content...",1)
        ssd.append(genSSEl(i,headings[i]))
        tcd.append(genTextEl(i,headings[i],content[i]))
    z.append(ss)
    z.append(tc)
    log("Appending Text and Scrollspy to file...",1)
    with open(file,"w") as t:
        t.write(str(x))
    log("Done!",0)
def genSSEl(id,content):
    return  BeautifulSoup('<a href="#'+str(id)+'">'+str(content)+'</a>',"html.parser")
def genTextEl(id, heading, content):
    return BeautifulSoup(f"""  <div id="{id}">
                    <h1>{heading}</h1>
                    <p>{content}</p>
                </div> ""","html.parser")
def parseContents(name):
    chfile = open(name.lower()+"/content",'r')
    headings = []
    content = []
    currentCont = ""
    for line in chfile.readlines():
        if line[0]=="#":
            headings.append(line[1:])
            if currentCont != "":
                content.append(currentCont)
            currentCont=""
        else:
            currentCont+=line+"<br/>"
    print(len(headings),len(content))
    return headings,content
def doShit():
    real_links = wikifoo.doLinks()
    res=""
    for l in real_links:
        if ".pdf" in l:
            link = l
            href = l.split("/")
            end = href[len(href)-1]
            end= end.split("--")[2]
            name = end.split(".")[0]
            name = name.replace("_"," ")
            s = f'<li><a href="{link}">{name}</a></li>\n'
            res+=s
    print(res)
def wikifyLinks(name):
    filename = name;
    file=name.lower()+".html"
    f = open(file,'r').read()
    root = BeautifulSoup(f,"html.parser")
    log("Loaded up "+name,0)
    real_links = wikifoo.doLinks()
    print(real_links)
    links = root.find_all("a")
    images = root.find_all("img")
    videos = root.find_all("source")
    footer= root.find("footer")
    footer.extract()
    for link in links:
        href = link["href"]
        if "html" in href and not "www" in href:
            log("Not Wikified Link found... Wikifying...",2)
            log("Link is "+href,2)
            parts = href.split("/")
            target = parts[len(parts)-1]
            fix  = list(target)
            fix[0] = fix[0].upper()
            target = "".join(fix)
            target = target[:-5]
            link["href"] = f"https://2019.igem.org/Team:TU_Kaiserslautern/{target}"
        if "pdf" in href:
            pdfname = href.split("/")
            print(pdfname)
            pdf = pdfname[len(pdfname)-1]
            for reallink in real_links:
                if pdf in reallink:
                    link["href"] = reallink
    for video in videos:
        src = video["src"]
        if "T--TU_Kaiserslautern--" in src: 
            continue
        log("UnWikified Src found... Wikifying...",2)
        parts = src.split("/")
        name = parts[len(parts)-1]
        newsrc = src
        for link in real_links:
            if name in link:
                newsrc = link
                print("New link is "+link)
        video["src"] = newsrc
    for image in images:
        print("ugh")
        src = image["src"]
        if "T--TU_Kaiserslautern--" in src: 
            continue
        log("UnWikified Src found... Wikifying...",2)
        parts = src.split("/")
        name = parts[len(parts)-1]
        newsrc = src
        if("algenbs" in src):
            newsrc="https://2019.igem.org/wiki/images/7/73/T--TU_Kaiserslautern--algen.svg"
        for link in real_links:
            if name in link:
                newsrc = link
                print("New link is "+link)
        image["src"] = newsrc
    file=filename.lower()+".wiki.html"
    template = open("wikitemplate","r")
    zeug = "".join(template.readlines()).split("###\n")
    root = root.find("body")
    print(root)
    with open(file,"w") as t:
        t.write(str(zeug[0]))
        t.write(str(root))
        t.write(str(zeug[1]))
    log("Written as "+file,0)
    log("Done!",0)
sites = ["Description","Design","Experiments","Contribution","Demonstrate","Improve","Attributions","Overview","Basic","Composite","Collection","Entrepreneurship","Plant","Model"]
if __name__=="__main__":
    if len(sys.argv) == 2:
        doShit()
    if len(sys.argv) > 2:
        if(sys.argv[1] == "replace"):
            replaceNav(sys.argv[2])
        elif(sys.argv[1] == "gen"):
            generate(sys.argv[2])
        elif(sys.argv[1] == "genText"):
            generateTextContent(sys.argv[2],*parseContents(sys.argv[2]))
        elif(sys.argv[1] == "wikify"):
            wikifyLinks(sys.argv[2])
        else:
            print("replace or gen?")
    elif len(sys.argv)==2 and sys.argv[1]=="gen":
        for site in sites:
            generate(site)
    else:
        print("learn to play no0b")