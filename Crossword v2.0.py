try: from Tkinter import Tk,Frame,Label,Button,Listbox,Checkbutton,IntVar
except: from tkinter import Tk,Frame,Label,Button,Listbox,Checkbutton,IntVar
from random import randint,choice


theme=choice([('blue','white'),('red','white'),('purple3','white'),('green4','white'),('gold4','white'),('orangered','white')])


def f():
    pass

def Exit():
    global rootB
    
    rootC=Tk()
    rootC.geometry('220x150+500+200')
    rootC.overrideredirect(True)

    def sure_exit():
        a1.place_forget()
        a2.place_forget()
        b.place_forget()
        c.place_forget()
        root.destroy()
        rootC.destroy()
        try: rootB.destroy()
        except: pass


    def cancel():
        rootC.destroy()
        
    a1=Label(rootC,text='Hope to see you soon. Thank You.')
    a1.place(x=15,y=20)
    
    a2=Label(rootC,text='Do you really want to Exit ?')
    a2.place(x=15,y=40)
    
    b=Button(rootC,text='Cancel',command=cancel)
    b.place(x=15,y=100)
    c=Button(rootC,text='Exit',command=sure_exit)
    c.place(x=160,y=100)
    rootC.mainloop()
    

def instruction():
    global rootB
    
    rootB=Tk()
    rootB.geometry('480x300+400+100')
    rootB.overrideredirect(True)

    def instruction_back():
        rootB.destroy()
    
    w=Listbox(rootB,height=30,width=80)
    s='''
    CROSSWORD v2.0 game consists of a 15x15 matrix consisting of words.
    The player has to found out the words one by one. Here name of fruit,
    sports,movies,animals has been used. Checkbuttons sends the desired choice
    Check button check for its validity. Build button stsrts new game.

    This is a beta version so user might face bugs in the game.
    Developments are still going on.
    Recommendations is gladly accepted.

    Tamojit Das
    IEM CSE
    '''
    s=s.split('\n')
    for c in range(len(s)):
        w.insert(c+1,s[c])
    #w.pack(expand='yes',fill='both')
    w.place(x=0,y=25)

    Button(rootB,text='<= Back',command=instruction_back).place(x=0,y=0)

    rootB.mainloop()


def send(text,a,b):
    global ram_word,LIST_button_tracker
    if len(LIST_button_tracker)==0 or ([a,b])!=LIST_button_tracker[-1]:
        ram_word+=text
        LIST[a][b].config(bg='pink')
        LIST_button_tracker.append([a,b])
    else:
        ram_word=ram_word[:-1]
        LIST[a][b].config(bg='gray75')


def print_ram_list():
    global ram_word,LIST_button_tracker,found_words_counter,found_words_place_y,words
    
    if ram_word in words:
        Label(found_words_frame,text=ram_word).place(x=90,y=found_words_place_y)
        found_words_place_y+=35
        found_words_counter+=1
        words.remove(ram_word)
        found_words.config(text='FOUND WORDS: '+str(found_words_counter))
    else:    
        for r in LIST_button_tracker:
            LIST[r[0]][r[1]].config(bg='gray75')
    LIST_button_tracker=[]
    ram_word=''

def game_button(text,x,y,a,b):
    global virtual_LIST
    return Button(root,text=text,bg='gray75',command=lambda: send(text,a,b),relief='groove',width=5)#.place(x=x,y=y)


    
def place_display_matrix():
    global LIST
    y=150
    for a in range(15):
        x=315
        for b in range(15):
            LIST[a][b]=game_button(virtual_LIST[a][b],x,y,a,b)
            LIST[a][b].place(x=x,y=y)
            x+=50
        y+=40

def build():

    try:
        global check_fruits,check_animals,check_sports,check_movies
        global fruits,animals,sports,movies
        global words

        global virtual_LIST_tracker,virtual_LIST,LIST,unreqd_character,found_words_counter,found_words_place_y
        try:
            for widgets in found_words_frame.winfo_children():
                widgets.destroy()
        except: pass
        l=[]
        
        if (check_fruits.get()):
            l.extend(fruits)
        if (check_animals.get()):
            l.extend(animals)
        if (check_sports.get()):
            l.extend(sports)
        if (check_movies.get()):
            l.extend(movies)

        words=[]

        for a in range(8):
            p=choice(l)
            words.append(p)
            l.remove(p)
            


        for w in words:
            random_place(w)

        for t in range(15):
            for u in range(15):
                if virtual_LIST[t][u]==' ':
                    virtual_LIST[t][u]=choice(unreqd_character)

        word_label.config(text='WORDS: '+str(len(virtual_LIST_tracker)))

        found_words_counter=0
        found_words_place_y=30

        place_display_matrix()

    except:
        pass

def hint_display():
    global hint_list
    hint_label.config(text=choice(hint_list))
    hint_label.after(1500,hint_display)
    
    




rootB=None

root=Tk()
root.state('zoomed')
root.resizable(0,0)
root.overrideredirect(True)

Frame(root,width=1500,height=120,bg=theme[0]).place(x=0,y=0)
Label(text='CROSSWORD',fg=theme[1],bg=theme[0],font=('Arial',55)).place(x=50,y=25)
Label(text='v 2.0',fg=theme[1],bg=theme[0],font=('Arial',25)).place(x=1200,y=55)
Label(text='@ TD').place(x=20,y=730)




LIST=[[0 for i in range(15)] for j in range(15)]

LIST_button_tracker=[]

### Frameset for checkbutton  starts  ###############

Frame(root,width=250,height=100,bg=theme[0]).place(x=20,y=550)
Frame(root,width=230,height=80).place(x=30,y=560)

