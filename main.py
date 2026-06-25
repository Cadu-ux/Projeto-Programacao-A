import tkinter as tk
from tkinter import ttk

# Quando mouse é pressionado
def iniciar_figura_nova(event):
    global figura_nova
    tipo = tipo_figura_var.get()
    cor_borda = cor_borda_var.get()
    cor_preenchimento = cor_preenchimento_var.get()
    
    if tipo in ('Linha', 'Retângulo', 'Oval'):
        figura_nova = (tipo, (event.x, event.y, event.x, event.y), cor_borda, cor_preenchimento)
    else:
        figura_nova = ("Rabisco", [(event.x, event.y)], cor_borda, cor_preenchimento)

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova is None:
        return
        
    fig, values, cor_borda, cor_preenchimento = figura_nova
    
    if fig == "Rabisco":
        values.append((event.x, event.y))
        figura_nova = (fig, values, cor_borda, cor_preenchimento)
    else: # figura_nova[0] == "linha"
        figura_nova = (fig, (values[0], values[1], event.x, event.y), cor_borda, cor_preenchimento)
        
    desenhar()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event):
    if figura_nova is not None and not incompleta(figura_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figuras.append(figura_nova)
    desenhar()

def desenhar():
    canvas.delete("all")
    for fig, values, cor_borda, cor_preenchimento in figuras:
        if fig == "Linha":
            canvas.create_line(values[0], values[1], values[2], values[3], fill=cor_borda)
        elif fig == "Rabisco":
            canvas.create_line(values, fill=cor_borda)
        elif fig == "Retângulo":
            canvas.create_rectangle(values[0], values[1], values[2], values[3], outline=cor_borda, fill=cor_preenchimento)
        elif fig == "Oval":
            canvas.create_oval(values[0], values[1], values[2], values[3], outline=cor_borda, fill=cor_preenchimento)

def desenhar_figura_nova():
    if figura_nova is None:
        return
        
    fig, values, cor_borda, cor_preenchimento = figura_nova
    
    if fig == "Linha":
        canvas.create_line(values[0], values[1], values[2], values[3], fill=cor_borda, dash=(4, 2))
    elif fig == "Rabisco":
        canvas.create_line(values, fill=cor_borda, dash=(4, 2))
    elif fig == "Retângulo":
        canvas.create_rectangle(values[0], values[1], values[2], values[3], outline=cor_borda, fill=cor_preenchimento, dash=(4, 2))
    elif fig == "Oval":
        canvas.create_oval(values[0], values[1], values[2], values[3], outline=cor_borda, fill=cor_preenchimento, dash=(4, 2))

def incompleta(figura):
    fig, values, cor_borda, cor_preenchimento = figura
    if fig in ("Linha", "Retângulo", "Oval"):
        return (values[0], values[1]) == (values[2], values[3])
    else : # fig == "rabisco"
        return len(values) <= 1


figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras


def main():
    global canvas, tipo_figura_var, cor_borda_var, cor_preenchimento_var

    root = tk.Tk()
    frame = tk.Frame(root)

    # Widgets arranjados com Layout grid dentro de frame
    paddings = {'padx': 5, 'pady': 5}

    # label
    ttk.Label(frame, text='Figura:').grid(column=0, row=0, sticky=tk.W, **paddings)
    
    # option menu
    tipo_figura_var = tk.StringVar(root) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
    option_menu_figura = ttk.OptionMenu(frame, tipo_figura_var, 'Linha', 'Linha', 'Rabisco', 'Retângulo', 'Oval')
    option_menu_figura.grid(column=1, row=0, sticky=tk.W, **paddings)

    ttk.Label(frame, text='Cor da Borda:').grid(column=0, row=1, sticky=tk.W, **paddings)
    cor_borda_var = tk.StringVar(root)
    option_menu_borda = ttk.OptionMenu(frame, cor_borda_var, 'black', 'black', 'red', 'green', 'blue', 'orange', 'purple')
    option_menu_borda.grid(column=1, row=1, sticky=tk.W, **paddings)

    ttk.Label(frame, text='Preenchimento:').grid(column=0, row=2, sticky=tk.W, **paddings)
    cor_preenchimento_var = tk.StringVar(root)
    option_menu_preenchimento = ttk.OptionMenu(frame, cor_preenchimento_var, '', '', 'black', 'red', 'green', 'blue', 'orange', 'purple', 'yellow')
    option_menu_preenchimento.grid(column=1, row=2, sticky=tk.W, **paddings)

    # Área de desenho
    canvas = tk.Canvas(frame, bg='white', width=600, height=600)
    canvas.grid(column=0, row=3, columnspan=2, sticky=tk.W, **paddings)

    frame.pack()

    # Eventos de mouse associados ao canvas - com seus callbacks
    canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
    canvas.bind('<B1-Motion>', atualizar_figura_nova)
    canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

    root.mainloop()


if __name__ == "__main__":
    main()