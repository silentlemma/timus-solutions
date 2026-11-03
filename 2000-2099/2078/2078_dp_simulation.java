public class Main {
    static final int FRAMES = 10, PINS = 10, MAX_LAST_ROLLS = 3, STATES = 4;
    static final int INF = FRAMES * PINS * MAX_LAST_ROLLS + 1;
    static int nextInt() throws Exception {
        int c = System.in.read();
        while (c <= ' ')
            c = System.in.read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }
    static void put(int[] low, int[] high, int state, int a, int b) {
        if (a < low[state])
            low[state] = a;
        if (b > high[state])
            high[state] = b;
    }
    public static void main(String[] args) throws Exception {
        int[] low = new int[STATES], high = new int[STATES], nextLow = new int[STATES],
              nextHigh = new int[STATES];
        for (int s = 1; s < STATES; s++) {
            low[s] = INF;
            high[s] = -1;
        }
        for (int f = 0; f < FRAMES - 1; f++) {
            int total = nextInt();
            for (int s = 0; s < STATES; s++) {
                nextLow[s] = INF;
                nextHigh[s] = -1;
            }
            for (int state = 0; state < STATES; state++) {
                if (high[state] < 0)
                    continue;
                int a = (state + 1) / 2, b = state / 2;
                if (total < PINS)
                    put(nextLow, nextHigh, 0, low[state] + total * (1 + b),
                        high[state] + total * (1 + a));
                else {
                    put(nextLow, nextHigh, 1, low[state] + PINS * (1 + b),
                        high[state] + PINS + (PINS - 1) * a + b);
                    // Old pending second-roll bonuses survive one strike roll.
                    int target = 2 + b, bonus = PINS * (1 + a);
                    put(nextLow, nextHigh, target, low[state] + bonus, high[state] + bonus);
                }
            }
            int[] temp = low;
            low = nextLow;
            nextLow = temp;
            temp = high;
            high = nextHigh;
            nextHigh = temp;
        }
        int last = nextInt(), answerLow = INF, answerHigh = -1;
        for (int state = 0; state < STATES; state++) {
            if (high[state] < 0)
                continue;
            int a = (state + 1) / 2, b = state / 2, lower, upper;
            if (last < PINS) {
                lower = b * last;
                upper = a * last;
            } else if (last <= 2 * PINS) {
                lower = PINS * b;
                upper = PINS * a + b * (last - PINS);
            } else {
                lower = PINS * (a + b);
                upper = lower;
            }
            answerLow = Math.min(answerLow, low[state] + last + lower);
            answerHigh = Math.max(answerHigh, high[state] + last + upper);
        }
        System.out.println(answerLow + " " + answerHigh);
    }
}
