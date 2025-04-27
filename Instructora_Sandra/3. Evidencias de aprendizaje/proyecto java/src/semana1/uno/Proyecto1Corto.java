import javax.swing.JOptionPane;

public class Proyecto1Corto {
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            JOptionPane.showMessageDialog(null, "Persona " + (i + 1));

            String nombre = JOptionPane.showInputDialog("Nombre:");
            int edad = getIntInput("Edad:");
            float estatura = getFloatInput("Estatura (metros):");
            double salario = getDoubleInput("Salario:");
            char genero = getGeneroInput();

            String mensaje = "Datos Persona " + (i + 1) + ":\n" +
                             "Nombre: " + nombre + "\n" +
                             "Edad: " + edad + "\n" +
                             "Estatura: " + estatura + "m\n" +
                             "Salario: $" + salario + "\n" +
                             "Género: " + genero;

            JOptionPane.showMessageDialog(null, mensaje, "Info Persona", JOptionPane.INFORMATION_MESSAGE);
        }
        JOptionPane.showMessageDialog(null, "Fin Programa", "Completo", JOptionPane.INFORMATION_MESSAGE);
        System.exit(0);
    }

   

    static int getIntInput(String mensaje) {
        while (true) {
            try {
                return Integer.parseInt(JOptionPane.showInputDialog(mensaje));
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Entrada inválida. Ingrese un número entero.");
            }
        }
    }

    static float getFloatInput(String mensaje) {
        while (true) {
            try {
                return Float.parseFloat(JOptionPane.showInputDialog(mensaje));
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Entrada inválida. Ingrese un número decimal.");
            }
        }
    }

    static double getDoubleInput(String mensaje) {
        while (true) {
            try {
                return Double.parseDouble(JOptionPane.showInputDialog(mensaje));
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Entrada inválida. Ingrese un número decimal.");
            }
        }
    }

    static char getGeneroInput() {
        while (true) {
            String generoStr = JOptionPane.showInputDialog("Género (M/F):").toUpperCase();
            if (generoStr.length() == 1 && (generoStr.charAt(0) == 'M' || generoStr.charAt(0) == 'F')) {
                return generoStr.charAt(0);
            } else {
                JOptionPane.showMessageDialog(null, "Género inválido. Ingrese M o F.");
            }
        }
    }
}