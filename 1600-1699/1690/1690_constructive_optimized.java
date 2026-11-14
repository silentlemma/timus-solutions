import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int CLASSES = 4;

    private static int magnitude(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && (c <= ' ' || c == '-')) {
            c = input.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = 10 * value + c - '0';
            c = input.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int count = magnitude(input);
        char[] indices = new char[CLASSES * count];
        int[] sizes = new int[CLASSES];
        for (int i = 1;; i++) {
            int x = magnitude(input), y = magnitude(input);
            int group = 2 * (x & 1) + (y & 1);
            int start = group * count;
            indices[start + sizes[group]++] = (char)i;
            if (sizes[group] == count) {
                StringBuilder output = new StringBuilder("OK\n");
                for (int j = 0; j < count; j++) {
                    if (j != 0) {
                        output.append(' ');
                    }
                    output.append((int)indices[start + j]);
                }
                System.out.println(output);
                return;
            }
        }
    }
}
