package semana3.dos;

import java.util.Random;

import javax.swing.JOptionPane;

public class Ejercicio1 {

    public static void main(String[] args) {
        
        // Crear una matriz de enteros de 6x2
        int[][] matriz = new int[6][2];

        // Asignar valores a la matriz
        asignacion(matriz);
        

        JOptionPane.showMessageDialog(null, "Por favor elija la modalidad que desea apostar: \n"
                + "1. Color \n"
                + "2. Número \n"
                + "3. Paridad \n"
                + "4. Rango \n"
                + "5. Salir");
  


         
    }

 public static void imprimir(int [][] matriz){

        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
  }


public static void adivinar(){
    
}  
 public static void asignacion(int [][] matriz){

        Random rand = new Random();
        
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                matriz[i][j] = rand.nextInt(8);
         
          }
            
        
    }
}

