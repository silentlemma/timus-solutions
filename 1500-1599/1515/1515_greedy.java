import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        // every sum from 1 to reach is made of the notes taken so far; a note
        // no larger than reach + 1 extends that to reach + note
        long reach = 0;
        for (int i = 0; i < n; i++) {
            in.nextToken();
            long d = (long)in.nval;
            if (d > reach + 1)
                break;
            reach += d;
        }
        System.out.println(reach + 1);
    }
}
