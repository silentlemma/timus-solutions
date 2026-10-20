import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashSet;

public class Main {
    private static final int LETTERS = 26;
    private static final int ALPHABET = LETTERS + 1;
    private static final int BUFFER_SIZE = 65536;
    private static final int INF = Integer.MAX_VALUE;

    private static final class FastScanner {
        private final BufferedInputStream input = new BufferedInputStream(System.in, BUFFER_SIZE);

        String next() throws IOException {
            StringBuilder token = new StringBuilder();
            int character;
            do {
                character = input.read();
            } while (character >= 0 && character <= ' ');
            while (character > ' ') {
                token.append((char) character);
                character = input.read();
            }
            return token.toString();
        }
    }

    private static final class Automaton {
        final int[] next;
        final int[] length;
        final int[] link;
        final int[] firstEnd;
        final int[] negative;
        final int[] missing;
        final HashSet<Integer>[] bags;
        int size = 1;

        @SuppressWarnings("unchecked")
        Automaton(int capacity, int teamCount) {
            next = new int[capacity * ALPHABET];
            length = new int[capacity];
            link = new int[capacity];
            firstEnd = new int[capacity];
            negative = new int[capacity];
            missing = new int[capacity];
            bags = (HashSet<Integer>[]) new HashSet<?>[capacity];
            Arrays.fill(firstEnd, INF);
            Arrays.fill(negative, teamCount);
            Arrays.fill(missing, 1);
            link[0] = -1;
        }

        int cloneState(int state, int newLength) {
            int clone = size++;
            length[clone] = newLength;
            link[clone] = link[state];
            System.arraycopy(next, state * ALPHABET, next, clone * ALPHABET, ALPHABET);
            return clone;
        }

        int extend(int last, int character) {
            int parent = last;
            int target = next[parent * ALPHABET + character];
            if (target != 0) {
                if (length[parent] + 1 == length[target]) {
                    return target;
                }
                int clone = cloneState(target, length[parent] + 1);
                while (parent >= 0 && next[parent * ALPHABET + character] == target) {
                    next[parent * ALPHABET + character] = clone;
                    parent = link[parent];
                }
                link[target] = clone;
                return clone;
            }

            int current = size++;
            length[current] = length[last] + 1;
            while (parent >= 0 && next[parent * ALPHABET + character] == 0) {
                next[parent * ALPHABET + character] = current;
                parent = link[parent];
            }
            if (parent < 0) {
                return current;
            }
            target = next[parent * ALPHABET + character];
            if (length[parent] + 1 == length[target]) {
                link[current] = target;
                return current;
            }
            int clone = cloneState(target, length[parent] + 1);
            while (parent >= 0 && next[parent * ALPHABET + character] == target) {
                next[parent * ALPHABET + character] = clone;
                parent = link[parent];
            }
            link[target] = clone;
            link[current] = clone;
            return current;
        }
    }

    public static void main(String[] arguments) throws IOException {
        FastScanner scanner = new FastScanner();
        int teamCount = Integer.parseInt(scanner.next());
        String[] names = new String[teamCount];
        boolean[] positive = new boolean[teamCount];
        int totalLength = 0;
        for (int team = 0; team < teamCount; ++team) {
            String token = scanner.next();
            positive[team] = token.charAt(token.length() - 1) == '+';
            names[team] = positive[team] ? token.substring(0, token.length() - 1) : token;
            totalLength += names[team].length();
        }

        Automaton automaton = new Automaton(2 * totalLength + 1, teamCount);
        int[] positiveTimes = new int[teamCount + 1];
        int positiveCount = 0;
        for (int team = 0; team < teamCount; ++team) {
            if (team > 0 && positive[team]) {
                positiveTimes[++positiveCount] = team;
            }
            int last = 0;
            for (int position = 0; position < names[team].length(); ++position) {
                char letter = names[team].charAt(position);
                int character = letter == '_' ? LETTERS : letter - 'a';
                last = automaton.extend(last, character);
                if (team == 0) {
                    automaton.firstEnd[last] = Math.min(automaton.firstEnd[last], position);
                } else if (positive[team]) {
                    if (automaton.bags[last] == null) {
                        automaton.bags[last] = new HashSet<>(2);
                    }
                    automaton.bags[last].add(positiveCount);
                } else {
                    automaton.negative[last] = Math.min(automaton.negative[last], team);
                }
            }
        }
        positiveTimes[positiveCount + 1] = teamCount;

        int[] counts = new int[totalLength + 1];
        for (int state = 0; state < automaton.size; ++state) {
            ++counts[automaton.length[state]];
        }
        for (int index = 1; index < counts.length; ++index) {
            counts[index] += counts[index - 1];
        }
        int[] order = new int[automaton.size];
        for (int state = 0; state < automaton.size; ++state) {
            order[--counts[automaton.length[state]]] = state;
        }

        int[] bestLength = new int[teamCount + 1];
        int[] bestLeft = new int[teamCount + 1];
        Arrays.fill(bestLength, INF);
        Arrays.fill(bestLeft, INF);
        // Suffix links collect all teams containing a state's substrings.
        for (int index = automaton.size - 1; index > 0; --index) {
            int state = order[index];
            HashSet<Integer> bag = automaton.bags[state];
            int absent = automaton.missing[state];
            if (bag != null) {
                while (bag.contains(absent)) {
                    ++absent;
                }
            }
            // Every substring in this state stops working at the same arrival.
            int deadline = Math.min(automaton.negative[state], positiveTimes[absent]);
            int parent = automaton.link[state];
            int candidateLength = automaton.length[parent] + 1;
            if (automaton.firstEnd[state] != INF) {
                int left = automaton.firstEnd[state] - candidateLength + 1;
                if (candidateLength < bestLength[deadline]
                        || candidateLength == bestLength[deadline] && left < bestLeft[deadline]) {
                    bestLength[deadline] = candidateLength;
                    bestLeft[deadline] = left;
                }
            }

            automaton.firstEnd[parent] = Math.min(automaton.firstEnd[parent],
                    automaton.firstEnd[state]);
            automaton.negative[parent] = Math.min(automaton.negative[parent],
                    automaton.negative[state]);
            automaton.missing[parent] = Math.max(automaton.missing[parent], absent);
            if (bag != null) {
                HashSet<Integer> target = automaton.bags[parent];
                if (target == null) {
                    automaton.bags[parent] = bag;
                } else {
                    if (target.size() < bag.size()) {
                        HashSet<Integer> temporary = target;
                        target = bag;
                        bag = temporary;
                    }
                    target.addAll(bag);
                    automaton.bags[parent] = target;
                }
                automaton.bags[state] = null;
            }
        }

        for (int time = teamCount - 1; time > 0; --time) {
            if (bestLength[time + 1] < bestLength[time]
                    || bestLength[time + 1] == bestLength[time]
                    && bestLeft[time + 1] < bestLeft[time]) {
                bestLength[time] = bestLength[time + 1];
                bestLeft[time] = bestLeft[time + 1];
            }
        }
        StringBuilder output = new StringBuilder();
        for (int team = 0; team < teamCount; ++team) {
            int length = bestLength[team + 1];
            int left = bestLeft[team + 1];
            if (length == INF) {
                output.append("-1 -1\n");
            } else {
                output.append(left).append(' ').append(left + length - 1).append('\n');
            }
        }
        System.out.print(output);
    }
}
