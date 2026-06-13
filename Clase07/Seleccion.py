class Seleccion:
    def_init__(Self,pais,confederacion):
    self. pais = pais
    self. confederacion= confederacion
    self. jugadores =[]

    def agregar_jugadores(self,jugador):
        self.jugadores.append(jugadores):

    def eliminar_jugador(self,jugador):
        for jugador_en_lista in self.jugadores:
            if jugador_en_lista == jugador:
                self.jugadores.remove(jugador_en_lista)
                break

argentina= Seleccion("Argentina", "COMMEBOL")
brasil= seleccion("Brasil","COMMEBOL")
españa=Seleccion("España", "UEFA")

argentina.agregar_jugador("Lionel Messi")
argentina.agregar_jugador("Angel di maria")
brasil.agregar_jugador("Neymar")
españa.agregar_jugador("Lamine yamal")
print(argentina.jugadores)
print(brasil.jugadores)
print("espanna.jugadores")
argentina.eliminar_jugadores("Angel Di maria")
