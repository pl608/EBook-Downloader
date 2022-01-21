from requests import get
import os, loadbar
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

        


def run(u,t,p):
    url = placeb(u)
    pages = [x for x in range(1,p+1)]
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
    #l.end()
    return pages, t
