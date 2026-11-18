import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int INPUT_BUFFER_SIZE = 512;

    private static int nextInt(BufferedInputStream input) throws IOException {
        int symbol;
        do {
            symbol = input.read();
        } while (symbol <= ' ' && symbol >= 0);
        int value = 0;
        while (symbol > ' ') {
            value = value * 10 + symbol - '0';
            symbol = input.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in, INPUT_BUFFER_SIZE);
        int count = nextInt(input);
        int total = 0;
        int largest = 0;
        for (int i = 0; i < count; i++) {
            int clearance = nextInt(input);
            total += clearance;
            if (clearance > largest) {
                largest = clearance;
            }
        }
        System.out.println(total + largest);
    }
}
