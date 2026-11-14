import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static final int CENTS = 100;
    private static final int DECIMAL = 10;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer fields = new StringTokenizer(input.readLine());
        int lastIndex = Integer.parseInt(fields.nextToken()) - 1;
        double firstHeight = Double.parseDouble(fields.nextToken());

        // The minimum of A/k + k is attained near sqrt(A).
        int k = (int)Math.sqrt(firstHeight);
        double lastHeight = 0;
        if (k < lastIndex) {
            if (firstHeight > k * (k + 1)) {
                k++;
            }
            lastHeight = (lastIndex - k) * (lastIndex - firstHeight / k);
        }

        long cents = Math.round(lastHeight * CENTS);
        long fraction = cents % CENTS;
        System.out.println(cents / CENTS + (fraction < DECIMAL ? ".0" : ".") + fraction);
    }
}
