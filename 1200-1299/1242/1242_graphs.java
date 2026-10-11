import java.io.*;
import java.util.*;

public class Main {
    // marks everyone reachable from the victims along one kind of link
    static void clear(List<Integer> start, List<List<Integer>> links, boolean[] cleared) {
        int[] stack = new int[links.size() + start.size()];
        int top = 0;
        for (int v : start)
            stack[top++] = v;
        boolean[] seen = new boolean[links.size()];
        while (top > 0) {
            int v = stack[--top];
            for (int u : links.get(v))
                if (!seen[u]) {
                    seen[u] = cleared[u] = true;
                    stack[top++] = u;
                }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line; (line = in.readLine()) != null;)
            all.append(line).append(' ');
        StringTokenizer st = new StringTokenizer(all.toString());
        int n = Integer.parseInt(st.nextToken());
        List<List<Integer>> parents = new ArrayList<>(), children = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            parents.add(new ArrayList<>());
            children.add(new ArrayList<>());
        }
        for (String word; !(word = st.nextToken()).equals("BLOOD");) {
            int child = Integer.parseInt(word), parent = Integer.parseInt(st.nextToken());
            parents.get(child).add(parent);
            children.get(parent).add(child);
        }
        boolean[] cleared = new boolean[n + 1];
        List<Integer> victims = new ArrayList<>();
        while (st.hasMoreTokens()) {
            int v = Integer.parseInt(st.nextToken());
            victims.add(v);
            cleared[v] = true;
        }
        // the werewolf spares its ancestors and descendants, so no ancestor and
        // no descendant of a victim can be the werewolf
        clear(victims, parents, cleared);
        clear(victims, children, cleared);
        StringBuilder out = new StringBuilder();
        for (int u = 1; u <= n; u++)
            if (!cleared[u])
                out.append(out.length() > 0 ? " " : "").append(u);
        System.out.println(out.length() > 0 ? out : "0");
    }
}
