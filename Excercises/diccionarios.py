capitales = {
    "Francia": "Paris",
    "Alemania": "Berlín",

}

# Lista anidada en un diccionario
viajes = {
    "Francia" : ["Paris","Lille", "Lyon"],
    "Alemania": ["Stuttgart", "Berlín"],

}
print(viajes["Francia"][2])

# Lista dentro de lista
lista_anidada = ["A", "B", ["C", "D"]]
print(lista_anidada[2][1])

#Listas y diccionarios anidados
visitado= {
    "Francia" : {"veces_visitado" : 4,
                 "ciudades_visitadas":["Paris","Lille", "Lyon"]
    },
    "Alemania": {"veces_visitado" : 5,
                 "ciudades_visitadas":["Stuttgart", "Berlín", "Hamburgo"]
    },
}
print (visitado["Alemania"]["ciudades_visitadas"][2])