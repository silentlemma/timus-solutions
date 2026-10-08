import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static final int MAX_COORD = 10, SIDE = MAX_COORD + 2;
    static final String LETTERS = "RTLB";
    static final int[] DX = {1, 0, -1, 0}, DY = {0, 1, 0, -1};

    // Breadth-first search from the lowest of the leftmost pixels; each line
    // names the neighbours seen for the first time.
    static void describe(boolean[][] black, int count, StringBuilder out) {
        int sx = 0, sy = 0;
        for (int x = MAX_COORD; x >= 1; x--) {
            for (int y = MAX_COORD; y >= 1; y--) {
                if (black[x][y]) {
                    sx = x;
                    sy = y;
                }
            }
        }
        int[] qx = new int[count], qy = new int[count];
        qx[0] = sx;
        qy[0] = sy;
        black[sx][sy] = false;
        int tail = 1;
        out.append(sx).append(' ').append(sy).append('\n');
        for (int head = 0; head < count; head++) {
            for (int d = 0; d < LETTERS.length(); d++) {
                int x = qx[head] + DX[d], y = qy[head] + DY[d];
                if (black[x][y]) {
                    black[x][y] = false;
                    qx[tail] = x;
                    qy[tail++] = y;
                    out.append(LETTERS.charAt(d));
                }
            }
            out.append(head + 1 < count ? ',' : '.').append('\n');
        }
    }

    // Replay the same search: the lines tell which pixels it adds.
    static void list(int sx, int sy, List<String> lines, StringBuilder out) {
        boolean[][] black = new boolean[SIDE][SIDE];
        List<int[]> queue = new ArrayList<>();
        queue.add(new int[] {sx, sy});
        black[sx][sy] = true;
        for (int head = 0; head < lines.size(); head++) {
            int[] p = queue.get(head);
            for (char c : lines.get(head).toCharArray()) {
                int d = LETTERS.indexOf(c);
                if (d >= 0) {
                    queue.add(new int[] {p[0] + DX[d], p[1] + DY[d]});
                    black[p[0] + DX[d]][p[1] + DY[d]] = true;
                }
            }
        }
        // the grid is scanned in the order of the list
        out.append(queue.size()).append('\n');
        for (int x = 1; x <= MAX_COORD; x++) {
            for (int y = 1; y <= MAX_COORD; y++) {
                if (black[x][y]) {
                    out.append(x).append(' ').append(y).append('\n');
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        List<String> tokens = new ArrayList<>();
        for (String line; (line = in.readLine()) != null;) {
            StringTokenizer st = new StringTokenizer(line);
            while (st.hasMoreTokens()) {
                tokens.add(st.nextToken());
            }
        }
        StringBuilder out = new StringBuilder();
        // only the description ends with a full stop
        if (tokens.get(tokens.size() - 1).endsWith(".")) {
            int sx = Integer.parseInt(tokens.get(0)), sy = Integer.parseInt(tokens.get(1));
            list(sx, sy, tokens.subList(2, tokens.size()), out);
        } else {
            boolean[][] black = new boolean[SIDE][SIDE];
            int count = Integer.parseInt(tokens.get(0));
            for (int i = 0; i < count; i++) {
                int x = Integer.parseInt(tokens.get(1 + 2 * i));
                black[x][Integer.parseInt(tokens.get(2 + 2 * i))] = true;
            }
            describe(black, count, out);
        }
        System.out.print(out);
    }
}
