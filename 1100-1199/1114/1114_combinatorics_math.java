import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static long ways(int boxes, int balls) {
        long result = 1;
        for (int count = 1; count <= balls; count++)
            result = result * (boxes + count) / count;
        return result;
    }

    public static void main(String[] args) throws Exception {
        StreamTokenizer input = new StreamTokenizer(new InputStreamReader(System.in));
        input.nextToken();
        int boxes = (int)input.nval;
        input.nextToken();
        int red = (int)input.nval;
        input.nextToken();
        int blue = (int)input.nval;
        // Each coefficient fits32unsigned bits, and its pre-division
        // intermediate fits signed64bits. The product fits unsigned64bits.
        long result = ways(boxes, red) * ways(boxes, blue);
        System.out.println(Long.toUnsignedString(result));
    }
}
