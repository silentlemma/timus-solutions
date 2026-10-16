import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    static final int FRESH = 0, WALKING = 1, DONE = 2;
    static DataInputStream in = new DataInputStream(new java.io.BufferedInputStream(System.in));

    static int readInt() throws IOException {
        int c = in.read();
        while (c < '0') {
            c = in.read();
        }
        int value = 0;
        while (c >= '0') {
            value = value * 10 + c - '0';
            c = in.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] to = new int[n + 1], incoming = new int[n + 1];
        for (int v = 1; v <= n; v++) {
            to[v] = readInt();
            incoming[to[v]]++;
        }
        // follow the arrows from every new programmer to find the cycles
        int[] state = new int[n + 1], path = new int[n];
        int cycles = 0, onCycles = 0, bare = 0;
        for (int start = 1; start <= n; start++) {
            int length = 0, v = start;
            while (state[v] == FRESH) {
                state[v] = WALKING;
                path[length++] = v;
                v = to[v];
            }
            if (state[v] == WALKING) {
                cycles++;
                // a cycle nobody else points into needs a group of its own
                boolean alone = true;
                int u = v;
                do {
                    onCycles++;
                    if (incoming[u] != 1) {
                        alone = false;
                    }
                    u = to[u];
                } while (u != v);
                if (alone) {
                    bare++;
                }
            }
            for (int k = 0; k < length; k++) {
                state[path[k]] = DONE;
            }
        }
        // fewest: every programmer nobody names starts a group, and so does
        // every bare cycle; most: a cycle goes into one group as soon as a
        // group enters it, and everyone else can stand alone
        int starts = 0;
        for (int v = 1; v <= n; v++) {
            if (incoming[v] == 0) {
                starts++;
            }
        }
        System.out.println((starts + bare) + " " + (n - onCycles + cycles));
    }
}
