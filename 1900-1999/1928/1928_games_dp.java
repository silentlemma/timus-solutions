import java.util.Scanner;

public class Main {
    static int[] optimalTotals(int budget, int gift, int limit) {
        int[] current = new int[budget + 1];
        int[] opponent = new int[budget + 1];
        for (int remaining = 1; remaining <= budget; remaining++) {
            int best = remaining < limit ? gift : -1;
            int other = 0;
            for (int request = 1; request <= Math.min(remaining, limit); request++) {
                int rest = remaining - request;
                int ownTotal = request + opponent[rest];
                int otherTotal = current[rest];
                if (ownTotal > best || (ownTotal == best && otherTotal < other)) {
                    best = ownTotal;
                    other = otherTotal;
                }
            }
            current[remaining] = best;
            opponent[remaining] = other;
        }
        return new int[] {current[budget], opponent[budget]};
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int budget = input.nextInt();
        int gift = input.nextInt();
        int limit = input.nextInt();
        int[] answer = optimalTotals(budget, gift, limit);
        System.out.println(answer[0] + " " + answer[1]);
    }
}
