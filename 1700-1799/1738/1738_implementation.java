import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
    static final int HEX_PINS = 1 << 16;
    static final int DIGITS = 4;
    static final int NIBBLE = 15;
    static final int BITS = 4;
    static final int BASE = 10;
    static final int HEX = 16;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        int[] pins = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            pins[i] = Integer.parseInt(in.readLine().trim(), HEX);
        }
        // differing hex digits of two pins: nonzero nibbles of their xor
        int[] differ = new int[HEX_PINS];
        for (int x = 1; x < HEX_PINS; x++) {
            differ[x] = differ[x >> BITS] + ((x & NIBBLE) != 0 ? 1 : 0);
        }
        long[] count = new long[DIGITS + 1];
        int longest = Integer.toString(n).length();
        for (int i = 1; i <= n; i++) {
            int pin = pins[i];
            // each pair is counted from its smaller number: a digit raised
            // in place, which never repeats a number, or a digit inserted
            for (int place = 1, rest = i; rest > 0; place *= BASE, rest /= BASE) {
                for (int d = rest % BASE + 1; d < BASE; d++) {
                    int j = i + (d - rest % BASE) * place;
                    if (j > n) {
                        break;
                    }
                    count[differ[pin ^ pins[j]]]++;
                }
            }
            String s = Integer.toString(i);
            if (s.length() >= longest) {
                continue;
            }
            Set<Integer> near = new HashSet<>();
            for (int p = 0; p <= s.length(); p++) {
                for (char d = '0'; d <= '9'; d++) {
                    String t = s.substring(0, p) + d + s.substring(p);
                    if (t.charAt(0) != '0') {
                        near.add(Integer.parseInt(t));
                    }
                }
            }
            for (int j : near) {
                if (j <= n) {
                    count[differ[pin ^ pins[j]]]++;
                }
            }
        }
        StringBuilder out = new StringBuilder();
        for (int k = 1; k <= DIGITS; k++) {
            out.append(count[k]).append(k < DIGITS ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
