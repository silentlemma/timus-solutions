import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    static final int BUFFER_SIZE = 1 << 16;
    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buffer = new byte[BUFFER_SIZE];
    static int length;
    static int index;

    static int read() throws IOException {
        if (index == length) {
            length = in.read(buffer, 0, BUFFER_SIZE);
            index = 0;
            if (length <= 0) {
                return -1;
            }
        }
        return buffer[index++];
    }

    static int number() throws IOException {
        int c = read();
        while (c < '0' || c > '9') {
            c = read();
        }
        int v = 0;
        while (c >= '0' && c <= '9') {
            v = v * 10 + (c - '0');
            c = read();
        }
        return v;
    }

    public static void main(String[] args) throws IOException {
        int n = number();
        int[][] spell = new int[2][n];
        for (int i = 0; i < n; i++) {
            spell[0][i] = number() - 1;
            spell[1][i] = number() - 1;
        }
        // the army gathers exactly when every pair of garrisons can be
        // forced together, one pair after another; a pair (u, v), u < v, is
        // the number u * n + v, and a day is her spell m, then his spell k
        int size = n * n;
        byte[] openMoves = new byte[2 * size]; // his replies keeping the pair apart
        int most = 2 * 2 * (n * (n - 1) / 2);
        int[] target = new int[most]; // the pair after both spells
        int[] source = new int[most]; // pair * 2 + her spell
        int count = 0;
        for (int u = 0; u < n; u++) {
            for (int v = u + 1; v < n; v++) {
                int p = u * n + v;
                for (int mine = 0; mine < 2; mine++) {
                    int x = spell[mine][u];
                    int y = spell[mine][v];
                    if (x == y) {
                        continue;
                    }
                    for (int k = 0; k < 2; k++) {
                        int s = spell[k][x];
                        int t = spell[k][y];
                        if (s == t) {
                            continue;
                        }
                        target[count] = s < t ? s * n + t : t * n + s;
                        source[count++] = 2 * p + mine;
                        openMoves[2 * p + mine]++;
                    }
                }
            }
        }
        // the replies that lead into every pair, grouped by that pair
        int[] start = new int[size + 1];
        for (int i = 0; i < count; i++) {
            start[target[i] + 1]++;
        }
        for (int q = 0; q < size; q++) {
            start[q + 1] += start[q];
        }
        int[] place = new int[size];
        System.arraycopy(start, 0, place, 0, size);
        int[] from = new int[count];
        for (int i = 0; i < count; i++) {
            from[place[target[i]]++] = source[i];
        }
        // a pair is won when some spell of hers leaves him no reply that
        // keeps the pair apart outside the won pairs
        boolean[] won = new boolean[size];
        int[] queue = new int[size];
        int tail = 0;
        for (int u = 0; u < n; u++) {
            for (int v = u + 1; v < n; v++) {
                int p = u * n + v;
                if (openMoves[2 * p] == 0 || openMoves[2 * p + 1] == 0) {
                    won[p] = true;
                    queue[tail++] = p;
                }
            }
        }
        for (int h = 0; h < tail; h++) {
            int q = queue[h];
            for (int e = start[q]; e < start[q + 1]; e++) {
                int move = from[e];
                int p = move >> 1;
                if (won[p]) {
                    continue;
                }
                if (--openMoves[move] == 0) {
                    won[p] = true;
                    queue[tail++] = p;
                }
            }
        }
        System.out.println(tail == n * (n - 1) / 2 ? "War" : "Peace");
    }
}
