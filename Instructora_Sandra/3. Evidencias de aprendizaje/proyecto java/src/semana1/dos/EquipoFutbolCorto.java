import javax.swing.JOptionPane;

public class EquipoFutbolCorto {
    public static void main(String[] args) {
        do {
            int sumaEdades = 0;
            int jugadoresValidos = 0;

            for (int i = 1; i <= 11; i++) {
                int edad = 0;
                boolean edadValida = false;
                do {
                    String edadStr = JOptionPane.showInputDialog("Ingresa la edad del jugador " + i + " (18-28 años):");
                    try {
                        edad = Integer.parseInt(edadStr);
                        if (edad >= 18 && edad <= 28) {
                            edadValida = true;
                        } else {
                            JOptionPane.showMessageDialog(null, "Edad fuera de rango. Debe estar entre 18 y 28.", "Error", JOptionPane.ERROR_MESSAGE);
                        }
                    } catch (NumberFormatException e) {
                        JOptionPane.showMessageDialog(null, "Entrada inválida. Ingresa un número entero.", "Error", JOptionPane.ERROR_MESSAGE);
                    }
                } while (!edadValida); 

                sumaEdades += edad;
                jugadoresValidos++; 
            }

            double promedioEdad = (double) sumaEdades / jugadoresValidos; 

            JOptionPane.showMessageDialog(null, "Promedio de edad del equipo: " + promedioEdad + " años", "Promedio de Edad", JOptionPane.INFORMATION_MESSAGE);

            int continuar = JOptionPane.showConfirmDialog(null, "¿Desea calcular el promedio de otro equipo?", "Continuar", JOptionPane.YES_NO_OPTION);
            if (continuar != JOptionPane.YES_OPTION) {
                break; 
            }
        } while (true);
        System.exit(0); 
    }
}