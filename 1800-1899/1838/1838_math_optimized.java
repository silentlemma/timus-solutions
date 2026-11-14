import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int BUFFER_SIZE = 8192;
    private static final int DECIMAL = 10;

    private static class Input {
        private final InputStream source;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int offset;
        private int end;

        Input(InputStream source) { this.source = source; }

        private int nextByte() throws IOException {
            if (offset >= end) {
                end = source.read(buffer);
                offset = 0;
                if (end <= 0) {
                    return -1;
                }
            }
            return buffer[offset++];
        }

        int number() throws IOException {
            int ch = nextByte();
            while (ch >= 0 && ch <= ' ') {
                ch = nextByte();
            }
            int value = 0;
            while (ch >= '0' && ch <= '9') {
                value = DECIMAL * value + ch - '0';
                ch = nextByte();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input(System.in);
        int length = input.number(), count = input.number();
        int[] supports = new int[count];
        for (int i = 0; i < count; i++) {
            supports[i] = input.number();
        }
        int minCut = 2 * supports[0], maxCut = 2 * supports[count - 1] - length;
        int safe = 0;
        if (minCut < maxCut) {
            for (int i = 1; i < count && supports[i - 1] < maxCut; i++) {
                int left = supports[i - 1], right = supports[i];
                if (right > minCut) {
                    int lo = Math.max(left, Math.max(minCut, 2 * right - length));
                    int hi = Math.min(right, Math.min(maxCut, 2 * left));
                    safe += Math.max(0, hi - lo);
                }
            }
        }
        System.out.println(length - safe);
    }
}
