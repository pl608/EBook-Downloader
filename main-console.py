import python.downloadC as download, python.stripC as strip, sys, getopt, zipfile, pickle, loadbar, python.zip2epub 
from tkinter.ttk import *

burl = ''
p = 0
def run(u,p,t):
    pages, title = download.run(u,t,p)
    strip.run(title, pages)
    zip2epub.run(title,pages=pages,path=input("path to place epub: ").replace('.epub',''))
    #print("Done\nfiles are in {}-out".format(title))
    def zip(title,pages):
        f = ''
        l = loadbar.LoadBar(max=len(pages),title='zipping...')
        l.start()
        if '.zip' not in f:
            f += '.zip'
        else:
            pass
        with zipfile.ZipFile(f, 'w') as zip_f:
            for x in pages:
                zip_f.write(f'{title}/page_{x}.html')
                l.update()
                
        print('done')
    #zip(t,p)
def GUI():
    i = '123456789'
    url = input('page 1 url: ')
    def pages(out):
        page = input('number of pages: ')
        if page[0] in i:
            out = int(page)
        else:
            print('please put an interger for the number of pages')
            pages(out)
    title = input('Title: ')
    p = 0
    pages(p)
    run(url, p, title)
    
    

GUI()
