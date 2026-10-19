import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    static class FastInput {
        final BufferedInputStream stream = new BufferedInputStream(System.in);

        int nextInt() throws IOException {
            int character;
            do {
                character = stream.read();
            } while (character <= ' ');
            int value = 0;
            while (character > ' ') {
                value = value * 10 + character - '0';
                character = stream.read();
            }
            return value;
        }
    }

    static int mostCompared(int[] values) {
        int championValue = values[0];
        int champion = 0;
        int best = 0;
        int currentCount = 0;
        int bestCount = 0;
        for (int index = 1; index < values.length; index++) {
            currentCount++;
            if (currentCount > bestCount) {
                bestCount = currentCount;
                best = champion;
            }
            if (values[index] < championValue) {
                championValue = values[index];
                champion = index;
                currentCount = 1;
            }
        }
        return best + 1;
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int count = input.nextInt();
        int[] values = new int[count];
        for (int i = 0; i < count; i++) {
            values[i] = input.nextInt();
        }
        System.out.println(mostCompared(values));
    }
}
