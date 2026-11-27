import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        in.nextToken();
        long k = (long)in.nval;
        long[] heights = new long[n * m];
        long lo = Long.MAX_VALUE;
        for (int i = 0; i < n * m; i++) {
            in.nextToken();
            heights[i] = (long)in.nval;
            lo = Math.min(lo, heights[i]);
        }
        // Filling the lowest sections raises stacks below the final minimum h to h.
        // Some stacks at h may get one more container; initially taller ones stay put.
        // The answer is the largest h with sum(max(0, h - height)) <= K.
        long hi = lo + k;
        while (lo < hi) {
            long mid = (lo + hi + 1) / 2, need = 0;
            for (long h : heights)
                if (h < mid)
                    need += mid - h;
            if (need <= k)
                lo = mid;
            else
                hi = mid - 1;
        }
        System.out.println(lo);
    }
}
