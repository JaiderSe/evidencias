import javax.swing.JOptionPane;

public class CalculadoraBasicaCorto {
    public static void main(String[] args) {
        do {
            double num1 = Double.parseDouble(JOptionPane.showInputDialog("Ingresa el primer número:"));
            double num2 = Double.parseDouble(JOptionPane.showInputDialog("Ingresa el segundo número:"));

            String operacion = JOptionPane.showInputDialog("Selecciona la operación (+, -, *, /):");
            double resultado = 0;
            String operacionTexto = ""; 

            switch (operacion) {
                case "+":
                    resultado = num1 + num2;
                    operacionTexto = "Suma";
                    break;
                case "-":
                    resultado = num1 - num2;
                    operacionTexto = "Resta";
                    break;
                case "*":
                    resultado = num1 * num2;
                    operacionTexto = "Multiplicación";
                    break;
                case "/":
                    if (num2 != 0) {
                        resultado = num1 / num2;
                        operacionTexto = "División";
                    } else {
                        JOptionPane.showMessageDialog(null, "¡Error! No se puede dividir por cero.", "Error", JOptionPane.ERROR_MESSAGE);
                        continue; 
                    }
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Operación no válida.", "Error", JOptionPane.ERROR_MESSAGE);
                    continue; 
            }

            JOptionPane.showMessageDialog(null, operacionTexto + ": " + resultado, "Resultado", JOptionPane.INFORMATION_MESSAGE);

            int continuar = JOptionPane.showConfirmDialog(null, "¿Desea realizar otra operación?", "Continuar", JOptionPane.YES_NO_OPTION);
            if (continuar != JOptionPane.YES_OPTION) {
                break; 
            }
        } while (true); 
    }
}