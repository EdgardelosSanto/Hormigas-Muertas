def contar_hormigas_pisoteadas(rastro):
    return rastro.count("t")

rastro = "...hormiga...hormiga.. nat .hormiga. t ..hormiga...hormiga...hormiga...hormiga. una hormiga.. t"
hormigas_pisoteadas = contar_hormigas_pisoteadas(rastro)
print("Número de hormigas muertas:", hormigas_pisoteadas)

