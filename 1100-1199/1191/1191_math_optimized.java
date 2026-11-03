import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        StreamTokenizer input = new StreamTokenizer(new InputStreamReader(System.in));
        input.nextToken();
        int gap = (int)input.nval;
        input.nextToken();
        int count = (int)input.nval;
        for (int i = 0; i < count; i++) {
            input.nextToken();
            int interval = (int)input.nval;
            // The smallest achievable departure gap is gap-gap%interval.
            gap -= gap % interval;
            if (gap == 0) {
                System.out.println("YES");
                return;
            }
        }
        System.out.println("NO");
    }
}
