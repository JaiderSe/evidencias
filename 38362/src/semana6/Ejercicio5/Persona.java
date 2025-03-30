package semana6.Ejercicio5;

public class Persona {
    private String nombre;
    private int edad;

    // Constructor por defecto
    public Persona() {
        this.nombre = "Sin nombre";
        this.edad = 0;
    }

    // Constructor con parámetros
    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    // Métodos getter y setter para 'nombre'
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    // Métodos getter y setter para 'edad'
    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    // Método toString para mostrar la información de la persona
    @Override
    public String toString() {
        return "Persona [Nombre: " + nombre + ", Edad: " + edad + "]";
    }
}