import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    static int at;

    // the number starting at s[at] (1 if there is none); at moves past it
    static long number(String s) {
        int j = at;
        while (j < s.length() && Character.isDigit(s.charAt(j))) {
            j++;
        }
        long v = j > at ? Long.parseLong(s.substring(at, j)) : 1;
        at = j;
        return v;
    }

    static Map<String, Long> totals(String formula) {
        Map<String, Long> result = new HashMap<>();
        for (String term : formula.split("\\+")) {
            at = 0;
            long times = number(term);
            // one level per open bracket; a closing bracket multiplies its
            // level by the number after it and adds it to the level outside
            Deque<Map<String, Long>> stack = new ArrayDeque<>();
            stack.push(new HashMap<>());
            while (at < term.length()) {
                char c = term.charAt(at);
                if (c == '(') {
                    stack.push(new HashMap<>());
                    at++;
                } else if (c == ')') {
                    Map<String, Long> inner = stack.pop();
                    at++;
                    long k = number(term);
                    for (Map.Entry<String, Long> e : inner.entrySet()) {
                        stack.peek().merge(e.getKey(), e.getValue() * k, Long::sum);
                    }
                } else {
                    int j = at + 1;
                    if (j < term.length() && Character.isLowerCase(term.charAt(j))) {
                        j++;
                    }
                    String name = term.substring(at, j);
                    at = j;
                    stack.peek().merge(name, number(term), Long::sum);
                }
            }
            for (Map.Entry<String, Long> e : stack.peek().entrySet()) {
                result.merge(e.getKey(), e.getValue() * times, Long::sum);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String left = in.next();
        int n = in.nextInt();
        Map<String, Long> want = totals(left);
        StringBuilder out = new StringBuilder();
        for (int q = 0; q < n; q++) {
            String right = in.next();
            out.append(left)
                .append(totals(right).equals(want) ? "==" : "!=")
                .append(right)
                .append('\n');
        }
        System.out.print(out);
    }
}
