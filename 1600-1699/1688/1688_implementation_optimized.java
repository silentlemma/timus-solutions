import java.io.IOException;

public class Main {
    static final long SHARES = 3; // a bill is split three ways

    static final int BUFFER_SIZE = 4096;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available;

    // refill a fixed chunk, so whitespace and the total input need not fit the buffer.
    static int readByte() throws IOException {
        if (position >= available) {
            available = System.in.read(buffer);
            position = 0;
            if (available < 0)
                return -1;
        }
        return buffer[position++];
    }

    static long nextLong() throws IOException {
        int ch;
        do {
            ch = readByte();
        } while (ch <= ' ' && ch != -1);
        long value = 0;
        while (ch > ' ') {
            value = value * 10 + ch - '0';
            ch = readByte();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        long threshold = SHARES * nextLong();
        int visits = (int)nextLong();
        // at most 3000 bills of 2000000 and three times the fee require long.
        long total = 0;
        int answer = 0;
        // every bill is read, even after the answer is known, so the whole input is consumed
        for (int i = 1; i <= visits; i++) {
            total += nextLong();
            // Vanya's share total / 3 exceeds n exactly when total > 3n
            if (answer == 0 && total > threshold)
                answer = i;
        }
        System.out.println(answer == 0 ? "Team.GOV!" : "Free after " + answer + " times.");
    }
}
