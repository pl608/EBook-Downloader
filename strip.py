import os,python.download as download
from requests import get
main_path = os.getenv('APPDATA')+'\\Ebook Downloader'

def run(title, pages,bar,root):
    bar['value'] = 0
    t = title + "-out"
    try:
        os.mkdir(main_path+'\\'+t)
    except:
        pass
    #l = loadbar.LoadBar(max=len(pages), title='Taking Out Some Unnessisary parts')
    #l.start()
    for x in pages:
        f = open(f'{main_path}\\{title}\\page_{x}.html','rb')
        r = f.read().decode('utf-8')
        ss = r.replace(r[0:r.find('<div class="grab-content-chap">')], '')
        ss = ss.replace(r[r.find('<div class="chapter-nav text-center"><a href="/dorothy-l-sayers/'):len(r)-1] ,'')
        s = ss.replace('Ã¢ÂÂ',"'")
        s = s.replace('Ã',' ')
        out = open(f'{main_path}\\{t}\\page_{x}.html', 'wb')
        out.write(bytes(s, 'utf-8'))
        out.close() 
        bar['value'] = (x/len(pages))*300
        root.update()
        print('done')
        #l.update()
    #l.end()
    #print("done")
def getcover(url):
    stuff = download.getstuff(url)
    thing = '_'
    auth = stuff[0].lower().replace(' ','-')
    title = stuff[1].lower().replace(' ',thing)
    u = f'https://picture.bookfrom.net/img/{auth}/{title}_preview.jpg'
    cover = get(u)
    return cover.content
#open('pic.jpg','wb').write(getcover('https://novelasfreeonline.com/dorothy-l-sayers/42755-in_the_teeth_of_the_evidence'))