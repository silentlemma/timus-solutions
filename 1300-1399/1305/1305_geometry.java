import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int minX = Integer.MAX_VALUE, maxX = Integer.MIN_VALUE;
        int minY = Integer.MAX_VALUE, maxY = Integer.MIN_VALUE;
        int minS = Integer.MAX_VALUE, maxS = Integer.MIN_VALUE;
        int minD = Integer.MAX_VALUE, maxD = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            in.nextToken();
            int x = (int)in.nval;
            in.nextToken();
            int y = (int)in.nval;
            minX = Math.min(minX, x);
            maxX = Math.max(maxX, x);
            minY = Math.min(minY, y);
            maxY = Math.max(maxY, y);
            minS = Math.min(minS, x + y);
            maxS = Math.max(maxS, x + y);
            minD = Math.min(minD, x - y);
            maxD = Math.max(maxD, x - y);
        }
        // the hull is cut out by eight lines, x, y, x + y and x - y each at
        // their extremes; going counterclockwise from the bottom edge, every
        // corner joins an axis line to a diagonal one
        int[][] corners = {
            {minS - minY, minY}, {maxD + minY, minY}, {maxX, maxX - maxD}, {maxX, maxS - maxX},
            {maxS - maxY, maxY}, {minD + maxY, maxY}, {minX, minX - minD}, {minX, minS - minX},
        };
        List<int[]> hull = new ArrayList<>();
        for (int[] p : corners) {
            if (hull.isEmpty() || !Arrays.equals(hull.get(hull.size() - 1), p))
                hull.add(p);
        }
        while (hull.size() > 1 && Arrays.equals(hull.get(0), hull.get(hull.size() - 1))) {
            hull.remove(hull.size() - 1);
        }
        // the sides left all point in different directions, so no corner is in
        // the middle of a straight side
        StringBuilder out = new StringBuilder();
        for (int[] p : hull)
            out.append(p[0]).append(' ').append(p[1]).append('\n');
        System.out.print(out);
    }
}
