import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {
    static final int DIGITS = 6; // the input has at most six digits after the point
    static final long SCALE = 1000000;

    // the number times 10^6 as an exact integer
    static long scaled(String token) {
        long sign = token.startsWith("-") ? -1 : 1;
        if (token.startsWith("-") || token.startsWith("+"))
            token = token.substring(1);
        int dot = token.indexOf('.');
        String whole = dot < 0 ? token : token.substring(0, dot);
        String frac = dot < 0 ? "" : token.substring(dot + 1);
        frac = (frac + "000000").substring(0, DIGITS);
        return sign * (Long.parseLong("0" + whole) * SCALE + Long.parseLong(frac));
    }

    static BigInteger mul(long a, long b) {
        return BigInteger.valueOf(a).multiply(BigInteger.valueOf(b));
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line; (line = in.readLine()) != null;)
            all.append(line).append(' ');
        StringTokenizer st = new StringTokenizer(all.toString());
        long ex = scaled(st.nextToken()), ey = scaled(st.nextToken());
        long tx = scaled(st.nextToken()), ty = scaled(st.nextToken());
        long ax = scaled(st.nextToken()), ay = scaled(st.nextToken());
        long bx = scaled(st.nextToken()), by = scaled(st.nextToken());
        // mirror from A along s; the eye and the target relative to A
        long sx = bx - ax, sy = by - ay;
        ex -= ax;
        ey -= ay;
        tx -= ax;
        ty -= ay;
        // heights above the mirror line (times |s|), both on one side
        long he = sx * ey - sy * ex, ht = sx * ty - sy * tx;
        if ((he > 0) != (ht > 0)) {
            System.out.println("INVISIBLE");
            return;
        }
        // the ray to the target's image meets the line at the projections
        // weighted by the heights: u = (pe * ht + pt * he) / ((he + ht) |s|^2)
        long pe = sx * ex + sy * ey, pt = sx * tx + sy * ty;
        BigInteger num = mul(pe, ht).add(mul(pt, he));
        BigInteger sum = BigInteger.valueOf(he).add(BigInteger.valueOf(ht));
        BigInteger den = sum.multiply(mul(sx, sx).add(mul(sy, sy)));
        if (den.signum() < 0) {
            num = num.negate();
            den = den.negate();
        }
        boolean seen = num.signum() >= 0 && num.compareTo(den) <= 0;
        System.out.println(seen ? "VISIBLE" : "INVISIBLE");
    }
}
