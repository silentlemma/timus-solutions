import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int solve(String south, String north) {
        int i = 0, j = 0, elapsed = 0;
        while (i < south.length() && j < north.length()) {
            char a = south.charAt(i), b = north.charAt(j);
            boolean goA = a != 'L' || b == 'L';
            boolean goB = b != 'L' || a == 'L';
            if (goA)
                i++;
            if (goB)
                j++;
            elapsed++;
        }
        return elapsed + south.length() - i + north.length() - j;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        java.io.StreamTokenizer tokens = new java.io.StreamTokenizer(in);
        tokens.nextToken();
        String south = tokens.sval;
        tokens.nextToken();
        String north = tokens.sval;
        System.out.println(solve(south, north));
    }
}
