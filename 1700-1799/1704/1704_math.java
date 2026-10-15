import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int BITS = 8; // bits of a character, the lowest first
    static final int ONE_FREQ = 2; // a one is sin(2 pi k / t), a zero sin(4 pi k / t)
    static final int ZERO_FREQ = 4;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int) in.nval;
        in.nextToken();
        int t = (int) in.nval;
        double[] samples = new double[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            samples[i] = in.nval;
        }
        // over a whole number of periods sin(2 pi k / t) and sin(4 pi k / t) are
        // orthogonal to each other and to a constant, so the correlation of a bit's
        // samples with each wave picks the wave that was sent
        int[] bits = new int[n / t];
        for (int b = 0; b < bits.length; b++) {
            double one = 0;
            double zero = 0;
            for (int k = 0; k < t; k++) {
                double x = Math.PI * k / t;
                one += samples[b * t + k] * Math.sin(ONE_FREQ * x);
                zero += samples[b * t + k] * Math.sin(ZERO_FREQ * x);
            }
            bits[b] = one > zero ? 1 : 0;
        }
        StringBuilder text = new StringBuilder();
        for (int start = 0; start < bits.length; start += BITS) {
            int c = 0;
            for (int j = 0; j < BITS; j++) {
                c |= bits[start + j] << j;
            }
            text.append((char) c);
        }
        System.out.println(text);
    }
}