check_fruits=IntVar()
check_animals=IntVar()
check_sports=IntVar()
check_movies=IntVar()

Checkbutton(root,text='fruits',variable=check_fruits,onvalue=1,offvalue=0,relief='groove',width=7).place(x=50,y=570)
Checkbutton(root,text='animals',variable=check_animals,onvalue=1,offvalue=0,relief='groove',width=7).place(x=170,y=570)
Checkbutton(root,text='sports',variable=check_sports,onvalue=1,offvalue=0,relief='groove',width=7).place(x=50,y=610)
Checkbutton(root,text='movies',variable=check_movies,onvalue=1,offvalue=0,relief='groove',width=7).place(x=170,y=610)

####  Frameset checkbutton ends   ############

####  Frameset for others buttons starts   #########

Frame(root,width=250,height=100,bg=theme[0]).place(x=1100,y=550)
Frame(root,width=230,height=80).place(x=1110,y=560)

Button(root,text='Instructions',command=instruction,width=10,relief='groove').place(x=1130,y=570)
Button(root,text='Exit',command=Exit,width=10,relief='groove').place(x=1250,y=570)
Button(root,text='Check',command=print_ram_list,width=10,relief='groove').place(x=1130,y=610)
Button(root,text='Build',command=build,width=10,relief='groove').place(x=1250,y=610)

########   Frameset for others buttons ends   ########

########   Found words frame  starts ###############

Frame(root,width=250,height=350,bg=theme[0]).place(x=20,y=150)
found_words_frame=Frame(root,width=230,height=330)
found_words_frame.place(x=30,y=160)

found_words=Label(text='FOUND WORDS: ',fg=theme[1],bg=theme[0])
found_words.place(x=40,y=170)

word_label=Label(text='WORDS: ',fg=theme[1],bg=theme[0])
word_label.place(x=180,y=170)


##########  Found words frmae ends  ##########

##########  Hint &  Instruction Frame starts  ##############

Frame(root,width=250,height=350,bg=theme[0]).place(x=1100,y=150)
Frame(root,width=230,height=330).place(x=1110,y=160)

hint_label=Label(root,text='')
hint_label.place(x=1120,y=300)



Label(root,text='Hint:-',fg=theme[1],bg=theme[0]).place(x=1140,y=165)

#########  Hint & instruction  frame ends  ###########

words=[]

fruits=['apple','mango','litchi','guava','grapes','banana','blueberry','pineapple','orange','peer','kiwi']
animals=['tiger','lion','bear','giraffe','deer','elephant','wolf','fox','zebra']
sports=['baseball','basketball','archery','boxing','fencing','judo','tennis','cricket','football','hockey','badminton','golf','volleyball']
movies=['sanju','lagaan','sholay','dangal','titanic','terminator','pk','devdas','border','wanted','raazi','inception','gladiator','avatar','jaws']

hint_list=['Search word topic by topic.','Mixing all the topics is very tough.','Words are horizontally and vertically.','No word would be found diagonally']


virtual_LIST=[[' ' for i in range(15)] for j in range(15)]
virtual_LIST_tracker=[]
unreqd_character=list('abcdefghijklmnopqrstuvwxyz')
ram_word=''


def random_place(x):
    global virtual_LIST,virtual_LIST_tracker
    virtual_LIST=[[' ' for i in range(15)] for j in range(15)]
    virtual_LIST_tracker=[]

    l=len(x)
    for e in range(10):
    #while True:
        p,q=randint(0,14),randint(0,14)
        #if [p,q] not in virtual_LIST_tracker:
            #virtual_LIST_tracker.append([p,q])
            #break
        #print p,q
        m=choice([1,2,3,4,5,6,7,8,9,10])
        if m%2==0:
            if p-l>=0:
                for a in range(p-l,p):
                    if virtual_LIST[a][q]!=' ':
                        break
                else:
                    c=0
                    for a in range(p-l,p):
                        #print a,q
                        virtual_LIST[a][q]=x[c]
                        c+=1
                    virtual_LIST_tracker.append([p,q])
                    break
                    
            elif p+l<=9:
                for a in range(p+1,p+l+1):
                    if virtual_LIST[a][q]!=' ':
                        break
                else:
                    c=0
                    for a in range(p+1,p+l+1):
                        #print a,q
                        virtual_LIST[a][q]=x[c]
                        c+=1
                    virtual_LIST_tracker.append([p,q])
                    break
        else:
            if q-l>=0:
                for a in range(q-l,q):
                    if virtual_LIST[p][a]!=' ':
                        break
                else:
                    c=0
                    for a in range(q-l,q):
                        #print p,a
                        virtual_LIST[p][a]=x[c]
                        c+=1
                    virtual_LIST_tracker.append([p,q])
                    break
                    
            elif q+l<=9:
                for a in range(q+1,q+l+1):
                    if virtual_LIST[p][a]!=' ':
                        break
                else:
                    c=0
                    for a in range(q+1,q+l+1):
                        #print p,a
                        virtual_LIST[p][a]=x[c]
                        c+=1
                    virtual_LIST_tracker.append([p,q])
                    break
                
##for w in words:
##    random_place(w)

##for t in range(15):
##    for u in range(15):
##        print virtual_LIST[t][u],
##    print
    


##for t in range(15):
##    for u in range(15):
##        if virtual_LIST[t][u]==' ':
##            virtual_LIST[t][u]=choice(unreqd_character)


#place matrix

#print len(virtual_LIST_tracker)

##word_label.config(text='WORDS: '+str(len(virtual_LIST_tracker))) 

hint_display()

root.mainloop()
