dict_students={}
n=int(input("Enter number of students: "))
t=0
for i in range(n):
    name=input("Enter name of student: ")
    dict_students[name] = [[0,0,0,0,0],[0,0,'0']]
    total=0
    for j in range (5):
        dict_students[name][0][j]=float(input(f"Enter marks of subject {j+1}: "))
        total+=dict_students[name][0][j]
    dict_students[name][1][0]=total
    dict_students[name][1][1]=total/5
    if(total>=450):
        dict_students[name][1][2]='A'
        t+=1
    elif(total>=400):
        dict_students[name][1][2]='B'
    elif(total>=350):
        dict_students[name][1][2]='C'
    elif(total>=300):
        dict_students[name][1][2]='D'
    elif(total>=250):
        dict_students[name][1][2]='E'
    else:
        dict_students[name][1][2]='F'
    # print("Toppers:\n")
    # if(dict_students[name][1][2]=='A'):
    #     print(name)
    # if(t==0):
    #     print("No toppers")
name_list=list(dict_students.keys())
if(t==0):
    print("No toppers")
else:
    print("Topper List")
    for i in range(n):
        if(dict_students[name_list[i]][1][2]=='A'):
            print(f"Name: {name_list[i]} Total: {dict_students[name_list[i]][1][0]} Average: {dict_students[name_list[i]][1][1]}")
print(dict_students)

