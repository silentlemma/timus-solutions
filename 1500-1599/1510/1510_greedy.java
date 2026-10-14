import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        // Boyer-Moore vote: a value met more often than all the others together
        // survives pairing every note with a different one
        long leader = 0, lead = 0;
        for (int i = 0; i < n; i++) {
            in.nextToken();
            long value = (long)in.nval;
            if (lead == 0) {
                leader = value;
                lead = 1;
            } else if (value == leader)
                lead++;
            else
                lead--;
        }
        System.out.println(leader);
    }
}
