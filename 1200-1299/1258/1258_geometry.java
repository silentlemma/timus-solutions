import java.io.*;
import java.util.*;

public class Main {
    // the distance along one axis once the room is mirrored at each hit
    static long unfolded(int start, int end, int size, char low, String hits) {
        if (hits.isEmpty())
            return Math.abs(end - start);
        int first = hits.charAt(0) == low ? start : size - start;
        int last = hits.charAt(hits.length() - 1) == low ? end : size - end;
        return first + (long)(hits.length() - 1) * size + last;
    }

    static int next(StringTokenizer st) { return Integer.parseInt(st.nextToken()); }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line; (line = in.readLine()) != null;)
            all.append(line).append(' ');
        StringTokenizer st = new StringTokenizer(all.toString());
        int w = next(st), d = next(st), x0 = next(st), y0 = next(st), x1 = next(st), y1 = next(st);
        StringBuilder side = new StringBuilder(), ends = new StringBuilder();
        while (st.hasMoreTokens())
            for (char c : st.nextToken().toCharArray())
                if (c == 'L' || c == 'R')
                    side.append(c);
                else if (c == 'F' || c == 'B')
                    ends.append(c);
        long dx = unfolded(x0, x1, w, 'L', side.toString());
        long dy = unfolded(y0, y1, d, 'F', ends.toString());
        System.out.println(
            String.format(Locale.ROOT, "%.4f", Math.sqrt((double)(dx * dx + dy * dy))));
    }
}
