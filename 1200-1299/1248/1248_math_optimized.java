import java.io.BufferedInputStream;
import java.io.IOException;
import java.math.BigInteger;

public class Main {
    private static final int DIGITS = 19;
    private static final int SHIFT = 300;
    private static final int POWER_COUNT = 450;

    private static String read(BufferedInputStream input, StringBuilder buffer) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        buffer.setLength(0);
        while (ch > ' ') {
            buffer.append((char)ch);
            ch = input.read();
        }
        return buffer.toString();
    }

    private static BigInteger scaled(String token, BigInteger[] powers) {
        int e = Math.max(token.indexOf('e'), token.indexOf('E'));
        int exponent = e < 0 ? 0 : Integer.parseInt(token.substring(e + 1));
        String mantissa = e < 0 ? token : token.substring(0, e);
        int point = mantissa.indexOf('.');
        if (point >= 0) {
            exponent -= mantissa.length() - point - 1;
            mantissa = mantissa.substring(0, point) + mantissa.substring(point + 1);
        }
        int scale = SHIFT + exponent;
        if (powers[scale] == null) {
            powers[scale] = BigInteger.TEN.pow(scale);
        }
        return new BigInteger(mantissa).multiply(powers[scale]);
    }

    private static String scientific(BigInteger value) {
        if (value.signum() == 0) {
            return "0.000000000000000000e0";
        }
        String exact = value.abs().toString();
        int exponent = exact.length() - 1 - SHIFT;
        char[] kept = new char[DIGITS];
        for (int i = 0; i < kept.length; i++) {
            kept[i] = i < exact.length() ? exact.charAt(i) : '0';
        }
        if (exact.length() > DIGITS && exact.charAt(DIGITS) >= '5') {
            int i = DIGITS - 1;
            while (i >= 0 && kept[i] == '9') {
                kept[i--] = '0';
            }
            if (i >= 0) {
                kept[i]++;
            } else {
                kept[0] = '1';
                exponent++;
            }
        }
        StringBuilder output = new StringBuilder();
        if (value.signum() < 0) {
            output.append('-');
        }
        return output.append(kept[0])
            .append('.')
            .append(kept, 1, DIGITS - 1)
            .append('e')
            .append(exponent)
            .toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        StringBuilder buffer = new StringBuilder();
        int count = Integer.parseInt(read(input, buffer));
        BigInteger[] powers = new BigInteger[POWER_COUNT];
        BigInteger total = BigInteger.ZERO;
        for (int i = 0; i < count; i++) {
            total = total.add(scaled(read(input, buffer), powers));
        }
        System.out.println(scientific(total));
    }
}
