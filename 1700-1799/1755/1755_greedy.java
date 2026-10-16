import java.util.Locale;
import java.util.Scanner;

public class Main {
    static class Good {
        final long worth, cost, amount;
        final int slot;

        Good(long worth, long cost, long amount, int slot) {
            this.worth = worth;
            this.cost = cost;
            this.amount = amount;
            this.slot = slot;
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long a1 = in.nextLong(), b1 = in.nextLong(), a2 = in.nextLong(), b2 = in.nextLong();
        long n = in.nextLong(), m = in.nextLong();
        // Karlsson leaves the piece he likes no more than half, so the best is
        // the piece of greatest worth to Little Boy within half of Karlsson's total:
        // a fractional knapsack where each ingredient is taken by worth per cost
        Good[] goods = {new Good(a1, a2, n, 0), new Good(b1, b2, m, 1)};
        // zero-cost goods first, then by worth over cost, highest first
        if (goods[1].worth * goods[0].cost > goods[0].worth * goods[1].cost) {
            Good t = goods[0];
            goods[0] = goods[1];
            goods[1] = t;
        }
        double room = (a2 * n + b2 * m) / 2.0;
        double[] piece = new double[goods.length];
        for (Good g : goods) {
            double take = g.cost * g.amount <= room ? g.amount : room / g.cost;
            piece[g.slot] = take;
            room -= take * g.cost;
        }
        System.out.printf(Locale.US, "%.8f %.8f%n", piece[0], piece[1]);
    }
}
