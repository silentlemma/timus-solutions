import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;

public class Main {
    static final long NINE = 9;
    static final long BASE = 10;
    static final int CHUNK = 1 << 16;

    // the whole input at once: 200 000 numbers are slow to read token by token
    static byte[] data;
    static int pos;

    static String word() {
        while (pos < data.length && (data[pos] < '0' || data[pos] > '9'))
            pos++;
        int start = pos;
        while (pos < data.length && data[pos] >= '0' && data[pos] <= '9')
            pos++;
        return new String(data, start, pos - start);
    }

    public static void main(String[] args) throws IOException {
        InputStream in = System.in;
        ByteArrayOutputStream raw = new ByteArrayOutputStream();
        byte[] buf = new byte[CHUNK];
        for (int got; (got = in.read(buf)) > 0;)
            raw.write(buf, 0, got);
        data = raw.toByteArray();
        int n = Integer.parseInt(word());
        String[] records = new String[n];
        long total = 0;
        for (int i = 0; i < n; i++) {
            records[i] = word();
            total += Long.parseLong(records[i]);
        }
        long diff = Long.parseLong(word()) - total;
        if (diff == 0) {
            System.out.println("Input has no error.");
            return;
        }
        // swapping digits a (at 10^(i+1)) and b (at 10^i) adds 9 * (b - a) * 10^i
        if (diff % NINE == 0) {
            long step = diff / NINE;
            int place = 0;
            while (step % BASE == 0) {
                step /= BASE;
                place++;
            }
            if (Math.abs(step) < BASE)
                for (int number = 0; number < n; number++) {
                    char[] digits = records[number].toCharArray();
                    int hi = digits.length - 2 - place; // index of the digit at 10^(i+1)
                    if (hi < 0 || digits[hi + 1] - digits[hi] != step)
                        continue;
                    if (hi == 0 && digits[1] == '0')
                        continue; // the swap would make a leading zero
                    char t = digits[hi];
                    digits[hi] = digits[hi + 1];
                    digits[hi + 1] = t;
                    System.out.println("Error in record #" + (number + 1) +
                                       ". Correct number is: " + new String(digits) + ".");
                    return;
                }
        }
        System.out.println("Unrecoverable error.");
    }
}
