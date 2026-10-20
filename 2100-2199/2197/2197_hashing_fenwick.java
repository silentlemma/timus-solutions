import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Main {
    static final long MOD = 1000000007L;
    static final long OTHER_MOD = 1000000009L;
    static final long BASE = 911382323L;
    static final int WORD_BITS = 64;
    static final int CACHE_LIMIT = 1024;

    static final class Hash {
        final long a, b;

        Hash(long a, long b) {
            this.a = a;
            this.b = b;
        }
        Hash add(Hash h) { return new Hash((a + h.a) % MOD, (b + h.b) % OTHER_MOD); }
        Hash sub(Hash h) {
            return new Hash((a - h.a + MOD) % MOD, (b - h.b + OTHER_MOD) % OTHER_MOD);
        }
        Hash mul(Hash h) { return new Hash(a * h.a % MOD, b * h.b % OTHER_MOD); }
        boolean same(Hash h) { return a == h.a && b == h.b; }
    }

    static final Hash ZERO = new Hash(0, 0);
    static final Hash ONE = new Hash(1, 1);

    static final class Positions {
        final long[] low, middle;
        long top;

        Positions(int n) {
            low = new long[n / WORD_BITS + 1];
            middle = new long[low.length / WORD_BITS + 1];
            insert(0);
        }

        static int highest(long bits) { return WORD_BITS - 1 - Long.numberOfLeadingZeros(bits); }
        static long below(int bit) { return bit == 0 ? 0 : -1L >>> (WORD_BITS - bit); }

        void insert(int position) {
            int block = position / WORD_BITS, group = block / WORD_BITS;
            low[block] |= 1L << (position % WORD_BITS);
            middle[group] |= 1L << (block % WORD_BITS);
            top |= 1L << group;
        }

        void erase(int position) {
            int block = position / WORD_BITS, group = block / WORD_BITS;
            low[block] &= ~(1L << (position % WORD_BITS));
            if (low[block] == 0) {
                middle[group] &= ~(1L << (block % WORD_BITS));
                if (middle[group] == 0) {
                    top &= ~(1L << group);
                }
            }
        }

        int predecessor(int position) {
            int block = position / WORD_BITS;
            long bits = low[block] & (-1L >>> (WORD_BITS - 1 - position % WORD_BITS));
            if (bits == 0) {
                int group = block / WORD_BITS;
                long groups = middle[group] & below(block % WORD_BITS);
                if (groups == 0) {
                    group = highest(top & below(group));
                    groups = middle[group];
                }
                block = group * WORD_BITS + highest(groups);
                bits = low[block];
            }
            return block * WORD_BITS + highest(bits);
        }
    }

    static final class Solver {
        final int n;
        final long[] hashes, otherHashes, power, otherPower;
        final long[] values, otherValues, fenwick, otherFenwick;
        final int[] following, sources, primes;
        final Positions positions;
        final Map<Integer, Hash> multipliers = new HashMap<>();
        final Map<Long, Long> cache = new HashMap<>();
        Hash whole;

        Solver(int n, CharSequence text) {
            this.n = n;
            hashes = new long[text.length() + 1];
            otherHashes = new long[text.length() + 1];
            power = new long[n + 1];
            otherPower = new long[n + 1];
            power[0] = otherPower[0] = 1;
            for (int i = 0; i < n; ++i) {
                power[i + 1] = power[i] * BASE % MOD;
                otherPower[i + 1] = otherPower[i] * BASE % OTHER_MOD;
            }
            for (int i = 0; i < text.length(); ++i) {
                hashes[i + 1] = (hashes[i] * BASE + text.charAt(i)) % MOD;
                otherHashes[i + 1] = (otherHashes[i] * BASE + text.charAt(i)) % OTHER_MOD;
            }
            values = new long[n + 1];
            otherValues = new long[n + 1];
            fenwick = new long[n + 1];
            otherFenwick = new long[n + 1];
            following = new int[n + 1];
            sources = new int[n + 1];
            java.util.Arrays.fill(following, n);
            positions = new Positions(n);
            whole = new Hash(hashes[n], otherHashes[n]);
            values[0] = whole.a;
            otherValues[0] = whole.b;
            for (int i = 1; i <= n; i *= 2) {
                fenwick[i] = whole.a;
                otherFenwick[i] = whole.b;
            }
            java.util.ArrayList<Integer> factors = new java.util.ArrayList<>();
            int remaining = n;
            for (int divisor = 2; divisor * divisor <= remaining; ++divisor) {
                if (remaining % divisor == 0) {
                    factors.add(divisor);
                    while (remaining % divisor == 0) {
                        remaining /= divisor;
                    }
                }
            }
            if (remaining > 1) {
                factors.add(remaining);
            }
            primes = new int[factors.size()];
            for (int i = 0; i < primes.length; ++i) {
                primes[i] = factors.get(i);
            }
        }

        // Static slices are weighted by their positions in the current string.
        Hash fingerprint(int source, int left, int right) {
            int length = right - left;
            long a = (hashes[source + length] - hashes[source] * power[length] % MOD + MOD) % MOD;
            long b = (otherHashes[source + length] -
                      otherHashes[source] * otherPower[length] % OTHER_MOD + OTHER_MOD) %
                     OTHER_MOD;
            return new Hash(a * power[n - right] % MOD, b * otherPower[n - right] % OTHER_MOD);
        }

        void setValue(int position, Hash value) {
            long a = value.a - values[position], b = value.b - otherValues[position];
            // Raw sums stay below the maximum length times the modulus.
            for (int i = position + 1; i <= n; i += i & -i) {
                fenwick[i] += a;
                otherFenwick[i] += b;
            }
            values[position] = value.a;
            otherValues[position] = value.b;
        }

        void replace(int begin, int end, int source) {
            int start = positions.predecessor(begin);
            Hash removed = ZERO;
            for (int position = start; position < end; position = following[position]) {
                int left = Math.max(position, begin), right = Math.min(following[position], end);
                Hash piece = left == position && right == following[position]
                                 ? new Hash(values[position], otherValues[position])
                                 : fingerprint(sources[position] + left - position, left, right);
                removed = removed.add(piece);
            }
            Hash replacement = fingerprint(source, begin, end);
            Hash delta = replacement.sub(removed);
            if (delta.same(ZERO) && end <= following[start]) {
                return;
            }
            whole = whole.add(delta);
            for (int position = start; position < end;) {
                int stop = following[position], oldSource = sources[position];
                if (position < begin) {
                    setValue(position, fingerprint(oldSource, position, begin));
                    following[position] = begin;
                } else if (position != begin) {
                    setValue(position, ZERO);
                    positions.erase(position);
                }
                if (end < stop) {
                    sources[end] = oldSource + end - position;
                    following[end] = stop;
                    setValue(end, fingerprint(sources[end], end, stop));
                    positions.insert(end);
                }
                position = stop;
            }
            sources[begin] = source;
            following[begin] = end;
            setValue(begin, replacement);
            positions.insert(begin);
        }

        Hash prefix(int length) {
            int position = positions.predecessor(length - 1);
            long a = 0, b = 0;
            for (int i = position; i > 0; i -= i & -i) {
                a += fenwick[i];
                b += otherFenwick[i];
            }
            Hash last = following[position] == length
                            ? new Hash(values[position], otherValues[position])
                            : fingerprint(sources[position], position, length);
            return new Hash(a % MOD, b % OTHER_MOD).add(last);
        }

        long answer() {
            long key = whole.a * OTHER_MOD + whole.b;
            Long known = cache.get(key);
            if (known != null) {
                return known;
            }
            int period = n;
            Hash repeated = new Hash(power[n], otherPower[n]).sub(ONE);
            // Remove prime factors while the shorter prefix still generates the string.
            for (int prime : primes) {
                while (period % prime == 0) {
                    int candidate = period / prime;
                    Hash multiplier = multipliers.get(candidate);
                    if (multiplier == null) {
                        multiplier =
                            new Hash(power[candidate], otherPower[candidate])
                                .sub(ONE)
                                .mul(new Hash(power[n - candidate], otherPower[n - candidate]));
                        multipliers.put(candidate, multiplier);
                    }
                    if (!whole.mul(multiplier).same(prefix(candidate).mul(repeated))) {
                        break;
                    }
                    period = candidate;
                }
            }
            long result = (long)n * period;
            if (cache.size() == CACHE_LIMIT) {
                cache.clear();
            }
            cache.put(key, result);
            return result;
        }
    }

    static final class Input {
        final BufferedInputStream stream = new BufferedInputStream(System.in);

        int first() throws IOException {
            int c;
            do {
                c = stream.read();
            } while (c >= 0 && c <= ' ');
            return c;
        }

        int number() throws IOException {
            int c = first(), value = 0;
            while (c > ' ') {
                value = value * 10 + c - '0';
                c = stream.read();
            }
            return value;
        }

        String next() throws IOException {
            StringBuilder result = new StringBuilder();
            int c = first();
            while (c > ' ') {
                result.append((char)c);
                c = stream.read();
            }
            return result.toString();
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int n = input.number(), m = input.number(), q = input.number();
        StringBuilder text = new StringBuilder(input.next());
        int[] starts = new int[m + 1], lengths = new int[m + 1];
        lengths[0] = n;
        for (int i = 1; i <= m; ++i) {
            String part = input.next();
            starts[i] = text.length();
            lengths[i] = part.length();
            text.append(part);
        }
        Solver solver = new Solver(n, text);
        StringBuilder output = new StringBuilder();
        output.append(solver.answer()).append('\n');
        for (int i = 0; i < q; ++i) {
            int begin = input.number() - 1, index = input.number();
            solver.replace(begin, begin + lengths[index], starts[index]);
            output.append(solver.answer()).append('\n');
        }
        System.out.print(output);
    }
}
