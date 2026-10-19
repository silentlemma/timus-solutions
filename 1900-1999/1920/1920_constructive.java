import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

    private static int nextInt() throws IOException {
        int value;
        do {
            value = INPUT.read();
        } while (value <= ' ' && value >= 0);
        int result = 0;
        while (value > ' ') {
            result = result * 10 + value - '0';
            value = INPUT.read();
        }
        return result;
    }

    private static void insertEar(int[] successor, int first, int second,
                                  int outerFirst, int outerSecond) {
        if (successor[first] != second) {
            int temporary = first;
            first = second;
            second = temporary;
            temporary = outerFirst;
            outerFirst = outerSecond;
            outerSecond = temporary;
        }
        successor[first] = outerFirst;
        successor[outerFirst] = outerSecond;
        successor[outerSecond] = second;
    }

    static int[] constructCycle(int size, int length) {
        if (length % 2 != 0 || length > size * size - size % 2) {
            return null;
        }
        int[] successor = new int[size * size];
        int[] initial = {0, 1, size + 1, size};
        for (int index = 0; index < initial.length; ++index) {
            successor[initial[index]] = initial[(index + 1) % initial.length];
        }
        int used = initial.length;
        int width = size - size % 2;
        for (int column = 2; column < width && used < length; ++column) {
            insertEar(successor, column - 1, size + column - 1, column, size + column);
            used += 2;
        }
        for (int row = 2; row < size && used < length; ++row) {
            for (int column = 0; column < width && used < length; column += 2) {
                int upper = (row - 1) * size + column;
                int lower = row * size + column;
                insertEar(successor, upper, upper + 1, lower, lower + 1);
                used += 2;
            }
        }
        if (size % 2 != 0) {
            for (int row = 0; row < size - 1 && used < length; row += 2) {
                int left = row * size + width - 1;
                insertEar(successor, left, left + size, left + 1, left + size + 1);
                used += 2;
            }
        }
        int[] result = new int[length];
        int current = 0;
        for (int index = 0; index < length; ++index) {
            result[index] = current;
            current = successor[current];
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        int size = nextInt();
        int length = nextInt();
        int[] cycle = constructCycle(size, length);
        StringBuilder output = new StringBuilder();
        if (cycle == null) {
            output.append("Unsuitable device\n");
        } else {
            output.append("Overwhelming power of magic\n");
            for (int vertex : cycle) {
                output.append(vertex / size + 1).append(' ')
                        .append(vertex % size + 1).append('\n');
            }
        }
        System.out.print(output);
    }
}
