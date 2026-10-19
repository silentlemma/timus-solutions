import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static final int SEATS = 4; // compartment seats in a block
    static final int SIDES = 2; // side seats in a block

    static int[] parent;

    static int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    static int f2;
    static int f3;
    static int f4;

    // can the fillers fill blocks with c4, c3, c2 free compartment seats (and
    // some with 1)? fours need a 4, threes take a 3 first and then a 4, twos
    // take what is left of the 2s, 3s and 4s
    static boolean fits(int c4, int c3, int c2) {
        if (f4 > c4 || f3 > c3 + c4 - f4) {
            return false;
        }
        int late = Math.max(0, f3 - c3); // threes in blocks with 4 free seats
        return f2 <= c2 + (c3 - f3 + late) + 2 * (c4 - f4 - late);
    }

    static List<Integer> pop(List<List<Integer>> list) {
        return list.remove(list.size() - 1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(text.toString());
        int n = Integer.parseInt(st.nextToken());
        String wish = st.nextToken();
        int m = Integer.parseInt(st.nextToken());
        int people = (SEATS + SIDES) * n;
        parent = new int[people];
        for (int i = 0; i < people; i++) {
            parent[i] = i;
        }
        for (int k = 0; k < m; k++) {
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            parent[find(a)] = find(b);
        }
        List<List<Integer>> members = new ArrayList<>();
        for (int p = 0; p < people; p++) {
            members.add(new ArrayList<>());
        }
        for (int p = 0; p < people; p++) {
            members.get(find(p)).add(p + 1);
        }
        // a group of friends wants a compartment seats and b side seats; a
        // block holds one group with b = 2, or two groups with b = 1, and
        // groups with b = 0 fill the compartment seats left: kind[b][a]
        List<List<List<List<Integer>>>> kind = new ArrayList<>();
        for (int b = 0; b <= SIDES; b++) {
            List<List<List<Integer>>> row = new ArrayList<>();
            for (int a = 0; a <= SEATS; a++) {
                row.add(new ArrayList<>());
            }
            kind.add(row);
        }
        for (List<Integer> g : members) {
            if (g.isEmpty()) {
                continue;
            }
            int a = 0;
            for (int p : g) {
                a += wish.charAt(p - 1) == '1' ? 1 : 0;
            }
            kind.get(g.size() - a).get(a).add(g);
        }
        List<List<List<Integer>>> fillers = kind.get(0);
        List<List<List<Integer>>> halves = kind.get(1);
        List<List<List<Integer>>> wholes = kind.get(SIDES);
        int s0 = halves.get(0).size();
        int s1 = halves.get(1).size();
        int s2 = halves.get(2).size();
        int s3 = halves.get(SEATS - 1).size();
        int s4 = halves.get(SEATS).size();
        int t0 = wholes.get(0).size();
        int t1 = wholes.get(1).size();
        int t2 = wholes.get(2).size();
        f2 = fillers.get(2).size();
        f3 = fillers.get(SEATS - 1).size();
        f4 = fillers.get(SEATS).size();
        // two halves with a1 and a2 leave 4 - a1 - a2 free seats; merging the
        // free seats of two blocks never hurts, so threes pair with ones when
        // they can, and two (0, 2) pairs would rather be (2, 2) and (0, 0)
        int x31 = Math.min(s3, s1);
        int x30 = s3 - x31;
        int ones = s1 - x31;
        int zeros = s0 - s4 - x30;
        // the seats of the two halves and how many such pairs
        int[][] plan = null;
        for (int x20 = 0; x20 <= 1 && plan == null; x20++) {
            for (int x21 = 0; x21 <= Math.min(s2 - x20, ones) && plan == null; x21++) {
                // with x11 pairs (1, 1) the zeros left pair up as base + 2 x11
                int base = zeros - x20 - ones + x21;
                if ((s2 - x21 - x20) % 2 != 0 || base % 2 != 0) {
                    continue;
                }
                // x11 must leave both kinds of pairs possible and give the
                // fours and the threes their blocks; the room for twos rises
                // until the free threes run short of threes, then falls
                int low = Math.max(Math.max(0, -base / 2), f4 - t0 - base / 2);
                int high = Math.min((ones - x21) / 2,
                        t0 + t1 + ones - x21 + base / 2 - f3 - f4);
                int peak = Math.min(Math.max((t1 + ones - x21 - f3) / 2, low), high);
                for (int x11 = peak - 1; x11 <= peak + 1; x11++) {
                    int x10 = ones - x21 - 2 * x11;
                    int x00 = base / 2 + x11;
                    if (low <= x11 && x11 <= high && fits(t0 + x00, t1 + x10, t2 + x20 + x11)) {
                        plan = new int[][] {
                            {SEATS, 0, s4}, {SEATS - 1, 1, x31}, {SEATS - 1, 0, x30},
                            {2, 2, (s2 - x21 - x20) / 2}, {2, 1, x21}, {2, 0, x20},
                            {1, 1, x11}, {1, 0, x10}, {0, 0, x00}};
                        break;
                    }
                }
            }
        }
        List<List<Integer>> blocks = new ArrayList<>();
        List<Integer> free = new ArrayList<>(); // free compartment seats of each block
        for (int a = 0; a <= SEATS; a++) {
            for (List<Integer> g : wholes.get(a)) {
                blocks.add(g);
                free.add(SEATS - a);
            }
        }
        for (int[] p : plan) {
            for (int k = 0; k < p[2]; k++) {
                List<Integer> g = new ArrayList<>(pop(halves.get(p[0])));
                g.addAll(pop(halves.get(p[1])));
                blocks.add(g);
                free.add(SEATS - p[0] - p[1]);
            }
        }
        // the fillers, largest first, as the check above assumes
        List<List<Integer>> open = new ArrayList<>();
        for (int c = 0; c <= SEATS; c++) {
            open.add(new ArrayList<>());
        }
        for (int i = 0; i < blocks.size(); i++) {
            open.get(free.get(i)).add(i);
        }
        for (int size = SEATS; size >= 1; size--) {
            for (List<Integer> g : fillers.get(size)) {
                int at = size;
                while (open.get(at).isEmpty()) {
                    at++;
                }
                List<Integer> bucket = open.get(at);
                int i = bucket.remove(bucket.size() - 1);
                blocks.get(i).addAll(g);
                open.get(at - size).add(i);
            }
        }
        StringBuilder out = new StringBuilder();
        for (List<Integer> b : blocks) {
            for (int k = 0; k < b.size(); k++) {
                out.append(k > 0 ? " " : "").append(b.get(k));
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
