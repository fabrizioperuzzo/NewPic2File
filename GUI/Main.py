import Tkinter as tk
from class_point2graph import *
import numpy as np
import sys
import os
import math

##########################################################
#            RICHIAMO TUTTE LE DEF
##########################################################
def read_label():

    try:

        f = open("SETTINGS\\label_input.txt", 'r')
        with f:
            ls_label = f.readlines()

        for i in ls_label:
            ls_label[ls_label.index(i)] = i.replace('\n', '')

        label_y_in = ls_label[0]
        unit_y_in = ls_label[1]
        label_x_in = ls_label[2]
        unit_x_in = ls_label[3]
        x0_in = ls_label[4]
        y0_in = ls_label[5]

    except:

        label_y_in = 'labely'
        unit_y_in = 'unity'
        label_x_in = 'labelx'
        unit_x_in = 'unitx'
        x0_in = 0
        y0_in = 0


    return label_y_in,unit_y_in,label_x_in,unit_x_in,x0_in,y0_in
##########################################################
def write_label(label_y,unit_y,label_x,unit_x,x0,y0):

    ls_label_in=[]
    ls_label_in.append(label_y+'\n')
    ls_label_in.append(unit_y+'\n')
    ls_label_in.append(label_x+'\n')
    ls_label_in.append(unit_x+'\n')
    ls_label_in.append(x0+'\n')
    ls_label_in.append(y0+'\n')
    

    f = open("SETTINGS\\label_input.txt", 'w')

    with f:
        ls_label = f.writelines(ls_label_in)
##########################################################
def print_entry():
    ycoo = ent.get()
    xcoo = ent1.get()
    print ycoo
    print xcoo

##########################################################

def store_lbl_entry():
    ls_lbl_out = [ent2.get(),ent4.get(),ent3.get(),ent5.get(),ent8.get(),ent7.get()]
    write_label(ls_lbl_out[0],ls_lbl_out[1],ls_lbl_out[2],ls_lbl_out[3],ls_lbl_out[4],ls_lbl_out[5])

    return ls_lbl_out


##########################################################
def write_files(list1,list2, label1, label2, unit1, unit2):

    csv_name = "OUTPUT\\"+ent6.get()+".csv"

    f = open(csv_name, 'w')
    f.write(ent6.get()+ '\n')
    f.write(label1+','+label2+'\n')
    f.write(unit1 + ',' + unit2 + '\n')


    for n in range(1,len(list1)):
        str_append = str(list1[n-1])+','+str(list2[n-1])+'\n'
        f.write(str_append)
    f.close()


##########################################################
def coordinates():

    ls_lbl_in_f = store_lbl_entry()

    cols=ist1.ls_point  #recupero le coord dalla classe creata (le prime 3 coo sono gli assi)
    coo=cols[3:]        #dalla 3 coordinata in poi lista punti grafico


    ly1=float(ent.get())
    ly2=float(ent7.get())
    lx1=float(ent1.get())
    lx2=float(ent8.get())

    if chkValueY == True: Lyt = math.log10(ly1)- math.log10(ly2)
    if chkValueX == True: Lxt = math.log10(lx1)- math.log10(lx2)

    if chkValueY == False: Lyt = float(ly1)- float(ly2)
    if chkValueX == False: Lxt = float(lx1)-float(lx2)

    xcoo = []
    ycoo = []

    for i in coo:
        xcoo.append(i[0] - cols[0][0])
        ycoo.append((i[1] - cols[0][1]))

    Lx = cols[1][0] - cols[0][0]
    Ly = cols[2][1] - cols[0][1]

    Lx1 = cols[2][0] - cols[0][0]
    Ly1 = cols[1][1] - cols[0][1]

    print 'Lx1 is:',Lx1
    print 'Lx is:', Lx

    if abs(Lx1) > abs(Lx) and abs(Ly1) > abs(Ly):
        Lx = Lx1
        Ly = Ly1

    print Lx1
    print Lx

    fattconvy = Lyt/Ly
    fattconvx = Lxt/Lx

    print Lx
    print Ly

    xcoot = []
    ycoot = []

    for i in xcoo:
        if chkValueX == True: xcoot.append((i*fattconvx)**10)
        if chkValueX == False: xcoot.append(i*fattconvx)

    for i in ycoo:
        if chkValueY == True: xcoot.append((i * fattconvx)**10)
        if chkValueY == False: xcoot.append(i * fattconvx)

    print 'Y coo: ', ycoot
    print 'X coo: ', xcoot

    write_files(ycoot, xcoot, ls_lbl_in_f[0], ls_lbl_in_f[2],ls_lbl_in_f[1],ls_lbl_in_f[3])

    return ycoot, xcoot
















