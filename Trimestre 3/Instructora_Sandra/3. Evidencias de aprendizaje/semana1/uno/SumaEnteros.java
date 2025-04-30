import javax.swing.JOptionPane;

public class SumaEnteros {
    public static void main(String[] args) {
        int numRepeticiones = Integer.parseInt(JOptionPane.showInputDialog("¿Cuántas veces quieres sumar?"));

        for (int i = 0; i < numRepeticiones; i++) {
            int num1 = Integer.parseInt(JOptionPane.showInputDialog("Ingresa el primer número entero:"));
            int num2 = Integer.parseInt(JOptionPane.showInputDialog("Ingresa el segundo número entero:"));
            int suma = num1 + num2;
            JOptionPane.showMessageDialog(null, "La suma es: " + suma, "Resultado", JOptionPane.INFORMATION_MESSAGE);
        }
    }
}