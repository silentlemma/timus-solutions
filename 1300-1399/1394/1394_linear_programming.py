"""Configuration LP, bounded subset-sum pricing, exact row search."""

import random
import sys

SIMPLEX_ITERATION_LIMIT = 1000
FILLING_COUNT_LIMIT = 1000000
INITIAL_FILLING_COUNT = 1000001
RANDOM_SEED = 12345
SIMPLEX_EPSILON = 1e-8
ELIMINATION_EPSILON = 1e-12
FEASIBILITY_EPSILON = 1e-7
PRICING_EPSILON = 1e-10
INFINITE_PRICE = 1e30
GREEDY_ATTEMPT_LIMIT = 64
PRICING_WORK_LIMIT = 160
COLUMN_ITERATION_LIMIT = 60


class LinearProgram:
    # Slack variables precede configuration variables. The slack columns are
    # B^-1, so newly priced columns can be appended without losing the basis.
    def __init__(self, limits):
        constraint_count = self.constraint_count = len(limits)
        self.width = constraint_count + 1
        self.column_count = 0
        self.basis = list(range(constraint_count))
        self.nonbasic = []
        tableau = self.tableau = [0.0] * ((constraint_count + 1) * (constraint_count + 1))
        for i in range(constraint_count):
            tableau[i * (constraint_count + 1) + i] = 1.0
            tableau[i * (constraint_count + 1) + constraint_count] = float(limits[i])

    def append(self, columns):
        constraint_count, old_width, old_tableau = self.constraint_count, self.width, self.tableau
        extra = len(columns)
        width = old_width + extra
        tableau = [0.0] * ((constraint_count + 1) * width)
        for i in range(constraint_count + 1):
            offset, old_offset = i * width, i * old_width
            tableau[offset : offset + old_width - 1] = old_tableau[
                old_offset : old_offset + old_width - 1
            ]
            tableau[offset + width - 1] = old_tableau[old_offset + old_width - 1]
            for j in range(extra):
                column = columns[j]
                value = -1.0 if i == constraint_count else 0.0
                for q in range(0, len(column), 2):
                    value += old_tableau[old_offset + column[q]] * column[q + 1]
                tableau[offset + old_width - 1 + j] = value
        self.column_count += extra
        self.nonbasic.extend(range(old_width - 1, width - 1))
        self.tableau, self.width = tableau, width

    def solve(self):
        simplex_epsilon = SIMPLEX_EPSILON
        elimination_epsilon = ELIMINATION_EPSILON
        tableau, constraint_count, width, basis = (
            self.tableau,
            self.constraint_count,
            self.width,
            self.basis,
        )
        nonbasic = self.nonbasic
        objective_offset = constraint_count * width
        for _ in range(SIMPLEX_ITERATION_LIMIT):
            pivot_column, lowest_cost = -1, -simplex_epsilon
            entering_position = -1
            for q in range(len(nonbasic)):
                j = nonbasic[q]
                coefficient = tableau[objective_offset + j]
                if coefficient < lowest_cost or (
                    coefficient == lowest_cost and pivot_column >= 0 and j < pivot_column
                ):
                    pivot_column, lowest_cost, entering_position = j, coefficient, q
            if pivot_column < 0:
                return
            row, ratio = -1, 0.0
            for i in range(constraint_count):
                coefficient = tableau[i * width + pivot_column]
                if coefficient > simplex_epsilon:
                    candidate_ratio = tableau[i * width + width - 1] / coefficient
                    if (
                        row < 0
                        or candidate_ratio < ratio - simplex_epsilon
                        or (
                            abs(candidate_ratio - ratio) < simplex_epsilon and basis[i] < basis[row]
                        )
                    ):
                        row, ratio = i, candidate_ratio
            if row < 0:
                return
            offset = row * width
            inverse_pivot = 1.0 / tableau[offset + pivot_column]
            leaving_column = basis[row]
            for j in nonbasic:
                tableau[offset + j] *= inverse_pivot
            tableau[offset + width - 1] *= inverse_pivot
            tableau[offset + leaving_column] = inverse_pivot
            for i in range(constraint_count + 1):
                if i != row:
                    target_offset = i * width
                    factor = tableau[target_offset + pivot_column]
                    if factor > elimination_epsilon or factor < -elimination_epsilon:
                        for j in nonbasic:
                            tableau[target_offset + j] -= factor * tableau[offset + j]
                        tableau[target_offset + width - 1] -= factor * tableau[offset + width - 1]
                        tableau[target_offset + leaving_column] = -factor * inverse_pivot
                        tableau[target_offset + pivot_column] = 0.0
            basis[row] = pivot_column
            nonbasic[entering_position] = leaving_column


