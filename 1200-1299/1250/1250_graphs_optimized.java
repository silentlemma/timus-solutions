import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int DECIMAL = 10;
    private static final int PADDING = 4;
    private static final byte SEA = 0;
    private static final byte LAND = 1;
    private static final byte EXTERIOR = 2;
    private static final byte BLOCKED = 4;
    private static final byte VISITED = 8;

    private static int number(BufferedInputStream input) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * DECIMAL + ch - '0';
            ch = input.read();
        }
        return value;
    }

    private static void flood(byte[] cells, int[] stack, int start, int[] steps, int mask,
                              int target, byte mark) {
        cells[start] = mark;
        int size = 1;
        stack[0] = start;
        while (size > 0) {
            int cell = stack[--size];
            for (int step : steps) {
                int neighbor = cell + step;
                if ((cells[neighbor] & mask) == target) {
                    cells[neighbor] = mark;
                    stack[size++] = neighbor;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int width = number(input);
        int height = number(input);
        int x = number(input);
        int y = number(input);
        int stride = width + PADDING;
        byte[] cells = new byte[stride * (height + PADDING)];
        Arrays.fill(cells, BLOCKED);
        // The inner ring represents the exterior; the outer ring guards the indices.
        for (int row = 1; row < height + PADDING - 1; row++) {
            Arrays.fill(cells, row * stride + 1, (row + 1) * stride - 1, EXTERIOR);
        }
        for (int row = 2; row < height + 2; row++) {
            for (int column = 2; column < width + 2; column++) {
                int ch = input.read();
                while (ch != '.' && ch != '#') {
                    ch = input.read();
                }
                cells[row * stride + column] = ch == '#' ? LAND : SEA;
            }
        }
        int[] sides = {1, -1, stride, -stride};
        int[] directions = {1,          -1,         stride,     -stride,
                            stride + 1, stride - 1, 1 - stride, -stride - 1};
        int[] stack = new int[cells.length];
        int start = (y + 1) * stride + x + 1;
        if (cells[start] == SEA) {
            flood(cells, stack, start, directions, LAND | EXTERIOR | BLOCKED, SEA, BLOCKED);
        }
        flood(cells, stack, stride + 1, sides, BLOCKED | VISITED, SEA, VISITED);
        int count = 0;
        for (int index = 0; index < cells.length; index++) {
            if (cells[index] == LAND) {
                count++;
                flood(cells, stack, index, sides, LAND, LAND, VISITED);
            }
        }
        System.out.println(count);
    }
}
