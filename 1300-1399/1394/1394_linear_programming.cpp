#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <numeric>
#include <random>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

const int SIMPLEX_ITERATION_LIMIT = 1000;
const int FILLING_COUNT_LIMIT = 1000000;
const int FAILED_STATE_LIMIT = 100000;
const int INITIAL_EXACT_BUDGET = 2000;
const long long MAX_EXACT_BUDGET = 1LL << 60;
const double SIMPLEX_EPSILON = 1e-8;
const double ELIMINATION_EPSILON = 1e-12;
const double FEASIBILITY_EPSILON = 1e-7;
const double PRICING_EPSILON = 1e-10;
const double INFINITE_PRICE = 1e30;
const unsigned RANDOM_SEED = 12345;
const int INITIAL_GREEDY_ATTEMPTS = 6;
const int RETRY_GREEDY_ATTEMPTS = 16;
const int PRICING_WORK_LIMIT = 160;
const int COLUMN_ITERATION_LIMIT = 60;
const int MAX_LENGTH = 100;
const int WORD_BITS = 64;
const int BYTE_BITS = 8;

using Word = uint64_t;
using Counts = array<unsigned char, MAX_LENGTH>;
static int countBits(Word bits) {
    int count = 0;
    while (bits) {
        bits &= bits - 1;
        ++count;
    }
    return count;
}
static int lowestBit(Word bits) {
    int count = 0;
    while (!(bits & 1)) {
        bits >>= 1;
        ++count;
    }
    return count;
}
struct ReachableSums {
    vector<Word> words;
    ReachableSums(int maxSum = 0) : words(maxSum / WORD_BITS + 1) {}
    bool get(int sum) const {
        return sum >= 0 && size_t(sum / WORD_BITS) < words.size() &&
               (words[sum / WORD_BITS] >> (sum % WORD_BITS) & 1);
    }
    // Descending updates add one ship without reusing its newly reached sums.
    void add(int shift) {
        int wordShift = shift / WORD_BITS, bitShift = shift % WORD_BITS;
        for (int i = int(words.size()) - 1; i >= wordShift; --i)
            words[i] |=
                words[i - wordShift] << bitShift |
                (bitShift && i > wordShift ? words[i - wordShift - 1] >> (WORD_BITS - bitShift)
                                           : 0);
    }
};
// Primal simplex maximizes filled rows subject to row and ship-count limits.
// Slack variables give a feasible zero basis; floating point only guides
// branching, and the exact search never relies on it.
struct LinearProgram {
    int constraintCount, columnCount;
    vector<vector<double>> tableau;
    vector<int> basis;
    LinearProgram(int constraints, int columns)
        : constraintCount(constraints), columnCount(columns),
          tableau(constraintCount + 1, vector<double>(columnCount + constraintCount + 1)),
          basis(constraintCount) {
        for (int i = 0; i < constraintCount; ++i) {
            tableau[i][columnCount + i] = 1;
            basis[i] = columnCount + i;
        }
    }
    void solve() {
        int rhsColumn = columnCount + constraintCount;
        for (int iteration = 0; iteration < SIMPLEX_ITERATION_LIMIT; ++iteration) {
            int pivotColumn = -1;
            for (int j = 0; j < rhsColumn; ++j)
                if (tableau[constraintCount][j] < -SIMPLEX_EPSILON &&
                    (pivotColumn < 0 ||
                     tableau[constraintCount][j] < tableau[constraintCount][pivotColumn]))
                    pivotColumn = j;
            if (pivotColumn < 0)
                return;
            int pivotRow = -1;
            double ratio = 0;
            for (int i = 0; i < constraintCount; ++i)
                if (tableau[i][pivotColumn] > SIMPLEX_EPSILON) {
                    double candidateRatio = tableau[i][rhsColumn] / tableau[i][pivotColumn];
                    if (pivotRow < 0 || candidateRatio < ratio - SIMPLEX_EPSILON ||
                        (abs(candidateRatio - ratio) < SIMPLEX_EPSILON &&
                         basis[i] < basis[pivotRow]))
                        pivotRow = i, ratio = candidateRatio;
                }
            if (pivotRow < 0)
                return;
            double pivotValue = tableau[pivotRow][pivotColumn];
            for (int j = 0; j <= rhsColumn; ++j)
                tableau[pivotRow][j] /= pivotValue;
            for (int i = 0; i <= constraintCount; ++i)
                if (i != pivotRow) {
                    double factor = tableau[i][pivotColumn];
                    if (abs(factor) > ELIMINATION_EPSILON) {
                        for (int j = 0; j <= rhsColumn; ++j)
                            tableau[i][j] -= factor * tableau[pivotRow][j];
                        tableau[i][pivotColumn] = 0;
                    }
                }
            basis[pivotRow] = pivotColumn;
        }
    }
};

