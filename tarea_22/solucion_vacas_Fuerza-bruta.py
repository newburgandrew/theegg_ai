##<script src="https://gist.github.com/chemacortes/dfc944320647f9a8486a.js"></script>
##gracias a chemacortes por el codigo que he adaptado libremente
from operator import itemgetter

#Paquetes: "Nombre de la vaca", Kilos, Precio
VACAS = (
    ("vaca 1", 360, 40), ("vaca 2", 250, 35), ("vaca 3", 400, 43), ("vaca 4", 180, 28),
    ("vaca 5", 50, 12), ("vaca 6", 90, 13))

#carga máxima del camión
PESOMAXIMO = 700

get_peso = itemgetter(1)
get_litros = itemgetter(2)

def total_peso(vacas):
    return sum(get_peso(x) for x in vacas)

def total_valor(vacas):
    return sum(get_litros(x) for x in vacas)

print(total_peso(VACAS), total_valor(VACAS))

def combinaciones(vacas, peso_maximo):

    paqs = [ p for p in vacas if get_peso(p) <= peso_maximo ]
    resultado = []
    for p in paqs:
        res = combinaciones([x for x in paqs if x!=p], peso_maximo - get_peso(p))
        if len(res) == 0:
            resultado.append([p])
            
        else:
            resultado.extend([[p]+x for x in res])
    return resultado;


#from pprint import pprint
# solución
sol = max(combinaciones(VACAS, PESOMAXIMO), key=total_valor)
print("Peso {} Valor {}".format(total_peso(sol), total_valor(sol)))
print(sol)

