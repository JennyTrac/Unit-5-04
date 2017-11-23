# created by jenny trac
# created on Nov 20 2017
# program lets user calculate average of marks

import ui

marks = []

def enter_touch_up_inside(sender):
    # button to add marks to the array
    
    global marks
    
    try:
        new_mark = int(view['input_textfield'].text)
        if new_mark >= 0 and new_mark <= 100:
            marks.append(new_mark)
            view['marks_textview'].text = view['marks_textview'].text + '\r' + str(new_mark)
            view['average_label'].text = " "
        else:
            view['average_label'].text = "Error: Not an acceptable input"
    except:
        view['average_label'].text = "Error: Not an acceptable input"

def calculate_average_touch_up_inside(sender):
    # button to calculate the average
    
    total = 0
    for every_mark in marks:
        total = total + every_mark
    average = total / len(marks)
    view['average_label'].text = "The average is: " + str(average)

view = ui.load_view()
view.present('sheet')
