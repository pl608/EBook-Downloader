import python.download as download, python.strip as strip, sys, getopt, zipfile, pickle, threading
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import *

burl = ''
p = 0
def run(u,p,t, bar,root):
    pages, title = download.run(u,t,p,bar,root)
    strip.run(title, pages,bar,root)
    print("Done\nfiles are in {}-out".format(title))
    bar['value'] = 0
    def zip(bar,root,title,pages):
        #l = Label(root, text=threading.current_thread)
        f = filedialog.asksaveasfilename(filetypes=[('Zip File','*.zip'),('All Files','*.*')])
        if '.zip' not in f:
            f += '.zip'
        else:
            pass
        with zipfile.ZipFile(f, 'w') as zip_f:
            for x in pages:
                zip_f.write(f'{title}/page_{x}.html')
                bar['value'] = (x/len(pages))*300
                root.update()
        print('done')
        bar['value'] = 0
        #l = Label(root, text=threading.current_thread)
        
    print('zip thread')
    z = threading.Thread(target=zip,args=(bar,root,title,pages),name='zipping')
    z.start()

    #messagebox.showinfo('Done',"Files are in {}-out".format(title))
    
def GUI():
    root = Tk()
    root.resizable(False,False)
    try:
        root.iconbitmap('python/icon.ico')
    except:
        root.iconbitmap('python/icon.png')
    urll = Label(root, text='Url of first page: ')
    urle = Entry(root,width=45)
    
    pl = Label(root, text='Number of pages: ')
    pe = Entry(root,width=45)

    tl = Label(root, text='Title of book: ')
    te = Entry(root,width=45)

    progress = Progressbar(root, orient = HORIZONTAL, length = 300, mode = 'determinate')
    prol = Label(root, text='')

    #sb = Button(root, text='Search Author',command=setdir)
    def seturl():
        if urle.get() == '':
            messagebox.showinfo('Error','You didnt put a url\nTry again')
        if pe.get() == '':
            messagebox.showinfo('Error','You didnt put a page number\nTry again')
        if te.get() == '':
            messagebox.showinfo('Error','You didnt put a title\nTry again')
        else:
            burl = urle.get()
            p = int(pe.get())
            t = te.get()
            y = threading.Thread(target=run,args=(burl,p,t,progress,root),name='proccesing')
            y.start()
    c = Button(root, text='Close', command=sys.exit)
    s = Button(root, text='Run', command=seturl)
    urll.grid(row=1,column=1)
    urle.grid(row=1,column=2)
    pl.grid(row=2,column=1)
    pe.grid(row=2,column=2)
    tl.grid(row=3,column=1)
    te.grid(row=3,column=2)
    c.grid(row=5,column=4)
    s.grid(row=5,column=1)
    progress.grid(row=5,column=2)
    prol.grid(row=5,column=3)
    #sdb.grid(row=3,column=3)
    root.mainloop()
if __name__=="__main__":
    x = threading.Thread(target=GUI,name='GUI')
    x.start()
    #GUI()
