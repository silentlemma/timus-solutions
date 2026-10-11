import java.io.*;
import java.util.*;

public class Main {
    static long solve(long k, long m) {
        String digits = Long.toString(k);
        // numbers not longer than k that come no later than k: for each length,
        // those from 10^(l-1) up to the first l digits of k; any N >= k has them
        long before = 0, low = 1;
        for (int l = 1; l <= digits.length(); l++) {
            before += Long.parseLong(digits.substring(0, l)) - low + 1;
            low *= 10;
        }
        if (m < before)
            return 0;
        // each further number before k is longer than k: of length l it lies in
        // [10^(l-1), k * 10^(l-len(k))), and N is the (m - before)-th of them
        long need = m - before, top = k * 10;
        if (need == 0)
            return k;
        for (; top > low; low *= 10, top *= 10) {
            if (top - low >= need)
                return low + need - 1;
            need -= top - low;
        }
        // k is a power of ten, and no longer number comes before it
        return 0;
    }

    public static void main(String[] args) throws IOException {
        StringTokenizer st =
            new StringTokenizer(new BufferedReader(new InputStreamReader(System.in)).readLine());
        long k = Long.parseLong(st.nextToken());
        long m = Long.parseLong(st.nextToken());
        System.out.println(solve(k, m));
    }
}
