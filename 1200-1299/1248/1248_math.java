import java.io.*;
import java.math.*;
import java.util.*;

public class Main {
    static final int DIGITS = 19;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line; (line = in.readLine()) != null;)
            all.append(line).append(' ');
        StringTokenizer st = new StringTokenizer(all.toString());
        int n = Integer.parseInt(st.nextToken());
        // BigDecimal adds the numbers exactly, exponents and all
        BigDecimal total = BigDecimal.ZERO;
        for (int i = 0; i < n; i++)
            total = total.add(new BigDecimal(st.nextToken()));
        if (total.signum() == 0) {
            System.out.println("0." + String.join("", Collections.nCopies(DIGITS - 1, "0")) + "e0");
            return;
        }
        // keep 19 significant digits, rounding half up on the rest
        BigDecimal kept = total.round(new MathContext(DIGITS, RoundingMode.HALF_UP));
        String sign = kept.signum() < 0 ? "-" : "";
        String text = kept.unscaledValue().abs().toString();
        int exponent = text.length() - 1 - kept.scale();
        while (text.length() < DIGITS)
            text += "0";
        text = text.substring(0, DIGITS);
        System.out.println(sign + text.charAt(0) + "." + text.substring(1) + "e" + exponent);
    }
}
