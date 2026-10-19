import java.io.DataInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

public class Main {
    static final int FACES = 6;
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

    static List<List<Integer>> near;

    // grid steps from start to every crystal
    static int[] spread(int start) {
        int[] steps = new int[near.size()];
        Arrays.fill(steps, -1);
        steps[start] = 0;
        int[] queue = new int[near.size()];
        int size = 0;
        queue[size++] = start;
        for (int i = 0; i < size; i++) {
            for (int w : near.get(queue[i])) {
                if (steps[w] < 0) {
                    steps[w] = steps[queue[i]] + 1;
                    queue[size++] = w;
                }
            }
        }
        return steps;
    }

    public static void main(String[] args) throws IOException {
        int side = number();
        int n = number();
        int count = n * n * n;
        // crystals with the same rune touch: the crystals and their
        // contacts form the n x n x n grid, whatever the turns of the
        // crystals
        near = new ArrayList<>();
        for (int c = 0; c < count; c++) {
            near.add(new ArrayList<>());
        }
        Map<Integer, Integer> first = new HashMap<>();
        for (int c = 0; c < count; c++) {
            for (int f = 0; f < FACES; f++) {
                int rune = number();
                if (rune == 0) {
                    continue;
                }
                Integer other = first.putIfAbsent(rune, c);
                if (other != null) {
                    near.get(c).add(other);
                    near.get(other).add(c);
                }
            }
        }
        // a corner touches the fewest crystals; the three corners n - 1
        // steps away lie along the edges from it, and the steps to a corner
        // and to one of them give the coordinate along that edge
        int corner = 0;
        for (int c = 1; c < count; c++) {
            if (near.get(c).size() < near.get(corner).size()) {
                corner = c;
            }
        }
        int[] origin = spread(corner);
        List<int[]> axes = new ArrayList<>();
        for (int c = 0; c < count; c++) {
            if (origin[c] == n - 1 && near.get(c).size() == near.get(corner).size()) {
                axes.add(spread(c));
            }
        }
        int m = number();
        StringBuilder out = new StringBuilder();
        for (int k = 0; k < m; k++) {
            int a = number() - 1;
            int b = number() - 1;
            double square = 0;
            for (int[] far : axes) {
                int x = (origin[a] - far[a] + n - 1) / 2;
                int y = (origin[b] - far[b] + n - 1) / 2;
                square += (double) (x - y) * (x - y);
            }
            out.append(String.format(Locale.US, "%.7f", side * Math.sqrt(square))).append('\n');
        }
        System.out.print(out);
    }
}
