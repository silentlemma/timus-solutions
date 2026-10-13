import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static int[] parent;

    static int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    static void union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b)
            parent[a] = b;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        List<String> pic = new ArrayList<>();
        for (String line = in.readLine(); line != null; line = in.readLine())
            pic.add(line);
        while (!pic.isEmpty() && pic.get(pic.size() - 1).isEmpty())
            pic.remove(pic.size() - 1);
        int h = pic.size(), w = 0;
        for (String row : pic)
            w = Math.max(w, row.length());
        // walls run along the middle lines of the cells, so the four quarters
        // around a corner of the grid always meet: the corners are the places
        // an agent can be, and a cell joins some of its four corners
        int side = w + 1;
        parent = new int[(h + 1) * side];
        for (int i = 0; i < parent.length; i++)
            parent[i] = i;
        List<Integer> secrets = new ArrayList<>(); // top-left corners in reading order
        for (int r = 0; r < h; r++) {
            String row = pic.get(r);
            int top = r * side, bottom = (r + 1) * side;
            List<Integer> inRow = new ArrayList<>();
            for (int c = 0; c < row.length(); c++) {
                char ch = row.charAt(c);
                if (ch == '.') {
                    union(top + c, top + c + 1);
                    union(top + c, bottom + c);
                    union(top + c, bottom + c + 1);
                } else if (ch == '-') { // keeps the upper and the lower pair apart
                    union(top + c, top + c + 1);
                    union(bottom + c, bottom + c + 1);
                } else if (ch == '|') { // keeps the left and the right pair apart
                    union(top + c, bottom + c);
                    union(top + c + 1, bottom + c + 1);
                } else if (ch == '#') {
                    inRow.add(top + c);
                }
            }
            // numbered from the right within a row
            for (int i = inRow.size() - 1; i >= 0; i--)
                secrets.add(inRow.get(i));
        }
        // an agent may not pass through a secret, so two secrets are joined when
        // some corner of one shares a region with some corner of the other
        int k = secrets.size();
        int[][] regions = new int[k][];
        for (int i = 0; i < k; i++) {
            int v = secrets.get(i);
            regions[i] = new int[] {find(v), find(v + 1), find(v + side), find(v + side + 1)};
        }
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < k; j++) {
                boolean shared = false;
                for (int x : regions[i])
                    for (int y : regions[j])
                        shared |= x == y;
                out.append(shared ? '1' : '0');
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
