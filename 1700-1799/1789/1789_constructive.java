import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        List<Integer> touches = new ArrayList<>();
        if (n == 2) {
            touches.add(1);
            touches.add(1);
        } else {
            // sweep 2..n-1 and back: the first pass catches one parity of the
            // start, the second pass the other
            for (int p = 2; p <= n - 1; p++) touches.add(p);
            for (int p = n - 1; p >= 2; p--) touches.add(p);
        }
        StringBuilder out = new StringBuilder();
        out.append(touches.size()).append('\n');
        for (int i = 0; i < touches.size(); i++) {
            if (i > 0) out.append(' ');
            out.append(touches.get(i));
        }
        System.out.println(out);
    }
}
