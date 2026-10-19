import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    private static final int HEALTHY = 3;
    private static final int TEAM_SIZE = 4;
    private static final int TRIPLE_SIZE = TEAM_SIZE - 1;

    private static final class FastScanner {
        private final BufferedInputStream in = new BufferedInputStream(System.in);

        String next() throws IOException {
            StringBuilder token = new StringBuilder();
            int current;
            do {
                current = in.read();
            } while (current <= ' ' && current != -1);
            while (current > ' ') {
                token.append((char) current);
                current = in.read();
            }
            return token.toString();
        }

        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
    }

    private static int find(int[] parent, int player) {
        while (parent[player] != player) {
            parent[player] = parent[parent[player]];
            player = parent[player];
        }
        return player;
    }

    private static void unite(int[] parent, int first, int second) {
        first = find(parent, first);
        second = find(parent, second);
        if (first > second) {
            int temporary = first;
            first = second;
            second = temporary;
        }
        parent[second] = first;
    }

    private static String solve() throws IOException {
        FastScanner in = new FastScanner();
        int n = in.nextInt();
        String[] names = new String[n];
        Map<String, Integer> index = new HashMap<>();
        int[] parent = new int[n];
        int[] health = new int[n];
        for (int player = 0; player < n; player++) {
            names[player] = in.next();
            index.put(names[player], player);
            parent[player] = player;
            health[player] = HEALTHY;
        }
        int m = in.nextInt();
        for (int event = 0; event < m; event++) {
            int actor = index.get(in.next());
            String action = in.next();
            if (health[actor] < 2) {
                return "FAKE\n";
            }
            if (action.equals("HIT")) {
                int target = index.get(in.next());
                in.next();
                int damage = in.next().equals("HEAD") ? 2 : 1;
                health[target] = Math.max(0, health[target] - damage);
            } else if (action.equals("USES")) {
                in.next();
                health[actor] = HEALTHY;
            } else {
                int target = index.get(in.next());
                if (health[target] != 1) {
                    return "FAKE\n";
                }
                health[target] = 2;
                unite(parent, actor, target);
            }
        }
        List<List<Integer>> groups = new ArrayList<>();
        List<List<List<Integer>>> buckets = new ArrayList<>();
        for (int player = 0; player < n; player++) {
            groups.add(new ArrayList<>());
        }
        for (int size = 0; size <= TEAM_SIZE; size++) {
            buckets.add(new ArrayList<>());
        }
        for (int player = 0; player < n; player++) {
            groups.get(find(parent, player)).add(player);
        }
        for (List<Integer> group : groups) {
            if (group.size() > TEAM_SIZE) {
                return "FAKE\n";
            }
            if (!group.isEmpty()) {
                buckets.get(group.size()).add(group);
            }
        }
        List<List<Integer>> singles = buckets.get(1);
        List<List<Integer>> triples = buckets.get(TRIPLE_SIZE);
        List<List<Integer>> pairs = buckets.get(2);
        if (singles.size() < triples.size()) {
            return "FAKE\n";
        }
        List<List<Integer>> teams = new ArrayList<>(buckets.get(TEAM_SIZE));
        int single = 0;
        for (List<Integer> group : triples) {
            List<Integer> team = new ArrayList<>(group);
            team.add(singles.get(single++).get(0));
            teams.add(team);
        }
        int pair = 0;
        while (pair + 1 < pairs.size()) {
            List<Integer> team = new ArrayList<>(pairs.get(pair));
            team.addAll(pairs.get(pair + 1));
            teams.add(team);
            pair += 2;
        }
        if (pair < pairs.size()) {
            List<Integer> team = new ArrayList<>(pairs.get(pair));
            team.add(singles.get(single++).get(0));
            team.add(singles.get(single++).get(0));
            teams.add(team);
        }
        while (single < singles.size()) {
            List<Integer> team = new ArrayList<>();
            for (int member = 0; member < TEAM_SIZE; member++) {
                team.add(singles.get(single++).get(0));
            }
            teams.add(team);
        }
        StringBuilder out = new StringBuilder("CORRECT\n");
        for (List<Integer> team : teams) {
            for (int member = 0; member < TEAM_SIZE; member++) {
                if (member > 0) {
                    out.append(' ');
                }
                out.append(names[team.get(member)]);
            }
            out.append('\n');
        }
        return out.toString();
    }

    public static void main(String[] args) throws IOException {
        System.out.print(solve());
    }
}
