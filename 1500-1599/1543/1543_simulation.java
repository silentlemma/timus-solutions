import java.io.*;
import java.util.*;

public class Main {
    static final int PERFECT = 0, GREAT = 1, GOOD = 2, BOO = 3, MISS = 4;
    static final String[] NAMES = {"Perfect", "Great", "Good", "Boo", "Miss"};
    static final long[] SCORE = {10, 5, 0, 0, 0};  // p
    static final long[] COMBO = {55, 33, 0, 0, 0}; // q
    static final int[] DANCE = {2, 1, 0, -4, -5};  // dance points
    static final long BASE_SCORE = 1000000, PERCENT = 100;
    // level bonuses: share of the most dance points needed, in percent
    static final long[] SHARES = {80, 64, 50};
    static final long[] SHARE_BONUS = {100000, 10000, 1000};
    static final long ALL_PERFECT = 10000000, ALL_GREAT = 1000000, LOW = 100;
    static final int SLOWEST = 1000; // ms per beat on Easy, halved on each harder level
    static final int TENTHS = 10;
    static final int PERFECT_TENTHS = 4; // under 40 % of the period
    static final int GREAT_TENTHS = 7;   // under 70 %
    static final List<String> LEVELS = Arrays.asList("Easy", "Medium", "Hard");
    static final String SEPARATOR = "--------------------";
    static final int HEADER = 3; // tokens before the log: duration, level, beats
    static final long KEY = 256; // a press is time * KEY + key, so that sorting goes by time

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        List<String> tokens = new ArrayList<>();
        for (String line; (line = in.readLine()) != null;)
            for (StringTokenizer st = new StringTokenizer(line); st.hasMoreTokens();)
                tokens.add(st.nextToken());
        String level = tokens.get(1), beats = tokens.get(2);
        int index = LEVELS.indexOf(level), diff = index + 1, period = SLOWEST >> index;
        int presses = (tokens.size() - HEADER) / 2;
        long[] log = new long[presses];
        for (int i = 0; i < presses; i++) {
            long time = Long.parseLong(tokens.get(HEADER + 2 * i));
            log[i] = time * KEY + tokens.get(HEADER + 2 * i + 1).charAt(0);
        }
        Arrays.sort(log);
        long steps = beats.chars().filter(b -> b != 'N').count();
        long unit = diff * BASE_SCORE / (steps * (steps + 1) / 2); // B div S
        long[] counts = new long[NAMES.length];
        long stage = 0, comboBonus = 0, run = 0, n = 0;
        int points = 0, k = 0; // k: the first logged press not before the current beat
        boolean wentNegative = false;
        for (int i = 0; i < beats.length(); i++) {
            long start = (long)i * period, end = start + period;
            while (k < presses && log[k] / KEY < start)
                k++;
            if (beats.charAt(i) == 'N')
                continue;
            n++;
            // only the first press within the beat counts
            int mark;
            if (k == presses || log[k] / KEY >= end)
                mark = BOO;
            else if (log[k] % KEY != beats.charAt(i))
                mark = MISS;
            else {
                long elapsed = log[k] / KEY - start;
                mark = TENTHS * elapsed < PERFECT_TENTHS * period ? PERFECT
                       : TENTHS * elapsed < GREAT_TENTHS * period ? GREAT
                                                                  : GOOD;
            }
            counts[mark]++;
            stage += SCORE[mark] * n * unit;
            run = mark <= GOOD ? run + 1 : 0;
            comboBonus += COMBO[mark] * run;
            points += DANCE[mark];
            wentNegative = wentNegative || points < 0;
        }
        long most = DANCE[PERFECT] * steps, bonus = LOW;
        if (wentNegative)
            bonus = 0;
        else if (counts[PERFECT] == steps)
            bonus = ALL_PERFECT;
        else if (counts[PERFECT] + counts[GREAT] == steps)
            bonus = ALL_GREAT;
        else
            for (int i = SHARES.length - 1; i >= 0; i--)
                if (PERCENT * points >= SHARES[i] * most)
                    bonus = SHARE_BONUS[i];
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < NAMES.length; i++)
            out.append(NAMES[i]).append(": ").append(counts[i]).append('\n');
        out.append(SEPARATOR).append('\n');
        out.append("Stage Score: ").append(stage).append('\n');
        out.append("Combo Bonus: ").append(comboBonus).append('\n');
        out.append("Dance Level Bonus: ").append(bonus).append('\n');
        out.append("Total Score: ").append(stage + comboBonus + bonus).append('\n');
        System.out.print(out);
    }
}
