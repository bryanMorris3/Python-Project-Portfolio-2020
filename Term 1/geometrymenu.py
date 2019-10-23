#Squad
#9/11/19
#Geometry assignment

#Shapes
def intro(name):
    print("""

    Welcome to Geometry
    please choose an option
    from the list below

    1: Perimeter of a square
    2: Area of a square
    3: Circumference of a circle
    4: Area of a triangle
    5: Volume of a cube
    6: Quit
    """)
def option1():
    print("""Perimeter of a square 
    *------------*
    |            | 
    |            | a
    |            |
    *------------*""")
    variable_a = int(input("Variable A = "))
    sqr_area = 4*variable_a
    print("Perimeter of a square:",sqr_area)
def option2():
    print("""Area of a square
    *------------*
    |            | 
    |            | a
    |            |
    *------------*""")
    variable_a = int(input("Variable A = "))
    sqr_area_sqrd = variable_a*variable_a
    print("Area of a square:",sqr_area_sqrd)
def option3():
    print("""Circumference of a circle
            _____
         .- ``` ' `-.           
       .'          /  `.         
      /           r     \\        
     ;           /        ;       
     |__________/_ |     
     ;         d          ;
      \\                 /       
       \\`.           .'       
         `-._____.-'""")
    
    variable_r = int(input("Variable R = "))
    variable_pi = 3.1415
    cir_circum = 2*variable_pi*variable_r
    print("Circumference of a circle:",cir_circum)
def option4():
    print("""Area of a triangle
            /|\\    
           / | \\
          /  |  \\
         /   h   \\
        /    |    \\
       /_____|_____\\
              b""")
    variable_b = int(input("Variable B = "))
    variable_h = int(input("Variable H = "))
    tri_area = variable_h*variable_b/2
    print("Area of a triangle:",tri_area)
def option5():
    print("""Volume of a cube
          +--------------+
          /|             /|
         / |            / |
        *--+-----------*  |
        |  |           |  | a
        |  |           |  |
        |  |           |  |
        |  +-----------+--+
        | /            | / a
        |/             |/ 
        *--------------*
               ___
               a """)
    variable_a = int(input("Variable A = "))
    cub_vol = variable_a**3
    print("Volume of a cube:",cub_vol) 
def option6():
    varify = input("Are you sure you want to quit?")
    varify = varify.lower()
    if "y" in varify:
        return True
    else:
        return False

def menu():
    
    while True:
        intro("example")
        choice = input("""1, 2, 3, 4, 5, or 6: """)
        if choice == "1":
            option1()
        elif choice == "2":
            option2()
        elif choice == "3":
            option3()
        elif choice == "4":
            option3()
        elif choice == "5":
            option3()     
        elif choice == "6":
            varify = option6()
            if varify:
                break
            else:
                continue
        else:
            print("That isn't an option")
menu()
input("press enter to exit")


input()



