package semana3.tres;

import javax.swing.JOptionPane;

public class Ejercicio3 {
    public static void main(String[] args) {
        
        
        JOptionPane.showMessageDialog(null, "Este programa promediará las temperaturas más bajas de la semana ");

        
        double vecTemperatura[]=new double[7];
        double promedio;
        promedio=0;

        promedio=promediar(vecTemperatura);
        
        
        JOptionPane.showMessageDialog(null, "El promedio de las temperaturas minimas de la semana es: "+promedio);
        JOptionPane.showMessageDialog(null,imprimir(vecTemperatura));  



    }

    public static double promediar(double[] vecTemperatura) {
        
        double promedio;
        double suma=0;
        
        for (int i = 0; i < 7; i++) {
        
            vecTemperatura[i]=Double.parseDouble(JOptionPane.showInputDialog("Ingrese la temperatura minima del día: "+(i+1)));
        }

        for (int i = 0; i < 7; i++) {
            suma+=vecTemperatura[i];
        }
        promedio=suma/7;
        return promedio;
    }

    public static String imprimir(double[] vecTemperatura) {      
        String message="";
        
        for (int i = 0; i < 7; i++) {
            message+="La temperatura minima del dia "+(i+1)+" es: "+vecTemperatura[i]+"\n";
        }

        return message;
    }

}
