import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Main {
    // beacons and control points lie on the grid from 1 to SIDE
    static final int SIDE = 200;

    // the numbers in a line, whatever separates them
    static List<Integer> numbers(String line) {
        List<Integer> out = new ArrayList<>();
        for (int k = 0; k < line.length();) {
            if (!Character.isDigit(line.charAt(k))) {
                k++;
                continue;
            }
            int v = 0;
            for (; k < line.length() && Character.isDigit(line.charAt(k)); k++) {
                v = v * 10 + (line.charAt(k) - '0');
            }
            out.add(v);
        }
        return out;
    }

    // the cells at distance exactly r from (x, y) in the max metric
    static List<int[]> ring(int x, int y, int r) {
        List<int[]> cells = new ArrayList<>();
        if (r == 0) {
            cells.add(new int[] {x, y});
            return cells;
        }
        for (int d = -r; d <= r; d++) {
            cells.add(new int[] {x + d, y - r});
            cells.add(new int[] {x + d, y + r});
        }
        for (int d = -r + 1; d < r; d++) {
            cells.add(new int[] {x - r, y + d});
            cells.add(new int[] {x + r, y + d});
        }
        return cells;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> header = new ArrayList<>();
        String head;
        while (header.isEmpty() && (head = in.readLine()) != null) {
            header = numbers(head);
        }
        if (header.isEmpty()) {
            return;
        }
        int m = header.get(0);
        Map<Integer, List<int[]>> seen = new TreeMap<>();
        for (int i = 0; i < m;) {
            String line = in.readLine();
            if (line == null) {
                break;
            }
            List<Integer> nums = numbers(line);
            if (nums.isEmpty()) {
                continue;
            }
            i++;
            for (int k = 2; k + 1 < nums.size(); k += 2) {
                seen.computeIfAbsent(nums.get(k), id -> new ArrayList<>())
                    .add(new int[] {nums.get(0), nums.get(1), nums.get(k + 1)});
            }
        }
        StringBuilder out = new StringBuilder();
        for (Map.Entry<Integer, List<int[]>> e : seen.entrySet()) {
            List<int[]> list = e.getValue();
            int[] first = list.get(0);
            List<int[]> places = new ArrayList<>();
            for (int[] c : ring(first[0], first[1], first[2])) {
                if (c[0] < 1 || c[0] > SIDE || c[1] < 1 || c[1] > SIDE) {
                    continue;
                }
                boolean fits = true;
                for (int[] q : list) {
                    fits = fits && Math.max(Math.abs(c[0] - q[0]), Math.abs(c[1] - q[1])) == q[2];
                }
                if (fits) {
                    places.add(c);
                }
            }
            out.append(e.getKey()).append(':');
            if (places.size() == 1) {
                out.append(places.get(0)[0]).append(',').append(places.get(0)[1]);
            } else {
                out.append("UNKNOWN");
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
