import java.io.*;
import java.util.*;

public class Main {
    static final int SIGNAL_DIGITS = 6; // signal values are read in millionths
    static final int FACTOR_DIGITS = 3; // A has at most three decimals
    static final long SIGNAL = 1000000, FACTOR = 1000;
    static final long WALL = 95, LOW = 35;
    static final int CHANNELS = 2;

    // a non-negative decimal as an exact multiple of 1 / 10^digits
    static long scaled(String token, int digits) {
        int dot = token.indexOf('.');
        String whole = dot < 0 ? token : token.substring(0, dot);
        String frac = dot < 0 ? "" : token.substring(dot + 1);
        frac = (frac + "000000").substring(0, digits);
        long scale = 1;
        for (int i = 0; i < digits; i++)
            scale *= 10;
        return Long.parseLong("0" + whole) * scale + Long.parseLong(frac);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line; (line = reader.readLine()) != null;)
            all.append(line).append(' ');
        StringTokenizer in = new StringTokenizer(all.toString());
        int n = Integer.parseInt(in.nextToken()), d = Integer.parseInt(in.nextToken());
        int[] start = new int[CHANNELS], stop = new int[CHANNELS], level = new int[CHANNELS];
        for (int c = 0; c < CHANNELS; c++) {
            start[c] = Integer.parseInt(in.nextToken());
            stop[c] = Integer.parseInt(in.nextToken());
            level[c] = Integer.parseInt(in.nextToken());
        }
        long a = scaled(in.nextToken(), FACTOR_DIGITS);
        long[] raw = new long[n];
        for (int i = 0; i < n; i++)
            raw[i] = scaled(in.nextToken(), SIGNAL_DIGITS);
        long unit = SIGNAL * FACTOR;
        StringBuilder out = new StringBuilder();
        // the front wall: the first value of 95 or more after a value of 35 or less
        int surface = -1;
        boolean low = false;
        for (int i = 0; i < n && surface < 0; i++) {
            if (low && raw[i] >= WALL * SIGNAL)
                surface = i;
            low = low || raw[i] <= LOW * SIGNAL;
        }
        if (surface < 0) {
            System.out.println("No surface.");
            return;
        }
        out.append("Surface found at ").append(surface + 1).append(".\n");
        // after the wall every value is multiplied by 1 + (m - f) A, here in
        // units of 1 / (SIGNAL * FACTOR)
        long[] value = new long[n];
        for (int i = 0; i < n; i++)
            value[i] = raw[i] * (i <= surface ? FACTOR : FACTOR + (i - surface) * a);
        int bottom = -1;
        low = false;
        for (int i = surface + 1; i < n && bottom < 0; i++) {
            if (low && i - surface >= d && value[i] >= WALL * unit)
                bottom = i;
            low = low || value[i] <= LOW * unit;
        }
        out.append(bottom < 0 ? "No bottom.\n" : "Bottom found at " + (bottom - surface) + ".\n");
        int end = bottom >= 0 ? bottom - 1 : n - 1;
        for (int c = 0; c < CHANNELS; c++) {
            int lo = surface + start[c], hi = Math.min(surface + stop[c], end);
            if (lo > hi) {
                out.append("Channel ").append(c + 1).append(": No search.\n");
                continue;
            }
            int best = lo;
            for (int i = lo + 1; i <= hi; i++)
                if (value[i] > value[best])
                    best = i;
            if (value[best] >= level[c] * unit)
                out.append("Channel ")
                    .append(c + 1)
                    .append(": Object at ")
                    .append(best - surface)
                    .append(".\n");
            else
                out.append("Channel ").append(c + 1).append(": No object.\n");
        }
        System.out.print(out);
    }
}
