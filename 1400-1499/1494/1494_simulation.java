import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    static final int BUFFER = 1 << 16;
    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buf = new byte[BUFFER];
    static int bufLen = 0, bufPos = 0;

    static int read() throws IOException {
        if (bufPos == bufLen) {
            bufLen = in.read(buf, 0, BUFFER);
            bufPos = 0;
            if (bufLen <= 0)
                return -1;
        }
        return buf[bufPos++];
    }

    static int readInt() throws IOException {
        int c = read();
        while (c < '0' || c > '9')
            c = read();
        int x = 0;
        for (; c >= '0' && c <= '9'; c = read())
            x = x * 10 + c - '0';
        return x;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] taken = new int[n];
        for (int i = 0; i < n; i++)
            taken[i] = readInt();
        // the pocket is a stack: roll the balls in order, and whenever the top
        // one is the next ball the inspector took out, take it out
        int[] pocket = new int[n];
        int top = 0, next = 0;
        for (int ball = 1; ball <= n; ball++) {
            pocket[top++] = ball;
            while (top > 0 && next < n && pocket[top - 1] == taken[next]) {
                top--;
                next++;
            }
        }
        System.out.println(next == n ? "Not a proof" : "Cheater");
    }
}
