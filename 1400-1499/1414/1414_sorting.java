import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeSet;

public class Main {
    static final int LIMIT = 20;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        TreeSet<String> names = new TreeSet<>();
        names.add("sun"); // the base starts with this one name
        StringBuilder out = new StringBuilder();
        for (String line; (line = in.readLine()) != null;) {
            line = line.trim();
            if (line.isEmpty())
                continue;
            String arg = line.substring(1);
            if (line.charAt(0) == '+') {
                names.add(arg);
                continue;
            }
            out.append(arg).append('\n');
            // names with this prefix form a run starting where the prefix would go
            int shown = 0;
            for (String name : names.tailSet(arg)) {
                if (shown == LIMIT || !name.startsWith(arg))
                    break;
                out.append("  ").append(name).append('\n');
                shown++;
            }
        }
        System.out.print(out);
    }
}
