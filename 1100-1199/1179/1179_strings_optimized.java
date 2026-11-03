import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int WALL = 36, SMALLEST = 2, BYTES = 256, BUFFER_SIZE = 8192;
    public static void main(String[] args) throws IOException {
        int[] value = new int[BYTES];
        Arrays.fill(value, WALL);
        for (int c = '0'; c <= '9'; c++)
            value[c] = c - '0';
        for (int c = 'A'; c <= 'Z'; c++)
            value[c] = c - 'A' + 10;
        int[] change = new int[WALL + 2];
        byte[] buffer = new byte[BUFFER_SIZE];
        int left = WALL;
        for (int count = System.in.read(buffer); count != -1; count = System.in.read(buffer)) {
            for (int i = 0; i < count; i++) {
                int right = value[buffer[i]];
                if (right < left) {
                    change[Math.max(SMALLEST, right + 1)]++;
                    change[left + 1]--;
                }
                left = right;
            }
        }
        int bestBase = SMALLEST, best = -1, running = 0;
        for (int base = SMALLEST; base <= WALL; base++) {
            running += change[base];
            if (running > best) {
                bestBase = base;
                best = running;
            }
        }
        System.out.println(bestBase + " " + best);
    }
}
