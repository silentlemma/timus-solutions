import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    // the three cabinets from left to right, with the names from the statement
    static final String[][] CABINETS = {
        {"Alice", "Ariel", "Aurora", "Phil", "Peter", "Olaf", "Phoebus", "Ralph", "Robin"},
        {"Bambi", "Belle", "Bolt", "Mulan", "Mowgli", "Mickey", "Silver", "Simba", "Stitch"},
        {"Dumbo", "Genie", "Jiminy", "Kuzko", "Kida", "Kenai", "Tarzan", "Tiana", "Winnie"},
    };

    public static void main(String[] args) {
        Map<String, Integer> cabinet = new HashMap<>();
        for (int i = 0; i < CABINETS.length; i++)
            for (String name : CABINETS[i])
                cabinet.put(name, i);
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int position = 0, steps = 0;
        for (int k = 0; k < n; k++) {
            int target = cabinet.get(in.next());
            steps += Math.abs(target - position);
            position = target;
        }
        System.out.println(steps);
    }
}
