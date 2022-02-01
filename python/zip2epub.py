import os
from python.PyPub import MakeBook as book
def run(title='',root=None, pages='',path='', bar=None,cover=None):
    try:
        name = str(path.split('/')[-1:][0])+'.epub'
        spl = path.split('/')
        path = ''
        for x in range(len(spl)):
            if x >= len(spl)-1:
                pass
            else:
                path += spl[x]+'/'
                
        if bar==None:
            import loadbar
            bar = loadbar.LoadBar(max=len(pages),title='Making Epub...')
            bar.start()
        else:
            pass
        def upbar(b,num=0,end=False):
            try:
                b['value'] = num
                root.update()
            except Exception as e:
                #print(e)
                if end:
                    b.end()
                else:
                    b.update()
        epub = book(title)
        for x in pages:
            epub.add_chapter(open(f'{title}-out/page_{x}.html','rb').read().decode('utf-8'))
            #epub.add_chapter(c)
            upbar(bar,(x/len(pages))*300)
        upbar(bar,300,True)
        epub.add_cover(cover)
        epub.write_book(path+'/'+name)
        upbar(bar,0,True)
        print('done {}\n{}'.format(name,path))
    except Exception as e:
        print(e)
    
        

