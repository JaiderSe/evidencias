import javax.swing.JOptionPane;

public class Pares1a100Corto {
    public static void main(String[] args) {
        String pares = "Números pares del 1 al 100:\n"; // String to store even numbers

        for (int i = 2; i <= 100; i += 2) { // Loop from 2 to 100, incrementing by 2 (only even numbers)
            pares += i + "\n"; // Append even number to the string with a newline
        }

        JOptionPane.showMessageDialog(null, pares, "Números Pares", JOptionPane.INFORMATION_MESSAGE);
        System.exit(0); // To properly close the program when using JOptionPane
    }
}