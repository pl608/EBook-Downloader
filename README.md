# EBook Downloader(pluss hopefully editer...)
downloads eBooks and takes away extra(useless) data

## Website
at the moment this only supports [this website](https://novelasfreeonline.com)
will try to add more
### I leave it up to you to get rid if the error:
   ``` saveB = Button(root, text='Save',command=lambda: save(root, progress),state=DISABLED)
  File "path\main-gui.pyw", line 53, in save
    z = threading.Thread(target=zip2epub.run,args=(tt,root,pp,f,bar,strip.getcover(uu)),name='epubing :)')
  File "path\python\strip.py", line 31, in getcover
    stuff = download.getstuff(url)
  File "path\python\download.py", line 56, in getstuff
    print(ra[2])
IndexError: list index out of range
```
Just a heads up I changed `print(ra[2])` --> `print(ra)` so if you cant find it here it is
##### FAQ (about this issue)
* some ~~specific~~ people where wondering where `download.py` is used. It is used in `main-gui.pyw` as a module in `run()` which is called when you press the run button in the GUI. It is also called in `strip(C).py` in `getcover()`
* also `C` in `downloadC.py` and `stripC.py` stands for console and is used in `main-console.py`
## To Do:
 - [ ]  add zip --> epub support
 - [ ]  [make it look REAL nice](#make-it-look-real-nice)
 - [ ]  MAYBE add .mobi support
 - [ ]  [better "useless data" deleter](#better-useless-data-deleter)
 - [ ]  clean up code/make it look more proffesional
 - [ ]  figure out a good way to realese it
 - [ ]  figure out how to spell realese

##### Make it look real nice:
 - [ ] full screen
 - [ ] previewer
 - [ ] loads of buttons+menu
 - [ ] good progress bar
##### better "useless data" deleter:
- [x] delete promotional+extra data at begining
- [ ] delete promotional+extra data at the end

## Done:
 - [x] add [gutenburg project](https://www.gutenberg.org/) support
 - [x] add epub support
 - [x] make a semi-working "useless data" deleter
 - [x] add .zip support(taking away zip so I can add epub)
 - [x] make it look acceptable

# ALSO
I leave it to you to fix the loading bar(if you cant just comment it out) ???
also: there is a chance that this is copyright infringment(or whatever that stuff is) but they stuck it on the internet in such a tempting way and it was a fun projects :) 
