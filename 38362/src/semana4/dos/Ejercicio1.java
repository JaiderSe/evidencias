package semana4.dos;

import java.util.Scanner;


public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] mensajesPorIntegrante;
        int numeroDeIntegrantes;
        char continuar;

        do {
            System.out.print("Ingrese el número de integrantes del grupo: ");
            numeroDeIntegrantes = scanner.nextInt();
            mensajesPorIntegrante = new int[numeroDeIntegrantes];

            for (int i = 0; i < numeroDeIntegrantes; i++) {
                System.out.print("Ingrese la cantidad de mensajes enviados por el integrante " + (i + 1) + ": ");
                mensajesPorIntegrante[i] = scanner.nextInt();
            }

            int activos = contarIntegrantesActivos(mensajesPorIntegrante);
            System.out.println("Cantidad de integrantes activos en el grupo: " + activos);

            System.out.print("¿Desea ingresar otro grupo? (s/n): ");
            continuar = scanner.next().charAt(0);
        } while (continuar == 's' || continuar == 'S');

        scanner.close();
    }

    public static int contarIntegrantesActivos(int[] mensajes) {
        int contador = 0;
        for (int mensaje : mensajes) {
            if (mensaje > 5) {
                contador++;
            }
        }
        return contador;
    }
}
