#initializing empty list
monday=[]
tuesday=[]
wednesday=[]
thursday=[]
friday=[]
saturday=[]
sunday=[]

#taking input and storing in list
for x  in range(1):

    M= input("enter monday tasks:")
    monday.append(M)

    T= input("enter tuesday tasks:")
    tuesday.append(T)

    W= input("enter wednesday tasks:")
    wednesday.append(W)

    TH= input("enter thursday tasks:")
    thursday.append(TH)

    F= input("enter friday here:")
    friday.append(F)

    S= input("enter saturday here:")
    saturday.append(S)

    SA= input("enter sunday tasks:")
    sunday.append(SA)

# input of day 
z = input("Enter Day here For Tasks:")

#using if to show tasks
if 'monday' in z:
    for z in monday:
        print(z)
elif 'tuesday' in z:
    for z in tuesday:
        print(z)
elif 'wednesday' in z:
    for z in wednesday:
        print(z)
elif 'thursday' in z:
    for z in thursday:
        print(z)
elif 'friday' in z:
    for z in friday:
        print(z)
elif 'saturday' in z:
    for z in saturday:
        print(z)
elif 'sunday' in z:
    for z in sunday:
        print(z)
