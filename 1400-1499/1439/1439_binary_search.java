import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        st.nextToken();
        int m = Integer.parseInt(st.nextToken());
        long[] gone = new long[m]; // original numbers of destroyed rooms, sorted
        int count = 0;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(in.readLine());
            char letter = st.nextToken().charAt(0);
            long x = Long.parseLong(st.nextToken());
            // gone[j] - j <= x holds for a prefix: the rooms gone below room x
            int lo = 0, hi = count;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (gone[mid] - mid <= x)
                    lo = mid + 1;
                else
                    hi = mid;
            }
            long original = x + lo;
            if (letter == 'D') {
                System.arraycopy(gone, lo, gone, lo + 1, count - lo);
                gone[lo] = original;
                count++;
            } else {
                out.append(original).append('\n');
            }
        }
        System.out.print(out);
    }
}
