import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static class Input {
        final StreamTokenizer input =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int nextInt() throws IOException {
            input.nextToken();
            return (int)input.nval;
        }
    }
    static int mostCompared(int[] values) {
        int championValue = values[0];
        int champion = 0;
        int best = 0;
        int currentCount = 0;
        int bestCount = 0;
        for (int index = 1; index < values.length; index++) {
            currentCount++;
            if (currentCount > bestCount) {
                bestCount = currentCount;
                best = champion;
            }
            if (values[index] < championValue) {
                championValue = values[index];
                champion = index;
                currentCount = 1;
            }
        }
        return best + 1;
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int count = input.nextInt();
        int[] values = new int[count];
        for (int i = 0; i < count; i++) {
            values[i] = input.nextInt();
        }
        System.out.println(mostCompared(values));
    }
}
