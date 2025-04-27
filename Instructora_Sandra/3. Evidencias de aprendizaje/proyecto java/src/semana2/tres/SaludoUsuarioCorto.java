import javax.swing.JOptionPane;

public class SaludoUsuarioCorto {

    static void saludarUsuario(String nombreUsuario) {
        JOptionPane.showMessageDialog(null, "¡Hola " + nombreUsuario + "! Bienvenid@ a mi programa!");
    }

    public static void main(String[] args) {
        String nombre = JOptionPane.showInputDialog("Ingrese su nombre:");
        saludarUsuario(nombre);
        System.exit(0);
    }
}