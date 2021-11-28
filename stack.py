stack = []
exit=True

def pushin():
    element=input("Enter the element:")
    stack.append(element)

def display():
    for i in stack:
        print(i)

def popout():
    popel=stack.pop()
    print("Element Popped:"+popel)

def isempty(stack):
    if len(stack)==0:
        print("stack underflow!")

print('\nStack Implemented!')
exit=True
while exit==True:
    print('\nChoose stack operation:')
    print('1.Push')
    print('2.Pop:')
    print('3.Display:')
    print('4.Exit:')
    choice=int(input("Enter your choice:"))

    if choice==1:
        pushin()
    elif choice==2:
        popout()
    elif choice==3:
        display()
    elif choice==4:
        exit=False
    else:
        print("Invalid choice")
    