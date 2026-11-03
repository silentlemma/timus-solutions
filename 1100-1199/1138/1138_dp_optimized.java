import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int PERCENT = 100;

    public static void main(String[] args) throws Exception {
        StreamTokenizer input = new StreamTokenizer(new InputStreamReader(System.in));
        input.nextToken();
        int n = (int)input.nval;
        input.nextToken();
        int start = (int)input.nval;
        if (start > n) {
            System.out.println(0);
            return;
        }
        // gcd(a,PERCENT) depends only on a modulo PERCENT; reuse the tiny
        // table instead of repeating Euclid for each reachable salary.
        int[] divisor = new int[PERCENT];
        for (int residue = 0; residue < PERCENT; residue++) {
            int a = residue, b = PERCENT;
            while (b != 0) {
                int remainder = a % b;
                a = b;
                b = remainder;
            }
            divisor[residue] = a;
        }
        int[] jobs = new int[n + 1];
        jobs[start] = 1;
        int answer = 1;
        for (int salary = start; salary <= n; salary++) {
            int here = jobs[salary];
            if (here == 0)
                continue;
            answer = Math.max(answer, here);
            int step = salary / divisor[salary % PERCENT];
            for (int following = salary + step; following <= n; following += step)
                jobs[following] = Math.max(jobs[following], here + 1);
        }
        System.out.println(answer);
    }
}
