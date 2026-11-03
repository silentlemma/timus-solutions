import java.io.*;

public class Main {
    static final int WALL = 36, SMALLEST = 2, BUFFER_SIZE = 8192;
    static int digit(byte c) {
        if (c >= '0' && c <= '9')
            return c - '0';
        if (c >= 'A' && c <= 'Z')
            return c - 'A' + 10;
        return WALL;
    }
    public static void main(String[] args) throws IOException {
        ByteArrayOutputStream input = new ByteArrayOutputStream();
        byte[] buffer = new byte[BUFFER_SIZE];
        for (int count = System.in.read(buffer); count != -1; count = System.in.read(buffer))
            input.write(buffer, 0, count);
        byte[] text = input.toByteArray();
        int best = -1, bestBase = SMALLEST;
        for (int base = SMALLEST; base <= WALL; base++) {
            boolean inside = false;
            int count = 0;
            for (byte c : text) {
                boolean current = digit(c) < base;
                if (current && !inside)
                    count++;
                inside = current;
            }
            if (count > best) {
                best = count;
                bestBase = base;
            }
        }
        System.out.println(bestBase + " " + best);
    }
}
