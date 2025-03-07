package semana4.tres;

import java.util.Random;

import javax.swing.JOptionPane;

public class Ejercicio3 {


    public static void main(String[] args) {
        int fila;
        int columnas;
        

        fila= 3;
        columnas=3;

        int scalar=0;
        
       
        int mat[][]= new int[fila][columnas];

        
        llenarMatriz(mat); 
        JOptionPane.showMessageDialog(null, imprimirMatriz(mat));
        scalar = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el escalar")); 
        multiplicarMatriz(mat, scalar);
        JOptionPane.showMessageDialog(null, imprimirMatriz(mat));
        

        
        
}
        public static String ImprimirDiagonal(int mat[][]) {

    String matriz="";
matriz+="Filas: "+ mat.length + "\nColumnas: "+mat[1].length + "\n";
    for (int i = 0; i < mat.length ; i++)
    {
        
        for (int j = 0; j < mat[i].length; j++) 
        {
              if (mat[i]==mat[j]) {
                matriz+=( "["+ i + "." + j + "]   ");
                
              }
              else{
                matriz+=( "["+ "0"+ "." + "0" + "]   ");
              }
        }
        
        matriz+="\n";    
    }
    
   
    return matriz;

    }

public static void llenarMatriz(int mat[][]) {
    int num1=0;
    num1 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el limite del valor random"));

    for (int i = 0; i < mat.length; i++) {
        for (int j = 0; j < mat[i].length; j++) {
           
            
            mat[i][j]=numeroRandom(num1);
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

public static int numeroRandom(int limite){
    int num1;
    num1=0;
    Random rand = new Random();
    
        num1=rand.nextInt(limite);
    return num1;
}

public static void multiplicarMatriz(int mat[][], int scalar) {
    for (int i = 0; i < mat.length; i++) {
        for (int j = 0; j < mat[i].length; j++) {
            mat[i][j] = mat[i][j] * scalar;
        }
    }
}

}
