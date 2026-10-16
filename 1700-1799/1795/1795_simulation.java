import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Scanner;

public class Main {
    static class Customer {
        String product;
        int wanted;
        int seen = -1; // the amount told at the last visit, -1 before the first

        Customer(String product, int wanted) {
            this.product = product;
            this.wanted = wanted;
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int m = in.nextInt();
        Map<String, Integer> stock = new HashMap<>();
        for (int i = 0; i < m; i++) {
            int amount = in.nextInt();
            in.next();
            stock.put(in.next(), amount);
        }
        int n = in.nextInt();
        LinkedList<Customer> line = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            int amount = in.nextInt();
            in.next();
            line.add(new Customer(in.next(), amount));
        }
        int minutes = 0;
        while (!line.isEmpty()) {
            Customer c = line.removeFirst();
            minutes++;
            int left = stock.getOrDefault(c.product, 0);
            if (left >= c.wanted) {
                stock.put(c.product, left - c.wanted);
            } else if (left == c.seen) {
                // the same rest as before the call: take it all
                stock.put(c.product, 0);
            } else if (left > 0) {
                // let the next one forward and call home; if the next one is
                // the last of the line, it is Mark's turn
                c.seen = left;
                if (line.isEmpty()) break;
                line.add(1, c);
            }
        }
        System.out.println(minutes);
    }
}
