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
        int[] jobs = new int[n + 1];
        jobs[start] = 1;
        int answer = 1;
        // Increasing salaries form a DAG; integer divisibility tests
        // whole percentages exactly, avoiding floating-point rounding.
        for (int salary = start; salary <= n; salary++) {
            if (jobs[salary] == 0)
                continue;
            answer = Math.max(answer, jobs[salary]);
            for (int following = salary + 1; following <= n; following++)
                if (PERCENT * following % salary == 0)
                    jobs[following] = Math.max(jobs[following], jobs[salary] + 1);
        }
        System.out.println(answer);
    }
}
