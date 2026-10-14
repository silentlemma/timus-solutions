import java.io.*;
import java.util.*;

public class Main {
    static String zeros(int count) {
        char[] z = new char[count];
        Arrays.fill(z, '0');
        return new String(z);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String s; (s = br.readLine()) != null;)
            all.append(s).append(' ');
        StringTokenizer st = new StringTokenizer(all.toString());
        int n = Integer.parseInt(st.nextToken());
        String p = st.nextToken(), q = st.nextToken();
        // A xor B equals A + B exactly when no position holds two ones. With a
        // equal to p, b follows q up to a 0 that becomes 1, then zeros, and that
        // prefix of q must avoid the ones of p, so it ends before the first clash
        int clash = 0;
        while (clash < n && !(p.charAt(clash) == '1' && q.charAt(clash) == '1'))
            clash++;
        for (int j = clash - 1; j >= 0; j--)
            if (p.charAt(j) == '0' && q.charAt(j) == '0') {
                System.out.println(p + "\n" + q.substring(0, j) + "1" + zeros(n - j - 1));
                return;
            }
        // otherwise the next a after p with b all zeros, or start over
        int last = p.lastIndexOf('0');
        String a = last < 0 ? zeros(n) : p.substring(0, last) + "1" + zeros(n - last - 1);
        System.out.println(a + "\n" + zeros(n));
    }
}
