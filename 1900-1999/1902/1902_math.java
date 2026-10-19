import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static class FastInput {
        private final BufferedInputStream input = new BufferedInputStream(System.in);

        int nextInt() throws IOException {
            int ch;
            do {
                ch = input.read();
            } while (ch <= ' ' && ch != -1);
            int value = 0;
            while (ch > ' ') {
                value = value * 10 + ch - '0';
                ch = input.read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int count = input.nextInt();
        int duration = input.nextInt();
        int start = input.nextInt();
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < count; ++i) {
            int other = input.nextInt();
            int doubledTime = start + duration + other;
            output.append(doubledTime / 2);
            output.append(doubledTime % 2 == 0 ? ".000000\n" : ".500000\n");
        }
        System.out.print(output);
    }
}
