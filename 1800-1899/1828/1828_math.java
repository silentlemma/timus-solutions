import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
                new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        long n = (long) in.nval;
        // least squares line through the points (i, a_i), i = 0 .. n - 1:
        // the normal equations give the step and then the first term
        long sumX = n * (n - 1) / 2, sumXX = 0, sumA = 0, sumXA = 0;
        for (long i = 0; i < n; i++) {
            in.nextToken();
            long v = (long) in.nval;
            sumXX += i * i;
            sumA += v;
            sumXA += i * v;
        }
        double step = (double) (n * sumXA - sumX * sumA) / (double) (n * sumXX - sumX * sumX);
        double first = (sumA - step * sumX) / n;
        System.out.printf("%.9f %.9f%n", first, step);
    }
}
