import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int FLOORS = 1000, EGGS = 10;

    public static void main(String[] args) throws Exception {
        int[][] best = new int[EGGS + 1][FLOORS + 1];
        for (int floors = 1; floors <= FLOORS; floors++)
            best[1][floors] = floors;
        // Ten eggs suffice for binary search over the allowed floors.
        // Try every first floor and minimize the worse of its two outcomes.
        for (int eggs = 2; eggs <= EGGS; eggs++)
            for (int floors = 1; floors <= FLOORS; floors++) {
                best[eggs][floors] = floors;
                for (int first = 1; first <= floors; first++)
                    best[eggs][floors] =
                        Math.min(best[eggs][floors], 1 + Math.max(best[eggs - 1][first - 1],
                                                                  best[eggs][floors - first]));
            }
        StreamTokenizer input =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        StringBuilder output = new StringBuilder();
        while (input.nextToken() != StreamTokenizer.TT_EOF) {
            int eggs = (int)input.nval;
            input.nextToken();
            int floors = (int)input.nval;
            if (eggs == 0 && floors == 0)
                break;
            output.append(best[Math.min(eggs, EGGS)][floors]).append('\n');
        }
        System.out.print(output);
    }
}
