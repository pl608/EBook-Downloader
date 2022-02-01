from requests import get,head
import os, loadbar
main_path = os.getenv('APPDATA')+'/Ebook Downloader'
main_path =''
#sample url:
#   url = "https://novelasfreeonline.com/dorothy-l-sayers/42755-in_the_teeth_of_the_evidence"
#
ints = '1234567890'
def placeb(url):
    r = ''
    i = 0
    for x in url.split('/'):
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
    for x in range(1,10+1):
        if type(num/x) == int:
            return x
def gd(url,title,barmax):
    l = loadbar.LoadBar(max=barmax)
    l.start()
    r = head(url, allow_redirects=True)
    header = r.headers
    print(header)
    Length = int(header['Content-Length'])
    print(Length)
    chunk = Length/div(Length)
    r = get(url, stream = True)
    with open(title+'.mobi','wb') as k:
        i = 0
        for x in r.iter_content(chunk_size=chunk):
            i += 1
            if x:
                k.write(x)
                l.update()
    l.end()
def getstuff(url):
    r,ra = placeb(url)
    auth = ra[3].replace('-',' ').title()
    title = ra[4].replace('-',' ')
    title = title.replace('_',' ')
    for x in ints:
        title = title.replace(x,'')
    if title[0] == ' ':
        title = title[1:]
    title = title.title()
    return auth, title
def run(u,t,p):
    url = placeb(u)
    pages = [x for x in range(1,p+1)]
    if 'www.gutenberg.org' in u:
        gd(u,t,len(pages))
    else:
        
        r = ""
        
        l = loadbar.LoadBar(max = len(pages), title='Downloading')
        t = t.replace(' ', '_')
        try:
            os.mkdir(t)
        except:
            pass
        l.start()
        for x in pages:
            r = ''
            #print(x)
            if x == 1:
                r = get(url.format(''))
            else:
                r = get(url.format(f'{x}-'))
            f = open(f'{t}/page_{x}.html','wb')
            f.write(bytes(r.text, 'utf-8'))
            f.close()
            l.update()
        l.end()
    return pages, t,getstuff(u)
