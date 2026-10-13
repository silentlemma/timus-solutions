import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Main {
    static final int POINTS = 4;
    static final double PAD = 1.0; // width given to a rectangle squeezed onto one line

    static long[] px = new long[POINTS], py = new long[POINTS];

    // the bounding box with sides along (dx, dy) if every point is on its border, or null
    static String frame(long dx, long dy) {
        long[] us = new long[POINTS], vs = new long[POINTS];
        long loU = Long.MAX_VALUE, hiU = Long.MIN_VALUE, loV = Long.MAX_VALUE, hiV = Long.MIN_VALUE;
        for (int i = 0; i < POINTS; i++) {
            us[i] = px[i] * dx + py[i] * dy; // exact integers in the turned frame
            vs[i] = py[i] * dx - px[i] * dy;
            loU = Math.min(loU, us[i]);
            hiU = Math.max(hiU, us[i]);
            loV = Math.min(loV, vs[i]);
            hiV = Math.max(hiV, vs[i]);
        }
        for (int i = 0; i < POINTS; i++)
            if (us[i] != loU && us[i] != hiU && vs[i] != loV && vs[i] != hiV)
                return null;
        double norm = Math.hypot(dx, dy);
        // back to real lengths; a flat box gets some width, still holding every point on a side
        double lu = loU / norm, hu = hiU / norm, lv = loV / norm, hv = hiV / norm;
        if (hiU == loU)
            hu += PAD;
        if (hiV == loV)
            hv += PAD;
        double ex = dx / norm, ey = dy / norm;
        double[] cu = {lu, hu, hu, lu}, cv = {lv, lv, hv, hv};
        StringBuilder out = new StringBuilder("+");
        for (int i = 0; i < POINTS; i++)
            out.append(String.format(Locale.US, " %.9f %.9f", cu[i] * ex - cv[i] * ey,
                                     cu[i] * ey + cv[i] * ex));
        return out.toString();
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        StringBuilder all = new StringBuilder();
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < POINTS; i++) {
                in.nextToken();
                px[i] = (long)in.nval;
                in.nextToken();
                py[i] = (long)in.nval;
            }
            // the valid turns form a closed set whose ends make two points tie,
            // so the directions between points are enough to try
            List<long[]> dirs = new ArrayList<>();
            for (int i = 0; i < POINTS; i++)
                for (int j = i + 1; j < POINTS; j++)
                    if (px[i] != px[j] || py[i] != py[j])
                        dirs.add(new long[] {px[j] - px[i], py[j] - py[i]});
            if (dirs.isEmpty())
                dirs.add(new long[] {1, 0});
            String line = "-";
            for (long[] d : dirs) {
                String box = frame(d[0], d[1]);
                if (box != null) {
                    line = box;
                    break;
                }
            }
            all.append(line).append('\n');
        }
        System.out.print(all);
    }
}
