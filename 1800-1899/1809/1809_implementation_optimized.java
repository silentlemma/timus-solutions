import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int SIDE = 20;
    private static final int COUNT = 4;

    private static int number(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = input.read();
        }
        return value;
    }

    private static boolean valid(int[] x, int[] y, int[] neighbors) {
        for (int i = 0; i < COUNT; i++) {
            neighbors[i] = 0;
        }
        // Three potatoes on one line would give the middle one two targets.
        for (int i = 0; i < COUNT; i++) {
            for (int j = 0; j < i; j++) {
                boolean sameX = x[i] == x[j];
                boolean sameY = y[i] == y[j];
                if (sameX && sameY) {
                    return false;
                }
                if (sameX || sameY) {
                    if (++neighbors[i] > 1 || ++neighbors[j] > 1) {
                        return false;
                    }
                }
            }
        }
        for (int degree : neighbors) {
            if (degree != 1) {
                return false;
            }
        }
        return true;
    }

    private static void arrange(int[] x, int[] y) {
        int[] neighbors = new int[COUNT];
        if (valid(x, y, neighbors)) {
            return;
        }
        for (int i = 0; i < COUNT; i++) {
            int oldX = x[i], oldY = y[i];
            for (int column = 1; column <= SIDE; column++) {
                x[i] = column;
                for (int row = 1; row <= SIDE; row++) {
                    y[i] = row;
                    if (valid(x, y, neighbors)) {
                        return;
                    }
                }
            }
            x[i] = oldX;
            y[i] = oldY;
        }

        // Keep the first two potatoes. Use rows occupied by neither.
        int firstRow = 1;
        while (firstRow == y[0] || firstRow == y[1]) {
            firstRow++;
        }
        int secondRow = firstRow + 1;
        while (secondRow == y[0] || secondRow == y[1]) {
            secondRow++;
        }
        int firstMoved = COUNT - 2, secondMoved = COUNT - 1;
        y[firstMoved] = firstRow;
        y[secondMoved] = secondRow;
        if (x[0] == x[1] || y[0] == y[1]) {
            // The kept potatoes already pair up. Build a pair in a free column.
            int column = 1;
            while (column == x[0] || column == x[1]) {
                column++;
            }
            x[firstMoved] = x[secondMoved] = column;
        } else {
            x[firstMoved] = x[0];
            x[secondMoved] = x[1];
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int[] x = new int[COUNT], y = new int[COUNT];
        for (int i = 0; i < COUNT; i++) {
            x[i] = number(input);
            y[i] = number(input);
        }
        arrange(x, y);
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < COUNT; i++) {
            output.append(x[i]).append(' ').append(y[i]).append('\n');
        }
        System.out.print(output);
    }
}