#############################################################
#               INIZIO             CODICE
#############################################################



root = tk.Tk()
root.title("   Geodata Point2Graph  ")
screenwidth = root.winfo_screenwidth()
distance = screenwidth - 500 # 500 se 500x700
root.geometry('500x600+'+str(distance)+'+100') # porta al di sotto dell'angolo di 100 pixel

curr_dir = os.path.dirname(__file__)
img_path = curr_dir + "/image/gd_small.gif"
photo = tk.PhotoImage(file=img_path)
root.tk.call("wm","iconphoto", root._w, photo)

w = tk.Label(root, text="Fill the form below")
w1 = tk.Label(root, text="Select options from file/menu")
w2 = tk.Label(root, text="Follow each step")
w3 = tk.Label(root, text="Grab your data")
w4 = tk.Label(root, text="              ")

w.pack()
w1.pack()
w2.pack()
w3.pack()
w4.pack()

###########################################   ENTRY LABEL

ls_lbl_in = read_label()

lab6 = tk.Label(root, text="Inserire nome file senza estensione")
lab6.pack()
ent6 = tk.Entry(root)
ent6.pack()

################################### YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY

lab = tk.Label(root, text="Inserire coordinata Y")
lab.pack()
ent = tk.Entry(root)
ent.pack()

chkValueY = tk.BooleanVar()
chkValueY = False
chb1 = tk.Checkbutton(root, text="Log scale",var=chkValueY)
chb1.pack()


lab7 = tk.Label(root, text="Inserire origine Y")
lab7.pack()
ent7 = tk.Entry(root)
ent7.insert(0, ls_lbl_in[5])
ent7.pack()

lab2 = tk.Label(root, text="Inserire label Y")
lab2.pack()
ent2 = tk.Entry(root)
ent2.insert(0, ls_lbl_in[0])
ent2.pack()

lab4 = tk.Label(root, text="Inserire unita di misura Y")
lab4.pack()
ent4 = tk.Entry(root)
ent4.insert(0, ls_lbl_in[1])
ent4.pack()

######################################## XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

lab1 = tk.Label(root, text="Inserire coordinata X")
lab1.pack()
ent1 = tk.Entry(root)
ent1.pack()

chkValueX = tk.BooleanVar()
chkValueX = False
chb2 = tk.Checkbutton(root, text="Log scale",var=chkValueX)
chb2.pack()

lab8 = tk.Label(root, text="Inserire origine X")
lab8.pack()
ent8 = tk.Entry(root)
ent8.insert(0, ls_lbl_in[4])
ent8.pack()

lab3 = tk.Label(root, text="Inserire label X")
lab3.pack()
ent3 = tk.Entry(root)
ent3.insert(0, ls_lbl_in[2])
ent3.pack()

lab5 = tk.Label(root, text="Inserire unita di misura X")
lab5.pack()
ent5 = tk.Entry(root)
ent5.insert(0, ls_lbl_in[3])
ent5.pack()




w5 = tk.Label(root,
              justify=tk.LEFT,
              padx = 10,
              text="Fabrizio Peruzzo 2019 Geodata S.p.a").pack(side="left")

#####################################################   FUNZIONI OPENCV  DALLA CLASSE

########################################
ist1 = point2graph()
############Menu########################

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff = 1)
menubar.add_cascade(label="File",  menu = filemenu)

filemenu.add_cascade(label="0) Print_Screen", command = lambda : ist1.print_screen())
filemenu.add_cascade(label="1) Crop_Image", command = lambda : ist1.crop_image())
filemenu.add_cascade(label="2) Pic_Orig_X_Y_Points", command = lambda : ist1.get_point())
entry = print_entry
filemenu.add_cascade(label="3) Print_Entry", command = lambda : entry())
filemenu.add_cascade(label="4) Print_Coordinate", command = lambda : coordinates()) # in automatico scrive il file

filemenu.add_separator()
filemenu.add_cascade(label="Exit", command = root.destroy)
root.config(menu=menubar)





root.mainloop()


