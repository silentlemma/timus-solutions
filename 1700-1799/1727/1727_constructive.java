import java.io.*;
import java.util.ArrayList;

public class Main {
    static final int LIMIT = 100000, BASE = 10, SMALL = BASE - 1;
    static final int REMAINDER = SMALL * (SMALL + 1) / 2;

    static int digitSum(int value) {
        int sum = 0;
        while (value > 0) {
            sum += value % BASE;
            value /= BASE;
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int remaining = (int)in.nval, value = LIMIT - 1;
        ArrayList<Integer> chosen = new ArrayList<>();
        // The first ten thousand candidates have digit sum 270000 in total.
        // This phase stops before any one-digit number is used.
        while (remaining > REMAINDER) {
            chosen.add(value);
            remaining -= digitSum(value--);
        }
        // Distinct digits 1..9 can make every sum from zero through 45.
        for (int digit = SMALL; digit > 0; digit--)
            if (digit <= remaining) {
                chosen.add(digit);
                remaining -= digit;
            }
        StringBuilder output = new StringBuilder();
        output.append(chosen.size()).append('\n');
        for (int number : chosen)
            output.append(number).append(' ');
        output.append('\n');
        System.out.print(output);
    }
}
