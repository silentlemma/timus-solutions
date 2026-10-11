import java.io.*;

public class Main {
    // "-7 3/4", "-7/11" or "11" as a numerator and denominator
    static long[] parse(String line) {
        line = line.trim();
        long sign = line.startsWith("-") ? -1 : 1;
        long whole = 0, num = 0, den = 1;
        for (String token : line.replace("-", " ").trim().split("\\s+")) {
            if (token.isEmpty())
                continue;
            int slash = token.indexOf('/');
            if (slash >= 0) {
                num = Long.parseLong(token.substring(0, slash));
                den = Long.parseLong(token.substring(slash + 1));
            } else {
                whole = Long.parseLong(token);
            }
        }
        return new long[] {sign * (whole * den + num), den};
    }

    static long gcd(long a, long b) { return b == 0 ? a : gcd(b, a % b); }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        long[] a = parse(in.readLine());
        String op = in.readLine().trim();
        long[] b = parse(in.readLine());
        long num, den;
        switch (op) {
        case "+":
            num = a[0] * b[1] + b[0] * a[1];
            den = a[1] * b[1];
            break;
        case "-":
            num = a[0] * b[1] - b[0] * a[1];
            den = a[1] * b[1];
            break;
        case "*":
            num = a[0] * b[0];
            den = a[1] * b[1];
            break;
        default:
            num = a[0] * b[1];
            den = a[1] * b[0];
        }
        if (den < 0) {
            num = -num;
            den = -den;
        }
        String sign = num < 0 ? "-" : "";
        num = Math.abs(num);
        long g = gcd(num, den);
        num /= g;
        den /= g;
        long whole = num / den, rest = num % den;
        if (rest == 0)
            System.out.println(sign + whole);
        else if (whole == 0)
            System.out.println(sign + rest + "/" + den);
        else
            System.out.println(sign + whole + " " + rest + "/" + den);
    }
}
