import turtle, pandas

screen = turtle.Screen()
screen.title('US States Game')
img = 'blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)

# screen.exitonclick()

data=pandas.read_csv('50_states.csv')

list_of_states=data['state'].to_list()

x = data['x']
y = data['y']

user_list=[]

while len(user_list)<50:
    answer_state = screen.textinput(title=f'{len(user_list)} the state', prompt='What is the next state?').title()
    #print(answer_state)
    if answer_state is None:
       print("Input cancelled. Please enter a valid state name.")
    if answer_state=='Exit':
        break
    #print(answer_state)

    if answer_state in list_of_states:
       user_list.append(answer_state)
      # print(user_list)
       text = turtle.Turtle()
       text.penup()
       text.hideturtle()
       text.goto(int(data[data['state'] == answer_state]['x'].iloc[0]),
                 int(data[data['state'] == answer_state]['y'].iloc[0]))
       text.write(f'{answer_state}', align='center', font=('Arial', 8, 'normal'))

       #print(data[data['state']==answer_state]['x'])

forgotten=[]

for item in list_of_states:
    if item not in user_list:
        forgotten.append(item)

my_df=pandas.DataFrame(forgotten, columns=['state'])
my_df.to_csv('forgotten_states')
