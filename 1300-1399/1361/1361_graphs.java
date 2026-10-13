import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static DataInputStream in = new DataInputStream(System.in);
    static final int BUFFER_SIZE = 1 << 16;
    static byte[] buf = new byte[BUFFER_SIZE];
    static int bufLen = 0, bufPos = 0;

    static int readByte() throws IOException {
        if (bufPos == bufLen) {
            bufLen = in.read(buf, 0, buf.length);
            bufPos = 0;
            if (bufLen <= 0)
                return -1;
        }
        return buf[bufPos++];
    }

    static int readInt() throws IOException {
        int c = readByte();
        while (c != -1 && (c < '0' || c > '9'))
            c = readByte();
        int n = 0;
        for (; c >= '0' && c <= '9'; c = readByte())
            n = n * 10 + (c - '0');
        return n;
    }

    // when the walk from start is at each node it reaches: the first moment
    // (or -1 if never) and the period, 0 for a node passed only once
    static long[][] visits(int[] step, int start) {
        int n = step.length - 1;
        long[] first = new long[n + 1], period = new long[n + 1];
        Arrays.fill(first, -1);
        int[] order = new int[n];
        int len = 0, v = start;
        while (first[v] < 0) {
            first[v] = len;
            order[len++] = v;
            v = step[v];
        }
        long loopStart = first[v], cycle = len - first[v];
        for (int i = 0; i < len; i++)
            if (first[order[i]] >= loopStart)
                period[order[i]] = cycle;
        return new long[][] {first, period};
    }

    static long gcd(long a, long b) { return b == 0 ? a : gcd(b, a % b); }

    // x with a x = 1 (mod m), for a and m coprime
    static long inverse(long a, long m) {
        long g = m, x = 0, x1 = 1, a1 = a % m;
        while (a1 != 0) {
            long q = g / a1, t = g - q * a1;
            g = a1;
            a1 = t;
            t = x - q * x1;
            x = x1;
            x1 = t;
        }
        return (x % m + m) % m;
    }

    // the least moment in both sets r + k L (k >= 0), or -1
    static long firstCommon(long ra, long la, long rb, long lb) {
        if (la == 0 && lb == 0)
            return ra == rb ? ra : -1;
        if (la == 0) {
            long t = ra;
            ra = rb;
            rb = t;
            t = la;
            la = lb;
            lb = t;
        }
        if (lb == 0) // one moment rb against the moments ra, ra + la, ...
            return rb >= ra && (rb - ra) % la == 0 ? rb : -1;
        long g = gcd(la, lb);
        if ((rb - ra) % g != 0)
            return -1;
        long m = lb / g;
        long k = 0;
        if (m > 1) {
            long diff = ((rb - ra) / g % m + m) % m;
            k = diff * inverse(la / g % m, m) % m;
        }
        long t = ra + la * k, whole = la / g * lb;
        if (t < rb)
            t += (rb - t + whole - 1) / whole * whole;
        return t;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] left = new int[n + 1], right = new int[n + 1];
        for (int v = 1; v <= n; v++) {
            int x = readInt(), last = 0;
            left[v] = x;
            while (x != 0) {
                last = x;
                x = readInt();
            }
            right[v] = last;
        }
        int a = readInt(), b = readInt();
        // A always takes the leftmost road and B the rightmost
        long[][] sa = visits(left, a), sb = visits(right, b);
        long best = -1;
        for (int v = 1; v <= n; v++) {
            if (sa[0][v] < 0 || sb[0][v] < 0)
                continue;
            long t = firstCommon(sa[0][v], sa[1][v], sb[0][v], sb[1][v]);
            if (t >= 0 && (best < 0 || t < best))
                best = t;
        }
        System.out.println(best);
    }
}
