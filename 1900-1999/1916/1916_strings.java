import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    private static final int MODULUS = 1000000007;

    private static final class Expansions {
        final int[][] rules;
        final int width;
        final int limit;
        final String[] prefixes;
        final String[] suffixes;
        final Set<String> parts = new HashSet<>();

        Expansions(int[][] rules, int width) {
            this.rules = rules;
            this.width = width;
            limit = width - 1;
            prefixes = new String[rules.length];
            suffixes = new String[rules.length];
        }

        void visit(int vertex) {
            if (prefixes[vertex] != null) {
                return;
            }
            if (rules[vertex].length == 0) {
                prefixes[vertex] = String.valueOf((char) (vertex + 1));
                suffixes[vertex] = prefixes[vertex];
                return;
            }
            String prefix = "";
            String suffix = "";
            for (int child : rules[vertex]) {
                visit(child);
                String span = suffix + prefixes[child];
                for (int start = 0; start + width <= span.length(); start++) {
                    parts.add(span.substring(start, start + width));
                }
                prefix += prefixes[child];
                if (prefix.length() > limit) {
                    prefix = prefix.substring(0, limit);
                }
                suffix += suffixes[child];
                if (suffix.length() > limit) {
                    suffix = suffix.substring(suffix.length() - limit);
                }
            }
            prefixes[vertex] = prefix;
            suffixes[vertex] = suffix;
        }
    }

    static int distinctParts(int[][] rules, int width) {
        Expansions expansions = new Expansions(rules, width);
        for (int vertex = 0; vertex < rules.length; vertex++) {
            expansions.visit(vertex);
        }
        return expansions.parts.size() % MODULUS;
    }

    private static final class Input {
        final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokens = new StringTokenizer("");

        int next() throws IOException {
            while (!tokens.hasMoreTokens()) {
                tokens = new StringTokenizer(reader.readLine());
            }
            return Integer.parseInt(tokens.nextToken());
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int count = input.next();
        int width = input.next();
        int[][] rules = new int[count][];
        for (int vertex = 0; vertex < count; vertex++) {
            int length = input.next();
            rules[vertex] = new int[length == -1 ? 0 : length];
            for (int index = 0; index < rules[vertex].length; index++) {
                rules[vertex][index] = input.next() - 1;
            }
        }
        System.out.println(distinctParts(rules, width));
    }
}
