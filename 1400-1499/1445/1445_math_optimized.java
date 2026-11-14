import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static int number(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
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
        int count = number(input);
        int largest = 0;
        int total = 0;
        for (int i = 0; i < count; i++) {
            int size = number(input);
            largest = Math.max(largest, size);
            total += size;
        }
        int best = Math.max(1, 2 * largest - total);
        System.out.print(best);
        System.out.print(' ');
        System.out.println(largest);
    }
}
