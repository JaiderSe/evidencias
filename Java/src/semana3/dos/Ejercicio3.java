package semana3.dos;

import javax.swing.JOptionPane;

public class Ejercicio3 {
    public static void main(String[] args) {
        int longitud;
        longitud=0;
        longitud=Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número entero: "));
        String vecNombre[]=new String[longitud];
        llenarArray(vecNombre);
        imprimirArray(vecNombre);



    }

    public static void llenarArray(String[] vecNombre) {
        for (int i = 0; i < vecNombre.length; i++) {
            vecNombre[i]=JOptionPane.showInputDialog("ingrese el nombre numero"+i);
        }
    }

    public static void imprimirArray(String[] vecNombre) {
        for (int i = 0; i < vecNombre.length; i++) {
            JOptionPane.showMessageDialog(null, "El nombre nunmero"+i+" es: "+vecNombre[i]);
        }
    }

}
