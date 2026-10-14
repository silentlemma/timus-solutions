import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Map<String, Long> bags = new HashMap<>();
        for (String color : new String[] {"Blue", "Red", "Yellow"})
            bags.put(color, in.nextLong());
        int k = in.nextInt();
        // one reagent from each needed bag, chosen independently
        long ways = 1;
        for (int i = 0; i < k; i++)
            ways *= bags.get(in.next());
        System.out.println(ways);
    }
}
