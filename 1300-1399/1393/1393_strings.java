import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.IOException;
import java.util.Locale;

public class Main {
    static final int ALPHABET = 256;

    public static void main(String[] args) throws IOException {
        DataInputStream in = new DataInputStream(new BufferedInputStream(System.in));
        int n = 0, c = in.read();
        while (c < '0' || c > '9')
            c = in.read();
        while (c >= '0' && c <= '9') {
            n = n * 10 + (c - '0');
            c = in.read();
        }
        byte[] text = new byte[n];
        for (int i = 0; i < n;) {
            c = in.read();
            if (c > ' ')
                text[i++] = (byte)c;
        }
        // the shortest period p of the cyclic string: T is u repeated n / p times
        int[] pi = new int[n];
        for (int i = 1; i < n; i++) {
            int k = pi[i - 1];
            while (k > 0 && text[i] != text[k])
                k = pi[k - 1];
            pi[i] = k + (text[i] == text[k] ? 1 : 0);
        }
        int p = n - pi[n - 1];
        if (n % p != 0)
            p = n;
        pi = null;
        // sort the rotations of u by doubling, all of them distinct
        int[] order = new int[p], cls = new int[p], tmp = new int[p], tmpCls = new int[p];
        int[] cnt = new int[Math.max(ALPHABET, p)];
        for (int i = 0; i < p; i++)
            cnt[text[i] & (ALPHABET - 1)]++;
        for (int i = 1; i < ALPHABET; i++)
            cnt[i] += cnt[i - 1];
        for (int i = p - 1; i >= 0; i--)
            order[--cnt[text[i] & (ALPHABET - 1)]] = i;
        int classes = 1;
        for (int i = 1; i < p; i++) {
            if (text[order[i]] != text[order[i - 1]])
                classes++;
            cls[order[i]] = classes - 1;
        }
        for (int len = 1; len < p && classes < p; len *= 2) {
            // sorted by the second half already: shift each start back by len
            for (int i = 0; i < p; i++)
                tmp[i] = (order[i] - len + p) % p;
            java.util.Arrays.fill(cnt, 0, classes, 0);
            for (int i = 0; i < p; i++)
                cnt[cls[tmp[i]]]++;
            for (int i = 1; i < classes; i++)
                cnt[i] += cnt[i - 1];
            for (int i = p - 1; i >= 0; i--)
                order[--cnt[cls[tmp[i]]]] = tmp[i];
            tmpCls[order[0]] = 0;
            classes = 1;
            for (int i = 1; i < p; i++) {
                int a = order[i], b = order[i - 1];
                if (cls[a] != cls[b] || cls[(a + len) % p] != cls[(b + len) % p])
                    classes++;
                tmpCls[a] = classes - 1;
            }
            int[] swap = cls;
            cls = tmpCls;
            tmpCls = swap;
        }
        // Kasai: the common prefix with the previous rotation drops by at most one per step
        long total = 0;
        int h = 0;
        for (int i = 0; i < p; i++) {
            if (cls[i] == 0) {
                h = 0;
                continue;
            }
            int j = order[cls[i] - 1];
            while (h < p && text[(i + h) % p] == text[(j + h) % p])
                h++;
            total += h;
            if (h > 0)
                h--;
        }
        // each rotation of u appears n / p times in a row, with common prefixes of n
        total += (long)p * (n / p - 1) * n;
        System.out.println(String.format(Locale.US, "%.3f", (double)total / (n - 1)));
    }
}