struct Solver {
    int rowCount, typeCount;
    vector<int> lengths, counts, rows;
    vector<vector<int>> answer;
    mt19937 rng{RANDOM_SEED};
    Solver(vector<int> ships, vector<int> rowLengths)
        : rowCount(int(rowLengths.size())), rows(rowLengths), answer(rowCount) {
        for (int length = MAX_LENGTH; length; --length) {
            int copies = int(count(ships.begin(), ships.end(), length));
            if (copies) {
                lengths.push_back(length);
                counts.push_back(copies);
            }
        }
        typeCount = int(lengths.size());
    }
    void storeRow(int row, const Counts &filling) {
        answer[row].clear();
        for (int i = 0; i < typeCount; ++i)
            for (int copies = 0; copies < filling[i]; ++copies)
                answer[row].push_back(lengths[i]);
    }
    // A cheap constructive front end. Failure makes no assertion of infeasibility.
    bool greedy(int attemptLimit) {
        vector<int> order(rowCount), remainingShips;
        iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(),
             [&](int leftRow, int rightRow) { return rows[leftRow] < rows[rightRow]; });
        for (int attempt = 0; attempt < attemptLimit; ++attempt) {
            remainingShips.clear();
            for (int i = 0; i < typeCount; ++i)
                for (int copies = 0; copies < counts[i]; ++copies)
                    remainingShips.push_back(lengths[i]);
            if (attempt == 1)
                reverse(remainingShips.begin(), remainingShips.end());
            if (attempt > 1) {
                shuffle(remainingShips.begin(), remainingShips.end(), rng);
                shuffle(order.begin(), order.end() - 1, rng);
            }
            bool completed = true;
            for (int j = 0; j < rowCount - 1; ++j) {
                int row = order[j], remainingLength = rows[row],
                    remainingCount = int(remainingShips.size());
                vector<ReachableSums> suffixSums(remainingCount + 1,
                                                 ReachableSums(remainingLength));
                suffixSums[remainingCount].words[0] = 1;
                for (int i = remainingCount - 1; i >= 0; --i) {
                    suffixSums[i] = suffixSums[i + 1];
                    suffixSums[i].add(remainingShips[i]);
                }
                if (!suffixSums[0].get(remainingLength)) {
                    completed = false;
                    break;
                }
                vector<int> unusedShips;
                answer[row].clear();
                for (int i = 0; i < remainingCount; ++i)
                    if (remainingShips[i] <= remainingLength &&
                        suffixSums[i + 1].get(remainingLength - remainingShips[i])) {
                        answer[row].push_back(remainingShips[i]);
                        remainingLength -= remainingShips[i];
                    } else
                        unusedShips.push_back(remainingShips[i]);
                remainingShips.swap(unusedShips);
            }
            if (completed) {
                answer[order.back()] = remainingShips;
                return true;
            }
        }
        return false;
    }
    unordered_set<string> failed;
    long long budget;
    bool budgetExhausted = false;
    vector<vector<ReachableSums>> suffix;
    vector<Counts> rowFillings;
    string failureKey(const vector<int> &remainingCounts, int activeRows) {
        string stateKey;
        stateKey.push_back(char(activeRows));
        stateKey.push_back(char(activeRows >> BYTE_BITS));
        for (int count : remainingCounts)
            stateKey.push_back(char(count));
        return stateKey;
    }
    // Count each multiset once. Saturation is safe here: coefficients are
    // formed only by addition, never by subtracting saturated coefficients.
    vector<int> countFillings(const vector<int> &remainingCounts, int maxSum, int countLimit) {
        vector<int> waysBySum(maxSum + 1), nextWays(maxSum + 1);
        waysBySum[0] = 1;
        for (int i = 0; i < typeCount; ++i) {
            fill(nextWays.begin(), nextWays.end(), 0);
            for (int sum = 0; sum <= maxSum; ++sum)
                if (waysBySum[sum])
                    for (int copies = 0;
                         copies <= remainingCounts[i] && sum + copies * lengths[i] <= maxSum;
                         ++copies) {
                        int &count = nextWays[sum + copies * lengths[i]];
                        count = min(countLimit, count + waysBySum[sum]);
                    }
            waysBySum.swap(nextWays);
        }
        return waysBySum;
    }
    // Suffix sums prune incomplete fillings; exhausted budgets never cache failure.
    bool enumerateExactRow(vector<int> &remainingCounts, int activeRows, int depth, int selectedRow,
                           int i, int remainingLength) {
        if (--budget < 0) {
            budgetExhausted = true;
            return false;
        }
        if (!remainingLength) {
            if (exact(remainingCounts, activeRows ^ (1 << selectedRow), depth + 1)) {
                storeRow(selectedRow, rowFillings[depth]);
                return true;
            }
            return false;
        }
        if (i == typeCount)
            return false;
        int availableCount = remainingCounts[i];
        for (int copies = min(availableCount, remainingLength / lengths[i]); copies >= 0; --copies)
            if (suffix[depth][i + 1].get(remainingLength - copies * lengths[i])) {
                remainingCounts[i] = availableCount - copies;
                rowFillings[depth][i] = copies;
                if (enumerateExactRow(remainingCounts, activeRows, depth, selectedRow, i + 1,
                                      remainingLength - copies * lengths[i]))
                    return true;
                if (budgetExhausted)
                    break;
            }
        remainingCounts[i] = availableCount;
        rowFillings[depth][i] = 0;
        return false;
    }
    // Complete fallback: dynamic minimum-domain row selection, exact multiset
    // keys, and suffix reachability. It has no final time cutoff.
    bool exact(vector<int> &remainingCounts, int activeRows, int depth) {
        if (--budget < 0) {
            budgetExhausted = true;
            return false;
        }
        if (!(activeRows & (activeRows - 1))) {
            int row = lowestBit(activeRows);
            Counts filling{};
            for (int i = 0; i < typeCount; ++i)
                filling[i] = remainingCounts[i];
            storeRow(row, filling);
            return true;
        }
        string stateKey = failureKey(remainingCounts, activeRows);
        if (failed.count(stateKey))
            return false;
        int totalLength = 0, maxSum = 0;
        for (int row = 0; row < rowCount; ++row)
            if (activeRows >> row & 1)
                totalLength += rows[row], maxSum = max(maxSum, rows[row]);
        maxSum = min(maxSum, totalLength / 2);
        auto fillingCounts = countFillings(remainingCounts, maxSum, FILLING_COUNT_LIMIT);
        int selectedRow = -1;
        for (int row = 0; row < rowCount; ++row)
            if (activeRows >> row & 1) {
                if (!fillingCounts[min(rows[row], totalLength - rows[row])])
                    return false;
                if (rows[row] <= totalLength / 2 &&
                    (selectedRow < 0 ||
                     fillingCounts[rows[row]] < fillingCounts[rows[selectedRow]]))
                    selectedRow = row;
            }
        int target = rows[selectedRow];
        auto &suffixSums = suffix[depth];
        suffixSums.assign(typeCount + 1, ReachableSums(target));
        suffixSums[typeCount].words[0] = 1;
        for (int i = typeCount - 1; i >= 0; --i) {
            suffixSums[i] = suffixSums[i + 1];
            for (int copy = 0; copy < remainingCounts[i]; ++copy)
                suffixSums[i].add(lengths[i]);
        }
        rowFillings[depth].fill(0);
        if (enumerateExactRow(remainingCounts, activeRows, depth, selectedRow, 0, target))
            return true;
        if (!budgetExhausted && failed.size() < FAILED_STATE_LIMIT)
            failed.insert(std::move(stateKey));
        return false;
    }
    using Column = pair<int, Counts>;
    // Dual ship prices turn column pricing into bounded subset sum.
    // Branching fixes complete fillings before the independent exact fallback.
    bool generateColumns(vector<int> &remainingCounts, int &pricingWork, int activeRows,
                         vector<Column> columns) {
        if (!(activeRows & (activeRows - 1))) {
            int row = lowestBit(activeRows);
            Counts filling{};
            for (int i = 0; i < typeCount; ++i)
                filling[i] = remainingCounts[i];
            storeRow(row, filling);
            return true;
        }
        if (pricingWork > PRICING_WORK_LIMIT)
            return false;
        int activeRowCount = countBits(activeRows), maxSum = 0;
        array<int, 10> rowConstraint{};
        int constraintIndex = 0;
        for (int row = 0; row < rowCount; ++row)
            if (activeRows >> row & 1) {
                rowConstraint[row] = constraintIndex++;
                maxSum = max(maxSum, rows[row]);
            }
        columns.erase(remove_if(columns.begin(), columns.end(),
                                [&](const Column &column) {
                                    if (!(activeRows >> column.first & 1))
                                        return true;
                                    for (int i = 0; i < typeCount; ++i)
                                        if (column.second[i] > remainingCounts[i])
                                            return true;
                                    return false;
                                }),
                      columns.end());
        vector<vector<double>> minimumCost(typeCount + 1, vector<double>(maxSum + 1));
        vector<vector<unsigned char>> chosenCount(typeCount + 1, vector<unsigned char>(maxSum + 1));
        vector<double> shipPrices(typeCount), rowPrices(rowCount), columnWeights;
        bool feasible = false;
        for (int iteration = 0;
             iteration < COLUMN_ITERATION_LIMIT && pricingWork < PRICING_WORK_LIMIT; ++iteration) {
            ++pricingWork;
            int columnCount = int(columns.size());
            LinearProgram lp(typeCount + activeRowCount, columnCount);
            int rhsColumn = lp.columnCount + lp.constraintCount;
            for (int i = 0; i < typeCount; ++i)
                lp.tableau[i][rhsColumn] = remainingCounts[i];
            for (int i = 0; i < activeRowCount; ++i)
                lp.tableau[typeCount + i][rhsColumn] = 1;
            for (int j = 0; j < columnCount; ++j) {
                int row = columns[j].first;
                lp.tableau[typeCount + rowConstraint[row]][j] = 1;
                lp.tableau[lp.constraintCount][j] = -1;
                for (int i = 0; i < typeCount; ++i)
                    lp.tableau[i][j] = columns[j].second[i];
            }
            lp.solve();
            columnWeights.assign(columnCount, 0);
            for (int i = 0; i < lp.constraintCount; ++i)
                if (lp.basis[i] < columnCount)
                    columnWeights[lp.basis[i]] = max(0., lp.tableau[i][rhsColumn]);
            if (lp.tableau[lp.constraintCount][rhsColumn] >= activeRowCount - FEASIBILITY_EPSILON) {
                feasible = true;
                break;
            }
            for (int i = 0; i < typeCount; ++i)
                shipPrices[i] = max(0., lp.tableau[lp.constraintCount][columnCount + i]);
            for (int row = 0; row < rowCount; ++row)
                if (activeRows >> row & 1)
                    rowPrices[row] = lp.tableau[lp.constraintCount]
                                               [columnCount + typeCount + rowConstraint[row]];
            fill(minimumCost[0].begin(), minimumCost[0].end(), INFINITE_PRICE);
            minimumCost[0][0] = 0;
            for (int i = 0; i < typeCount; ++i) {
                minimumCost[i + 1] = minimumCost[i];
                fill(chosenCount[i + 1].begin(), chosenCount[i + 1].end(), 0);
                for (int copies = 1; copies <= remainingCounts[i]; ++copies) {
                    int shift = copies * lengths[i];
                    double cost = copies * shipPrices[i];
                    for (int sum = shift; sum <= maxSum; ++sum) {
                        double candidateCost = minimumCost[i][sum - shift] + cost;
                        if (candidateCost < minimumCost[i + 1][sum] - PRICING_EPSILON) {
                            minimumCost[i + 1][sum] = candidateCost;
                            chosenCount[i + 1][sum] = copies;
                        }
                    }
                }
            }
            int added = 0;
            for (int row = 0; row < rowCount; ++row)
                if (activeRows >> row & 1) {
                    if (minimumCost[typeCount][rows[row]] + rowPrices[row] > 1 - SIMPLEX_EPSILON)
                        continue;
                    Counts filling{};
                    int remainingLength = rows[row];
                    for (int i = typeCount; i > 0; --i) {
                        int copies = chosenCount[i][remainingLength];
                        filling[i - 1] = copies;
                        remainingLength -= copies * lengths[i - 1];
                    }
                    if (remainingLength)
                        continue;
                    bool exists = false;
                    for (auto &column : columns)
                        if (column.first == row && column.second == filling) {
                            exists = true;
                            break;
                        }
                    if (!exists) {
                        columns.push_back({row, filling});
                        ++added;
                    }
                }
            if (!added)
                return false;
        }
        if (!feasible)
            return false;
        int selectedRow = -1;
        double largestWeight = -1;
        for (int j = 0; j < int(columns.size()); ++j)
            if (columnWeights[j] > largestWeight) {
                largestWeight = columnWeights[j];
                selectedRow = columns[j].first;
            }
        vector<int> order;
        for (int j = 0; j < int(columns.size()); ++j)
            if (columns[j].first == selectedRow)
                order.push_back(j);
        stable_sort(order.begin(), order.end(), [&](int leftColumn, int rightColumn) {
            return columnWeights[leftColumn] > columnWeights[rightColumn];
        });
        for (int j : order) {
            const Counts filling = columns[j].second;
            for (int i = 0; i < typeCount; ++i)
                remainingCounts[i] -= filling[i];
            if (generateColumns(remainingCounts, pricingWork, activeRows ^ (1 << selectedRow),
                                columns)) {
                storeRow(selectedRow, filling);
                return true;
            }
            for (int i = 0; i < typeCount; ++i)
                remainingCounts[i] += filling[i];
            if (pricingWork >= PRICING_WORK_LIMIT)
                break;
        }
        return false;
    }
    bool columnGenerate() {
        int pricingWork = 0;
        vector<int> remainingCounts = counts;
        return generateColumns(remainingCounts, pricingWork, (1 << rowCount) - 1, {});
    }

    bool solve() {
        if (greedy(INITIAL_GREEDY_ATTEMPTS))
            return true;
        if (columnGenerate())
            return true;
        suffix.resize(rowCount);
        rowFillings.resize(rowCount);
        failed.clear();
        // Double exact-search budgets and retry greedy orders between attempts.
        for (long long limit = INITIAL_EXACT_BUDGET;; limit = min(limit * 2, MAX_EXACT_BUDGET)) {
            vector<int> remainingCounts = counts;
            budgetExhausted = false;
            budget = limit;
            if (exact(remainingCounts, (1 << rowCount) - 1, 0))
                return true;
            if (greedy(RETRY_GREEDY_ATTEMPTS))
                return true;
        }
    }
};
int main() {
    int shipCount, rowCount;
    if (scanf("%d%d", &shipCount, &rowCount) != 2)
        return 0;
    vector<int> ships(shipCount), rows(rowCount);
    for (int &length : ships)
        scanf("%d", &length);
    for (int &length : rows)
        scanf("%d", &length);
    Solver solver(ships, rows);
    solver.solve();
    for (const auto &row : solver.answer) {
        printf("%d\n", int(row.size()));
        for (int length : row)
            printf("%d ", length);
        puts("");
    }
    return 0;
}
