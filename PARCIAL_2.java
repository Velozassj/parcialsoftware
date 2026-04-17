interface Operable {
    void iniciarOperacion();
    void finalizarOperacion();
}

abstract class UnidadEntrega {
    protected String id;

    public UnidadEntrega(String id) {
        this.id = id;
    }

    public void mostrarInfo() {
        System.out.println("ID: " + id);
    }

    public abstract void realizarEntrega();
}

class Bicicleta extends UnidadEntrega implements Operable {
    public Bicicleta(String id) {
        super(id);
    }

    public void realizarEntrega() {
        System.out.println("Bicicleta entrega ecologica");
    }

    public void iniciarOperacion() {
        System.out.println("Inicia bicicleta");
    }

    public void finalizarOperacion() {
        System.out.println("Finaliza bicicleta");
    }
}

class Motocicleta extends UnidadEntrega implements Operable {
    public Motocicleta(String id) {
        super(id);
    }

    public void realizarEntrega() {
        System.out.println("Motocicleta entrega rapida");
    }

    public void iniciarOperacion() {
        System.out.println("Inicia motocicleta");
    }

    public void finalizarOperacion() {
        System.out.println("Finaliza motocicleta");
    }
}

class Drone extends UnidadEntrega implements Operable {
    public Drone(String id) {
        super(id);
    }

    public void realizarEntrega() {
        System.out.println("Drone entrega aerea");
    }

    public void iniciarOperacion() {
        System.out.println("Inicia drone");
    }

    public void finalizarOperacion() {
        System.out.println("Finaliza drone");
    }
}

public class Main {
    public static void main(String[] args) {
        UnidadEntrega[] unidades = {
            new Bicicleta("B001"),
            new Motocicleta("M002"),
            new Drone("D003")
        };

        for (UnidadEntrega u : unidades) {
            System.out.println("\n--- " + u.id + " ---");
            u.mostrarInfo();
            u.iniciarOperacion();
            u.realizarEntrega();
            u.finalizarOperacion();
        }
    }
}