import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static final int MINUTES = 60, FIRST_HOUR = 7, WITH_LEONID = 13, ALREADY_IN = 42;
    static int[][] place;
    static List<int[]> buses = new ArrayList<>();
    static int chosenStart, chosen;

    // whether a passenger waiting at src for dst takes the chosen bus: no bus
    // seen by Leonid serves the trip and comes to src sooner, or at the same
    // minute reaching dst sooner, or as soon with a smaller route
    static boolean picked(int src, int dst) {
        int[] here = place[chosen];
        if (here[src] < 0 || here[dst] < 0 || here[src] >= here[dst]) return false;
        int[] mine = {chosenStart + here[src], chosenStart + here[dst], chosen};
        for (int[] b : buses) {
            int start = b[0], route = b[1];
            int[] there = place[route];
            boolean serves = there[src] >= 0 && there[dst] >= 0 && there[src] < there[dst];
            if (start < 0 || !serves) continue;
            int[] other = {start + there[src], start + there[dst], route};
            for (int i = 0; i < other.length; i++) {
                if (other[i] != mine[i]) {
                    if (other[i] < mine[i]) return false;
                    break;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(text.toString(), " :");
        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
        List<List<Integer>> order = new ArrayList<>();
        place = new int[m][n + 1];
        for (int r = 0; r < m; r++) {
            java.util.Arrays.fill(place[r], -1);
            List<Integer> stops = new ArrayList<>();
            while (true) {
                int s = Integer.parseInt(st.nextToken());
                if (s == -1) break;
                place[r][s] = stops.size();
                stops.add(s);
            }
            order.add(stops);
        }
        int k = Integer.parseInt(st.nextToken());
        for (int i = 0; i < k; i++) {
            int hh = Integer.parseInt(st.nextToken()), mm = Integer.parseInt(st.nextToken());
            int route = Integer.parseInt(st.nextToken()) - 1;
            // the minute this bus left the first stop of its route
            buses.add(new int[] {(hh - FIRST_HOUR) * MINUTES + mm - place[route][1], route});
        }
        chosenStart = buses.get(k - 1)[0];
        chosen = buses.get(k - 1)[1];
        // buses not seen at stop 1 either come to a stop before it later than the
        // chosen bus, or need not run at all
        List<Integer> stops = order.get(chosen);
        int one = place[chosen][1], two = place[chosen][2];
        boolean leaveNew = false, stayNew = false, leaveOld = false, stayOld = false;
        for (int d = one + 1; d < stops.size(); d++) {
            boolean early = d < two;
            if (picked(1, stops.get(d))) {
                leaveNew |= early;
                stayNew |= !early;
            }
            for (int s = 0; s < one; s++) {
                if (picked(stops.get(s), stops.get(d))) {
                    leaveOld |= early;
                    stayOld |= !early;
                }
            }
        }
        // each group can all ride to a stop of one kind, so the counts are all or
        // nothing for the 13 who got on with Leonid and the 42 already inside
        int low = (leaveNew ? 0 : WITH_LEONID) + (leaveOld ? 0 : ALREADY_IN);
        int high = (stayNew ? WITH_LEONID : 0) + (stayOld ? ALREADY_IN : 0);
        System.out.println(low + " " + high);
    }
}
