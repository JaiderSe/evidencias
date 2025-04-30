public class Publicacion {
    protected String titulo;
    protected double precio;

    public Publicacion(String titulo, double precio) {
        this.titulo = titulo;
        this.precio = precio;
    }

    public void mostrarDatos() {
        System.out.println("Título: " + titulo);
        System.out.println("Precio: $" + precio);
    }
}