# Fill rows with suffix subset sums; the last row receives all unused ships.
def greedy(ships, rows, attempt_limit, rng):
    row_count = len(rows)
    order = sorted(range(row_count), key=rows.__getitem__)
    for attempt in range(attempt_limit):
        remaining_ships = ships[:]
        if attempt == 1:
            remaining_ships.reverse()
        elif attempt > 1:
            rng.shuffle(remaining_ships)
            prefix = order[:-1]
            rng.shuffle(prefix)
            order[:-1] = prefix
        answer = [None] * row_count
        for j in range(row_count - 1):
            row = order[j]
            remaining_length = rows[row]
            limit = (1 << (remaining_length + 1)) - 1
            remaining_count = len(remaining_ships)
            suffix = [0] * (remaining_count + 1)
            reachable = suffix[remaining_count] = 1
            for i in range(remaining_count - 1, -1, -1):
                reachable = (reachable | reachable << remaining_ships[i]) & limit
                suffix[i] = reachable
            if not (reachable >> remaining_length & 1):
                break
            selected_ships, unused_ships = [], []
            for i in range(remaining_count):
                length = remaining_ships[i]
                if length <= remaining_length and suffix[i + 1] >> (remaining_length - length) & 1:
                    selected_ships.append(length)
                    remaining_length -= length
                else:
                    unused_ships.append(length)
            answer[row] = selected_ships
            remaining_ships = unused_ships
        else:
            answer[order[-1]] = remaining_ships
            return answer
    return None


# Binary chunks represent bounded multiplicities in the reachable-sum bitsets.
def suffix_sums(lengths, remaining_counts, max_sum):
    type_count = len(lengths)
    suffix = [0] * (type_count + 1)
    reachable = suffix[type_count] = 1
    sum_mask = (1 << (max_sum + 1)) - 1
    for i in range(type_count - 1, -1, -1):
        copies, step = remaining_counts[i], 1
        while copies:
            chunk = min(copies, step)
            reachable |= reachable << (lengths[i] * chunk)
            copies -= chunk
            step <<= 1
        reachable &= sum_mask
        suffix[i] = reachable
    return suffix


