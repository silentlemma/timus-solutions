import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    static final int COLOR_COUNT = 3, TRIANGLE_SIZE = 3;
    public static void main(String[] args) throws Exception {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine().trim());
        String text = input.readLine().trim();
        int[] color = new int[n], left = new int[n], right = new int[n];
        boolean[] alive = new boolean[n];
        int[] counts = new int[COLOR_COUNT], pending = new int[n + 2 * n];
        int head = 0, tail = 0;
        for (int v = 0; v < n; v++) {
            color[v] = text.charAt(v) == 'R' ? 0 : text.charAt(v) == 'G' ? 1 : 2;
            counts[color[v]]++;
            left[v] = (v + n - 1) % n;
            right[v] = (v + 1) % n;
            alive[v] = true;
        }
        for (int v = 0; v < n; v++) {
            if (color[left[v]] != color[right[v]])
                pending[tail++] = v;
        }
        StringBuilder output = new StringBuilder();
        output.append(n - TRIANGLE_SIZE).append('\n');
        int remaining = n;
        while (remaining > TRIANGLE_SIZE) {
            if (counts[0] == 1 || counts[1] == 1 || counts[2] == 1) {
                int anchor = 0;
                while (!alive[anchor] || counts[color[anchor]] != 1)
                    anchor++;
                for (int v = right[right[anchor]]; right[v] != anchor; v = right[v]) {
                    output.append(anchor + 1).append(' ').append(v + 1).append('\n');
                }
                break;
            }
            int v = pending[head++];
            if (!alive[v] || color[left[v]] == color[right[v]])
                continue;
            int before = left[v], after = right[v];
            output.append(before + 1).append(' ').append(after + 1).append('\n');
            alive[v] = false;
            right[before] = after;
            left[after] = before;
            counts[color[v]]--;
            remaining--;
            // A cut changes only two neighbours, so the queue needs at most 3*n entries.
            pending[tail++] = before;
            pending[tail++] = after;
        }
        System.out.print(output);
    }
}
