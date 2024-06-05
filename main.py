import turtle
import pandas as pd

df=pd.read_csv(r'50_states.csv')
all_states=df.state.to_list()
guessed_states=[]
screen=turtle.Screen()
screen.title("Guess the U.S. States ")
image=r"blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
#code to get the coordinates from the map (blank_states_img.gif)
#def get_mouse_click_coor(x,y):
#    print(x,y)

#turtle.onscreenclick(get_mouse_click_coor)

#turtle.mainloop()
while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 states correct",prompt="What's another state's name?").title()
    if answer_state=="Exit":
        missing_states=[state for state in all_states if state not in guessed_states]
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv(r"/Users/arnabkumartripathy/Desktop/US_state_game/States_missed.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=df[df.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)#t.write(state_data.state.item())

