import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        long d = (long)in.nval;
        // sell to everyone who can be served: by the end of month i at most
        // i * d yachts exist, so the running total of sales is capped there
        long[] sales = new long[n];
        long total = 0;
        for (int i = 1; i <= n; i++) {
            in.nextToken();
            long next = Math.min(total + (long)in.nval, i * d);
            sales[i - 1] = next - total;
            total = next;
        }
        // build every yacht as late as possible: going backwards, whatever a
        // month cannot build is built earlier and waits one month per boundary
        long carry = 0, storage = 0;
        for (int i = n - 1; i >= 0; i--) {
            storage += carry;
            carry = Math.max(0, sales[i] + carry - d);
        }
        System.out.println(total + " " + storage);
    }
}
