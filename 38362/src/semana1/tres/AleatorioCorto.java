import javax.swing.JOptionPane;
import java.util.Random;

public class AleatorioCorto {

    public static int generarNumeroAleatorio(int limite) {
        Random random = new Random();
        return random.nextInt(limite) + 1;
    }

    public static void main(String[] args) {
        do {
            int limite = 0;
            boolean limiteValido = false;
            while (!limiteValido) {
                try {
                    limite = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el valor límite (mayor que 0):"));
                    if (limite > 0) {
                        limiteValido = true;
                    } else {
                        JOptionPane.showMessageDialog(null, "El límite debe ser mayor que cero.");
                    }
                } catch (NumberFormatException e) {
                    JOptionPane.showMessageDialog(null, "Ingrese un número válido.");
                }
            }

            int numeroAleatorio = generarNumeroAleatorio(limite);
            JOptionPane.showMessageDialog(null, "Número aleatorio generado: " + numeroAleatorio);

            int continuar = JOptionPane.showConfirmDialog(null, "¿Generar otro número?", "Continuar", JOptionPane.YES_NO_OPTION);
            if (continuar != JOptionPane.YES_OPTION) break;
        } while (true);
        System.exit(0);
    }
}