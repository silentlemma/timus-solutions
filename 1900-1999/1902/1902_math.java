import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer input =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        input.nextToken();
        int count = (int)input.nval;
        input.nextToken();
        int duration = (int)input.nval;
        input.nextToken();
        int start = (int)input.nval;
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < count; ++i) {
            input.nextToken();
            int other = (int)input.nval;
            int doubledTime = start + duration + other;
            output.append(doubledTime / 2);
            output.append(doubledTime % 2 == 0 ? ".000000\n" : ".500000\n");
        }
        System.out.print(output);
    }
}
