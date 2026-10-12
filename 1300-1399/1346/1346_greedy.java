import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int a = (int)in.nval;
        in.nextToken();
        int b = (int)in.nval, n = b - a + 1;
        int[] f = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            f[i] = (int)in.nval;
        }
        int pieces = 0;
        for (int i = 0; i < n;) {
            // stretch this piece while it stays monotone; its way up or down is
            // fixed by its first step that is not flat
            pieces++;
            int way = 0, j = i;
            for (; j + 1 < n; j++) {
                int step = Integer.compare(f[j + 1], f[j]);
                if (step != 0 && way != 0 && step != way)
                    break;
                if (way == 0)
                    way = step;
            }
            i = j + 1;
        }
        System.out.println(pieces);
    }
}
