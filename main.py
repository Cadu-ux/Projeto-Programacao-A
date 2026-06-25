import tkinter as tk
from tkinter import ttk
from figuras import Linha, Rabisco, Retangulo, Oval, Poligono

# Dicionário que mapeia a string do menu para a Classe correspondente
MAPA_FIGURAS = {
    'Linha': Linha,
    'Rabisco': Rabisco,
    'Retângulo': Retangulo,
    'Oval': Oval,
    'Polígono': Poligono
}

# Variáveis globais de estado
figuras = []       
figura_nova = None 

def iniciar_figura_nova(event):
    global figura_nova
    tipo = tipo_figura_var.get()
    cor_borda = cor_borda_var.get()
    cor_preenchimento = cor_preenchimento_var.get()
    
    # Recupera a classe correspondente ao tipo selecionado
    ClasseFigura = MAPA_FIGURAS.get(tipo)
    
    if ClasseFigura:
        # Instancia o objeto da figura, delegando a ele a responsabilidade de iniciar os dados
        figura_nova = ClasseFigura(event.x, event.y, cor_borda, cor_preenchimento)

def atualizar_figura_nova(event):
    if figura_nova is None:
        return
        
    # Polimorfismo: Não importa que figura seja, basta mandar atualizar suas coordenadas
    figura_nova.atualizar(event.x, event.y)
    desenhar()

def incluir_figura_nova(event):
    global figura_nova
    if figura_nova is not None and not figura_nova.incompleta():
        figuras.append(figura_nova)
    
    figura_nova = None # Reseta o estado
    desenhar()

def desenhar():
    canvas.delete("all")
    
    # Desenha todas as figuras definitivas
    for fig in figuras:
        fig.desenhar(canvas)
        
    # Desenha a figura que está em processo de criação (com borda tracejada)
    if figura_nova is not None:
        figura_nova.desenhar(canvas, preview=True)

def main():
    global canvas, tipo_figura_var, cor_borda_var, cor_preenchimento_var

    root = tk.Tk()
    root.title("Editor de Desenho (Orientado a Objetos)")
    frame = tk.Frame(root)
    paddings = {'padx': 5, 'pady': 5}

    # --- Seletor de Tipo de Figura ---
    ttk.Label(frame, text='Figura:').grid(column=0, row=0, sticky=tk.W, **paddings)
    tipo_figura_var = tk.StringVar(root)
    option_menu_figura = ttk.OptionMenu(frame, tipo_figura_var, 'Linha', *MAPA_FIGURAS.keys())
    option_menu_figura.grid(column=1, row=0, sticky=tk.W, **paddings)

    # --- Seletor de Cor da Borda ---
    ttk.Label(frame, text='Cor da Borda:').grid(column=0, row=1, sticky=tk.W, **paddings)
    cor_borda_var = tk.StringVar(root)
    option_menu_borda = ttk.OptionMenu(frame, cor_borda_var, 'black', 'black', 'red', 'green', 'blue', 'orange', 'purple')
    option_menu_borda.grid(column=1, row=1, sticky=tk.W, **paddings)

    # --- Seletor de Cor de Preenchimento ---
    ttk.Label(frame, text='Preenchimento:').grid(column=0, row=2, sticky=tk.W, **paddings)
    cor_preenchimento_var = tk.StringVar(root)
    option_menu_preenchimento = ttk.OptionMenu(frame, cor_preenchimento_var, '', '', 'black', 'red', 'green', 'blue', 'orange', 'purple', 'yellow')
    option_menu_preenchimento.grid(column=1, row=2, sticky=tk.W, **paddings)

    # --- Área de desenho ---
    canvas = tk.Canvas(frame, bg='white', width=600, height=500, cursor="crosshair")
    canvas.grid(column=0, row=3, columnspan=2, sticky=tk.W, **paddings)

    frame.pack(padx=10, pady=10)

    # Eventos
    canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
    canvas.bind('<B1-Motion>', atualizar_figura_nova)
    canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

    root.mainloop()

if __name__ == "__main__":
    main()