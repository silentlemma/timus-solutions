import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Locale;

public class Main {
    private static final int GESTURE_COUNT = 3;
    private static final int OUTPUT_DIGITS = 12;

    private static double expectedRounds(int count) {
        double[] expected = new double[count + 1];
        double powerThree = 1.0;
        double powerTwo = 2.0;
        for (int players = 2; players <= count; players++) {
            powerThree *= GESTURE_COUNT;
            powerTwo *= 2;
            double weightedSuccessors = 0.0;
            double combination = 1.0;
            for (int survivors = 1; survivors < players; survivors++) {
                combination = combination * (players - survivors + 1) / survivors;
                weightedSuccessors += combination * expected[survivors];
            }
            expected[players] = (powerThree + weightedSuccessors) / (powerTwo - 2);
        }
        return expected[count];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int count = Integer.parseInt(input.readLine().trim());
        System.out.printf(Locale.US, "%." + OUTPUT_DIGITS + "f%n", expectedRounds(count));
    }
}
