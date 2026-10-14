import java.util.*;

public class Main {
    static String join(List<Integer> order) {
        StringBuilder s = new StringBuilder();
        for (int i = 0; i < order.size(); i++)
            s.append(i > 0 ? " " : "").append(order.get(i));
        return s.append('\n').toString();
    }

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // the cheapest round trip, as a cycle through n: one side of n goes
        // 2, n - 2, 4, n - 4, ..., the other 1, n - 1, 3, n - 3, ...; step k
        // takes the pair k, k + 1 for odd k and n - k, n - k + 1 for even k
        boolean[] used = new boolean[n + 1];
        used[n] = true;
        List<Integer> oneSide = new ArrayList<>(), otherSide = new ArrayList<>();
        for (int k = 1;; k++) {
            int a = k % 2 == 1 ? k + 1 : n - k, b = k % 2 == 1 ? k : n - k + 1;
            if (a < 1 || used[a] || used[b])
                break;
            oneSide.add(a);
            otherSide.add(b);
            used[a] = used[b] = true;
        }
        // the cycle: n, one side, the city left where the two sides meet if
        // any, and the other side back to n; it ends with city 1
        List<Integer> cycle = new ArrayList<>();
        cycle.add(n);
        cycle.addAll(oneSide);
        for (int v = 1; v < n; v++)
            if (!used[v])
                cycle.add(v);
        Collections.reverse(otherSide);
        cycle.addAll(otherSide);
        List<Integer> cheap = new ArrayList<>();
        cheap.add(cycle.get(cycle.size() - 1));
        cheap.addAll(cycle.subList(0, cycle.size() - 1));
        // the dearest: odd numbers up, then even numbers down, so that every
        // city is next to the two closest in size
        List<Integer> dear = new ArrayList<>();
        for (int v = 1; v <= n; v += 2)
            dear.add(v);
        for (int v = n - n % 2; v >= 2; v -= 2)
            dear.add(v);
        System.out.print(join(cheap) + join(dear));
    }
}
