import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int PERCENT = 100;
    private static final long OUTPUT_SCALE = 1000000000L;
    private static final double HALF = 0.5;
    private static final int MIN_DECIMALS = 3;

    private static String nextToken(BufferedInputStream input) throws IOException {
        int symbol = input.read();
        while (symbol != -1 && symbol <= ' ') {
            symbol = input.read();
        }
        StringBuilder token = new StringBuilder();
        while (symbol > ' ') {
            token.append((char) symbol);
            symbol = input.read();
        }
        return token.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int seatCount = Integer.parseInt(nextToken(input));
        int vacancyPercent = Integer.parseInt(nextToken(input));
        String seats = nextToken(input);

        int left = 0;
        int right = 0;
        int occupiedLeft = 0;
        boolean beforeOwnSeat = true;
        for (int index = 0; index < seatCount; ++index) {
            char seat = seats.charAt(index);
            if (seat == '2') {
                beforeOwnSeat = false;
            } else if (seat == '0') {
                if (beforeOwnSeat) {
                    ++left;
                } else {
                    ++right;
                }
            } else if (beforeOwnSeat) {
                ++occupiedLeft;
            }
        }

        int empty = left + right;
        double[] step = new double[empty + 1];
        double[] expected = new double[empty + 1];
        double arrival = 0;
        double remaining = 0;
        // Observed arrivals update the distribution of the final audience size.
        for (int count = 1; count <= empty; ++count) {
            double weight = (double) (count * (PERCENT - vacancyPercent));
            arrival = weight / (weight
                    + (double) ((empty - count + 1) * vacancyPercent) * (1 - arrival));
            remaining = arrival * (1 + remaining);
            step[count] = arrival / count;
            expected[count] = remaining / count;
        }

        double[] best = new double[right + 1];
        // The current cell compares sitting now with waiting for the next arrival.
        for (int l = 1; l <= left; ++l) {
            for (int r = 1; r <= right; ++r) {
                int count = l + r;
                double stop = r * expected[count];
                double wait = step[count] * (l * (1 + best[r]) + r * best[r - 1]);
                best[r] = Math.min(stop, wait);
            }
        }

        double answer = occupiedLeft + best[right];
        long rounded = (long) Math.floor(answer * OUTPUT_SCALE + HALF);
        String fraction = Long.toString(rounded % OUTPUT_SCALE + OUTPUT_SCALE).substring(1);
        while (fraction.length() > MIN_DECIMALS && fraction.endsWith("0")) {
            fraction = fraction.substring(0, fraction.length() - 1);
        }
        System.out.println(rounded / OUTPUT_SCALE + "." + fraction);
    }
}
