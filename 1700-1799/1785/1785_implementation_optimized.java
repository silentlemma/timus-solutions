import java.io.IOException;

public class Main {
    private static final int LEGION_MIN = 1000;
    private static final int ZOUNDS_MIN = 500;
    private static final int SWARM_MIN = 250;
    private static final int THRONG_MIN = 100;
    private static final int HORDE_MIN = 50;
    private static final int LOTS_MIN = 20;
    private static final int SEVERAL_MIN = 5;
    // the smallest number for each word, from the largest down
    // (the bounds and the words are those of the statement)
    private static final int[] FROM = {LEGION_MIN, ZOUNDS_MIN, SWARM_MIN,   THRONG_MIN, HORDE_MIN,
                                       LOTS_MIN,   10,         SEVERAL_MIN, 1};
    private static final String[] WORDS = {"legion", "zounds", "swarm",   "throng", "horde",
                                           "lots",   "pack",   "several", "few"};

    // the numbers are parsed byte by byte from System.in, which needs much
    // less memory than Scanner
    private static int nextInt() throws IOException {
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = System.in.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value * sign;
    }

    public static void main(String[] args) throws IOException {
        int n = nextInt();
        int i = 0;
        while (n < FROM[i]) {
            i++;
        }
        System.out.println(WORDS[i]);
    }
}
