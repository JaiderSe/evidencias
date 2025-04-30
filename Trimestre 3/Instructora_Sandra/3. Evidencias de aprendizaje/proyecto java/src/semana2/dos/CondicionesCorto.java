import javax.swing.JOptionPane;

public class CondicionesCorto {
    public static void main(String[] args) {
        do {
            try {
                double numero = Double.parseDouble(JOptionPane.showInputDialog("Ingrese un número:"));
                double x = Double.parseDouble(JOptionPane.showInputDialog("Ingrese el valor de x:"));
                String mensaje = "";

                if (numero > x) {
                    mensaje += "Número es mayor que " + x + "\n";
                }
                if (numero != 20 && numero < 80) {
                    mensaje += "Número es diferente de 20 y menor que 80\n";
                }

                if (mensaje.isEmpty()) {
                    mensaje = "No se cumple ninguna de las condiciones.";
                }

                JOptionPane.showMessageDialog(null, mensaje);

            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Por favor, ingrese números válidos.");
            }

            int continuar = JOptionPane.showConfirmDialog(null, "¿Verificar otro número?", "Continuar", JOptionPane.YES_NO_OPTION);
            if (continuar != JOptionPane.YES_OPTION) break;

        } while (true);
        System.exit(0);
    }
}