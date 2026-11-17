import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static String[] associations(String line, int from) {
        StringTokenizer tokenizer = new StringTokenizer(line.substring(from));
        String[] values = new String[tokenizer.countTokens()];
        for (int i = 0; i < values.length; i++) {
            values[i] = tokenizer.nextToken();
        }
        Arrays.sort(values);
        int unique = 0;
        for (String value : values) {
            if (unique == 0 || !values[unique - 1].equals(value)) {
                values[unique++] = value;
            }
        }
        return unique == values.length ? values : Arrays.copyOf(values, unique);
    }

    static int intersect(String[] left, int size, String[] right) {
        int i = 0, j = 0, keep = 0;
        while (i < size && j < right.length) {
            int comparison = left[i].compareTo(right[j]);
            if (comparison == 0) {
                left[keep++] = left[i++];
                j++;
            } else if (comparison < 0) {
                i++;
            } else {
                j++;
            }
        }
        return keep;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(input.readLine().trim());
        Map<String, String[]> known = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String line = input.readLine();
            int colon = line.indexOf(':');
            known.put(line.substring(0, colon), associations(line, colon + 1));
        }
        int m = Integer.parseInt(input.readLine().trim());
        for (int i = 0; i < m; i++) {
            StringTokenizer objects = new StringTokenizer(input.readLine());
            String[] common = known.get(objects.nextToken()).clone();
            int size = common.length;
            while (size > 0 && objects.hasMoreTokens()) {
                size = intersect(common, size, known.get(objects.nextToken()));
            }
            if (size == 0) {
                output.write("No solution.");
            }
            for (int j = 0; j < size; j++) {
                if (j > 0) {
                    output.write(' ');
                }
                output.write(common[j]);
            }
            output.newLine();
        }
        output.flush();
    }
}
