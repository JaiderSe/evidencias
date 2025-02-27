package semana3.dos;

import java.util.Random;

import javax.swing.JOptionPane;

public class Ejercicio1 {

    public static void main(String[] args) {
        
        // Crear una matriz de enteros de 6x2
        int[][] matriz = new int[6][2];
        int[][] matrizusuario = new int[6][2];

        // Asignar valores a la matriz
        asignacion(matriz);
        adivinar(matrizusuario);

    /*     JOptionPane.showMessageDialog(null, "Por favor elija la modalidad que desea apostar: \n"
                + "1. Color \n"
                + "2. Número \n"
                + "3. Paridad \n"
                + "4. Rango \n"
                + "5. Salir"); */

        
        imprimir(matriz);
        imprimir(matrizusuario);

  


         
    }

 public static void imprimir(int [][] matriz){

        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
  }


public static void adivinar(int [][] matrizusuario){
   
     for (int i = 0; i < matrizusuario.length; i++) {
            for (int j = 0; j < matrizusuario[i].length; j++) {

                if (j == 0) {
                    matrizusuario[i][j] = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el número de la balota numero " + (i+1)));
                } else {
                    matrizusuario[i][j] = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el color de la balota numero " + (i+1) + "\n"
                        + "1. Amarillo\n"
                        + "2. Azul\n"
                        + "3. Rojo\n"
                        + "4. Verde\n"
                        + "5. Blanco\n"
                        + "6. Negro\n"));
                }
            }
    
        }
}  
 

public static int comparar(int [][] matriz, int [][] matrizusuario){
    
    int aciertos = 0;
    int fallos = 0;
    
    for (int i = 0; i < matriz.length; i++) {
        for (int j = 0; j < matriz[i].length; j++) {
            if (matriz[i][j] == matrizusuario[i][j]) {
                aciertos++;
            } else {
                fallos++;
            }
        }
        }

     return aciertos;
}   


public static void asignacion(int [][] matriz){

        Random rand = new Random();
        
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                matriz[i][j] = rand.nextInt(8);
         
          }
            
        
    }
 
}

}


