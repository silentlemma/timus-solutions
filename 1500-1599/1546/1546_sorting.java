import java.io.*;
import java.util.*;

public class Main {
    // a name written so that plain string order compares it: a number becomes "0",
    // its length without leading zeros in seven digits and those digits, a letter
    // becomes "1" and itself, so numbers come first and compare by value
    static String mainKey(String s, List<Integer> zeros) {
        StringBuilder key = new StringBuilder();
        int i = 0;
        while (i < s.length()) {
            if (!Character.isDigit(s.charAt(i))) {
                key.append('1').append(s.charAt(i++));
                continue;
            }
            int start = i;
            while (i < s.length() && s.charAt(i) == '0')
                i++;
            int digits = i;
            while (i < s.length() && Character.isDigit(s.charAt(i)))
                i++;
            key.append('0').append(String.format("%07d", i - digits)).append(s, digits, i);
            zeros.add(start - digits);
        }
        return key.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        List<String> names = new ArrayList<>();
        for (String line; (line = in.readLine()) != null;)
            for (StringTokenizer st = new StringTokenizer(line); st.hasMoreTokens();)
                names.add(st.nextToken());
        int n = names.size();
        String[] main = new String[n];
        List<List<Integer>> zeros = new ArrayList<>();
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) {
            zeros.add(new ArrayList<>());
            main[i] = mainKey(names.get(i), zeros.get(i));
            order[i] = i;
        }
        // letters and numbers by value first; then, run by run, more leading zeros first
        Arrays.sort(order, (a, b) -> {
            int c = main[a].compareTo(main[b]);
            if (c != 0)
                return c;
            for (int i = 0; i < zeros.get(a).size(); i++) {
                c = Integer.compare(zeros.get(a).get(i), zeros.get(b).get(i));
                if (c != 0)
                    return c;
            }
            return 0;
        });
        StringBuilder out = new StringBuilder();
        for (int i : order)
            out.append(names.get(i)).append('\n');
        System.out.print(out);
    }
}
