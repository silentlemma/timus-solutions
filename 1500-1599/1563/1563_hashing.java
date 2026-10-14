import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        Set<String> seen = new HashSet<>();
        int repeats = 0;
        String line;
        // a name is the whole line, spaces included; readLine drops the line end
        for (int i = 0; i < n && (line = in.readLine()) != null; i++)
            if (!seen.add(line))
                repeats++;
        System.out.println(repeats);
    }
}
