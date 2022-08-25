import turtle
from prettytable import PrettyTable

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.color('DarkKhaki')
turtle.forward(100)
my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

my_table = PrettyTable()
my_table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
my_table.add_column('Type', ['Electric', 'Water', 'Fire'])
my_table.align = 'l'
print(my_table)
