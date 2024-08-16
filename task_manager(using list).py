# initialzing variables and list
monday="Go for a walk. Water the plants. Plan the week's goals."
tuesday="Write a blog post. Do 30 minutes of exercise. Call a friend."
wednesday="Organize your workspace.Read a chapter of a book. Prepare a healthy meal."
thursday="Finish a coding challenge. Review your finances. Catch up on emails."
friday="Clean the house. Watch a documentary. Update your resume."
saturday="Go grocery shopping. Do laundry. Spend time with family."
sunday="Plan next week. Go for a hike. Meditate for 20 minutes."

#storing in list 
a=[monday,tuesday,wednesday,thursday,friday,saturday,sunday]

#taking input from user
b=input("enter day: ")

#using if elif statements and for loop
if 'monday' in b:
    for x in range(1):
        print(a[0])
elif 'tuesday' in b:
    for x in range(1):
        print(a[1])
elif 'wednesday' in b:
    for x in range(1):
        print(a[2])
elif 'thursday' in b:
    for x in range(1):
        print(a[3])
elif 'friday' in b:
    for x in range(1):
        print(a[4])
elif 'saturday' in b:
    for x in range(1):
        print(a[5])
elif 'sunday' in b:
    for x in range(1):
        print(a[6])
else :
    print("Not entered!")


