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
        // filling the lowest sections first raises every section to a level h
        // and some of them one higher, so the answer is the largest h whose
        // missing containers, the sum of h - height below h, fit into K
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
