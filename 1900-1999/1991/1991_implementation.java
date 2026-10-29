import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        StreamTokenizer input =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        input.nextToken();
        int count = (int)input.nval;
        input.nextToken();
        long capacity = (long)input.nval;
        long unused = 0, survivors = 0;
        for (int i = 0; i < count; ++i) {
            input.nextToken();
            long amount = (long)input.nval;
            if (amount > capacity)
                unused += amount - capacity;
            else
                survivors += capacity - amount;
        }
        System.out.println(unused + " " + survivors);
    }
}
