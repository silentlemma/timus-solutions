import java.io.*;
import java.util.*;

public class Main {
    static final long DAY = 1440, HOUR = 60;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null)
            text.append(line).append(' ');
        StringTokenizer in = new StringTokenizer(text.toString());
        int n = Integer.parseInt(in.nextToken());
        long now = 0;
        for (int i = 1; i < n; i++) {
            int q = Integer.parseInt(in.nextToken());
            long delay = Long.parseLong(in.nextToken());
            long flight = Long.parseLong(in.nextToken());
            long best = -1;
            for (int j = 0; j < q; j++) {
                String[] parts = in.nextToken().split(":");
                long leave = Long.parseLong(parts[0]) * HOUR + Long.parseLong(parts[1]) + delay;
                if (leave < now) // the same flight on a later day
                    leave += (now - leave + DAY - 1) / DAY * DAY;
                if (best < 0 || leave < best)
                    best = leave;
            }
            now = best + flight;
        }
        System.out.println(now);
    }
}
