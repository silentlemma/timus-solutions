import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static String draw(int[] xs, int[] ys) {
        int left = 0, right = 0, lower = 0, upper = 0;
        for (int index = 0; index < xs.length; ++index) {
            left = Math.min(left, xs[index]);
            right = Math.max(right, xs[index]);
            lower = Math.min(lower, ys[index]);
            upper = Math.max(upper, ys[index]);
        }
        int width = right - left + 1;
        char[][] grid = new char[upper - lower + 1][width];
        for (char[] row : grid) {
            Arrays.fill(row, '.');
            row[-left] = '|';
        }
        Arrays.fill(grid[upper], '-');
        grid[upper][-left] = '+';
        for (int index = 0; index < xs.length; ++index)
            grid[upper - ys[index]][xs[index] - left] = '*';
        StringBuilder output = new StringBuilder();
        for (char[] row : grid)
            output.append(row).append('\n');
        return output.toString();
    }

    static int nextInt(BufferedInputStream in) throws IOException {
        int symbol;
        do {
            symbol = in.read();
        } while (symbol <= ' ' && symbol != -1);
        int sign = 1;
        if (symbol == '-' || symbol == '+') {
            if (symbol == '-')
                sign = -1;
            symbol = in.read();
        }
        int value = 0;
        while (symbol > ' ') {
            value = value * 10 + symbol - '0';
            symbol = in.read();
        }
        return sign * value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream in = new BufferedInputStream(System.in);
        int size = nextInt(in);
        int[] xs = new int[size], ys = new int[size];
        for (int index = 0; index < size; ++index) {
            xs[index] = nextInt(in);
            ys[index] = nextInt(in);
        }
        System.out.print(draw(xs, ys));
    }
}
