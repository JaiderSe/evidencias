package semana4.tres;

import javax.swing.JOptionPane;

public class Ejercicio2 {

    public static void main(String[] args) {
        
        int fila;
        int columnas;
        
        fila= 3;
        columnas=3;
        
       
        int mat[][]= new int[fila][columnas];
          
        JOptionPane.showMessageDialog(null, ImprimirDiagonal(mat));
        
        
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




}

