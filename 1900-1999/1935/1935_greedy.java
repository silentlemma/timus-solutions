import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static int minimumSheets(int[] clearances) {
        int total = 0;
        int largest = 0;
        for (int clearance : clearances) {
            total += clearance;
            largest = Math.max(largest, clearance);
        }
        return total + largest;
    }

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
        BufferedInputStream input = new BufferedInputStream(System.in);
        int count = nextInt(input);
        int[] clearances = new int[count];
        for (int index = 0; index < count; index++) {
            clearances[index] = nextInt(input);
        }
        System.out.println(minimumSheets(clearances));
    }
}
