import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int AREA_SCALE = 4;
    public static void main(String[] args) throws Exception {
        StreamTokenizer input = new StreamTokenizer(new InputStreamReader(System.in));
        input.nextToken();
        double a = input.nval;
        input.nextToken();
        double b = input.nval;
        // The maximal area occurs at a135-degree angle between the sticks.
        double area = (a * a + b * b + 2 * Math.sqrt(2) * a * b) / AREA_SCALE;
        System.out.println(area);
    }
}