def price_patterns(lengths, remaining_counts, prices, max_sum):
    # Flat reconstruction table, one bounded-knapsack stage per ship type.
    pricing_epsilon = PRICING_EPSILON
    sum_count, type_count = max_sum + 1, len(lengths)
    chosen_counts = [0] * (sum_count * type_count)
    previous_costs = [INFINITE_PRICE] * sum_count
    previous_costs[0] = 0.0
    processed_length = 0
    for i in range(type_count):
        costs = previous_costs[:]
        value, count, price = lengths[i], remaining_counts[i], prices[i]
        offset = i * sum_count
        previous_max_sum = min(max_sum, processed_length)
        for copies in range(1, min(count, max_sum // value) + 1):
            shift = copies * value
            cost = copies * price
            stop = min(max_sum, previous_max_sum + shift) + 1
            for sum_length in range(shift, stop):
                candidate_cost = previous_costs[sum_length - shift] + cost
                if candidate_cost < costs[sum_length] - pricing_epsilon:
                    costs[sum_length] = candidate_cost
                    chosen_counts[offset + sum_length] = copies
        processed_length += count * value
        previous_costs = costs
    return previous_costs, chosen_counts


class Solver:
    def __init__(self, ships, rows):
        self.rows = rows
        self.row_count = len(rows)
        self.lengths = sorted(set(ships), reverse=True)
        self.counts = [ships.count(length) for length in self.lengths]
        self.type_count = len(self.lengths)
        self.ships = sorted(ships, reverse=True)
        self.rng = random.Random(RANDOM_SEED)
        self.answer = [None] * self.row_count
        self.pricing_work = 0

    def store_row(self, row, filling):
        self.answer[row] = [
            length for i, length in enumerate(self.lengths) for _ in range(filling[i])
        ]

    # Price complete fillings with bounded knapsack, then branch on one row.
    # Floating-point decisions affect only this bounded construction stage.
    def column_generate(self, remaining_counts, row_mask, previous_columns):
        if not row_mask & (row_mask - 1):
            self.store_row(row_mask.bit_length() - 1, remaining_counts)
            return True
        if self.pricing_work >= PRICING_WORK_LIMIT:
            return False
        lengths, type_count, rows = self.lengths, self.type_count, self.rows
        row_indices = [row for row in range(self.row_count) if row_mask >> row & 1]
        active_row_count = len(row_indices)
        active_types = [i for i in range(type_count) if remaining_counts[i]]
        active_type_count = len(active_types)
        row_constraint = [0] * self.row_count
        for j, row in enumerate(row_indices):
            row_constraint[row] = active_type_count + j
        columns = []
        for row, filling in previous_columns:
            if row_mask >> row & 1 and all(
                filling[i] <= remaining_counts[i] for i in range(type_count)
            ):
                columns.append((row, filling))
        seen = set(columns)
        lp = LinearProgram([remaining_counts[i] for i in active_types] + [1] * active_row_count)

        def append(start):
            sparse = []
            for j in range(start, len(columns)):
                row, filling = columns[j]
                column = [row_constraint[row], 1]
                for q in range(active_type_count):
                    i = active_types[q]
                    if filling[i]:
                        column.extend((q, filling[i]))
                sparse.append(column)
            lp.append(sparse)

        if columns:
            append(0)
        max_sum = max(rows[row] for row in row_indices)
        sum_count = max_sum + 1
        feasible = False
        for _ in range(COLUMN_ITERATION_LIMIT):
            if self.pricing_work >= PRICING_WORK_LIMIT:
                break
            self.pricing_work += 1
            lp.solve()
            tableau, width, constraint_count = lp.tableau, lp.width, lp.constraint_count
            objective_offset = constraint_count * width
            if tableau[objective_offset + width - 1] >= active_row_count - FEASIBILITY_EPSILON:
                feasible = True
                break
            prices = [0.0] * type_count
            for q in range(active_type_count):
                prices[active_types[q]] = max(0.0, tableau[objective_offset + q])
            minimum_cost, chosen_counts = price_patterns(lengths, remaining_counts, prices, max_sum)
            start = len(columns)
            for row in row_indices:
                cost = minimum_cost[rows[row]] + tableau[objective_offset + row_constraint[row]]
                if cost > 1.0 - SIMPLEX_EPSILON:
                    continue
                filling = [0] * type_count
                remaining_length = rows[row]
                for i in range(type_count - 1, -1, -1):
                    copies = chosen_counts[i * sum_count + remaining_length]
                    filling[i] = copies
                    remaining_length -= copies * lengths[i]
                if remaining_length:
                    continue
                column = (row, tuple(filling))
                if column not in seen:
                    seen.add(column)
                    columns.append(column)
            if len(columns) == start:
                return False
            append(start)
        if not feasible:
            return False
        column_weights = [0.0] * len(columns)
        for i in range(constraint_count):
            j = lp.basis[i] - constraint_count
            if j >= 0:
                column_weights[j] = max(0.0, tableau[i * width + width - 1])
        # Rounding is accepted only after checking the integer multiplicities.
        # This also avoids rebuilding residual LPs for an integral solution.
        chosen = [-1] * self.row_count
        for j in range(len(columns)):
            row = columns[j][0]
            if chosen[row] < 0 or column_weights[j] > column_weights[chosen[row]]:
                chosen[row] = j
        used = [0] * type_count
        for row in row_indices:
            filling = columns[chosen[row]][1]
            for i in range(type_count):
                used[i] += filling[i]
        if used == remaining_counts:
            for row in row_indices:
                self.store_row(row, columns[chosen[row]][1])
            return True
        selected_row = columns[max(range(len(columns)), key=column_weights.__getitem__)][0]
        # Fix a complete filling of the row with the largest LP weight.
        order = [j for j in range(len(columns)) if columns[j][0] == selected_row]
        order.sort(key=column_weights.__getitem__, reverse=True)
        for j in order:
            filling = columns[j][1]
            unused_counts = [remaining_counts[i] - filling[i] for i in range(type_count)]
            if self.column_generate(unused_counts, row_mask ^ (1 << selected_row), columns):
                self.store_row(selected_row, filling)
                return True
            if self.pricing_work >= PRICING_WORK_LIMIT:
                break
        return False

    def exact(self, remaining_counts, row_mask):
        # No floating-point decision can prune this search. Every complete
        # filling of the selected row is enumerated, with exact failure keys.
        if not row_mask & (row_mask - 1):
            self.store_row(row_mask.bit_length() - 1, remaining_counts)
            return True
        key = (row_mask, bytes(remaining_counts))
        if key in self.failed:
            return False
        lengths, type_count, rows = self.lengths, self.type_count, self.rows
        row_indices = [row for row in range(self.row_count) if row_mask >> row & 1]
        total = sum(rows[row] for row in row_indices)
        max_sum = min(max(rows[row] for row in row_indices), total // 2)
        # Exact coefficients until saturation; no subtraction of saturated
        # entries. This counts multisets, not permutations of equal ships.
        filling_counts = [0] * (max_sum + 1)
        filling_counts[0] = 1
        for i in range(type_count):
            next_counts = [0] * (max_sum + 1)
            value = lengths[i]
            for sum_length in range(max_sum + 1):
                ways = filling_counts[sum_length]
                if ways:
                    for target_sum in range(
                        sum_length,
                        min(max_sum, sum_length + remaining_counts[i] * value) + 1,
                        value,
                    ):
                        next_counts[target_sum] = min(
                            FILLING_COUNT_LIMIT, next_counts[target_sum] + ways
                        )
            filling_counts = next_counts
        selected_row, fewest_fillings = -1, INITIAL_FILLING_COUNT
        for row in row_indices:
            target = rows[row]
            if not filling_counts[min(target, total - target)]:
                self.failed.add(key)
                return False
            if target <= total // 2 and filling_counts[target] < fewest_fillings:
                selected_row, fewest_fillings = row, filling_counts[target]
        target = rows[selected_row]
        suffix = suffix_sums(lengths, remaining_counts, target)
        filling = [0] * type_count
        remaining_rows = row_mask ^ (1 << selected_row)
        # Enumerate a row with an explicit stack. Only selecting the next row
        # recurses, so Python call depth is bounded by the number of rows.
        remaining_by_type = [0] * type_count
        next_count = [0] * type_count
        remaining_by_type[0] = target
        next_count[0] = min(remaining_counts[0], target // lengths[0])
        i = 0
        while i >= 0:
            copies = next_count[i]
            if copies < 0:
                filling[i] = 0
                i -= 1
                continue
            next_count[i] = copies - 1
            remainder = remaining_by_type[i] - copies * lengths[i]
            if not (suffix[i + 1] >> remainder & 1):
                continue
            filling[i] = copies
            if remainder:
                i += 1
                remaining_by_type[i] = remainder
                next_count[i] = min(remaining_counts[i], remainder // lengths[i])
            else:
                unused_counts = [remaining_counts[j] - filling[j] for j in range(type_count)]
                if self.exact(unused_counts, remaining_rows):
                    self.store_row(selected_row, filling)
                    return True
        self.failed.add(key)
        return False

    def solve(self):
        answer = greedy(self.ships, self.rows, GREEDY_ATTEMPT_LIMIT, self.rng)
        if answer is not None:
            return answer
        if self.column_generate(self.counts, (1 << self.row_count) - 1, []):
            return self.answer
        self.failed = set()
        if self.exact(self.counts, (1 << self.row_count) - 1):
            return self.answer
        raise ValueError("No solution")


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    ship_count, row_count = data[:2]
    answer = Solver(
        data[2 : 2 + ship_count], data[2 + ship_count : 2 + ship_count + row_count]
    ).solve()
    output_lines = []
    for group in answer:
        output_lines.append(str(len(group)))
        output_lines.append(" ".join(map(str, group)))
    sys.stdout.write("\n".join(output_lines) + "\n")


if __name__ == "__main__":
    main()
