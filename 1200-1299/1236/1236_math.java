import java.io.*;

public class Main {
    static final int SPACE = ' ', HEX = 16;
    static final char[] DIGITS = "0123456789ABCDEF".toCharArray();

    static int[] decode(String s) {
        int[] bytes = new int[s.length() / 2];
        for (int i = 0; i < bytes.length; i++)
            bytes[i] = Integer.parseInt(s.substring(2 * i, 2 * i + 2), HEX);
        return bytes;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int[] shorter = decode(in.readLine().trim()), longer = decode(in.readLine().trim());
        // the long message is a space followed by the short one, so its first
        // byte gives the first key byte, and byte i+1 of the long message hides
        // the same clear byte as byte i of the short one
        int[] key = new int[longer.length];
        key[0] = longer[0] ^ SPACE;
        for (int i = 0; i < shorter.length; i++)
            key[i + 1] = longer[i + 1] ^ shorter[i] ^ key[i];
        StringBuilder sb = new StringBuilder();
        for (int k : key)
            sb.append(DIGITS[k / HEX]).append(DIGITS[k % HEX]);
        System.out.println(sb);
    }
}
