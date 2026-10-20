import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Main {
    private static final int MAX_VALUE = 100;
    private static final long UNREACHABLE = -1;

    private static class FastInput {
        private final BufferedInputStream input = new BufferedInputStream(System.in);

        int nextInt() throws IOException {
            int value = 0;
            int ch = input.read();
            while (ch <= ' ') {
                ch = input.read();
            }
            while (ch > ' ') {
                value = value * 10 + ch - '0';
                ch = input.read();
            }
            return value;
        }
    }

    private static class Line {
        final long slope;
        final long intercept;

        Line(long slope, long intercept) {
            this.slope = slope;
            this.intercept = intercept;
        }

        long value(long day) {
            return slope * day + intercept;
        }
    }

    private static class Rich {
        final int day;
        final int income;
        final long money;

        Rich(int day, int income, long money) {
            this.day = day;
            this.income = income;
            this.money = money;
        }
    }

    private static List<Line> makeHull(List<Line> lines) {
        lines.sort(Comparator.comparingLong((Line line) -> line.slope)
                .thenComparingLong(line -> line.intercept));
        List<Line> hull = new ArrayList<>();
        for (Line line : lines) {
            if (!hull.isEmpty() && hull.get(hull.size() - 1).slope == line.slope) {
                if (hull.get(hull.size() - 1).intercept >= line.intercept) {
                    continue;
                }
                hull.remove(hull.size() - 1);
            }
            while (hull.size() >= 2) {
                Line a = hull.get(hull.size() - 2);
                Line b = hull.get(hull.size() - 1);
                if ((a.intercept - b.intercept) * (line.slope - b.slope)
                        < (b.intercept - line.intercept) * (b.slope - a.slope)) {
                    break;
                }
                hull.remove(hull.size() - 1);
            }
            hull.add(line);
        }
        return hull;
    }

    private static long maximum(List<Line> hull, long day) {
        int left = 0;
        int right = hull.size() - 1;
        while (left < right) {
            int middle = (left + right) / 2;
            if (hull.get(middle).value(day) <= hull.get(middle + 1).value(day)) {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        return hull.get(left).value(day);
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int count = input.nextInt();
        int[] best = new int[MAX_VALUE + 1];
        for (int i = 0; i < count; ++i) {
            int cost = input.nextInt();
            best[cost] = Math.max(best[cost], input.nextInt());
        }
        int[] costs = new int[MAX_VALUE];
        int[] incomes = new int[MAX_VALUE];
        int optionCount = 0;
        int peak = 0;
        for (int cost = 1; cost <= MAX_VALUE; ++cost) {
            if (best[cost] > peak) {
                peak = best[cost];
                costs[optionCount] = cost;
                incomes[optionCount] = peak;
                ++optionCount;
            }
        }
        int cap = costs[optionCount - 1];
        int topIncome = incomes[optionCount - 1];
        int length = cap + 1;
        int stateCount = cap + 2 * topIncome + 1;
        long[] current = new long[stateCount];
        Arrays.fill(current, UNREACHABLE);
        current[0] = 0;
        List<List<Line>> workEvents = new ArrayList<>();
        List<Rich> rich = new ArrayList<>();
        int day = 0;
        boolean active = true;
        while (active) {
            long[] following = new long[stateCount];
            Arrays.fill(following, UNREACHABLE);
            List<Line> events = new ArrayList<>();
            long greatest = UNREACHABLE;
            for (int income = stateCount - 1; income >= 0; --income) {
                long money = current[income];
                if (money <= greatest) {
                    continue;
                }
                greatest = money;
                if (income >= cap && money >= cap) {
                    rich.add(new Rich(day, income, money));
                    continue;
                }
                events.add(new Line(income + 1, money - (long) (income + 1) * day));
                // Move any affordable purchase before the next work day.
                if (money < cap) {
                    following[income] = Math.max(following[income], money + income + 1);
                }
                for (int option = 0; option < optionCount; ++option) {
                    int cost = costs[option];
                    if (cost > money) {
                        break;
                    }
                    int target = income + incomes[option];
                    following[target] = Math.max(following[target], money - cost + income);
                }
            }
            workEvents.add(events);
            current = following;
            ++day;
            active = false;
            for (long money : current) {
                if (money >= 0) {
                    active = true;
                    break;
                }
            }
        }
        int limit = workEvents.size() - 1 + length;
        long[] suffix = new long[limit + 1];
        for (int remaining = 0; remaining < limit; ++remaining) {
            long gain = 1;
            for (int option = 0; option < optionCount; ++option) {
                gain = Math.max(gain, (long) incomes[option] * remaining - costs[option]);
            }
            suffix[remaining + 1] = suffix[remaining] + gain;
        }
        long correction = suffix[length] - (long) topIncome * length * (length - 1) / 2
                + (long) cap * length;
        long[] answers = new long[limit + 1];
        long[] workBest = new long[stateCount];
        boolean[] workPresent = new boolean[stateCount];
        for (int horizon = 0; horizon <= limit; ++horizon) {
            if (horizon < workEvents.size()) {
                for (Line line : workEvents.get(horizon)) {
                    int slope = (int) line.slope;
                    if (!workPresent[slope] || line.intercept > workBest[slope]) {
                        workBest[slope] = line.intercept;
                        workPresent[slope] = true;
                    }
                }
            }
            for (int slope = 0; slope < stateCount; ++slope) {
                if (workPresent[slope]) {
                    answers[horizon] = Math.max(answers[horizon],
                            (long) slope * horizon + workBest[slope]);
                }
            }
        }
        List<Line> lines = new ArrayList<>();
        for (Rich state : rich) {
            for (int remaining = 0; remaining <= limit - state.day; ++remaining) {
                int horizon = state.day + remaining;
                long candidate = state.money + (long) state.income * remaining + suffix[remaining];
                answers[horizon] = Math.max(answers[horizon], candidate);
            }
            long slope = state.income - (long) topIncome * state.day;
            long intercept = state.money - (long) state.income * state.day
                    + (long) topIncome * state.day * (state.day + 1) / 2;
            lines.add(new Line(slope, intercept + (long) cap * state.day + correction));
        }
        List<Line> richHull = makeHull(lines);
        lines = new ArrayList<>();
        for (int slope = 0; slope < stateCount; ++slope) {
            if (workPresent[slope]) {
                lines.add(new Line(slope, workBest[slope]));
            }
        }
        List<Line> workHull = makeHull(lines);
        count = input.nextInt();
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < count; ++i) {
            long horizon = input.nextInt();
            long answer;
            if (horizon <= limit) {
                answer = answers[(int) horizon];
            } else {
                long common = topIncome * horizon * (horizon - 1) / 2 - cap * horizon;
                answer = Math.max(maximum(workHull, horizon), common + maximum(richHull, horizon));
            }
            output.append(answer).append('\n');
        }
        System.out.print(output);
    }
}
