from abc import ABC, abstractmethod

class Operable(ABC):
    @abstractmethod
    def iniciar_operacion(self):
        pass
    @abstractmethod
    def finalizar_operacion(self):
        pass

class UnidadEntrega(ABC):
    def __init__(self, identificador, nombre_operador, capacidad_carga, zona_operacion):
        self.identificador = identificador
        self.nombre_operador = nombre_operador
        self.capacidad_carga = capacidad_carga
        self.zona_operacion = zona_operacion

    def mostrar_informacion(self):
        print(f"ID: {self.identificador}, Operador: {self.nombre_operador}, Capacidad: {self.capacidad_carga}kg, Zona: {self.zona_operacion}")

    @abstractmethod
    def realizar_entrega(self):
        pass

class Bicicleta(UnidadEntrega, Operable):
    def __init__(self, identificador, nombre_operador, capacidad_carga, zona_operacion, tiene_canasta):
        super().__init__(identificador, nombre_operador, capacidad_carga, zona_operacion)
        self.tiene_canasta = tiene_canasta

    def realizar_entrega(self):
        print(f"Bicicleta {self.identificador} entrega ecologica en trayecto corto.")

    def iniciar_operacion(self):
        print(f"Bicicleta {self.identificador} inicia pedaleo.")

    def finalizar_operacion(self):
        print(f"Bicicleta {self.identificador} finaliza entrega.")

class Motocicleta(UnidadEntrega, Operable):
    def __init__(self, identificador, nombre_operador, capacidad_carga, zona_operacion, cilindraje):
        super().__init__(identificador, nombre_operador, capacidad_carga, zona_operacion)
        self.cilindraje = cilindraje

    def realizar_entrega(self):
        print(f"Motocicleta {self.identificador} entrega rapida en zona urbana.")

    def iniciar_operacion(self):
        print(f"Motocicleta {self.identificador} arranca motor.")

    def finalizar_operacion(self):
        print(f"Motocicleta {self.identificador} entrega completada.")

class Drone(UnidadEntrega, Operable):
    def __init__(self, identificador, nombre_operador, capacidad_carga, zona_operacion, nivel_bateria):
        super().__init__(identificador, nombre_operador, capacidad_carga, zona_operacion)
        self.nivel_bateria = nivel_bateria

    def realizar_entrega(self):
        print(f"Drone {self.identificador} entrega aerea con autonomia limitada.")

    def iniciar_operacion(self):
        print(f"Drone {self.identificador} despegando. Bateria: {self.nivel_bateria}%")

    def finalizar_operacion(self):
        print(f"Drone {self.identificador} aterriza.")

if __name__ == "__main__":
    unidades = [
        Bicicleta("B001", "Carlos", 15, "Centro", True),
        Motocicleta("M002", "Ana", 50, "Norte", 125),
        Drone("D003", "Sistema", 2, "Sur", 85)
    ]

    for u in unidades:
        print(f"\n--- {u.identificador} ---")
        u.mostrar_informacion()
        u.iniciar_operacion()
        u.realizar_entrega()
        u.finalizar_operacion()