import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static final int LETTERS = 26;
    static final int SYMBOLS = LETTERS * (LETTERS + 1);
    static final int MAX_DEPTH = 50;
    static final int DECIMAL = 10;

    static boolean digit(char c) { return '0' <= c && c <= '9'; }

    static void totals(String formula, short[] counts, int[] parents) {
        Arrays.fill(counts, (short)0);
        int start = 0;
        while (start < formula.length()) {
            int end = formula.indexOf('+', start);
            if (end < 0) {
                end = formula.length();
            }
            int first = start;
            int product = 0;
            while (digit(formula.charAt(first))) {
                product = product * DECIMAL + formula.charAt(first++) - '0';
            }
            if (first == start) {
                product = 1;
            }
            start = end + 1;
            int depth = 0;
            // In reverse order, the multiplier comes before its group.
            for (int i = end - 1; i >= first; i--) {
                int count = 0;
                int place = 1;
                while (digit(formula.charAt(i))) {
                    count += (formula.charAt(i--) - '0') * place;
                    place *= DECIMAL;
                }
                if (place == 1) {
                    count = 1;
                }
                char c = formula.charAt(i);
                if (c == ')') {
                    parents[depth++] = product;
                    product *= count;
                } else if (c == '(') {
                    product = parents[--depth];
                } else {
                    int suffix = 0;
                    if ('a' <= c && c <= 'z') {
                        suffix = c - 'a' + 1;
                        c = formula.charAt(--i);
                    }
                    counts[(c - 'A') * (LETTERS + 1) + suffix] += count * product;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String left = input.readLine();
        int n = Integer.parseInt(input.readLine().trim());
        short[] expected = new short[SYMBOLS];
        short[] actual = new short[SYMBOLS];
        int[] parents = new int[MAX_DEPTH];
        totals(left, expected, parents);
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < n; i++) {
            String right = input.readLine();
            totals(right, actual, parents);
            output.append(left).append(Arrays.equals(actual, expected) ? "==" : "!=");
            output.append(right).append('\n');
        }
        System.out.print(output);
    }
}
