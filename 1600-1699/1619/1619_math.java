import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int t = (int)in.nval;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < t; i++) {
            in.nextToken();
            long k = (long)in.nval;
            in.nextToken();
            long m = (long)in.nval;
            // the ballot theorem: the elder stays ahead or level with this chance
            if (m > k)
                out.append("0\n");
            else
                out.append(String.format(Locale.ROOT, "%.10f%n", (double)(k - m + 1) / (k + 1)));
        }
        System.out.print(out);
    }
}
