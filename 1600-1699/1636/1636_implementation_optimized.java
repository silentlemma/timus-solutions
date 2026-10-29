import java.io.IOException;

public class Main {
    static final int PROBLEMS = 10;
    static final int PER_ATTEMPT = 20; // minutes for each rejected attempt

    // the numbers are parsed byte by byte from System.in, which needs much
    // less memory than Scanner
    private static int readInt() throws IOException {
        int ch;
        do {
            ch = System.in.read();
        } while (ch <= ' ' && ch != -1);
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int t1 = readInt(), t2 = readInt();
        int clean = t2;
        for (int i = 0; i < PROBLEMS; i++)
            clean -= PER_ATTEMPT * readInt();
        // without the rejected attempts ZZZ wins only with strictly less time
        System.out.println(clean < t1 ? "Dirty debug :(" : "No chance.");
    }
}
