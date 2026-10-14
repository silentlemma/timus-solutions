import java.io.*;

public class Main {
    // the digits of the line, without the brackets
    static String digitsOf(String line) {
        StringBuilder s = new StringBuilder();
        for (char c : line.toCharArray())
            if (c >= '0' && c <= '9')
                s.append(c);
        return s.toString();
    }

    // x as k digits, the least significant first
    static String lowFirst(long x, int k) {
        StringBuilder s = new StringBuilder();
        for (int i = 0; i < k; i++, x /= 10)
            s.append((char)('0' + x % 10));
        return s.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String[] nums = new String[2];
        String line;
        for (int i = 0; i < 2 && (line = in.readLine()) != null;)
            if (!digitsOf(line).isEmpty())
                nums[i++] = digitsOf(line);
        int k = nums[0].length();
        long top = 1;
        for (int i = 0; i < k; i++)
            top *= 10;
        long total = Long.parseLong(nums[0]) + Long.parseLong(nums[1]);
        // without a carry every block is the plain sum; with one, the lowest block
        // sends a carry on, and every block above it gets the carry and sends one
        String p, digits;
        if (total < top) {
            p = lowFirst(total, k);
            digits = p;
        } else {
            p = lowFirst(total + 1 - top, k);
            digits = lowFirst(total - top, k) + p;
        }
        // the shortest period of the repeated block, then the shortest tail after
        // which every digit repeats the digit that period further up
        int d = 1;
        while (k % d != 0 || !p.equals(p.substring(d) + p.substring(0, d)))
            d++;
        digits += p + p;
        int start = digits.length() - 2 * k;
        while (start > 0 && digits.charAt(start - 1) == digits.charAt(start - 1 + d))
            start--;
        String period = new StringBuilder(digits.substring(start, start + d)).reverse().toString();
        String tail = new StringBuilder(digits.substring(0, start)).reverse().toString();
        System.out.println("(" + period + ")" + tail);
    }
}
