import java.io.*;
import java.util.*;

public class Main {
    static final int AXES = 3;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String s; (s = br.readLine()) != null;)
            all.append(s).append(' ');
        StringTokenizer st = new StringTokenizer(all.toString());
        long[] size = new long[AXES];
        for (int a = 0; a < AXES; a++)
            size[a] = Long.parseLong(st.nextToken());
        // empty when there are no instructions
        String program = st.hasMoreTokens() ? st.nextToken() : "";
        // the moves along each axis: decrease, increase
        String down = "ldb", up = "ruf";
        long total = 1;
        for (int a = 0; a < AXES; a++) {
            // each move keeps neighbouring starts at most one apart and in order,
            // so the finishes fill the range between the extreme starts
            long low = 1, high = size[a];
            for (int i = 0; i < program.length(); i++) {
                char step = program.charAt(i);
                if (step == up.charAt(a)) {
                    low = Math.min(low + 1, size[a]);
                    high = Math.min(high + 1, size[a]);
                } else if (step == down.charAt(a)) {
                    low = Math.max(low - 1, 1);
                    high = Math.max(high - 1, 1);
                }
            }
            total *= high - low + 1;
        }
        System.out.println(total);
    }
}
