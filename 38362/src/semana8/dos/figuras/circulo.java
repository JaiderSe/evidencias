

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

    public double setPerimetro(double perimetro) {
        if (perimetro < 0) {
            throw new IllegalArgumentException("El perímetro no puede ser negativo.");
        }
        return perimetro;
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
