import javax.swing.JOptionPane;

public class CalculadoraModularCorto {

    static double sumar(double a, double b) {
        return a + b;
    }

    static double restar(double a, double b) {
        return a - b;
    }

    static double multiplicar(double a, double b) {
        return a * b;
    }

    static double dividir(double a, double b) {
        if (b == 0) {
            JOptionPane.showMessageDialog(null, "Error: No se puede dividir por cero.");
            return Double.NaN;
        }
        return a / b;
    }

    public static void main(String[] args) {
        do {
            try {
                double num1 = Double.parseDouble(JOptionPane.showInputDialog("Ingrese el primer número:"));
                double num2 = Double.parseDouble(JOptionPane.showInputDialog("Ingrese el segundo número:"));
                String operacion = JOptionPane.showInputDialog("Seleccione operación (+, -, *, /):");
                double resultado = 0;

                switch (operacion) {
                    case "+": resultado = sumar(num1, num2); break;
                    case "-": resultado = restar(num1, num2); break;
                    case "*": resultado = multiplicar(num1, num2); break;
                    case "/": resultado = dividir(num1, num2); break;
                    default: JOptionPane.showMessageDialog(null, "Operación inválida."); continue;
                }

                if (!Double.isNaN(resultado)) {
                    JOptionPane.showMessageDialog(null, "Resultado: " + resultado);
                }

            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Entrada inválida. Ingrese números válidos.");
            }

            int continuar = JOptionPane.showConfirmDialog(null, "¿Realizar otra operación?", "Continuar", JOptionPane.YES_NO_OPTION);
            if (continuar != JOptionPane.YES_OPTION) break;

        } while (true);
        System.exit(0);
    }
}