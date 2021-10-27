andares = {
    "inferior": ["roupas", "comidas"],
    "superior": ["esportes", "tênis"],
    "subsolo":  ["jardinagem", "moveis"]

}
encontrar = False 
solicitado = "comidas"
atual = "superior"
if solicitado in andares[atual] :
    print("Sim, neste andar.")
    encontrar = True
else:
     for andar in ["inferior", "superior", "subsolo"]:
        if solicitado in andares[andar]:
            print(f"No andar {andar}.")           