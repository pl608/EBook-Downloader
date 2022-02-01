import os, loadbar
def run(title, pages):
    
    t = title + "-out"
    try:
        os.mkdir(t)
    except:
        pass
    l = loadbar.LoadBar(max=len(pages), title='Taking Out Some Unnessisary parts')
    l.start()
    for x in pages:
        f = open(f'{title}/page_{x}.html','rb')
        r = f.read().decode('utf-8')
        s = r.replace(r[0:r.find('<div class="grab-content-chap">')], '')
        s = s.replace(r[r.find('<div class="chapter-nav text-center"><a href="/dorothy-l-sayers/'):-1] ,'')
        out = open(f'{t}/page_{x}.html', 'wb')
        out.write(bytes(s, 'utf-8'))
        out.close() 
        l.update()
    l.end()
    #print("done")
