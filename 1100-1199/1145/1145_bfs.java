import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int cols;
    static boolean[] free;

    // breadth-first search; the free cells form a tree, so distances along
    // it are the only paths; returns the last cell reached and its distance
    static int[] farthest(int start) {
        int[] dist = new int[free.length];
        Arrays.fill(dist, -1);
        int[] queue = new int[free.length];
        int[] steps = {1, -1, cols, -cols};
        int head = 0, tail = 0;
        queue[tail++] = start;
        dist[start] = 0;
        while (head < tail) {
            int cur = queue[head++];
            for (int s : steps) {
                int next = cur + s;
                if (free[next] && dist[next] < 0) {
                    dist[next] = dist[cur] + 1;
                    queue[tail++] = next;
                }
            }
        }
        int last = queue[tail - 1];
        return new int[] {last, dist[last]};
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer first = new StringTokenizer(in.readLine());
        int width = Integer.parseInt(first.nextToken());
        int height = Integer.parseInt(first.nextToken());
        // a border of walls around the maze keeps every neighbour in range
        cols = width + 2;
        free = new boolean[(height + 2) * cols];
        int start = -1;
        for (int r = 1; r <= height; r++) {
            String row = in.readLine().trim();
            for (int c = 1; c <= width; c++) {
                if (row.charAt(c - 1) == '.') {
                    free[r * cols + c] = true;
                    if (start < 0) {
                        start = r * cols + c;
                    }
                }
            }
        }
        // the farthest cell from any cell is an end of a longest path
        int end = farthest(start)[0];
        System.out.println(farthest(end)[1]);
    }
}
