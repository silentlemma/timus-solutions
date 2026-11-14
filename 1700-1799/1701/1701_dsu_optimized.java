import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int MAX_SALARY = 1000000000;
    private static final int DECIMAL_DIGITS = 10;

    private static int number(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        boolean negative = c == '-';
        if (negative) {
            c = input.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = 10 * value + c - '0';
            c = input.read();
        }
        return negative ? -value : value;
    }

    private static void writeInt(BufferedOutputStream out, byte[] digits, int value)
        throws IOException {
        int start = digits.length;
        do {
            digits[--start] = (byte)('0' + value % 10);
            value /= 10;
        } while (value > 0);
        out.write(digits, start, digits.length - start);
    }

    private static final class Dsu {
        final int[] parent;
        final int[] offset;
        final int[] low;
        final int[] high;

        Dsu(int size) {
            parent = new int[size];
            offset = new int[size];
            low = new int[size];
            high = new int[size];
            Arrays.fill(parent, -1);
            Arrays.fill(high, MAX_SALARY);
            high[0] = 0;
        }

        int find(int vertex) {
            int previous = parent[vertex];
            if (previous < 0) {
                return vertex;
            }
            int root = find(previous);
            offset[vertex] += offset[previous];
            parent[vertex] = root;
            return root;
        }

        boolean add(int a, int b, int difference) {
            int left = find(a);
            int right = find(b);
            int shift = offset[a] - offset[b] - difference;
            if (left == right) {
                return shift == 0;
            }

            // A negative parent gives the component size at its root.
            if (parent[left] > parent[right]) {
                int previous = left;
                left = right;
                right = previous;
                shift = -shift;
            }
            // Translate the right root's range before intersecting it with the left range.
            low[left] = Math.max(low[left], low[right] - shift);
            high[left] = Math.min(high[left], high[right] - shift);
            if (low[left] > high[left]) {
                return false;
            }
            parent[left] += parent[right];
            parent[right] = left;
            offset[right] = shift;
            return true;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int people = number(input);
        int statements = number(input);
        Dsu staff = new Dsu(people);
        for (int k = 1; k <= statements; k++) {
            if (!staff.add(number(input), number(input), number(input))) {
                System.out.println("Impossible after " + k + " statements");
                return;
            }
        }

        System.out.println("Possible");
        BufferedOutputStream output = new BufferedOutputStream(System.out);
        byte[] digits = new byte[DECIMAL_DIGITS];
        for (int employee = 0; employee < people; employee++) {
            int root = staff.find(employee);
            writeInt(output, digits, staff.low[root] + staff.offset[employee]);
            output.write('\n');
        }
        output.flush();
    }
}
