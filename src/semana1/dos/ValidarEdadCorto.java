import javax.swing.JOptionPane;

public class ValidarEdadCorto {
    public static void main(String[] args) {
        int edad;
        do {
            String edadStr = JOptionPane.showInputDialog("Ingresa la edad de la persona (0-120):");
            try {
                edad = Integer.parseInt(edadStr);
                if (edad < 0 || edad > 120) {
                    JOptionPane.showMessageDialog(null, "Edad no válida. Debe estar entre 0 y 120.", "Error", JOptionPane.ERROR_MESSAGE);
                } else {
                    break; // Edad válida, salir del ciclo
                }
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Entrada inválida. Ingresa un número entero.", "Error", JOptionPane.ERROR_MESSAGE);
            }
        } while (true);

        JOptionPane.showMessageDialog(null, "Edad ingresada correctamente: " + edad, "Edad Válida", JOptionPane.INFORMATION_MESSAGE);
        System.exit(0);
    }
}