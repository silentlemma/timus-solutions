import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        StreamTokenizer input = new StreamTokenizer(new InputStreamReader(System.in));
        input.nextToken();
        int stones = (int)input.nval;
        input.nextToken();
        int count = (int)input.nval;
        int[] moves = new int[count];
        for (int i = 0; i < count; i++) {
            input.nextToken();
            moves[i] = (int)input.nval;
        }
        Arrays.sort(moves);
        boolean[] win = new boolean[stones + 1];
        // Taking the last stone loses. Larger moves cannot be made at all.
        for (int left = 1; left <= stones; left++)
            for (int take : moves) {
                if (take >= left)
                    break;
                if (!win[left - take]) {
                    win[left] = true;
                    break;
                }
            }
        System.out.println(win[stones] ? 1 : 2);
    }
}
