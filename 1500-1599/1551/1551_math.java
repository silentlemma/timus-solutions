import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer st = new StreamTokenizer(in);
        st.nextToken();
        int n = (int)st.nval, largest = 0;
        Map<String, Integer> count = new HashMap<>();
        for (int i = 0; i < 1 << n; i++) {
            st.nextToken(); // the name
            st.nextToken();
            int c = count.merge(st.sval, 1, Integer::sum);
            largest = Math.max(largest, c);
        }
        // c wrestlers of one prefecture can avoid each other in all rounds but
        // ceil(log2 c) of them, and dealing the wrestlers sorted by prefecture
        // round-robin into that many top-level groups achieves it for all at once
        int unsafe = 0;
        while (1 << unsafe < largest)
            unsafe++;
        System.out.println(n - unsafe);
    }
}
