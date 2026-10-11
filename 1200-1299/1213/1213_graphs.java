import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Set<String> names = new HashSet<>();
        names.add(in.next());
        while (in.hasNext()) {
            String line = in.next();
            if (line.equals("#")) {
                break;
            }
            names.addAll(Arrays.asList(line.split("-", 2)));
        }
        // every other compartment must be emptied through one opened partition,
        // and the partitions of a tree towards the airlock are enough
        System.out.println(names.size() - 1);
    }
}
