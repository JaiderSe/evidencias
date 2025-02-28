package semana3.tres;

import javax.swing.JOptionPane;

public class Ejercicio2 {
    public static void main(String[] args) {
        
        int longitud;
        longitud=0;
        longitud=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el numero de personas "));
        String vecNombre[]=new String[longitud];
        String vecEdad[]=new String[longitud];
        String vecEstatura[]=new String[longitud];
        llenarArray(vecNombre, vecEdad, vecEstatura);
        imprimirArray(vecNombre, vecEdad, vecEstatura);    




    }

    public static void llenarArray(String[] vecNombre, String[] vecEdad, String[] vecEstatura) {
        for (int i = 0; i < vecNombre.length; i++) {
            vecNombre[i]=JOptionPane.showInputDialog("ingrese el nombre numero"+i);
            vecEdad[i]=JOptionPane.showInputDialog("ingrese la edad numero"+i);
            vecEstatura[i]=JOptionPane.showInputDialog("ingrese la estatura numero"+i);
        }
    }

    public static void imprimirArray(String[] vecNombre, String[] vecEdad, String[] vecEstatura) {      
        for (int i = 0; i < vecNombre.length; i++) {
            JOptionPane.showMessageDialog(null, "La persona numero"+i+" es: "+vecNombre[i]
            +"\nEdad: "+vecEdad[i]+"\nEstatura: "+vecEstatura[i]);
            
        }
    }
}
