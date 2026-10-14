import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        StringBuilder sb = new StringBuilder();
        // g(n) = n by induction, so f(n) = 1 + sum of i f(i) = n f(n - 1) = n!
        while (in.nextToken() != StreamTokenizer.TT_EOF) {
            long n = (long)in.nval;
            in.nextToken();
            long p = (long)in.nval;
            if (n == 0 && p == 0)
                break;
            long r = n >= p ? 0 : 1; // when n >= p, p itself is a factor of n!
            for (long i = 2; i <= n && r != 0; i++)
                r = r * i % p;
            sb.append(r).append('\n');
        }
        System.out.print(sb);
    }
}
