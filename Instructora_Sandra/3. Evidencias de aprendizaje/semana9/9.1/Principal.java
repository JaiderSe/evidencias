import java.util.ArrayList;
import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Publicacion> publicaciones = new ArrayList<>();

        int opcion;
        do {
            System.out.println("\n1. Agregar Libro");
            System.out.println("2. Agregar Disco");
            System.out.println("3. Mostrar Publicaciones");
            System.out.println("4. Salir");
            System.out.print("Seleccione una opción: ");
            opcion = scanner.nextInt();
            scanner.nextLine(); // limpiar buffer

            switch (opcion) {
                case 1:
                    System.out.print("Título del libro: ");
                    String tituloLibro = scanner.nextLine();
                    System.out.print("Precio del libro: ");
                    double precioLibro = scanner.nextDouble();
                    System.out.print("Número de páginas: ");
                    int paginas = scanner.nextInt();
                    System.out.print("Año de publicación: ");
                    int anio = scanner.nextInt();
                    publicaciones.add(new Libro(tituloLibro, precioLibro, paginas, anio));
                    break;
                case 2:
                    System.out.print("Título del disco: ");
                    String tituloDisco = scanner.nextLine();
                    System.out.print("Precio del disco: ");
                    double precioDisco = scanner.nextDouble();
                    System.out.print("Duración en minutos: ");
                    int duracion = scanner.nextInt();
                    publicaciones.add(new Disco(tituloDisco, precioDisco, duracion));
                    break;
                case 3:
                    System.out.println("\n--- Publicaciones Registradas ---");
                    for (Publicacion pub : publicaciones) {
                        pub.mostrarDatos();
                        System.out.println("----------------------");
                    }
                    break;
                case 4:
                    System.out.println("Saliendo...");
                    break;
                default:
                    System.out.println("Opción inválida. Intente de nuevo.");
            }
        } while (opcion != 4);

        scanner.close();
    }
}
