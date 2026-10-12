import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        long limit = new Scanner(System.in).nextLong();
        // going back from the last replacement: reach is the longest run that
        // the replacements chosen so far turn into a single space
        List<Long> plan = new ArrayList<>();
        long reach = 1;
        while (reach < limit) {
            long step = (reach + 1) / 2 + 1; // the best length to replace here
            long groups = reach + 2 - step;  // most groups in a run that still fits
            reach = groups * step + step - 2;
            plan.add(step);
        }
        StringBuilder out = new StringBuilder();
        out.append(plan.size()).append('\n');
        for (int i = plan.size() - 1; i >= 0; i--)
            out.append(plan.get(i)).append('\n');
        System.out.print(out);
    }
}
