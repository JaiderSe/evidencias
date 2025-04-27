


import javax.swing.JOptionPane;

public class ParImparCorto {
    public static void main(String[] args) {
        int numRepeticiones = Integer.parseInt(JOptionPane.showInputDialog("¿Cuántos números quieres verificar?"));

        for (int i = 0; i < numRepeticiones; i++) {
            int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingresa un número entero:"));

            String mensaje = (numero % 2 == 0) ? "El número " + numero + " es PAR." : "El número " + numero + " es IMPAR.";
            JOptionPane.showMessageDialog(null, mensaje, "Resultado", JOptionPane.INFORMATION_MESSAGE);
        }
    }
}