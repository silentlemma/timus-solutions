import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static final int DIVISOR = 7;
    static final String KEY = "1234";

    static int remainderOf(String s) {
        int r = 0;
        for (char c : s.toCharArray()) {
            r = (r * 10 + (c - '0')) % DIVISOR;
        }
        return r;
    }

    static void permute(String prefix, String rest, List<String> out) {
        if (rest.isEmpty()) {
            out.add(prefix);
            return;
        }
        for (int i = 0; i < rest.length(); i++) {
            permute(prefix + rest.charAt(i), rest.substring(0, i) + rest.substring(i + 1), out);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null) {
            text.append(line).append(' ');
        }
        StringTokenizer tok = new StringTokenizer(text.toString());
        // the 24 orders of 1, 2, 3, 4 leave every remainder modulo 7
        List<String> orders = new ArrayList<>();
        permute("", KEY, orders);
        int n = Integer.parseInt(tok.nextToken());
        StringBuilder out = new StringBuilder();
        for (int k = 0; k < n; k++) {
            StringBuilder number = new StringBuilder(tok.nextToken());
            for (char d : KEY.toCharArray()) {
                number.deleteCharAt(number.indexOf(String.valueOf(d)));
            }
            // zeros go to the end, where they do not change divisibility by 7
            String head = number.toString().replace("0", "");
            StringBuilder zeros = new StringBuilder();
            for (int i = head.length(); i < number.length(); i++) {
                zeros.append('0');
            }
            for (String o : orders) {
                if (remainderOf(head + o) == 0) {
                    out.append(head).append(o).append(zeros).append("\n");
                    break;
                }
            }
        }
        System.out.print(out);
    }
}
