package semana6.Ejercicio5;

import javax.swing.JOptionPane;

public class Ejercicio1 {

    Persona obj;

    public static void main(String[] args) {

        Persona      obj1=  new       Persona();
    //  tipo de dato objeto operador  metodo
        
    obj1.setNombre("hola");
    JOptionPane.showMessageDialog(null, "estado del objeto  "+obj1.getNombre()+obj1.toString());    
    
        
    }

}
