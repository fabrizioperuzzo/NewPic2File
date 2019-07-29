import Tkinter as tk
from class_point2graph import *
import numpy as np
import sys
import os

#########################################################################
#            RICHIAMO TUTTE LE DEF
#########################################################################
def read_label():

    img_path = "SETTINGS\\label_input.txt"

    f = open(img_path, 'r')
    with f:
        ls_label = f.readlines()

    for i in ls_label:
        ls_label[ls_label.index(i)] = i.replace('\n', '')

    label_y_in = ls_label[0]
    unit_y_in = ls_label[1]
    label_x_in = ls_label[2]
    unit_x_in = ls_label[3]

    return label_y_in,unit_y_in,label_x_in,unit_x_in
##########################################################
def write_label(label_y,unit_y,label_x,unit_x):

    ls_label_in=[]
    ls_label_in.append(label_y+'\n')
    ls_label_in.append(unit_y+'\n')
    ls_label_in.append(label_x+'\n')
    ls_label_in.append(unit_x+'\n')

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
    ls_lbl_out = [ent2.get(),ent4.get(),ent3.get(),ent5.get()]
    write_label(ls_lbl_out[0],ls_lbl_out[1],ls_lbl_out[2],ls_lbl_out[3])

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

    cols=ist1.ls_point
    coo=cols[3:]
    Lyt = float(ent.get())
    Lxt = float(ent1.get())
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
        xcoot.append(i*fattconvx)

    for i in ycoo:
        ycoot.append(i*fattconvy)

    print 'Y coo: ', ycoot
    print 'X coo: ', xcoot

    write_files(ycoot, xcoot, ls_lbl_in_f[0], ls_lbl_in_f[2],ls_lbl_in_f[1],ls_lbl_in_f[3])

    return ycoot, xcoot



##########################################################################
def resize_cmd_win():

    from ctypes import windll, create_string_buffer

    # stdin handle is -10
    # stdout handle is -11
    # stderr handle is -12

    h = windll.kernel32.GetStdHandle(-12)
    csbi = create_string_buffer(22)
    res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)

    if res:
        import struct
        (bufx, bufy, curx, cury, wattr,
         left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
        sizex = right - left + 1
        sizey = bottom - top + 1
    else:
        sizex, sizey = 80, 25  # can't determine actual size - return default values

    print sizex, sizey
    os.system('mode con: cols=100 lines=10')


##########################################################################
def resize_cmd_win_small():

    from ctypes import windll, create_string_buffer

    # stdin handle is -10
    # stdout handle is -11
    # stderr handle is -12

    h = windll.kernel32.GetStdHandle(-12)
    csbi = create_string_buffer(22)
    res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)

    if res:
        import struct
        (bufx, bufy, curx, cury, wattr,
         left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
        sizex = right - left + 1
        sizey = bottom - top + 1
    else:
        sizex, sizey = 80, 25  # can't determine actual size - return default values

    print sizex, sizey
    os.system('mode con: cols=50 lines=5')


















############################################################################
#               INIZIO             CODICE
############################################################################

resize_cmd_win_small()

root = tk.Tk()
root.title("   Geodata Point2Graph  ")
screenwidth = root.winfo_screenwidth()
distance = screenwidth - 500 # 500 se 500x700
root.geometry('500x700+'+str(distance)+'+100') # porta al di sotto dell'angolo di 100 pixel

img_path = "image\\gd_small.gif"

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

##########

lab = tk.Label(root, text="Inserire coordinata Y")
lab.pack()
ent = tk.Entry(root)
ent.pack()

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

###########

lab1 = tk.Label(root, text="Inserire coordinata X")
lab1.pack()
ent1 = tk.Entry(root)
ent1.pack()

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

ent7 = tk.Entry(root)
ent7.insert(0, 'Here the Python output are shown')
ent7.pack()



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
filemenu.add_cascade(label=" Resize_cmd_window_BIG", command = lambda : resize_cmd_win()) # in automatico scrive il file
filemenu.add_cascade(label=" Resize_cmd_window_SMALL", command = lambda : resize_cmd_win_small()) # in automatico scrive il file

filemenu.add_separator()
filemenu.add_cascade(label="Exit", command = root.destroy)
root.config(menu=menubar)





root.mainloop()


