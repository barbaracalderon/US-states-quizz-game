import turtle
import pandas

screen = turtle.Screen()
screen.title("United States of America 'State Quiz' Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
us_states = data.state.to_list()
correct_states = []
while len(correct_states) < 50:
    user_state = screen.textinput(title=f"{len(correct_states)}/50 US 'State' Quiz!",
                                  prompt="What's another US state name?").strip().title()
    if user_state == "Exit":
        missed_states = [state for state in us_states if state not in correct_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if user_state in us_states:
        correct_states.append(user_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(f'{state_data.state.item()}', True, align="center", font=("Arial", 7, "normal"))

screen.exitonclick()
