class Figura:
    """Classe base abstrata para todas as figuras."""
    def __init__(self, x, y, cor_borda, cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    def atualizar(self, x, y):
        pass

    def desenhar(self, canvas, preview=False):
        pass

    def incompleta(self):
        pass

# --- Agrupamentos por comportamento ---

class FiguraDoisPontos(Figura):
    """Figuras definidas apenas por um ponto inicial e um final (ex: Linha, Retângulo, Oval)."""
    def __init__(self, x, y, cor_borda, cor_preenchimento):
        super().__init__(x, y, cor_borda, cor_preenchimento)
        self.x1, self.y1 = x, y
        self.x2, self.y2 = x, y

    def atualizar(self, x, y):
        self.x2, self.y2 = x, y

    def incompleta(self):
        return (self.x1, self.y1) == (self.x2, self.y2)


class FiguraMultiplosPontos(Figura):
    """Figuras formadas por um rastro contínuo de pontos (ex: Rabisco, Polígono livre)."""
    def __init__(self, x, y, cor_borda, cor_preenchimento):
        super().__init__(x, y, cor_borda, cor_preenchimento)
        self.pontos = [(x, y)]

    def atualizar(self, x, y):
        self.pontos.append((x, y))

    def incompleta(self):
        return len(self.pontos) <= 1


# --- Classes Concretas ---

class Linha(FiguraDoisPontos):
    def desenhar(self, canvas, preview=False):
        dash = (4, 2) if preview else None
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.cor_borda, dash=dash)

class Retangulo(FiguraDoisPontos):
    def desenhar(self, canvas, preview=False):
        dash = (4, 2) if preview else None
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.cor_borda, fill=self.cor_preenchimento, dash=dash)

class Oval(FiguraDoisPontos):
    def desenhar(self, canvas, preview=False):
        dash = (4, 2) if preview else None
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline=self.cor_borda, fill=self.cor_preenchimento, dash=dash)

class Rabisco(FiguraMultiplosPontos):
    def desenhar(self, canvas, preview=False):
        dash = (4, 2) if preview else None
        if len(self.pontos) > 1:
            canvas.create_line(self.pontos, fill=self.cor_borda, dash=dash)

class Poligono(FiguraMultiplosPontos):
    def desenhar(self, canvas, preview=False):
        dash = (4, 2) if preview else None
        if len(self.pontos) > 2:
            # Polígonos precisam de pelo menos 3 pontos para serem desenhados corretamente
            canvas.create_polygon(self.pontos, outline=self.cor_borda, fill=self.cor_preenchimento, dash=dash)
        elif len(self.pontos) == 2:
            # Fallback para o usuário enxergar algo no primeiro movimento
            canvas.create_line(self.pontos, fill=self.cor_borda, dash=dash)