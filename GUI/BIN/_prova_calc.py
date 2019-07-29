cols = [[17, 32], [17, 62], [45, 32], [332, 228], [402, 165], [145, 894], [456, 78], [23, 89], [78, 45], [89, 45]]
coo = cols[3:]

xcoo=[]
ycoo=[]

for i in coo:
    xcoo.append(i[0]-cols[0][0])
    ycoo.append((i[1]-cols[0][1]))

Lx = cols[1][0]-cols[0][0]
Ly = cols[2][1]-cols[0][1]
Lx1 = cols[1][1]-cols[0][0]
Ly1 = cols[2][0]-cols[0][1]

if Lx1>Lx and Ly1>Ly:
    Lx=Lx1
    Ly=Ly1

a=float(-10.1518418912891)

a=round(a,2)

print abs(a)

#######################################################

def write_files(list1,list2):
    f = open("OUTPUT\\coo.txt", 'w')
    e=0
    f.write('z,qc\n')
    for n in range(1,len(list1)):
        str_append = str(list1[n-1])+','+str(list2[n-1])+'\n'
        f.write(str_append)
    f.close()

###############################

a
print xcoo
print type(xcoo)

write_files(xcoo,ycoo)

xcoo_str =[]

for i in xcoo:
    xcoo_str.append(str(i))

f = open("OUTPUT\\list_coo.txt", 'w')
with f:
    f.writelines(xcoo_str)

print 'controlla se la funzione e chiusa:', f.closed
print xcoo_str
print type(xcoo_str)


################

def read_label():
    f = open("OUTPUT\\label_input.txt", 'r')
    with f:
        ls_label = f.readlines()

    for i in ls_label:
        ls_label[ls_label.index(i)] = i.replace('\n', '')

    label_y_in = ls_label[0]
    unit_y_in = ls_label[1]
    label_x_in = ls_label[2]
    unit_x_in = ls_label[3]

    return label_y_in,unit_y_in,label_x_in,unit_x_in

list_in = read_label()

print list_in


#################

def write_label(label_y,unit_y,label_x,unit_x):

    ls_label_in=[]

    ls_label_in.append(label_y+'\n')
    ls_label_in.append(unit_y+'\n')
    ls_label_in.append(label_x+'\n')
    ls_label_in.append(unit_x+'\n')

    f = open("OUTPUT\\label_input_.txt", 'w')

    with f:
        ls_label = f.writelines(ls_label_in)




