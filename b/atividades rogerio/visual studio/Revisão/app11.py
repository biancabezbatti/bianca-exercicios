class Receita:
    def __init__(self, nome, ingredientes, tempo_preparo):
        self.nome = nome
        self.ingredientes = ingredientes 
        self.tempo_preparo = tempo_preparo

    def exibir_receita(self):
            print(f'Receita: {self.nome}')
            print(f'Ingredientes:{self.ingredientes}')
            for ingrediente in self.ingredientes:
                print(f"-{ingrediente}")
            print(f"Tempo de preparo:{self.tempo_preparo}minutos")

bolochocolate = Receita(
    "Bolo de chocolate",
    ["2 xícara de farinha",
     "1 xícara de açucar",
     "1 xícara de chocolate em pó",
     "3 ovos",
     "1 xícara de leite"],
     45
)
bolodemorango = Receita(
    "Bolo de morango",
    ["2 xícaras de farinha",
     "1 xícara de açucar",
     "1 xícara de morango picados",
     "3 ovos",
     "1 xícara de leite"],
     50
)
tortadebolacha = Receita(
    "torta de bolacha",
    ["200 gramas de bolacha",
    "1 lata de leite condensado",
    "1 lata de creme de leite",
    "1 xícara de café forte"],
    30
)
bolochocolate.exibir_receita()
bolodemorango.exibir_receita()
tortadebolacha.exibir_receita()