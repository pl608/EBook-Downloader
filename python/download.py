from requests import get,head
import os
from time import sleep as s
main_path = os.getenv('APPDATA')+'\\Ebook Downloader'
#url = "https://novelasfreeonline.com/dorothy-l-sayers/{}42755-in_the_teeth_of_the_evidence"
ints = '1234567890'
def placeb(url):
    r = ''
    ra = []
    i = 0
    for x in url.split('/'):
        ra.append(x)
        if len(x) > 2:
            if x[0] in ints:
                r += "/{}"+x
            elif i == 0:
                r += x
            else:
                r += "/"+x
        else:
            r+="/"
        i += 1

    return r
def div(num):
    outs = []
    for x in range(1,10+1):
        if(num%x==0):
            outs.append(x)
            
    return outs[-2:][0]
    
def gd(url,title,bar,root):
    r = head(url, allow_redirects=True)
    header = r.headers
    Length = int(header['Content-Length'])
    print(Length)
    print(div(Length))
    chunk = int(Length/div(Length))
    chunk = 1
    print(chunk)
    r = get(url, stream = True)
    out = bytes('','utf-8')
    for x in r.iter_content(chunk_size=chunk):
        i += 1
        s(.2)
        if x:
            out += x
            bar['value'] = (i/chunk)*300
            print(x)
            root.update()
    with open(title+'.mobi','wb') as k:
        k.write(out)       
def getstuff(url):
    ra = url.split('/')
    print(ra)
    auth = ra[3]
    title = ra[4].replace('-',' ')
    title = title.replace('_',' ')
    for x in ints:
        title = title.replace(x,'')
    if title[0] == ' ':
        title = title[1:]
    title = title.title()
    return [auth, title]
def run(u,t,p,bar,root):
    bar['value'] = 0
    pages = [x for x in range(1,p+1)]
    t = t.replace(' ', '_')
    g = False
    if 'www.gutenberg.org' in u:
        g = True
        gd(u,t,bar,root)
    else:
        g = False
        url = placeb(u)
        r = ""
        try:
            os.mkdir(main_path+'\\'+t)
            
        except Exception as e:
            print(e)
            pass
        for x in pages:
            r = ''
            if x == 1:
                r = get(url.format(''))
            else:
                r = get(url.format(f'{x}-'))
            f = open(f'{main_path}\\{t}\\page_{x}.html','wb')
            f.write(bytes(r.text, 'utf-8'))
            f.close()
            bar['value'] = (x/len(pages))*300
            root.update()
    if g:
        from tkinter import messagebox
        messagebox.askokcancel('Done','Finished Downloading')
        bar['value'] = 0
        root.update()
    else:
        pass
    return g,pages, t
#gd('https://www.gutenberg.org/ebooks/67173f.kindle.images','mobi'#)
#getstuff('https://novelasfreeonline.com/dorothy-l-sayers/42756-the_documents_in_the_case')
print(os.getenv('APPDATA'))
