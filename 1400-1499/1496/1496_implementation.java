import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        // a team that submitted more than once is the spammer; the teams are
        // printed in the order of their first submission
        Map<String, Integer> count = new LinkedHashMap<>();
        for (int i = 0; i < n; i++)
            count.merge(in.next(), 1, Integer::sum);
        StringBuilder out = new StringBuilder();
        for (Map.Entry<String, Integer> e : count.entrySet())
            if (e.getValue() > 1)
                out.append(e.getKey()).append('\n');
        System.out.print(out);
    }
}
