public class Libro extends Publicacion {
    private int paginas;
    private int anio;

    public Libro(String titulo, double precio, int paginas, int anio) {
        super(titulo, precio);
        this.paginas = paginas;
        this.anio = anio;
    }

    @Override
    public void mostrarDatos() {
        super.mostrarDatos();
        System.out.println("Páginas: " + paginas);
        System.out.println("Año de publicación: " + anio);
    }
}
