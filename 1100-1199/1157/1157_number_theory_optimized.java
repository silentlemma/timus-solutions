import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int LIMIT = 10000;

    public static void main(String[] args) throws Exception {
        StreamTokenizer input = new StreamTokenizer(new InputStreamReader(System.in));
        input.nextToken();
        int before = (int)input.nval;
        input.nextToken();
        int after = (int)input.nval;
        input.nextToken();
        int added = (int)input.nval;
        byte[] shapes = new byte[LIMIT + 1];
        // At most sqrt(LIMIT)=100 smaller sides fit; signed bytes suffice.
        for (int side = 1; side * side <= LIMIT; side++)
            for (int tiles = side * side; tiles <= LIMIT; tiles += side)
                shapes[tiles]++;
        int answer = 0;
        for (int tiles = added + 1; tiles <= LIMIT; tiles++)
            if (shapes[tiles] == after && shapes[tiles - added] == before) {
                answer = tiles;
                break;
            }
        System.out.println(answer);
    }
}
