import java.io.BufferedInputStream;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Main {
    private static final int START = 100000;

    private static int number(BufferedInputStream input) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = 10 * value + ch - '0';
            ch = input.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int n = number(input);
        int[] x = new int[n + 1];
        char[] height = new char[START + 1], path = new char[n];
        for (int id = 1; id <= n; ++id) {
            x[id] = number(input);
            height[number(input)] = (char)id;
        }
        int count = 0;
        boolean right = false;
        for (int y = START; y >= 0; --y) {
            char id = height[y];
            if (id == 0) {
                continue;
            }
            if (count == 0) {
                path[count++] = id;
                continue;
            }
            boolean step = x[id] > x[path[count - 1]];
            // A step in the same direction moves the endpoint to the new extreme.
            if (count == 1 || step != right) {
                path[count++] = id;
            } else {
                path[count - 1] = id;
            }
            right = step;
        }
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));
        output.write(Integer.toString(count));
        output.newLine();
        for (int i = 0; i < count; ++i) {
            if (i > 0) {
                output.write(' ');
            }
            output.write(Integer.toString(path[i]));
        }
        output.newLine();
        output.flush();
    }
}
