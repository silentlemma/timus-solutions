import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    static StringBuilder out = new StringBuilder();
    static int count = 0;

    // a convex face is cut into triangles by diagonals from its first vertex,
    // as the first and the last of its sides already exist
    static void fan(List<Integer> face) {
        for (int i = 2; i + 1 < face.size(); i++) {
            out.append(face.get(0)).append(' ').append(face.get(i)).append('\n');
            count++;
        }
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int k = (int)in.nval;
        List<List<Integer>> ending = new ArrayList<>(); // cuts u-v with u < v, kept at v
        for (int v = 0; v <= n; v++)
            ending.add(new ArrayList<>());
        for (int i = 0; i < k; i++) {
            in.nextToken();
            int a = (int)in.nval;
            in.nextToken();
            int b = (int)in.nval;
            ending.get(Math.max(a, b)).add(Math.min(a, b));
        }
        // walk the vertices in order: a cut u-v closes the face formed by u,
        // the vertices still stacked above it, and v; nearer u first
        List<Integer> stack = new ArrayList<>();
        for (int v = 1; v <= n; v++) {
            stack.add(v);
            List<Integer> starts = ending.get(v);
            starts.sort(Collections.reverseOrder());
            for (int u : starts) {
                stack.remove(stack.size() - 1);
                int start = stack.size() - 1;
                while (stack.get(start) != u)
                    start--;
                List<Integer> face = new ArrayList<>(stack.subList(start, stack.size()));
                face.add(v);
                fan(face);
                stack.subList(start + 1, stack.size()).clear();
                stack.add(v);
            }
        }
        fan(stack); // the last face, closed by the side n-1
        System.out.print(count + "\n" + out);
    }
}
