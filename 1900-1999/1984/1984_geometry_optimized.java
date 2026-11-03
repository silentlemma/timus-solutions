import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        StreamTokenizer input = new StreamTokenizer(new InputStreamReader(System.in));
        input.nextToken();
        int count = (int)input.nval;
        double radius = count == 1 ? 1.0 : 1.0 + 1.0 / Math.sin(Math.PI / count);
        // Double.toString is locale-independent and preserves more precision
        // than the required tolerance, without loading a decimal Formatter.
        System.out.println(radius);
    }
}
