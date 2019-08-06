import Tkinter as tk
from class_point2graph import *
import tkMessageBox
import sys
import os
import math
#from main_def import *






# FUNZIONI OPENCV  DALLA CLASSE
#############################################################################
ist1 = point2graph()    #######    INITIALIZE THE CLASS -_> ISTANCE   #######
############Menu#############################################################





##########################################################
#            RICHIAMO TUTTE LE DEF
##########################################################
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


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

    except:  # se non trova il file con input .txt

        label_y_in = 'labely'
        unit_y_in = 'unity'
        label_x_in = 'labelx'
        unit_x_in = 'unitx'
        x0_in = 0
        y0_in = 0

    return label_y_in, unit_y_in, label_x_in, unit_x_in, x0_in, y0_in
##########################################################


def write_label(label_y, unit_y, label_x, unit_x, x0, y0):

    ls_label_in = []
    ls_label_in.append(label_y + '\n')
    ls_label_in.append(unit_y + '\n')
    ls_label_in.append(label_x + '\n')
    ls_label_in.append(unit_x + '\n')
    ls_label_in.append(x0 + '\n')
    ls_label_in.append(y0 + '\n')

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
    ls_lbl_out = [ent2.get(), ent4.get(), ent3.get(),
                  ent5.get(), ent8.get(), ent7.get()]
    write_label(ls_lbl_out[0], ls_lbl_out[1], ls_lbl_out[2],
                ls_lbl_out[3], ls_lbl_out[4], ls_lbl_out[5])

    return ls_lbl_out


##########################################################
# scrivi file con coordinate FINALI SU CSV
def write_files(list1, list2, label1, label2, unit1, unit2):

    csv_name = "OUTPUT\\" + ent6.get() + ".csv"

    f = open(csv_name, 'w')
    f.write(ent6.get() + '\n')
    f.write(label1 + ';' + label2 + '\n')
    f.write(unit1 + ';' + unit2 + '\n')

    for n in range(1, (len(list1)+1)):
        str_append = str(list2[n - 1]) + ';' + str(list1[n - 1]) + '\n'
        f.write(str_append)
    f.close()


##########################################################
def coordinates():

    # salva le entries in un file per averlo come input
    # nella sessione successiva
    ls_lbl_in_f = store_lbl_entry()

    # recupero le coord dalla classe creata (le prime 3 coo sono gli assi)
    cols = ist1.ls_point
    coo = cols[3:]  # dalla 3 coordinata in poi lista punti grafico

    ckvY = chkValueY.get()
    ckvX = chkValueX.get()

    try:
        if ckvY == True:
            ly1 = math.log10(float(ent.get()))
            ly2 = math.log10(float(ent7.get()))  # origin of Y axis
        else:
            ly1 = float(ent.get())
            ly2 = float(ent7.get())  # origin of Y axis

        if ckvX == True:
            lx1 = math.log10(float(ent1.get()))
            lx2 = math.log10(float(ent8.get()))  # origin of Y axis
        else:
            lx1 = float(ent1.get())
            lx2 = float(ent8.get())  # origin of X axis
    except:
        tkMessageBox.showerror("Error", "Errore formato")

    Lyt = ly1 - ly2
    Lxt = lx1 - lx2

    xcoo = []
    ycoo = []

    for i in coo:
        xcoo.append(i[0] - cols[0][0])
        ycoo.append((i[1] - cols[0][1]))

    Lx = cols[1][0] - cols[0][0]
    Ly = cols[2][1] - cols[0][1]

    Lx1 = cols[2][0] - cols[0][0]
    Ly1 = cols[1][1] - cols[0][1]

    print 'Lx1 is:', Lx1
    print 'Lx is:', Lx

    if abs(Lx1) > abs(Lx) and abs(Ly1) > abs(Ly):
        Lx = Lx1
        Ly = Ly1

    print 'Lx is:', Lx
    print 'Ly is:', Ly
    print 'Lyt is:', Lyt
    print 'Lxt is:', Lxt
    print 'ly1 is:', ly1
    print 'lx1 is:', lx1
    print 'chkvaluey is:', ckvY
    print 'chkvaluex is:', ckvX

    fattconvy = Lyt / Ly
    fattconvx = Lxt / Lx

    print Lx
    print Ly

    xcoot = []
    ycoot = []

    for i in xcoo:
        if ckvX == True:
            xcoot.append(math.pow(10, (i * fattconvx + lx2)))
        else:
            xcoot.append(i * fattconvx + lx2)

    for i in ycoo:
        if ckvY == True:
            ycoot.append(math.pow(10, (i * fattconvy + ly2)))
        else:
            ycoot.append(i * fattconvy + ly2)

    if ckvY == True:
        print 'Y coo: ', ['%.2E' % x for x in ycoot]
    else:
        print 'Y coo: ', ycoot

    if ckvX == True:
        print 'X coo:', ['%.2E' % x for x in xcoot]
    else:
        print 'X coo: ', xcoot

    write_files(
        ycoot, xcoot, ls_lbl_in_f[0], ls_lbl_in_f[2], ls_lbl_in_f[1], ls_lbl_in_f[3])

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
























#############################################################
#               INIZIO             CODICE
#############################################################

# tk= tkinter is the module
# Tk is the class inside tkinter you dont need arguments


resize_cmd_win_small()

root = tk.Tk()






########      TOP FRAME   ######################################################





root.title("   Geodata Point2Graph  ")
screenwidth = root.winfo_screenwidth()
winwidth = 400
winheight = 600
distance = screenwidth - winwidth -20
# porta al di sotto dell'angolo di 100 pixel
root.geometry(str(winwidth) + 'x' + str(winheight) +
              '+' + str(distance) + '+100')

