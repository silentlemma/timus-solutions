import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    static final int LETTERS = 26;

    static String text;
    static int pos;

    // the number of digits at pos; pos moves past it
    static long number() {
        long value = 0;
        while (pos < text.length() && Character.isDigit(text.charAt(pos)))
            value = value * 10 + (text.charAt(pos++) - '0');
        return value;
    }

    // a polynomial as a map from the powers of a .. z, as a string key, to coefficients
    static Map<String, Long> parse(String line) {
        text = line.replaceAll("\\s", ""); // spaces may stand anywhere
        pos = 0;
        Map<String, Long> poly = new HashMap<>();
        long sign = 1;
        while (pos < text.length()) {
            if (text.charAt(pos) == '+' || text.charAt(pos) == '-')
                sign = text.charAt(pos++) == '-' ? -1 : 1;
            long coef = 1;
            int[] powers = new int[LETTERS];
            while (true) {
                if (Character.isDigit(text.charAt(pos)))
                    coef *= number();
                else {
                    int var = text.charAt(pos++) - 'a', power = 1;
                    if (pos < text.length() && text.charAt(pos) == '^') {
                        pos++;
                        power = (int)number();
                    }
                    powers[var] += power;
                }
                if (pos < text.length() && text.charAt(pos) == '*')
                    pos++;
                else
                    break;
            }
            poly.merge(key(powers), sign * coef, Long::sum);
        }
        return poly;
    }

    static String key(int[] powers) {
        StringBuilder sb = new StringBuilder();
        for (int e : powers)
            sb.append(e).append(',');
        return sb.toString();
    }

    static int[] powers(String key) {
        String[] parts = key.split(",");
        int[] p = new int[LETTERS];
        for (int v = 0; v < LETTERS; v++)
            p[v] = Integer.parseInt(parts[v]);
        return p;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        Map<String, Long> first = parse(in.readLine()), second = parse(in.readLine());
        Map<String, Long> product = new HashMap<>();
        for (Map.Entry<String, Long> x : first.entrySet())
            for (Map.Entry<String, Long> y : second.entrySet()) {
                int[] p = powers(x.getKey()), q = powers(y.getKey());
                for (int v = 0; v < LETTERS; v++)
                    p[v] += q[v];
                product.merge(key(p), x.getValue() * y.getValue(), Long::sum);
            }
        List<int[]> keys = new ArrayList<>();
        List<Long> coefs = new ArrayList<>();
        for (Map.Entry<String, Long> t : product.entrySet())
            if (t.getValue() != 0) {
                keys.add(powers(t.getKey()));
                coefs.add(t.getValue());
            }
        Integer[] order = new Integer[keys.size()];
        for (int i = 0; i < order.length; i++)
            order[i] = i;
        // by total degree, then by the powers of a, b, ... from the largest
        java.util.Arrays.sort(order, (i, j) -> {
            int si = 0, sj = 0;
            for (int v = 0; v < LETTERS; v++) {
                si += keys.get(i)[v];
                sj += keys.get(j)[v];
            }
            if (si != sj)
                return Integer.compare(sj, si);
            for (int v = 0; v < LETTERS; v++)
                if (keys.get(i)[v] != keys.get(j)[v])
                    return Integer.compare(keys.get(j)[v], keys.get(i)[v]);
            return 0;
        });
        StringBuilder out = new StringBuilder();
        for (int k = 0; k < order.length; k++) {
            int[] p = keys.get(order[k]);
            long coef = coefs.get(order[k]);
            List<String> factors = new ArrayList<>();
            for (int v = 0; v < LETTERS; v++)
                if (p[v] == 1)
                    factors.add(String.valueOf((char)('a' + v)));
                else if (p[v] > 1)
                    factors.add((char)('a' + v) + "^" + p[v]);
            if (Math.abs(coef) != 1 || factors.isEmpty())
                factors.add(0, String.valueOf(Math.abs(coef)));
            String body = String.join("*", factors);
            if (k == 0)
                out.append(coef < 0 ? "-" : "").append(body);
            else
                out.append(coef < 0 ? " - " : " + ").append(body);
        }
        System.out.println(out.length() == 0 ? "0" : out.toString());
    }
}
