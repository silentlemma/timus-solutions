import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    // character classes, ordered: the end, other characters, dot, at, letters
    static final int OTHER = 1, DOT = 2, AT = 3, LETTER = 4, ALPHABET = LETTER + 26;
    static final int BUFFER = 1 << 16;

    static int[] order, rank;

    // cyclic prefix doubling with counting sort; code ends with a 0
    static void suffixArray(byte[] code) {
        int n = code.length;
        int[] count = new int[Math.max(n, ALPHABET)];
        order = new int[n];
        int[] cls = new int[n], shifted = new int[n], fresh = new int[n];
        for (byte c : code) {
            count[c]++;
        }
        for (int i = 1; i < ALPHABET; i++) {
            count[i] += count[i - 1];
        }
        for (int i = n - 1; i >= 0; i--) {
            order[--count[code[i]]] = i;
        }
        int classes = 1;
        for (int i = 1; i < n; i++) {
            if (code[order[i]] != code[order[i - 1]]) {
                classes++;
            }
            cls[order[i]] = classes - 1;
        }
        for (int shift = 1; shift < n && classes < n; shift *= 2) {
            for (int i = 0; i < n; i++) {
                int p = order[i] - shift;
                shifted[i] = p < 0 ? p + n : p;
            }
            Arrays.fill(count, 0, classes, 0);
            for (int p : shifted) {
                count[cls[p]]++;
            }
            for (int i = 1; i < classes; i++) {
                count[i] += count[i - 1];
            }
            for (int i = n - 1; i >= 0; i--) {
                order[--count[cls[shifted[i]]]] = shifted[i];
            }
            fresh[order[0]] = 0;
            classes = 1;
            for (int i = 1; i < n; i++) {
                int cur = order[i], prev = order[i - 1];
                if (cls[cur] != cls[prev] || cls[(cur + shift) % n] != cls[(prev + shift) % n]) {
                    classes++;
                }
                fresh[cur] = classes - 1;
            }
            int[] swap = cls;
            cls = fresh;
            fresh = swap;
        }
        rank = cls;
    }

    public static void main(String[] args) throws IOException {
        InputStream in = System.in;
        ByteArrayOutputStream all = new ByteArrayOutputStream();
        byte[] buf = new byte[BUFFER];
        for (int got; (got = in.read(buf)) > 0;) {
            all.write(buf, 0, got);
        }
        byte[] text = all.toByteArray();
        int n = text.length;
        byte[] code = new byte[n + 1];
        int[] letters = new int[n + 1];
        for (int i = 0; i < n; i++) {
            byte ch = text[i];
            boolean letter = ch >= 'a' && ch <= 'z';
            int kind = ch == '.' ? DOT : ch == '@' ? AT : OTHER;
            code[i] = (byte) (letter ? LETTER + ch - 'a' : kind);
            letters[i + 1] = letters[i] + (letter ? 1 : 0);
        }
        // around an at sign, users start no earlier than just past the last other
        // character, at or double dot, and domains end no later than just before
        // the next of them
        int[] firstStart = new int[n], lastEnd = new int[n], nextAt = new int[n];
        int barrier = -1, twin = -1;
        for (int i = 0; i < n; i++) {
            if (code[i] == AT) {
                firstStart[i] = Math.max(barrier, twin) + 1;
            }
            if (code[i] == DOT && i > 0 && code[i - 1] == DOT) {
                twin = i;
            }
            if (code[i] == OTHER || code[i] == AT) {
                barrier = i;
            }
        }
        barrier = n;
        twin = n;
        int upcoming = -1;
        for (int i = n - 1; i >= 0; i--) {
            if (code[i] == AT) {
                lastEnd[i] = Math.min(barrier, twin) - 1;
            }
            if (code[i] == OTHER) {
                upcoming = -1;
            }
            nextAt[i] = upcoming;
            if (code[i] == DOT && code[i + 1] == DOT) {
                twin = i + 1;
            }
            if (code[i] == OTHER || code[i] == AT) {
                barrier = i;
            }
            if (code[i] == AT) {
                upcoming = i;
            }
        }
        suffixArray(code);
        // being an address is a property of the string alone, so every
        // address is counted once, at the first suffix in sorted order that
        // starts with it: only prefixes longer than the common part before
        long total = 0;
        int common = 0;
        for (int start = 0; start < n; start++) {
            int prev = order[rank[start] - 1];
            while (code[start + common] != 0 && code[start + common] == code[prev + common]) {
                common++;
            }
            int lcp = common;
            if (common > 0) {
                common--;
            }
            if (code[start] < LETTER) {
                continue;
            }
            int a = nextAt[start];
            if (a < 0 || start < firstStart[a] || code[a - 1] < LETTER) {
                continue;
            }
            int end = lastEnd[a];
            if (a + 1 > end || code[a + 1] < LETTER) {
                continue;
            }
            int lo = Math.max(start + lcp, a + 1);
            if (lo <= end) {
                total += letters[end + 1] - letters[lo];
            }
        }
        System.out.println(total);
    }
}
