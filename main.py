import tkinter as tk

root = tk.Tk()
root.title('Radio Buttons e Select Box')
root['borderwidth'] = 10

def on_botao_clicado():
    label_text = var_curso.get()
    label_escolha.config(text = 'Curso escolhido: ' + label_text.upper())
    print(var_email.get())

var_curso = tk.StringVar(root, value=' ')
var_email = tk.BooleanVar(root)

label_curso = tk.Label(root, text='Curso: ')
label_escolha = tk.Label(root, text='')
radio_elt = tk.Radiobutton(root, text='Eletrônica', value = 'elt', variable = var_curso)
radio_edi = tk.Radiobutton(root, text='Edificações', value = 'edi', variable = var_curso)
radio_mec = tk.Radiobutton(root, text='Mecânica', value = 'mec', variable = var_curso)
radio_min = tk.Radiobutton(root, text='Mineração', value = 'min', variable = var_curso)
check_email = tk.Checkbutton(root, text="Concordo com os termos de serviço", variable = var_email)
button = tk.Button(root, text='Teste')
button['command'] = on_botao_clicado

label_curso.grid(row=0, column=0, padx=(0,10), sticky = tk.E)
radio_elt .grid(row=0, column=1, sticky=tk.W)
radio_edi .grid(row=1, column=1, sticky=tk.W)
radio_mec .grid(row=2, column=1, sticky=tk.W)
radio_min .grid(row=3, column=1, sticky=tk.W)
check_email.grid(row=4, column = 0, columnspan = 2)
button.grid(row=5, column = 0, columnspan = 2)
label_escolha.grid(row=6, column = 0, sticky=tk.W, pady=(15,0))

root.mainloop()

