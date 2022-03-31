#En esta hoja creare la clase trabajador para poder importarla luego en la hoja de mi trabajo final

class Trabajador():
    def __init__(self, name, categoria, Horaextra, tardanza):
        self.name = name
        self.categoria = categoria
        self.Horaextra = Horaextra
        self.tardanza = tardanza
        self.Sueldobase = self.Dsueldoxcategoria(categoria)
        self.PagoxHoraxtra = self.Dpagohoraextra(Horaextra ,categoria)
        self.DescuentoT = self.Ddescuentotardanza(tardanza)
        self.sueldoneto = self.Dsueldoneto()

    def Dsueldoxcategoria(self, categoria):
        if categoria == "A":
            SueldoBase = 3000
        if categoria == "B":
            SueldoBase = 2500
        if categoria == "C":
            SueldoBase = 2000
        return SueldoBase

    def Dpagohoraextra(self, Horaextra, categoria):
        if categoria == "A":
            PagoxHoraxtra = 3000 / 240 * Horaextra * 4
        if categoria == "B":
            PagoxHoraxtra = 2500 / 240 * Horaextra * 3
        if categoria == "C":
            PagoxHoraxtra = 2000 / 240 * Horaextra * 2
        return PagoxHoraxtra

    def Ddescuentotardanza(self,tardanza):
        DescuentoT = self.Sueldobase / 240 * tardanza / 60
        return DescuentoT

    def Dsueldoneto(self):

        sueldoneto = (self.Sueldobase + self.PagoxHoraxtra) - self.DescuentoT
        return sueldoneto




