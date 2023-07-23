from trabajador import Trabajador

print("Datos de Entrada")

name = input("Trabajador:         ")
categoria = (input("Categoría [A-B-C]: ")).upper()
Horaextra = int(input("Horas Extras:       "))
tardanza = int(input("Tardanzas (minutos): "))

obj = Trabajador(name, categoria, Horaextra, tardanza)

class BoletadePago(Trabajador):
    def Boleta(self):
        print("\n-------Boleta de Pago-------*")
        print("Nombre:..........", self.name)
        print("Categoría:.......", self.categoria)
        print("Sueldo Básico:.S/ {:.2f}" .format(self.Sueldobase))
        print("Descuento Tardanza:...S/ {:.2f}" .format(self.DescuentoT))
        print("Pagos Horas Extras:.....S/ {:.2f}" .format(self.PagoxHoraxtra))
        print("Sueldo Neto:....S/ {:.2f}" .format(self.sueldoneto))


boleta = BoletadePago(obj.name,obj.categoria,obj.Horaextra,obj.tardanza)
boleta.Boleta()