

public class circulo extends figuras {
    
    private double radio;
    
    public circulo(double radio) {
        this.radio = radio;
    }
    
    public double getRadio() {
        return radio;
    }

    public void setRadio(double radio) {
        if (radio < 0) {
            throw new IllegalArgumentException("El radio no puede ser negativo.");
        }
        this.radio = radio;
    }

    public double getPerimetro() {
        return 2 * radio*Math.PI;
    }


    
    @Override
    public double area() {
        return Math.PI * radio * radio;
    }
    
    @Override
    public double perimetro() {
        return 2 * Math.PI * radio;
    }
    
    @Override
    public String tipoFigura() {
        return "Círculo";
    }

}
