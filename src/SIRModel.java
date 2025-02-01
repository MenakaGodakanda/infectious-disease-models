public class SIRModel {
    public static void main(String[] args) {
        double beta = 0.3, gamma = 0.1;
        double S = 990, I = 10, R = 0, N = S + I + R;
        int days = 100;

        System.out.println("Day\tS\tI\tR");
        for (int t = 0; t < days; t++) {
            double newInfected = (beta * S * I) / N;
            double newRecovered = gamma * I;

            S -= newInfected;
            I += newInfected - newRecovered;
            R += newRecovered;

            System.out.printf("%d\t%.2f\t%.2f\t%.2f\n", t, S, I, R);
        }
    }
}

