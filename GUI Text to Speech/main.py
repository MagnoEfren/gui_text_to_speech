# Youtube: Magno Efren

from tkinter import Tk , Frame, Button,PhotoImage,Label
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk 
from tkinter import filedialog, messagebox
import pyttsx3


def open_file():
	filepath = filedialog.askopenfilename(title= 'Seleccione archivo',
		filetype = (('archivo txt', '*.txt*'), ('Todos', '*.*')))
	if filepath != ' ':
		file = open(filepath, 'r')
		content = file.read()
		text.delete('1.0', 'end')
		text.insert('0.0', content)
		window.title(filepath)

def start_read():
	text_read = text.get('1.0', 'end')
	voice = selec_voice.get()
	voices = engine.getProperty('voices')
	if voice == 'Ingles':
		engine.setProperty('voice', voices[0].id)
	if voice == 'Español':
		engine.setProperty('voice', voices[1].id)

	if len(text_read)>2:
		engine.say(text_read)
		engine.runAndWait()
		engine.stop()
	else:
		messagebox.showerror('Error', 'No hay un texto para leer')
 
def speed_sound(event):
	level = int(scale_speed.get())
	engine.setProperty('rate', level)
	signal_speed['text']= str(level)

def volume_sound(event):
	level = (scale_volume.get())
	engine.setProperty('volume', round(level,2))
	signal_volume['text']= str(round(level,2))

def save_sound():
	if len(text.get('1.0', 'end'))>2:
		name = text.get('1.0', 'end').split(' ')
		print(name)
		name = name[0:1][0]
		engine.save_to_file(text.get('1.0', 'end'), f'{name}.mp3')
		engine.runAndWait()
		messagebox.showinfo('Aviso', 'Audio guardado correctamente')
	else:
		messagebox.showerror('Error', 'No hay un texto para grabar')


window = Tk() 
window.geometry('600x400+400+100')
window.title('Texto a Voz')
window.config(bg='black')
window.minsize(500, 300)
window.iconbitmap('assets/icon.ico')
engine = pyttsx3.init('sapi5')

image_woman = PhotoImage(file= 'assets/woman.png')
image_record = PhotoImage(file= 'assets/record.png')
image_file = PhotoImage(file= 'assets/file.png')


frame_text = Frame(window, bg= 'white', width=400, height=400)
frame_text.grid(column=0, row=0, sticky='nsew', pady = 5, padx=5)

frame_control = Frame(window, bg= 'black', width=200, height=400)
frame_control.grid(column=1, row=0, sticky='nsew', pady = 5, padx=5)

window.columnconfigure(0, weight=6)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)

frame_text.grid_propagate(0)
frame_control.grid_propagate(0)

frame_text.columnconfigure(0, weight=1)
frame_text.rowconfigure(0, weight=1)

frame_control.columnconfigure([0,1], weight=1)
frame_control.rowconfigure([0,1,2,3,4,5,6,7,8], weight=1)



text = ScrolledText(frame_text, font = ('Corbel', 12, 'italic'), insertbackground= 'blue',
	bg= 'black', fg= 'white')
text.grid(column=0, row=0, sticky= 'nsew')



button_open = Button(frame_control,image = image_file,compound= 'left',text= 'ABRIR ARCHIVO',
font= ('Arial', 11, 'bold') , bg= 'blue', command= open_file)
button_open.grid(columnspan=2, column=0, row=0, sticky='ew')

button_read = Button(frame_control,image = image_woman,compound= 'left',text= 'LEER',
font= ('Arial', 11, 'bold') , bg= 'blue', command= start_read)
button_read.grid(columnspan=2, column=0, row=1, sticky='ew')

button_grab = Button(frame_control,image = image_record,compound= 'left',text= 'GRABAR AUDIO',
font= ('Arial', 11, 'bold') , bg= 'blue', command= save_sound)
button_grab.grid(columnspan=2, column=0, row=2, sticky='ew')

Label(frame_control,  bg='black', fg= 'blue', text= 'Idioma', font= ('Arial', 11, 
	'bold')).grid(columnspan=2, column=0, row=3, sticky='ew')

selec_voice = ttk.Combobox(frame_control, values=['Ingles', 'Español'], state= 'readonly')
selec_voice.grid(columnspan=2, column=0, row=4, sticky='ew')
selec_voice.set('Ingles')

Label(frame_control,  bg='black', fg= 'blue', text= 'Velocidad', font= ('Arial', 11, 
	'bold')).grid(columnspan=2, column=0, row=5, sticky='ew')

scale_speed = ttk.Scale(frame_control,from_= 150,to=350, command= speed_sound)
scale_speed.grid(column=0, row= 6, sticky='ew')

signal_speed = Label(frame_control,  bg='black', fg= 'blue', text= '200', font= ('Arial', 11, 
	'bold'))
signal_speed.grid(column=1, row=6, sticky='ew')


Label(frame_control,  bg='black', fg= 'blue', text= 'Volumen', font= ('Arial', 11, 
	'bold')).grid(columnspan=2, column=0, row= 7, sticky='ew')

scale_volume = ttk.Scale(frame_control,from_= 0, to=1, command= volume_sound)
scale_volume.grid(column=0, row= 8, sticky='ew')

signal_volume = Label(frame_control,  bg='black', fg= 'blue', text= '1', font= ('Arial', 11, 
	'bold'))
signal_volume.grid(column=1, row=8, sticky='ew')

style = ttk.Style()
style.configure('Horizontal.TScale', background='black')

window.mainloop()