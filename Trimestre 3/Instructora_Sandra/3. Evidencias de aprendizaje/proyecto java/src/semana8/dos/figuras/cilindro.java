public class cilindro extends figuras {
    
    private double radio;
    private double altura;
    
    public cilindro(double radio, double altura) {
        this.radio = radio;
        this.altura = altura;
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

    public double getAltura() {
        return altura;
    }

    public double setAltura(double altura) {
        if (altura < 0) {
            throw new IllegalArgumentException("La altura no puede ser negativa.");
        }
        return altura;
    }

    @Override
    public double area() {
        return 2 * Math.PI * radio * (radio + altura);
    }
    
    @Override
    public double perimetro() {
        return 2 * Math.PI * radio * altura;
    }
    
    @Override
    public String tipoFigura() {
        return "Cilindro";
    }

}
