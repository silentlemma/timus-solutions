import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static final int SOUTH = 0, NORTH = 1, WEST = 2, EAST = 3; // also the order cars prefer
    static final int SIDES = 4;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer head = new StringTokenizer(in.readLine());
        int w = Integer.parseInt(head.nextToken()), h = Integer.parseInt(head.nextToken());
        int width = w + 2;
        // the plan with a frame of buildings, as one flat array
        char[][] rows = new char[h][];
        boolean[] road = new boolean[width * (h + 2)];
        int count = 0;
        for (int r = 0; r < h; r++) {
            String line = in.readLine();
            rows[r] = Arrays.copyOf((line == null ? "" : line).toCharArray(), w);
            for (int c = 0; c < w; c++) {
                road[(r + 1) * width + c + 1] = rows[r][c] == '#' || rows[r][c] == 'o';
                if (rows[r][c] == 'o')
                    count++;
            }
        }
        // control points numbered from the bottom row up, left to right
        int[] points = new int[count];
        int k = 0;
        for (int r = h - 1; r >= 0; r--) {
            for (int c = 0; c < w; c++) {
                if (rows[r][c] == 'o')
                    points[k++] = (r + 1) * width + c + 1;
            }
        }
        int[] steps = {width, -width, -1, 1}; // south, north, west, east
        StringBuilder restText = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine())
            restText.append(line).append(' ');
        StringTokenizer rest = new StringTokenizer(restText.toString());
        int m = rest.hasMoreTokens() ? Integer.parseInt(rest.nextToken()) : 0;
        int[] dist = new int[road.length], side = new int[road.length],
              order = new int[road.length];
        StringBuilder out = new StringBuilder();
        for (int number = 1; number <= m; number++) {
            int goal = points[Integer.parseInt(rest.nextToken()) - 1];
            Arrays.fill(dist, -1);
            dist[goal] = 0;
            int size = 0;
            order[size++] = goal;
            for (int i = 0; i < size; i++) {
                int cell = order[i];
                for (int step : steps) {
                    int near = cell + step;
                    if (road[near] && dist[near] < 0) {
                        dist[near] = dist[cell] + 1;
                        order[size++] = near;
                    }
                }
            }
            // every cell inherits the side its car arrives from from the cell it
            // moves to; cells one step away arrive straight from their own side
            for (int i = 1; i < size; i++) {
                int cell = order[i];
                for (int s = 0; s < SIDES; s++) {
                    int near = cell + steps[s];
                    if (dist[near] == dist[cell] - 1) {
                        // stepping in one direction onto the goal arrives from the opposite side
                        side[cell] = near != goal ? side[near] : s ^ 1;
                        break;
                    }
                }
            }
            int[] counts = new int[SIDES];
            for (int p : points) {
                if (p != goal && dist[p] > 0)
                    counts[side[p]]++;
            }
            out.append("Experiment #").append(number).append(": North: ").append(counts[NORTH]);
            out.append(", South: ").append(counts[SOUTH]).append(", East: ").append(counts[EAST]);
            out.append(", West: ").append(counts[WEST]).append('\n');
        }
        System.out.print(out);
    }
}
