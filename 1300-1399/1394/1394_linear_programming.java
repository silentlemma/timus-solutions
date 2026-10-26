import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int SIMPLEX_ITERATION_LIMIT = 1000;
    static final int FILLING_COUNT_LIMIT = 1000000;
    static final int FAILED_STATE_LIMIT = 100000;
    static final int INITIAL_EXACT_BUDGET = 2000;
    static final int BUDGET_BITS = 60;
    static final long MAX_EXACT_BUDGET = 1L << BUDGET_BITS;
    static final double SIMPLEX_EPSILON = 1e-8;
    static final double ELIMINATION_EPSILON = 1e-12;
    static final double FEASIBILITY_EPSILON = 1e-7;
    static final double PRICING_EPSILON = 1e-10;
    static final double INFINITE_PRICE = 1e30;
    static final int RANDOM_SEED = 12345;
    static final int INITIAL_GREEDY_ATTEMPTS = 6;
    static final int RETRY_GREEDY_ATTEMPTS = 16;
    static final int PRICING_WORK_LIMIT = 160;
    static final int COLUMN_ITERATION_LIMIT = 60;
    static final int MAX_LENGTH = 100;
    static final int WORD_BITS = 64;
    static final int WORD_SHIFT = 6;
    static final int WORD_MASK = WORD_BITS - 1;
    static final int INT_BITS = 32;
    static final long UNSIGNED_INT = 0xffffffffL;
    static final long INT_RANGE = 1L << INT_BITS;

    static boolean get(long[] words, int sum) {
        return sum >= 0
                && (sum >>> WORD_SHIFT) < words.length
                && ((words[sum >>> WORD_SHIFT] >>> (sum & WORD_MASK)) & 1) != 0;
    }

    // Descending updates add one ship without reusing its newly reached sums.
    static void add(long[] words, int shift) {
        int wordShift = shift >>> WORD_SHIFT;
        int bitShift = shift & WORD_MASK;
        for (int i = words.length - 1; i >= wordShift; --i) {
            words[i] |=
                    words[i - wordShift] << bitShift
                            | (bitShift != 0 && i > wordShift
                                    ? words[i - wordShift - 1] >>> (WORD_BITS - bitShift)
                                    : 0);
        }
    }

    static void swap(int[] values, int left, int right) {
        int value = values[left];
        values[left] = values[right];
        values[right] = value;
    }

    // This is std::mt19937, including its unsigned seeding and tempering steps.
    static final class MersenneTwister {
        static final int STATE_SIZE = 624;
        static final int RECURRENCE_OFFSET = 397;
        static final int SEED_SHIFT = 30;
        static final int SEED_MULTIPLIER = 1812433253;
        static final int UPPER_MASK = 0x80000000;
        static final int LOWER_MASK = 0x7fffffff;
        static final int TWIST_MASK = 0x9908b0df;
        static final int TEMPER_FIRST = 11;
        static final int TEMPER_SECOND = 7;
        static final int TEMPER_THIRD = 15;
        static final int TEMPER_LAST = 18;
        static final int TEMPER_SECOND_MASK = 0x9d2c5680;
        static final int TEMPER_THIRD_MASK = 0xefc60000;
        final int[] state = new int[STATE_SIZE];
        int position = STATE_SIZE;

        MersenneTwister() {
            state[0] = RANDOM_SEED;
            for (int i = 1; i < STATE_SIZE; ++i) {
                state[i] = SEED_MULTIPLIER * (state[i - 1] ^ (state[i - 1] >>> SEED_SHIFT)) + i;
            }
        }

        int next() {
            if (position == STATE_SIZE) {
                for (int i = 0; i < STATE_SIZE; ++i) {
                    int bits = (state[i] & UPPER_MASK) | (state[(i + 1) % STATE_SIZE] & LOWER_MASK);
                    state[i] =
                            state[(i + RECURRENCE_OFFSET) % STATE_SIZE]
                                    ^ (bits >>> 1)
                                    ^ ((bits & 1) != 0 ? TWIST_MASK : 0);
                }
                position = 0;
            }
            int value = state[position++];
            value ^= value >>> TEMPER_FIRST;
            value ^= (value << TEMPER_SECOND) & TEMPER_SECOND_MASK;
            value ^= (value << TEMPER_THIRD) & TEMPER_THIRD_MASK;
            return value ^ (value >>> TEMPER_LAST);
        }

        // libstdc++ uses Lemire's multiply-and-reject mapping for a 32-bit engine.
        int bounded(int bound) {
            long product = (next() & UNSIGNED_INT) * bound;
            long low = product & UNSIGNED_INT;
            if (low < bound) {
                long threshold = INT_RANGE % bound;
                while (low < threshold) {
                    product = (next() & UNSIGNED_INT) * bound;
                    low = product & UNSIGNED_INT;
                }
            }
            return (int) (product >>> INT_BITS);
        }

        // libstdc++ shuffles two positions per draw when the range fits the engine.
        void shuffle(int[] values, int size) {
            if (size == 0) {
                return;
            }
            int position = 1;
            if ((size & 1) == 0) {
                swap(values, position++, bounded(2));
            }
            while (position < size) {
                int range = position + 1;
                int combined = bounded(range * (range + 1));
                swap(values, position++, combined / (range + 1));
                swap(values, position++, combined % (range + 1));
            }
        }
    }

    // Primal simplex maximizes filled rows; slack variables give a feasible zero basis.
    // Floating point only guides branching; the exact search never relies on it.
    static final class LinearProgram {
        final int constraintCount;
        final int columnCount;
        final double[][] tableau;
        final int[] basis;

        LinearProgram(int constraints, int columns) {
            constraintCount = constraints;
            columnCount = columns;
            tableau = new double[constraints + 1][columns + constraints + 1];
            basis = new int[constraints];
            for (int i = 0; i < constraints; ++i) {
                tableau[i][columns + i] = 1;
                basis[i] = columns + i;
            }
        }

        void solve() {
            int rhsColumn = columnCount + constraintCount;
            double[] objective = tableau[constraintCount];
            for (int iteration = 0; iteration < SIMPLEX_ITERATION_LIMIT; ++iteration) {
                int pivotColumn = -1;
                for (int j = 0; j < rhsColumn; ++j) {
                    if (objective[j] < -SIMPLEX_EPSILON
                            && (pivotColumn < 0 || objective[j] < objective[pivotColumn])) {
                        pivotColumn = j;
                    }
                }
                if (pivotColumn < 0) {
                    return;
                }
                int pivotRow = -1;
                double ratio = 0;
                for (int i = 0; i < constraintCount; ++i) {
                    if (tableau[i][pivotColumn] > SIMPLEX_EPSILON) {
                        double candidateRatio = tableau[i][rhsColumn] / tableau[i][pivotColumn];
                        if (pivotRow < 0
                                || candidateRatio < ratio - SIMPLEX_EPSILON
                                || (Math.abs(candidateRatio - ratio) < SIMPLEX_EPSILON
                                        && basis[i] < basis[pivotRow])) {
                            pivotRow = i;
                            ratio = candidateRatio;
                        }
                    }
                }
                if (pivotRow < 0) {
                    return;
                }
                double[] pivot = tableau[pivotRow];
                double pivotValue = pivot[pivotColumn];
                for (int j = 0; j <= rhsColumn; ++j) {
                    pivot[j] /= pivotValue;
                }
                for (int i = 0; i <= constraintCount; ++i) {
                    if (i != pivotRow) {
                        double[] target = tableau[i];
                        double factor = target[pivotColumn];
                        if (Math.abs(factor) > ELIMINATION_EPSILON) {
                            for (int j = 0; j <= rhsColumn; ++j) {
                                target[j] -= factor * pivot[j];
                            }
                            target[pivotColumn] = 0;
                        }
                    }
                }
                basis[pivotRow] = pivotColumn;
            }
        }
    }

    // Stable primitive mergesort preserves enumeration order when scores tie.
    static void sortByScore(int[] order, double[] scores) {
        int[] buffer = new int[order.length];
        for (int width = 1; width < order.length; width *= 2) {
            for (int start = 0; start < order.length; start += 2 * width) {
                int middle = Math.min(start + width, order.length);
                int end = Math.min(start + 2 * width, order.length);
                int left = start;
                int right = middle;
                for (int j = start; j < end; ++j) {
                    if (right == end
                            || (left < middle && !(scores[order[right]] > scores[order[left]]))) {
                        buffer[j] = order[left++];
                    } else {
                        buffer[j] = order[right++];
                    }
                }
            }
            System.arraycopy(buffer, 0, order, 0, order.length);
        }
    }

    // Exact keys pack each count in only the bits needed for its original multiplicity.
    // Linear probing compares every packed word, so hash collisions cannot prune solutions.
    static final class FailedStates {
        static final int INITIAL_CAPACITY = 16;
        static final int HASH_SHIFT = 33;
        static final long HASH_MULTIPLIER = 0xff51afd7ed558ccdL;
        final int[] widths;
        final int rowBits;
        final int keyWords;
        long[] keys;
        int[] occupied;
        int size;

        FailedStates(int[] counts, int rows) {
            rowBits = rows;
            widths = new int[counts.length];
            int bits = rows;
            for (int i = 0; i < counts.length; ++i) {
                widths[i] = INT_BITS - Integer.numberOfLeadingZeros(counts[i]);
                bits += widths[i];
            }
            keyWords = (bits + WORD_BITS - 1) / WORD_BITS;
            keys = new long[INITIAL_CAPACITY * keyWords];
            occupied = new int[INITIAL_CAPACITY];
        }

        long[] key(int[] counts, int activeRows) {
            long[] result = new long[keyWords];
            result[0] = activeRows;
            int bit = rowBits;
            for (int i = 0; i < counts.length; ++i) {
                int word = bit >>> WORD_SHIFT;
                int offset = bit & WORD_MASK;
                result[word] |= (long) counts[i] << offset;
                if (offset + widths[i] > WORD_BITS) {
                    result[word + 1] |= (long) counts[i] >>> (WORD_BITS - offset);
                }
                bit += widths[i];
            }
            return result;
        }

        int slot(long[] key) {
            long hash = 0;
            for (long word : key) {
                hash = (hash ^ word) * HASH_MULTIPLIER;
                hash ^= hash >>> HASH_SHIFT;
            }
            int mask = occupied.length - 1;
            int slot = (int) hash & mask;
            while (occupied[slot] != 0) {
                int i = 0;
                while (i < keyWords && keys[slot * keyWords + i] == key[i]) {
                    ++i;
                }
                if (i == keyWords) {
                    return slot;
                }
                slot = (slot + 1) & mask;
            }
            return slot;
        }

        boolean contains(long[] key) {
            return occupied[slot(key)] != 0;
        }

        void insert(long[] key) {
            if (size >= FAILED_STATE_LIMIT) {
                return;
            }
            if ((size + 1) * 2 > occupied.length) {
                long[] previousKeys = keys;
                int[] previousOccupied = occupied;
                occupied = new int[previousOccupied.length * 2];
                keys = new long[occupied.length * keyWords];
                long[] previousKey = new long[keyWords];
                for (int j = 0; j < previousOccupied.length; ++j) {
                    if (previousOccupied[j] != 0) {
                        System.arraycopy(previousKeys, j * keyWords, previousKey, 0, keyWords);
                        int destination = slot(previousKey);
                        occupied[destination] = 1;
                        System.arraycopy(previousKey, 0, keys, destination * keyWords, keyWords);
                    }
                }
            }
            int destination = slot(key);
            if (occupied[destination] == 0) {
                occupied[destination] = 1;
                System.arraycopy(key, 0, keys, destination * keyWords, keyWords);
                ++size;
            }
        }

        void clear() {
            Arrays.fill(occupied, 0);
            size = 0;
        }
    }

    static final class Solver {
        final int rowCount;
        final int typeCount;
        final int shipCount;
        final int[] lengths;
        final int[] counts;
        final int[] rows;
        int[][] answer;
        final MersenneTwister rng = new MersenneTwister();
        FailedStates failed;
        long budget;
        boolean budgetExhausted;
        long[][][] suffix;
        byte[][] rowFillings;
        int pricingWork;

        Solver(int[] ships, int[] rowLengths) {
            shipCount = ships.length;
            rowCount = rowLengths.length;
            rows = rowLengths;
            answer = new int[rowCount][];
            int[] frequencies = new int[MAX_LENGTH + 1];
            for (int length : ships) {
                ++frequencies[length];
            }
            int distinct = 0;
            for (int frequency : frequencies) {
                if (frequency != 0) {
                    ++distinct;
                }
            }
            typeCount = distinct;
            lengths = new int[typeCount];
            counts = new int[typeCount];
            int index = 0;
            for (int length = MAX_LENGTH; length > 0; --length) {
                if (frequencies[length] != 0) {
                    lengths[index] = length;
                    counts[index++] = frequencies[length];
                }
            }
        }

        void storeRow(int row, byte[] filling) {
            int size = 0;
            for (byte copies : filling) {
                size += copies;
            }
            int[] ships = new int[size];
            int position = 0;
            for (int i = 0; i < typeCount; ++i) {
                for (int copies = 0; copies < filling[i]; ++copies) {
                    ships[position++] = lengths[i];
                }
            }
            answer[row] = ships;
        }

        byte[] fillingOf(int[] remainingCounts) {
            byte[] filling = new byte[typeCount];
            for (int i = 0; i < typeCount; ++i) {
                filling[i] = (byte) remainingCounts[i];
            }
            return filling;
        }

        // There are fewer than ten rows: libstdc++ uses stable insertion sort here.
        void sortRows(int[] order) {
            for (int i = 1; i < order.length; ++i) {
                int row = order[i];
                int j = i;
                while (j > 0 && rows[row] < rows[order[j - 1]]) {
                    order[j] = order[j - 1];
                    --j;
                }
                order[j] = row;
            }
        }

        // A cheap constructive front end. Failure makes no assertion of infeasibility.
        boolean greedy(int attemptLimit) {
            int[] order = new int[rowCount];
            for (int i = 0; i < rowCount; ++i) {
                order[i] = i;
            }
            sortRows(order);
            int[] remainingShips = new int[shipCount];
            int[] unusedShips = new int[shipCount];
            for (int attempt = 0; attempt < attemptLimit; ++attempt) {
                int remainingCount = 0;
                for (int i = 0; i < typeCount; ++i) {
                    for (int copies = 0; copies < counts[i]; ++copies) {
                        remainingShips[remainingCount++] = lengths[i];
                    }
                }
                if (attempt == 1) {
                    for (int i = 0; i < remainingCount / 2; ++i) {
                        swap(remainingShips, i, remainingCount - 1 - i);
                    }
                }
                if (attempt > 1) {
                    rng.shuffle(remainingShips, remainingCount);
                    rng.shuffle(order, rowCount - 1);
                }
                boolean completed = true;
                for (int j = 0; j < rowCount - 1; ++j) {
                    int row = order[j];
                    int remainingLength = rows[row];
                    int width = (remainingLength >>> WORD_SHIFT) + 1;
                    long[][] suffixSums = new long[remainingCount + 1][width];
                    suffixSums[remainingCount][0] = 1;
                    for (int i = remainingCount - 1; i >= 0; --i) {
                        System.arraycopy(suffixSums[i + 1], 0, suffixSums[i], 0, width);
                        add(suffixSums[i], remainingShips[i]);
                    }
                    if (!get(suffixSums[0], remainingLength)) {
                        completed = false;
                        break;
                    }
                    int unusedCount = 0;
                    int[] selected = new int[remainingCount];
                    int selectedCount = 0;
                    for (int i = 0; i < remainingCount; ++i) {
                        if (remainingShips[i] <= remainingLength
                                && get(suffixSums[i + 1], remainingLength - remainingShips[i])) {
                            selected[selectedCount++] = remainingShips[i];
                            remainingLength -= remainingShips[i];
                        } else {
                            unusedShips[unusedCount++] = remainingShips[i];
                        }
                    }
                    answer[row] = Arrays.copyOf(selected, selectedCount);
                    int[] temporary = remainingShips;
                    remainingShips = unusedShips;
                    unusedShips = temporary;
                    remainingCount = unusedCount;
                }
                if (completed) {
                    answer[order[rowCount - 1]] = Arrays.copyOf(remainingShips, remainingCount);
                    return true;
                }
            }
            return false;
        }

        // Count each multiset once; only addition is used, so saturation is safe.
        int[] countFillings(int[] remainingCounts, int maxSum, int countLimit) {
            int[] waysBySum = new int[maxSum + 1];
            int[] nextWays = new int[maxSum + 1];
            waysBySum[0] = 1;
            for (int i = 0; i < typeCount; ++i) {
                Arrays.fill(nextWays, 0);
                for (int sum = 0; sum <= maxSum; ++sum) {
                    if (waysBySum[sum] != 0) {
                        for (int copies = 0;
                                copies <= remainingCounts[i] && sum + copies * lengths[i] <= maxSum;
                                ++copies) {
                            int target = sum + copies * lengths[i];
                            nextWays[target] =
                                    Math.min(countLimit, nextWays[target] + waysBySum[sum]);
                        }
                    }
                }
                int[] temporary = waysBySum;
                waysBySum = nextWays;
                nextWays = temporary;
            }
            return waysBySum;
        }

        long[][] suffixSums(int[] remainingCounts, int target) {
            int width = (target >>> WORD_SHIFT) + 1;
            long[][] sums = new long[typeCount + 1][width];
            sums[typeCount][0] = 1;
            for (int i = typeCount - 1; i >= 0; --i) {
                System.arraycopy(sums[i + 1], 0, sums[i], 0, width);
                for (int copy = 0; copy < remainingCounts[i]; ++copy) {
                    add(sums[i], lengths[i]);
                }
            }
            return sums;
        }

        // Suffix sums prune incomplete fillings; exhausted budgets never cache failure.
        boolean enumerateExactRow(
                int[] remainingCounts,
                int activeRows,
                int depth,
                int selectedRow,
                int i,
                int remainingLength) {
            if (--budget < 0) {
                budgetExhausted = true;
                return false;
            }
            if (remainingLength == 0) {
                if (exact(remainingCounts, activeRows ^ (1 << selectedRow), depth + 1)) {
                    storeRow(selectedRow, rowFillings[depth]);
                    return true;
                }
                return false;
            }
            if (i == typeCount) {
                return false;
            }
            int availableCount = remainingCounts[i];
            for (int copies = Math.min(availableCount, remainingLength / lengths[i]);
                    copies >= 0;
                    --copies) {
                if (get(suffix[depth][i + 1], remainingLength - copies * lengths[i])) {
                    remainingCounts[i] = availableCount - copies;
                    rowFillings[depth][i] = (byte) copies;
                    if (enumerateExactRow(
                            remainingCounts,
                            activeRows,
                            depth,
                            selectedRow,
                            i + 1,
                            remainingLength - copies * lengths[i])) {
                        return true;
                    }
                    if (budgetExhausted) {
                        break;
                    }
                }
            }
            remainingCounts[i] = availableCount;
            rowFillings[depth][i] = 0;
            return false;
        }

        // Complete fallback: minimum-domain rows, exact multiset keys and no final cutoff.
        boolean exact(int[] remainingCounts, int activeRows, int depth) {
            if (--budget < 0) {
                budgetExhausted = true;
                return false;
            }
            if ((activeRows & (activeRows - 1)) == 0) {
                storeRow(Integer.numberOfTrailingZeros(activeRows), fillingOf(remainingCounts));
                return true;
            }
            long[] key = failed.key(remainingCounts, activeRows);
            if (failed.contains(key)) {
                return false;
            }
            int totalLength = 0;
            int maxSum = 0;
            for (int row = 0; row < rowCount; ++row) {
                if ((activeRows & (1 << row)) != 0) {
                    totalLength += rows[row];
                    maxSum = Math.max(maxSum, rows[row]);
                }
            }
            maxSum = Math.min(maxSum, totalLength / 2);
            int[] fillingCounts = countFillings(remainingCounts, maxSum, FILLING_COUNT_LIMIT);
            int selectedRow = -1;
            for (int row = 0; row < rowCount; ++row) {
                if ((activeRows & (1 << row)) != 0) {
                    if (fillingCounts[Math.min(rows[row], totalLength - rows[row])] == 0) {
                        return false;
                    }
                    if (rows[row] <= totalLength / 2
                            && (selectedRow < 0
                                    || fillingCounts[rows[row]]
                                            < fillingCounts[rows[selectedRow]])) {
                        selectedRow = row;
                    }
                }
            }
            int target = rows[selectedRow];
            suffix[depth] = suffixSums(remainingCounts, target);
            Arrays.fill(rowFillings[depth], (byte) 0);
            if (enumerateExactRow(remainingCounts, activeRows, depth, selectedRow, 0, target)) {
                return true;
            }
            if (!budgetExhausted) {
                failed.insert(key);
            }
            return false;
        }

        // Dual prices turn column pricing into bounded subset sum; full fillings are branched on.
        boolean generateColumns(
                int[] remainingCounts,
                int activeRows,
                int[] previousRows,
                byte[][] previousFillings,
                int previousCount) {
            if ((activeRows & (activeRows - 1)) == 0) {
                storeRow(Integer.numberOfTrailingZeros(activeRows), fillingOf(remainingCounts));
                return true;
            }
            if (pricingWork > PRICING_WORK_LIMIT) {
                return false;
            }
            int activeRowCount = Integer.bitCount(activeRows);
            int maxSum = 0;
            int[] rowConstraint = new int[rowCount];
            int constraintIndex = 0;
            for (int row = 0; row < rowCount; ++row) {
                if ((activeRows & (1 << row)) != 0) {
                    rowConstraint[row] = constraintIndex++;
                    maxSum = Math.max(maxSum, rows[row]);
                }
            }
            // At most one column per active row is added in each pricing iteration.
            int capacity = previousCount + activeRowCount * COLUMN_ITERATION_LIMIT;
            int[] columnRows = new int[capacity];
            byte[][] columnFillings = new byte[capacity][];
            int columnCount = 0;
            for (int j = 0; j < previousCount; ++j) {
                if ((activeRows & (1 << previousRows[j])) == 0) {
                    continue;
                }
                boolean fits = true;
                for (int i = 0; i < typeCount; ++i) {
                    if (previousFillings[j][i] > remainingCounts[i]) {
                        fits = false;
                        break;
                    }
                }
                if (fits) {
                    columnRows[columnCount] = previousRows[j];
                    columnFillings[columnCount++] = previousFillings[j];
                }
            }
            // Only the previous and current cost layers are needed; choices retain all layers.
            double[] minimumCost = new double[maxSum + 1];
            double[] nextCost = new double[maxSum + 1];
            byte[][] chosenCount = new byte[typeCount + 1][maxSum + 1];
            double[] shipPrices = new double[typeCount];
            double[] rowPrices = new double[rowCount];
            double[] columnWeights = null;
            boolean feasible = false;
            for (int iteration = 0;
                    iteration < COLUMN_ITERATION_LIMIT && pricingWork < PRICING_WORK_LIMIT;
                    ++iteration) {
                ++pricingWork;
                LinearProgram lp = new LinearProgram(typeCount + activeRowCount, columnCount);
                int rhsColumn = lp.columnCount + lp.constraintCount;
                for (int i = 0; i < typeCount; ++i) {
                    lp.tableau[i][rhsColumn] = remainingCounts[i];
                }
                for (int i = 0; i < activeRowCount; ++i) {
                    lp.tableau[typeCount + i][rhsColumn] = 1;
                }
                for (int j = 0; j < columnCount; ++j) {
                    int row = columnRows[j];
                    lp.tableau[typeCount + rowConstraint[row]][j] = 1;
                    lp.tableau[lp.constraintCount][j] = -1;
                    for (int i = 0; i < typeCount; ++i) {
                        lp.tableau[i][j] = columnFillings[j][i];
                    }
                }
                lp.solve();
                columnWeights = new double[columnCount];
                for (int i = 0; i < lp.constraintCount; ++i) {
                    if (lp.basis[i] < columnCount) {
                        columnWeights[lp.basis[i]] = Math.max(0, lp.tableau[i][rhsColumn]);
                    }
                }
                if (lp.tableau[lp.constraintCount][rhsColumn]
                        >= activeRowCount - FEASIBILITY_EPSILON) {
                    feasible = true;
                    break;
                }
                for (int i = 0; i < typeCount; ++i) {
                    shipPrices[i] = Math.max(0, lp.tableau[lp.constraintCount][columnCount + i]);
                }
                for (int row = 0; row < rowCount; ++row) {
                    if ((activeRows & (1 << row)) != 0) {
                        rowPrices[row] =
                                lp.tableau[lp.constraintCount][
                                        columnCount + typeCount + rowConstraint[row]];
                    }
                }
                Arrays.fill(minimumCost, INFINITE_PRICE);
                minimumCost[0] = 0;
                for (int i = 0; i < typeCount; ++i) {
                    System.arraycopy(minimumCost, 0, nextCost, 0, maxSum + 1);
                    Arrays.fill(chosenCount[i + 1], (byte) 0);
                    for (int copies = 1; copies <= remainingCounts[i]; ++copies) {
                        int shift = copies * lengths[i];
                        double cost = copies * shipPrices[i];
                        for (int sum = shift; sum <= maxSum; ++sum) {
                            double candidateCost = minimumCost[sum - shift] + cost;
                            if (candidateCost < nextCost[sum] - PRICING_EPSILON) {
                                nextCost[sum] = candidateCost;
                                chosenCount[i + 1][sum] = (byte) copies;
                            }
                        }
                    }
                    double[] temporary = minimumCost;
                    minimumCost = nextCost;
                    nextCost = temporary;
                }
                int added = 0;
                for (int row = 0; row < rowCount; ++row) {
                    if ((activeRows & (1 << row)) == 0) {
                        continue;
                    }
                    if (minimumCost[rows[row]] + rowPrices[row] > 1 - SIMPLEX_EPSILON) {
                        continue;
                    }
                    byte[] filling = new byte[typeCount];
                    int remainingLength = rows[row];
                    for (int i = typeCount; i > 0; --i) {
                        int copies = chosenCount[i][remainingLength];
                        filling[i - 1] = (byte) copies;
                        remainingLength -= copies * lengths[i - 1];
                    }
                    if (remainingLength != 0) {
                        continue;
                    }
                    boolean exists = false;
                    for (int j = 0; j < columnCount; ++j) {
                        if (columnRows[j] == row && Arrays.equals(columnFillings[j], filling)) {
                            exists = true;
                            break;
                        }
                    }
                    if (!exists) {
                        columnRows[columnCount] = row;
                        columnFillings[columnCount++] = filling;
                        ++added;
                    }
                }
                if (added == 0) {
                    return false;
                }
            }
            if (!feasible) {
                return false;
            }
            int selectedRow = -1;
            double largestWeight = -1;
            for (int j = 0; j < columnCount; ++j) {
                if (columnWeights[j] > largestWeight) {
                    largestWeight = columnWeights[j];
                    selectedRow = columnRows[j];
                }
            }
            int orderSize = 0;
            for (int j = 0; j < columnCount; ++j) {
                if (columnRows[j] == selectedRow) {
                    ++orderSize;
                }
            }
            int[] order = new int[orderSize];
            int position = 0;
            for (int j = 0; j < columnCount; ++j) {
                if (columnRows[j] == selectedRow) {
                    order[position++] = j;
                }
            }
            sortByScore(order, columnWeights);
            for (int j : order) {
                byte[] filling = columnFillings[j];
                for (int i = 0; i < typeCount; ++i) {
                    remainingCounts[i] -= filling[i];
                }
                if (generateColumns(
                        remainingCounts,
                        activeRows ^ (1 << selectedRow),
                        columnRows,
                        columnFillings,
                        columnCount)) {
                    storeRow(selectedRow, filling);
                    return true;
                }
                for (int i = 0; i < typeCount; ++i) {
                    remainingCounts[i] += filling[i];
                }
                if (pricingWork >= PRICING_WORK_LIMIT) {
                    break;
                }
            }
            return false;
        }

        boolean columnGenerate() {
            pricingWork = 0;
            return generateColumns(
                    counts.clone(), (1 << rowCount) - 1, new int[0], new byte[0][], 0);
        }

        boolean solve() {
            if (greedy(INITIAL_GREEDY_ATTEMPTS) || columnGenerate()) {
                return true;
            }
            failed = new FailedStates(counts, rowCount);
            suffix = new long[rowCount][][];
            rowFillings = new byte[rowCount][typeCount];
            failed.clear();
            // Double exact-search budgets and retry greedy orders between attempts.
            for (long limit = INITIAL_EXACT_BUDGET;
                    ;
                    limit = Math.min(limit * 2, MAX_EXACT_BUDGET)) {
                int[] remainingCounts = counts.clone();
                budgetExhausted = false;
                budget = limit;
                if (exact(remainingCounts, (1 << rowCount) - 1, 0)
                        || greedy(RETRY_GREEDY_ATTEMPTS)) {
                    return true;
                }
            }
        }
    }

    static final class FastInput {
        final BufferedInputStream input = new BufferedInputStream(System.in);

        int nextInt() throws IOException {
            int character;
            do {
                character = input.read();
            } while (character >= 0 && character <= ' ');
            if (character < 0) {
                return -1;
            }
            int value = 0;
            while (character > ' ') {
                value = value * 10 + character - '0';
                character = input.read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int shipCount = input.nextInt();
        if (shipCount < 0) {
            return;
        }
        int rowCount = input.nextInt();
        int[] ships = new int[shipCount];
        int[] rows = new int[rowCount];
        for (int i = 0; i < shipCount; ++i) {
            ships[i] = input.nextInt();
        }
        for (int i = 0; i < rowCount; ++i) {
            rows[i] = input.nextInt();
        }
        Solver solver = new Solver(ships, rows);
        solver.solve();
        StringBuilder output = new StringBuilder();
        for (int[] row : solver.answer) {
            output.append(row.length).append('\n');
            for (int length : row) {
                output.append(length).append(' ');
            }
            output.append('\n');
        }
        System.out.print(output);
    }
}