curr_dir = os.path.dirname(__file__)

img_path = curr_dir + "/image/gd_small.gif"

photo = tk.PhotoImage(file=img_path)
root.tk.call("wm", "iconphoto", root._w, photo)







topframe = tk.Frame(root, bg="blue")
topframe.pack()

button1 = tk.Button(topframe, text="1 PRNT SCR", fg="black", command=lambda: ist1.print_screen())
button2 = tk.Button(topframe, text="2 CROP IMG", fg="black", command=lambda: ist1.crop_image())
button3 = tk.Button(topframe, text="3 PIC PNT", fg="black", command=lambda: ist1.get_point())
button4 = tk.Button(topframe, text="4 PRNT COOR", fg="black", command=lambda: coordinates())

button1.pack(side='left', padx=4, pady=2)
button2.pack(side='left', padx=4, pady=2)
button3.pack(side='left', padx=4, pady=2)
button4.pack(side='left', padx=4, pady=2)

topframe.pack(side="top", fill="x")







w = tk.Label(root, text="Fill the form below")
#w1 = tk.Label(root, text="Select options from file/menu ")
w2 = tk.Label(root, text="Follow steps from 1 to 4")
w3 = tk.Label(root, text="Grab csv data in 'OUTPUT' folder")
w4 = tk.Label(root, text="              ")

w.pack()
#w1.pack()
w2.pack()
w3.pack()
w4.pack()

# ENTRY LABEL

ls_lbl_in = read_label()

lab6 = tk.Label(root, text="Inserire nome file senza estensione")
lab6.pack()
ent6 = tk.Entry(root)
ent6.pack()











#############        BOTTOM    FRAME      ********************************
####            to be inserted before every other things
####   il primo che indico come bottom ha la precedenza sugli altri

bottomframe = tk.Frame(root)


# ent9 = tk.Entry(bottomframe)
# ent9.insert(0, 'Here the Python output are shown')
# ent9.pack()


w5 = tk.Label(bottomframe,
              justify=tk.LEFT,
              padx=10,
              text="Fabrizio Peruzzo 2019 Geodata S.p.a").pack(side="left")

bottomframe.pack(side="bottom", padx = 5 )






########               LEFT FRAME             ##############################

leftframe = tk.Frame(root)

lab = tk.Label(leftframe, text="Inserire coordinata Y")
lab.pack()
ent = tk.Entry(leftframe)
ent.pack()

chkValueY = tk.BooleanVar()
#chkValueY = False
chb1 = tk.Checkbutton(leftframe, text="Log scale", variable=chkValueY)
chb1.pack()


lab7 = tk.Label(leftframe, text="Inserire origine Y")
lab7.pack()
ent7 = tk.Entry(leftframe)
ent7.insert(0, ls_lbl_in[5])
ent7.pack()

lab2 = tk.Label(leftframe, text="Inserire label Y")
lab2.pack()
ent2 = tk.Entry(leftframe)
ent2.insert(0, ls_lbl_in[0])
ent2.pack()

lab4 = tk.Label(leftframe, text="Inserire unita di misura Y")
lab4.pack()
ent4 = tk.Entry(leftframe)
ent4.insert(0, ls_lbl_in[1])
ent4.pack()



leftframe.pack(side="left", padx = 5)













#############        RIGHT    FRAME      ********************************


rightframe = tk.Frame(root)

lab1 = tk.Label(rightframe, text="Inserire coordinata X")
lab1.pack(padx=5)
ent1 = tk.Entry(rightframe)
ent1.pack(padx=5)

chkValueX = tk.BooleanVar()
#chkValueX = False
chb2 = tk.Checkbutton(rightframe, text="Log scale", var=chkValueX)
chb2.pack()

lab8 = tk.Label(rightframe, text="Inserire origine X")
lab8.pack()
ent8 = tk.Entry(rightframe)
ent8.insert(0, ls_lbl_in[4])
ent8.pack()

lab3 = tk.Label(rightframe, text="Inserire label X")
lab3.pack(padx=5)
ent3 = tk.Entry(rightframe)
ent3.insert(0, ls_lbl_in[2])
ent3.pack(padx=5)

lab5 = tk.Label(rightframe, text="Inserire unita di misura X")
lab5.pack(padx=5)
ent5 = tk.Entry(rightframe)
ent5.insert(0, ls_lbl_in[3])
ent5.pack(padx=5)

rightframe.pack(side="right")






















#########           menubar  ****************************



menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=1)
menubar.add_cascade(label="File",  menu=filemenu)

filemenu.add_cascade(label="1) Print_Screen", command=lambda: ist1.print_screen())
filemenu.add_cascade(label="2) Crop_Image", command=lambda: ist1.crop_image())
filemenu.add_cascade(label="3) Pic_Orig_X_Y_Points", command=lambda: ist1.get_point())
entry = print_entry
#filemenu.add_cascade(label="3) Print_Entry", command=lambda: entry()) donna inutile
filemenu.add_cascade(label="4) Print_Coordinate", command=lambda: coordinates())  # in automatico scrive il file

filemenu.add_separator()
filemenu.add_cascade(label=" Resize_cmd_window_BIG",
                     command=lambda: resize_cmd_win())  # in automatico scrive il file
filemenu.add_cascade(label=" Resize_cmd_window_SMALL",
                     command=lambda: resize_cmd_win_small())  # in automatico scrive il file

filemenu.add_separator()
filemenu.add_cascade(label="Reset Data", command=lambda: ist1.reinitialize())
#filemenu.add_cascade(label="Restart", command=lambda: restart_program()) non funziona bene quando vado a riprendere i punti
filemenu.add_cascade(label="Exit", command=root.destroy)

root.config(menu=menubar)










root.mainloop()
