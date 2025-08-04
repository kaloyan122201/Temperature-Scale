from tkinter import *

def update_label(current_value_of_the_scale):       #takes the current value every time user moves the scroll
    value_as_int = int(current_value_of_the_scale) # I take the int of that value because before that is str
    if value_as_int <=33:               # depending on the temperature i put different color
        color = "blue"                  # Hot-Red;Normal-Orange;Cold-Blue
    elif value_as_int <=66:
        color = "Orange"
    else:
        color = "Red"
                                        #print the message with the proper color
    value_label.config(text=f"{current_value_of_the_scale} °C",fg=color)
def submit():
    if scale.get() == scale["to"]:      #if the value of the scrolling point = 0
        print(f"It is freezing, the scale has frozen at {str(scale.get())} degree °C")
    elif scale.get() == scale["from"]:  #elif the value = 100 degrees
        print(f"Everything is melting, the scale has stopped at {str(scale.get())} degree °C")
    else:
        print(f"Temperature is {scale.get()} degree °C")


window = Tk()
window.config(width=300, height= 700)
window.title("Temperature scale")       #title of the program


hot_label = Label(window,text = "🔥",font= ("Arial",40))
hot_label.pack()



scale = Scale(window,
              from_=100,        #sets starting point - 100 degrees
              to=0,             #sets stopping point - 0 degrees
              font =("Arial",20),
              orient=VERTICAL,  #choosing vertical or horizontal scale
              width=30,         #width of the scale
              length=600,       #height of the scale
              tickinterval=10,  #intervals between start and stop point
              showvalue = False,    # show tha value on the scroll = False
              bg = "White",         #background color
              fg = "Red",           #foreground color
              troughcolor="grey",    #color of the scroll
              command= update_label
              )

value_label = Label(window, text=f"{scale.get()} °C", font=("Arial", 16))
value_label.pack()


scale.config(command=update_label)
scale.set(((scale["from"] - scale["to"]) /2 + scale["to"]))     #setting that point to start at the middle of the scale
scale.pack()

cold_label = Label(window,text ="❄",font=("Arial",30))      #cannot upload image so i use emoji
cold_label.pack()
submit = Button(window,text="Submit",command=submit)        #submit button to print messages with functions
submit.pack()
window.mainloop()