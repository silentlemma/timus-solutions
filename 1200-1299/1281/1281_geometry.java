import java.io.*;
import java.util.*;

public class Main {
    static double[][][] rivers;
    static List<List<Integer>> tributaries = new ArrayList<>();

    static double cross(double[] o, double[] a, double[] b) {
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
    }

    // area of the convex hull, by the monotone chain and the shoelace
    static double hullArea(List<double[]> pts) {
        pts.sort((a, b) -> a[0] != b[0] ? Double.compare(a[0], b[0]) : Double.compare(a[1], b[1]));
        List<double[]> h = new ArrayList<>();
        for (double[] p : pts) {
            while (h.size() >= 2 && cross(h.get(h.size() - 2), h.get(h.size() - 1), p) <= 0)
                h.remove(h.size() - 1);
            h.add(p);
        }
        for (int i = pts.size() - 2, t = h.size() + 1; i >= 0; i--) {
            while (h.size() >= t &&
                   cross(h.get(h.size() - 2), h.get(h.size() - 1), pts.get(i)) <= 0)
                h.remove(h.size() - 1);
            h.add(pts.get(i));
        }
        double area = 0;
        for (int i = 0; i + 1 < h.size(); i++)
            area += h.get(i)[0] * h.get(i + 1)[1] - h.get(i)[1] * h.get(i + 1)[0];
        return Math.abs(area) / 2;
    }

    static void basin(int i, List<double[]> out) {
        out.addAll(Arrays.asList(rivers[i]));
        for (int t : tributaries.get(i))
            basin(t, out);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line; (line = reader.readLine()) != null;)
            all.append(line).append(' ');
        StringTokenizer in = new StringTokenizer(all.toString());
        int n = Integer.parseInt(in.nextToken());
        rivers = new double[n][][];
        for (int i = 0; i < n; i++) {
            int k = Integer.parseInt(in.nextToken());
            rivers[i] = new double[k][];
            for (int j = 0; j < k; j++)
                rivers[i][j] = new double[] {Double.parseDouble(in.nextToken()),
                                             Double.parseDouble(in.nextToken())};
            tributaries.add(new ArrayList<>());
        }
        // a river is a tributary of the one whose inner vertex is its mouth
        Map<String, Integer> owner = new HashMap<>();
        for (int i = 0; i < n; i++)
            for (int j = 1; j + 1 < rivers[i].length; j++)
                owner.put(rivers[i][j][0] + " " + rivers[i][j][1], i);
        for (int i = 0; i < n; i++) {
            double[] mouth = rivers[i][rivers[i].length - 1];
            Integer o = owner.get(mouth[0] + " " + mouth[1]);
            if (o != null && o != i)
                tributaries.get(o).add(i);
        }
        double best = 0;
        for (int i = 0; i < n; i++) {
            List<double[]> pts = new ArrayList<>();
            basin(i, pts);
            best = Math.max(best, hullArea(pts));
        }
        System.out.println(String.format(Locale.ROOT, "%.2f", best));
    }
}
