import javax.swing.JOptionPane;

public class PuedeVotarCorto {
    public static void main(String[] args) {
        do {
            try {
                int edad = Integer.parseInt(JOptionPane.showInputDialog("Ingrese su edad:"));
                String mensaje = (edad >= 18) ? "Usted puede votar." : "Usted no puede votar.";
                JOptionPane.showMessageDialog(null, mensaje);
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Por favor, ingrese un número válido.");
            }
            int continuar = JOptionPane.showConfirmDialog(null, "¿Verificar otra persona?", "Continuar", JOptionPane.YES_NO_OPTION);
            if (continuar != JOptionPane.YES_OPTION) break;
        } while (true);
        System.exit(0);
    }
}