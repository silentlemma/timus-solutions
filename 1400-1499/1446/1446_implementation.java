import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    static final String[] HOUSES = {"Slytherin", "Hufflepuff", "Gryffindor", "Ravenclaw"};

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        Map<String, List<String>> lists = new HashMap<>();
        for (String house : HOUSES)
            lists.put(house, new ArrayList<>());
        for (int i = 0; i < n; i++) {
            // names keep their inner spaces, so only the line break is dropped
            String name = in.readLine();
            String house = in.readLine().trim();
            lists.get(house).add(name);
        }
        StringBuilder out = new StringBuilder();
        for (int h = 0; h < HOUSES.length; h++) {
            if (h > 0)
                out.append('\n');
            out.append(HOUSES[h]).append(":\n");
            for (String name : lists.get(HOUSES[h]))
                out.append(name).append('\n');
        }
        System.out.print(out);
    }
}
