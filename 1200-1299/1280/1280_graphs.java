import java.io.*;

public class Main {
    static int next(StreamTokenizer in) throws IOException {
        in.nextToken();
        return (int)in.nval;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int n = next(in), m = next(in);
        int[] from = new int[m], to = new int[m], place = new int[n + 1];
        for (int i = 0; i < m; i++) {
            from[i] = next(in);
            to[i] = next(in);
        }
        for (int i = 0; i < n; i++)
            place[next(in)] = i;
        // the plan is right exactly when every rule points forward in it; a
        // rule from a subject to itself can never hold
        boolean ok = true;
        for (int i = 0; i < m; i++)
            if (place[from[i]] >= place[to[i]])
                ok = false;
        System.out.println(ok ? "YES" : "NO");
    }
}
