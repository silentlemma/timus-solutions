import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Scanner;
import java.util.TreeMap;

public class Main {
    static final String CHAMPION = "Isenbaev";
    static final int TEAM = 3;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int teams = in.nextInt();
        Map<String, List<String>> mates = new TreeMap<>();
        for (int t = 0; t < teams; t++) {
            String[] names = new String[TEAM];
            for (int i = 0; i < TEAM; i++) {
                names[i] = in.next();
            }
            for (String name : names) {
                mates.computeIfAbsent(name, k -> new ArrayList<>()).addAll(Arrays.asList(names));
            }
        }
        // breadth-first search from the champion over shared teams
        Map<String, Integer> number = new HashMap<>();
        if (mates.containsKey(CHAMPION)) {
            number.put(CHAMPION, 0);
            Queue<String> queue = new ArrayDeque<>();
            queue.add(CHAMPION);
            while (!queue.isEmpty()) {
                String name = queue.poll();
                for (String mate : mates.get(name)) {
                    if (!number.containsKey(mate)) {
                        number.put(mate, number.get(name) + 1);
                        queue.add(mate);
                    }
                }
            }
        }
        StringBuilder out = new StringBuilder();
        for (String name : mates.keySet()) {
            Integer v = number.get(name);
            out.append(name).append(' ').append(v == null ? "undefined" : v.toString());
            out.append('\n');
        }
        System.out.print(out);
    }
}
