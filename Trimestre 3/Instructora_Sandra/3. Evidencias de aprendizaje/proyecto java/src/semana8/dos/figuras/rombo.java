public class rombo extends cuadrado {
        
        private double diagonalMayor;
        private double diagonalMenor;
        
        public rombo(double lado, double diagonalMayor, double diagonalMenor) {
            super(lado);
            this.diagonalMayor = diagonalMayor;
            this.diagonalMenor = diagonalMenor;
        }
        
        public double getDiagonalMayor() {
            return diagonalMayor;
        }
        
        public void setDiagonalMayor(double diagonalMayor) {
            if (diagonalMayor < 0) {
                throw new IllegalArgumentException("La diagonal mayor no puede ser negativa.");
            }
            this.diagonalMayor = diagonalMayor;
        }
    
    }
