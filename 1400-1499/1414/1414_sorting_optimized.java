import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.TreeSet;

public class Main {
    static final int LIMIT = 20;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));
        TreeSet<String> names = new TreeSet<>();
        names.add("sun");
        for (String query; (query = input.readLine()) != null;) {
            query = query.trim();
            if (query.isEmpty()) {
                continue;
            }
            String text = query.substring(1);
            if (query.charAt(0) == '+') {
                names.add(text);
                continue;
            }
            output.write(text);
            output.newLine();
            int remaining = LIMIT;
            for (String name : names.tailSet(text)) {
                if (remaining == 0 || !name.startsWith(text)) {
                    break;
                }
                output.write("  ");
                output.write(name);
                output.newLine();
                remaining--;
            }
        }
        output.flush();
    }
}
