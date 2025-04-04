public class circulo extends figuras {
    
    private double radio;
    
    public circulo(double radio) {
        this.radio = radio;
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
