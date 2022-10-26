from tkinter import *
# from tkinter.ttk import *

"""
int A1=5
int BBB2 =1034
int cresult = A1 +BBB2 * BBB2
if (cresult >10):
    print(“TinyPie ” )
"""
current_line_index = 0


def next_line():
    global current_line_index

    # insert line number into line_num_TextBox and update fields
    line_num_TextBox.delete("1.0", "end")
    #print("current line is " + str(current_line_index) + '\n')
    line_num_TextBox.insert('end', str(current_line_index))

    text = input_TextBox.get('1.0', 'end-1c').split('\n')
    if current_line_index >= len(text):
        return

    output_TextBox.insert('end', text[current_line_index] + '\n')
    current_line_index += 1


lex = Tk()
lex.title('Lexer for TinyPie')
lex.geometry("800x600")

input_label = Label(lex, text='Source Code')
input_label.place(x=50, y=25)
input_TextBox = Text(lex, height=20, width=40)
input_TextBox.pack(expand=False)
input_TextBox.place(x=50, y=50)

output_label = Label(lex, text='Tokens')
output_label.place(x=400, y=25)
output_TextBox = Text(lex, height=20, width=40)
output_TextBox.pack(expand=True)
output_TextBox.place(x=400, y=50)

line_num_label = Label(lex, text='Current line number:')
line_num_label.place(x=50, y=385)
line_num_TextBox = Text(lex, height=1, width=3)
line_num_TextBox.place(x=165, y=385)

next_button = Button(lex, text='Next Line', command=next_line)
next_button.place(x=50, y=420)

exit_button = Button(lex, text='Exit', width=10, command=lex.destroy)
exit_button.place(x=550, y=420)

lex.mainloop()
