package semana4.tres;

public class Ejercicio1 {
    public static void main(String[] args) {
        
        int fila;
        int columnas;
        
        //Tamaño de la matriz: 5X3
        fila= 3;
        columnas=3;
        
       
        int mat[][]= new int[fila][columnas];
        System.out.println("Filas: "+ mat.length + "\nColumnas: "+mat[1].length);
 

        ImprimirDiagonal(mat);
        
    }
public static void ImprimirDiagonal( int mat[][]) {

       
    for (int i = 0; i < mat.length ; i++)
    {
        
        for (int j = 0; j < mat[i].length; j++) 
        {
              if (mat[i]==mat[j]) {
                System.out.print( "["+ i + "." + j + "]   ");
                
              }
              else{
                System.out.print( "["+ "0"+ "." + "0" + "]   ");
              }
        }
        
        System.out.println("\n");
    }

}}

