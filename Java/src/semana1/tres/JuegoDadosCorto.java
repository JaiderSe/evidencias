import javax.swing.JOptionPane;
import java.util.Random;

public class JuegoDadosCorto {
    public static void main(String[] args) {
        int numLanzamientos = Integer.parseInt(JOptionPane.showInputDialog("¿Cuántos lanzamientos de dados desea hacer?"));
        Random random = new Random();
        int sumasPares = 0;
        int sumasImpares = 0;

        for (int i = 0; i < numLanzamientos; i++) {
            int dado1 = random.nextInt(6) + 1;
            int dado2 = random.nextInt(6) + 1;
            int suma = dado1 + dado2;
            String mensaje = "Dado 1: " + dado1 + "\nDado 2: " + dado2 + "\nSuma: " + suma;
            JOptionPane.showMessageDialog(null, mensaje, "Lanzamiento " + (i + 1), JOptionPane.INFORMATION_MESSAGE);
            if (suma % 2 == 0) {
                sumasPares++;
            } else {
                sumasImpares++;
            }
        }

        String resultadoFinal = "Total de sumas pares: " + sumasPares + "\nTotal de sumas impares: " + sumasImpares;
        JOptionPane.showMessageDialog(null, resultadoFinal, "Resultados Finales", JOptionPane.INFORMATION_MESSAGE);
        System.exit(0);
    }
}