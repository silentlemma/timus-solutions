import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    // from the centre, r1 reaches the farthest point and r2 reaches across it:
    // area / (pi r1 r2) is 1 for any oval and 2 / pi for a square, and
    // area / (pi r1^2) is 2 / pi for a square, at most 0.41 for a triangle
    static final double OVAL = 0.8, SQUARE = 0.5;
    static final double HALF = 0.5; // a pixel reaches half a pixel beyond its centre
    static final int BUFFER_SIZE = 1 << 16;

    static DataInputStream in = new DataInputStream(System.in);
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
        while (c < '0' || c > '9')
            c = readByte();
        int n = 0;
        for (; c >= '0' && c <= '9'; c = readByte())
            n = n * 10 + (c - '0');
        return n;
    }

    public static void main(String[] args) throws IOException {
        int w = readInt(), h = readInt();
        // the first and last pixel of each row
        double[] ex = new double[2 * h], ey = new double[2 * h];
        int k = 0;
        double count = 0, sx = 0, sy = 0;
        for (int y = 0; y < h; y++) {
            int first = -1, last = -1;
            for (int x = 0; x < w; x++) {
                int ch = readByte();
                while (ch != '0' && ch != '1')
                    ch = readByte();
                if (ch == '1') {
                    if (first < 0)
                        first = x;
                    last = x;
                    count++;
                    sx += x;
                    sy += y;
                }
            }
            if (first >= 0) {
                ex[k] = first;
                ey[k++] = y;
                ex[k] = last;
                ey[k++] = y;
            }
        }
        double cx = sx / count, cy = sy / count;
        int far = 0;
        for (int i = 0; i < k; i++)
            if (Math.hypot(ex[i] - cx, ey[i] - cy) > Math.hypot(ex[far] - cx, ey[far] - cy))
                far = i;
        double r1 = Math.hypot(ex[far] - cx, ey[far] - cy);
        double ux = (ex[far] - cx) / r1, uy = (ey[far] - cy) / r1, r2 = 0;
        for (int i = 0; i < k; i++)
            r2 = Math.max(r2, Math.abs((ey[i] - cy) * ux - (ex[i] - cx) * uy));
        if (count / (Math.PI * (r1 + HALF) * (r2 + HALF)) > OVAL)
            System.out.println("circle");
        else if (count / (Math.PI * (r1 + HALF) * (r1 + HALF)) > SQUARE)
            System.out.println("square");
        else
            System.out.println("triangle");
    }
}
