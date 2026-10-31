import java.util.HashSet;
import java.util.Set;

public class Main {
    static final class Input {
        private final java.io.BufferedReader reader =
            new java.io.BufferedReader(new java.io.InputStreamReader(System.in));
        private java.util.StringTokenizer words = new java.util.StringTokenizer("");

        String next() throws java.io.IOException {
            while (!words.hasMoreTokens()) {
                String line = reader.readLine();
                if (line == null)
                    return null;
                words = new java.util.StringTokenizer(line);
            }
            return words.nextToken();
        }
    }

    // buffered tokens avoid scanner regex initialization and temporary match objects.
    public static void main(String[] args) throws java.io.IOException {
        Input in = new Input();
        Set<String> names = new HashSet<>();
        names.add(in.next());
        for (String line; (line = in.next()) != null;) {
            if (line.equals("#")) {
                break;
            }
            int dash = line.indexOf('-');
            names.add(line.substring(0, dash));
            names.add(line.substring(dash + 1));
        }
        // every other compartment must be emptied through one opened partition,
        // and the partitions of a tree towards the airlock are enough
        System.out.println(names.size() - 1);
    }
}
