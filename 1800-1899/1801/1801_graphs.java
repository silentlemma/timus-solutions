import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens = new StringTokenizer("");

    static String next() throws IOException {
        while (!tokens.hasMoreTokens()) tokens = new StringTokenizer(in.readLine());
        return tokens.nextToken();
    }

    static int groups;
    static int[] pot, party, colour, atPot, atParty;

    static void paint(int e, int c) {
        colour[e] = c;
        atPot[pot[e] * groups + c] = e;
        atParty[party[e] * groups + c] = e;
    }

    public static void main(String[] args) throws IOException {
        groups = Integer.parseInt(next());
        int pots = Integer.parseInt(next()), total = groups * pots;
        // each team is an edge from its pot to its party; a colouring of the
        // edges with one colour per group, never repeated at a vertex, is an
        // answer
        String[] team = new String[total];
        pot = new int[total];
        party = new int[total];
        Map<String, Integer> partyId = new HashMap<>();
        List<Integer> size = new ArrayList<>();
        for (int e = 0; e < total; e++) {
            team[e] = next();
            String name = next();
            Integer id = partyId.get(name);
            if (id == null) {
                id = size.size();
                partyId.put(name, id);
                size.add(0);
            }
            pot[e] = e / groups;
            party[e] = id;
            size.set(id, size.get(id) + 1);
        }
        for (int s : size) {
            if (s > groups) {
                System.out.println("No");
                return;
            }
        }
        // atPot[u * groups + c], atParty[v * groups + c]: the edge of colour c
        atPot = new int[pots * groups];
        atParty = new int[size.size() * groups];
        Arrays.fill(atPot, -1);
        Arrays.fill(atParty, -1);
        colour = new int[total];
        int[] path = new int[total];
        for (int e = 0; e < total; e++) {
            int u = pot[e], v = party[e], a = 0, b = 0;
            while (atPot[u * groups + a] != -1) a++;
            while (atParty[v * groups + b] != -1) b++;
            // colour a is free at the pot and b at the party; swap a and b
            // along the path from the pot that alternates b and a, which
            // cannot reach the party, and b becomes free at both ends
            int length = 0, at = u, want = b;
            boolean onPot = true;
            while (a != b) {
                int f = onPot ? atPot[at * groups + want] : atParty[at * groups + want];
                if (f == -1) break;
                path[length++] = f;
                at = onPot ? party[f] : pot[f];
                onPot = !onPot;
                want = a + b - want;
            }
            for (int i = 0; i < length; i++) {
                int f = path[i];
                atPot[pot[f] * groups + colour[f]] = -1;
                atParty[party[f] * groups + colour[f]] = -1;
            }
            for (int i = 0; i < length; i++) paint(path[i], a + b - colour[path[i]]);
            paint(e, b);
        }
        String[][] members = new String[groups][pots];
        for (int e = 0; e < total; e++) members[colour[e]][pot[e]] = team[e];
        StringBuilder out = new StringBuilder("Yes\n");
        for (String[] group : members) {
            out.append('\n');
            for (String name : group) out.append(name).append('\n');
        }
        System.out.print(out);
    }
}
