#Los diccionarios son variables especiales que me permiten almacenar múltiples datos de diferente tipo 
#en una sola variable (el atributo en comillas y el valor lo que yo quiera llevar)

empleado={
    'nombre':"Juan",
    'cedula':71387294,
    'cargo':"Analista de datos",
    'salario':8000000,
    'horasTrabajadas':40,
    'aplicaSubsidioTransporte':False,
    'deudas':[1500000,800000]
}
#print(empleado)
#print(empleado['deudas'][1])

#RECORRIENDO UN DICCIONARIO (a quien observo, a quien voy a observar)

for observadorAtributo,observadorValor in empleado.items():
    print(observadorAtributo)
    print(observadorValor)