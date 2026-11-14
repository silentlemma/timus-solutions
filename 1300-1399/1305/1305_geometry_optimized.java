import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int DECIMAL = 10;
    private static final int INPUT_BUFFER = 8192;

    private static class Input {
        final InputStream stream;
        final byte[] buffer = new byte[INPUT_BUFFER];
        int offset;
        int end;

        Input(InputStream stream) { this.stream = stream; }

        int read() throws IOException {
            if (offset >= end) {
                end = stream.read(buffer);
                offset = 0;
                if (end <= 0) {
                    return -1;
                }
            }
            return buffer[offset++];
        }

        int number() throws IOException {
            int ch = read();
            while (ch >= 0 && ch <= ' ') {
                ch = read();
            }
            int value = 0;
            while (ch >= '0' && ch <= '9') {
                value = DECIMAL * value + ch - '0';
                ch = read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input(System.in);
        int n = input.number();
        int x = input.number(), y = input.number();
        int minX = x, maxX = x, minY = y, maxY = y;
        int minSum = x + y, maxSum = x + y, minDiff = x - y, maxDiff = x - y;
        for (int i = 1; i < n; i++) {
            x = input.number();
            y = input.number();
            minX = Math.min(minX, x);
            maxX = Math.max(maxX, x);
            minY = Math.min(minY, y);
            maxY = Math.max(maxY, y);
            minSum = Math.min(minSum, x + y);
            maxSum = Math.max(maxSum, x + y);
            minDiff = Math.min(minDiff, x - y);
            maxDiff = Math.max(maxDiff, x - y);
        }
        int[] xs = {minSum - minY, maxDiff + minY, maxX, maxX,
                    maxSum - maxY, minDiff + maxY, minX, minX};
        int[] ys = {minY, minY, maxX - maxDiff, maxSum - maxX,
                    maxY, maxY, minX - minDiff, minSum - minX};
        StringBuilder answer = new StringBuilder();
        int previous = xs.length - 1;
        for (int i = 0; i < xs.length; i++) {
            if (xs[i] != xs[previous] || ys[i] != ys[previous]) {
                answer.append(xs[i]).append(' ').append(ys[i]).append('\n');
            }
            previous = i;
        }
        if (answer.length() == 0) {
            answer.append(xs[0]).append(' ').append(ys[0]).append('\n');
        }
        System.out.print(answer);
    }
}
