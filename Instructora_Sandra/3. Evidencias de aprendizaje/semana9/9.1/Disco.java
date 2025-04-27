public class Disco extends Publicacion {
    private int duracion; // en minutos

    public Disco(String titulo, double precio, int duracion) {
        super(titulo, precio);
        this.duracion = duracion;
    }

    @Override
    public void mostrarDatos() {
        super.mostrarDatos();
        System.out.println("Duración: " + duracion + " minutos");
    }
}
