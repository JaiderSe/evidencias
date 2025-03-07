package semana4.tres;

import java.util.Random;

import javax.swing.JOptionPane;

public class Ejercicio4 {
        public static void main(String[] args) {
            // Declaración y creación de un array bidimensional de enteros de 3 filas y 4 columnas
            int num1;
            num1 =0;

            num1=personas();
            int[][] matriz = new int[num1][num1];
    
            // Inicialización del array bidimensional
           numeroRandom();
            llenarMatriz(matriz);
    
            // Impresión del array bidimensional
            System.out.println(imprimirMatriz(matriz));
            JOptionPane.showMessageDialog(null, imprimirMatriz(matriz));
            // 
           imprimirMatriz(matriz);
    
            // Acceso a los elementos del array bidimensional
            for (int i = 0; i < matriz.length; i++) {
                for (int j = 0; j < matriz[i].length; j++) {
                    System.out.print(matriz[i][j] + " ");
                }
                System.out.println();
            }


            
        }


public static int personas(){
            
            int num1;
            num1 = 0;

            num1=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el numero de personas"));

            return num1;
        }
        
public static void llenarMatriz(int mat[][]) {
 

    for (int i = 0; i < mat.length; i++) {
        for (int j = 0; j < mat[i].length; j++) {
           
            
            mat[i][j]=numeroRandom();
        }
    }
}

public static String imprimirMatriz(int mat[][]) {
     String matriz="";
matriz+="Filas: "+ mat.length + "\nColumnas: "+mat[1].length + "\n";
    for (int i = 0; i < mat.length ; i++)
    {
        
        for (int j = 0; j < mat[i].length; j++) 
        {
            matriz+=( "["+ mat[i][j] + "]   ");
        }
        
        matriz+="\n";    
    }
    
   
    return matriz;

}

public static int numeroRandom() {
    int num1;
    num1=0;
    Random rand = new Random();
    
        num1=rand.nextInt(1);
    return num1;
}



        
    }