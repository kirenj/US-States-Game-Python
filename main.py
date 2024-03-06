import turtle
import pandas

screen =  turtle.Screen()
turtle1 = turtle.Turtle()

screen.title("U.S States Game")
image = "./blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
turtle1.hideturtle()
turtle1.penup()
turtle1.color('black')


### The below code is to get the x,y coordinates of the state from the map
# def get_mouse_click_coord(x,y):
#   print(x,y)

# # The below code is an alternate for screen.exitonclick()
# turtle.onscreenclick(get_mouse_click_coord)
# screen.mainloop()

data = pandas.read_csv("./50_states.csv")
states = data["state"]
game_continue = True
state_count = 0
already_answered = []

while game_continue is True:
  answer = screen.textinput(title=f"{state_count}/50 States Correct", prompt="What's another state's name?")
  if answer is not None:
    answer = answer.title()  
    for i in states:
      if i == answer and i not in already_answered:
        state = data[data["state"] == i]
        x_pos = float(state.x.iloc[0])
        y_pos = float(state.y.iloc[0])
        turtle1.goto(x_pos, y_pos)
        turtle1.write(arg=i, align='center', font=('Ariel', 8, 'normal'))
        already_answered.append(i)
        state_count += 1
          # print(f"X_pos = {x_pos}, Y_pos = {y_pos}")
      # else:
      #   pass
    if answer == 'Exit':      
      break
  if state_count == 50:
    game_continue = False



# screen.mainloop()

