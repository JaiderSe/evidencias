package semana6.Ejercicio6;

public class Circulo {
        
            private double radio;

            // Constructor por defecto
            public Circulo() {
                this.radio = 1.0; // Valor por defecto
            }

            // Constructor con parámetros
            public Circulo(double radio) {
                this.radio = radio;
            }

            // Método para cambiar el radio
            public void setRadio(double radio) {
                this.radio = radio;
            }

            // Método para obtener el radio
            public double getRadio() {
                return radio;
            }

            // Método para calcular el área
            public double calcularArea() {
                return Math.PI * radio * radio;
            }

            // Método para calcular el perímetro
            public double calcularPerimetro() {
                return 2 * Math.PI * radio;
            }
            
             // Método toString
             @Override
             public String toString() {
                 return "Circulo [radio=" + radio + "]";
             }
        }

       

