use std::fmt::Write as FormatWrite;
use std::io::{self, Read, Write};

const SIMPLEX_ITERATION_LIMIT: usize = 1000;
const FILLING_COUNT_LIMIT: usize = 1000000;
const FAILED_STATE_LIMIT: usize = 100000;
const INITIAL_EXACT_BUDGET: i64 = 2000;
const BUDGET_BITS: u32 = 60;
const MAX_EXACT_BUDGET: i64 = 1 << BUDGET_BITS;
const SIMPLEX_EPSILON: f64 = 1e-8;
const ELIMINATION_EPSILON: f64 = 1e-12;
const FEASIBILITY_EPSILON: f64 = 1e-7;
const PRICING_EPSILON: f64 = 1e-10;
const INFINITE_PRICE: f64 = 1e30;
const RANDOM_SEED: u32 = 12345;
const INITIAL_GREEDY_ATTEMPTS: usize = 6;
const RETRY_GREEDY_ATTEMPTS: usize = 16;
const PRICING_WORK_LIMIT: usize = 160;
const COLUMN_ITERATION_LIMIT: usize = 60;
const MAX_LENGTH: usize = 100;
const MAX_ROWS: usize = 10;
const WORD_BITS: usize = 64;
const BYTE_BITS: usize = 8;
const STACK_SIZE: usize = 8_388_608;

const MT_SIZE: usize = 624;
const MT_OFFSET: usize = 397;
const MT_UPPER_MASK: u32 = 0x80000000;
const MT_LOWER_MASK: u32 = 0x7fffffff;
const MT_TWIST_MASK: u32 = 0x9908b0df;
const MT_SEED_MULTIPLIER: u32 = 1812433253;
const MT_SEED_SHIFT: u32 = 30;
const MT_SHIFT_FIRST: u32 = 11;
const MT_SHIFT_SECOND: u32 = 7;
const MT_SHIFT_THIRD: u32 = 15;
const MT_SHIFT_LAST: u32 = 18;
const MT_MASK_SECOND: u32 = 0x9d2c5680;
const MT_MASK_THIRD: u32 = 0xefc60000;
const RANDOM_WORD_BITS: u32 = 32;
const HASH_OFFSET: u64 = 0xcbf29ce484222325;
const HASH_MULTIPLIER: u64 = 0x100000001b3;
const INITIAL_HASH_CAPACITY: usize = 256;

type Counts = [u8; MAX_LENGTH];
type StateKey = [u8; MAX_LENGTH + 2];
type Column = (usize, Counts);

struct MersenneTwister {
    state: [u32; MT_SIZE],
    position: usize,
}

impl MersenneTwister {
    // The standard MT19937 recurrence uses wrapping unsigned arithmetic.
    fn new() -> Self {
        let mut state = [0; MT_SIZE];
        state[0] = RANDOM_SEED;
        for i in 1..MT_SIZE {
            let previous = state[i - 1];
            state[i] = MT_SEED_MULTIPLIER
                .wrapping_mul(previous ^ (previous >> MT_SEED_SHIFT))
                .wrapping_add(i as u32);
        }
        Self {
            state,
            position: MT_SIZE,
        }
    }

    fn next(&mut self) -> u32 {
        if self.position == MT_SIZE {
            for i in 0..MT_SIZE {
                let joined = (self.state[i] & MT_UPPER_MASK)
                    | (self.state[(i + 1) % MT_SIZE] & MT_LOWER_MASK);
                self.state[i] = self.state[(i + MT_OFFSET) % MT_SIZE] ^ (joined >> 1);
                if joined & 1 != 0 {
                    self.state[i] ^= MT_TWIST_MASK;
                }
            }
            self.position = 0;
        }
        let mut value = self.state[self.position];
        self.position += 1;
        value ^= value >> MT_SHIFT_FIRST;
        value ^= (value << MT_SHIFT_SECOND) & MT_MASK_SECOND;
        value ^= (value << MT_SHIFT_THIRD) & MT_MASK_THIRD;
        value ^= value >> MT_SHIFT_LAST;
        value
    }

    // libstdc++ downscales a full 32-bit engine with Lemire's rejection method.
    fn below(&mut self, bound: u32) -> usize {
        let mut product = u64::from(self.next()) * u64::from(bound);
        if (product as u32) < bound {
            let threshold = bound.wrapping_neg() % bound;
            while (product as u32) < threshold {
                product = u64::from(self.next()) * u64::from(bound);
            }
        }
        (product >> RANDOM_WORD_BITS) as usize
    }

    // All fleets fit libstdc++'s paired-swap path, including its even-size prefix.
    fn shuffle(&mut self, values: &mut [usize]) {
        if values.is_empty() {
            return;
        }
        let mut position = 1;
        if values.len() % 2 == 0 {
            values.swap(position, self.below(2));
            position += 1;
        }
        while position < values.len() {
            let first_bound = position + 1;
            let draw = self.below((first_bound * (first_bound + 1)) as u32);
            values.swap(position, draw / (first_bound + 1));
            values.swap(position + 1, draw % (first_bound + 1));
            position += 2;
        }
    }
}

// Open addressing compares complete keys, so collisions never prune a valid state.
#[derive(Default)]
struct FailedStates {
    slots: Vec<usize>,
    keys: Vec<StateKey>,
}

impl FailedStates {
    fn hash(key: &StateKey) -> usize {
        let mut hash = HASH_OFFSET;
        for &byte in key {
            hash = (hash ^ u64::from(byte)).wrapping_mul(HASH_MULTIPLIER);
        }
        hash as usize
    }

    fn contains(&self, key: &StateKey) -> bool {
        if self.slots.is_empty() {
            return false;
        }
        let mut slot = Self::hash(key) & (self.slots.len() - 1);
        while self.slots[slot] != 0 {
            if self.keys[self.slots[slot] - 1] == *key {
                return true;
            }
            slot = (slot + 1) & (self.slots.len() - 1);
        }
        false
    }

    fn insert(&mut self, key: StateKey) {
        if self.keys.len() >= FAILED_STATE_LIMIT || self.contains(&key) {
            return;
        }
        if self.slots.is_empty() || (self.keys.len() + 1) * 2 > self.slots.len() {
            self.slots = vec![0; INITIAL_HASH_CAPACITY.max(self.slots.len() * 2)];
            for (index, stored) in self.keys.iter().enumerate() {
                let mut slot = Self::hash(stored) & (self.slots.len() - 1);
                while self.slots[slot] != 0 {
                    slot = (slot + 1) & (self.slots.len() - 1);
                }
                self.slots[slot] = index + 1;
            }
        }
        let mut slot = Self::hash(&key) & (self.slots.len() - 1);
        while self.slots[slot] != 0 {
            slot = (slot + 1) & (self.slots.len() - 1);
        }
        self.keys.push(key);
        self.slots[slot] = self.keys.len();
    }

    fn clear(&mut self) {
        self.slots.fill(0);
        self.keys.clear();
    }
}

fn reachable(words: &[u64], sum: usize) -> bool {
    sum / WORD_BITS < words.len() && (words[sum / WORD_BITS] >> (sum % WORD_BITS)) & 1 != 0
}

// Descending updates add one ship without reusing newly reached sums.
fn add_ship(words: &mut [u64], shift: usize) {
    let word_shift = shift / WORD_BITS;
    let bit_shift = shift % WORD_BITS;
    for i in (word_shift..words.len()).rev() {
        let mut added = words[i - word_shift] << bit_shift;
        if bit_shift != 0 && i > word_shift {
            added |= words[i - word_shift - 1] >> (WORD_BITS - bit_shift);
        }
        words[i] |= added;
    }
}

#[derive(Clone, Default)]
struct SuffixSums {
    width: usize,
    words: Vec<u64>,
}

impl SuffixSums {
    fn new(size: usize, max_sum: usize) -> Self {
        let width = max_sum / WORD_BITS + 1;
        let mut words = vec![0; size * width];
        words[(size - 1) * width] = 1;
        Self { width, words }
    }

    fn get(&self, index: usize, sum: usize) -> bool {
        reachable(
            &self.words[index * self.width..(index + 1) * self.width],
            sum,
        )
    }

    fn prepend(&mut self, index: usize, length: usize, copies: usize) {
        let start = index * self.width;
        self.words
            .copy_within(start + self.width..start + 2 * self.width, start);
        let words = &mut self.words[start..start + self.width];
        for _ in 0..copies {
            add_ship(words, length);
        }
    }
}

// Primal simplex uses the same entering columns, ratio ties, and operation order.
// The flat tableau keeps elimination contiguous; prices guide search only.
struct LinearProgram {
    constraint_count: usize,
    column_count: usize,
    width: usize,
    tableau: Vec<f64>,
    basis: Vec<usize>,
}

impl LinearProgram {
    fn new(constraints: usize, columns: usize) -> Self {
        let width = columns + constraints + 1;
        let mut tableau = vec![0.0; (constraints + 1) * width];
        let mut basis = vec![0; constraints];
        for i in 0..constraints {
            tableau[i * width + columns + i] = 1.0;
            basis[i] = columns + i;
        }
        Self {
            constraint_count: constraints,
            column_count: columns,
            width,
            tableau,
            basis,
        }
    }

    fn get(&self, row: usize, column: usize) -> f64 {
        self.tableau[row * self.width + column]
    }

    fn set(&mut self, row: usize, column: usize, value: f64) {
        self.tableau[row * self.width + column] = value;
    }

    fn solve(&mut self) {
        let rhs = self.column_count + self.constraint_count;
        let objective = self.constraint_count;
        let mut pivot_values = vec![0.0; self.width];
        for _ in 0..SIMPLEX_ITERATION_LIMIT {
            let mut pivot_column = None;
            for column in 0..rhs {
                if self.get(objective, column) < -SIMPLEX_EPSILON
                    && pivot_column.map_or(true, |previous| {
                        self.get(objective, column) < self.get(objective, previous)
                    })
                {
                    pivot_column = Some(column);
                }
            }
            let Some(column) = pivot_column else {
                return;
            };
            let mut pivot_row = None;
            let mut ratio = 0.0;
            for row in 0..self.constraint_count {
                if self.get(row, column) > SIMPLEX_EPSILON {
                    let candidate = self.get(row, rhs) / self.get(row, column);
                    if pivot_row.map_or(true, |previous| {
                        candidate < ratio - SIMPLEX_EPSILON
                            || ((candidate - ratio).abs() < SIMPLEX_EPSILON
                                && self.basis[row] < self.basis[previous])
                    }) {
                        pivot_row = Some(row);
                        ratio = candidate;
                    }
                }
            }
            let Some(row) = pivot_row else {
                return;
            };
            let pivot = self.get(row, column);
            let pivot_slice = &mut self.tableau[row * self.width..(row + 1) * self.width];
            for value in pivot_slice.iter_mut() {
                *value /= pivot;
            }
            pivot_values.copy_from_slice(pivot_slice);
            for (index, values) in self.tableau.chunks_exact_mut(self.width).enumerate() {
                if index == row {
                    continue;
                }
                let factor = values[column];
                if factor.abs() > ELIMINATION_EPSILON {
                    for (value, &pivot_value) in values.iter_mut().zip(&pivot_values) {
                        *value -= factor * pivot_value;
                    }
                    values[column] = 0.0;
                }
            }
            self.basis[row] = column;
        }
    }
}

struct Solver {
    row_count: usize,
    type_count: usize,
    lengths: Vec<usize>,
    counts: Vec<usize>,
    rows: Vec<usize>,
    answer: Vec<Vec<usize>>,
    rng: MersenneTwister,
    failed: FailedStates,
    budget: i64,
    budget_exhausted: bool,
    suffix: Vec<SuffixSums>,
    row_fillings: Vec<Counts>,
}

impl Solver {
    fn new(ships: &[usize], rows: Vec<usize>) -> Self {
        let row_count = rows.len();
        let mut lengths = Vec::new();
        let mut counts = Vec::new();
        for length in (1..=MAX_LENGTH).rev() {
            let copies = ships.iter().filter(|&&ship| ship == length).count();
            if copies > 0 {
                lengths.push(length);
                counts.push(copies);
            }
        }
        let type_count = lengths.len();
        Self {
            row_count,
            type_count,
            lengths,
            counts,
            rows,
            answer: vec![Vec::new(); row_count],
            rng: MersenneTwister::new(),
            failed: FailedStates::default(),
            budget: 0,
            budget_exhausted: false,
            suffix: Vec::new(),
            row_fillings: Vec::new(),
        }
    }

    fn store_row(&mut self, row: usize, filling: &Counts) {
        self.answer[row].clear();
        for (i, &copies) in filling[..self.type_count].iter().enumerate() {
            for _ in 0..copies {
                self.answer[row].push(self.lengths[i]);
            }
        }
    }

    // Small row orders use stable insertion order, as libstdc++ sort does below 16.
    // A suffix subset-sum table lets each greedy row take every feasible ship.
    fn greedy(&mut self, attempt_limit: usize) -> bool {
        let mut order: Vec<usize> = (0..self.row_count).collect();
        order.sort_by_key(|&row| self.rows[row]);
        let mut remaining_ships = Vec::new();
        for attempt in 0..attempt_limit {
            remaining_ships.clear();
            for i in 0..self.type_count {
                for _ in 0..self.counts[i] {
                    remaining_ships.push(self.lengths[i]);
                }
            }
            if attempt == 1 {
                remaining_ships.reverse();
            }
            if attempt > 1 {
                self.rng.shuffle(&mut remaining_ships);
                self.rng.shuffle(&mut order[..self.row_count - 1]);
            }
            let mut completed = true;
            for &row in &order[..self.row_count - 1] {
                let mut remaining_length = self.rows[row];
                let remaining_count = remaining_ships.len();
                let mut suffix = SuffixSums::new(remaining_count + 1, remaining_length);
                for i in (0..remaining_count).rev() {
                    suffix.prepend(i, remaining_ships[i], 1);
                }
                if !suffix.get(0, remaining_length) {
                    completed = false;
                    break;
                }
                let mut unused = Vec::with_capacity(remaining_count);
                self.answer[row].clear();
                for (i, &ship) in remaining_ships.iter().enumerate() {
                    if ship <= remaining_length && suffix.get(i + 1, remaining_length - ship) {
                        self.answer[row].push(ship);
                        remaining_length -= ship;
                    } else {
                        unused.push(ship);
                    }
                }
                remaining_ships = unused;
            }
            if completed {
                self.answer[*order.last().unwrap()] = remaining_ships;
                return true;
            }
        }
        false
    }

    fn failure_key(&self, remaining: &[usize], active_rows: usize) -> StateKey {
        let mut key = [0; MAX_LENGTH + 2];
        key[0] = active_rows as u8;
        key[1] = (active_rows >> BYTE_BITS) as u8;
        for (i, &count) in remaining.iter().enumerate() {
            key[i + 2] = count as u8;
        }
        key
    }

    // Saturation is safe because the multiset coefficients use addition only.
    fn count_fillings(&self, remaining: &[usize], max_sum: usize, limit: usize) -> Vec<usize> {
        let mut ways = vec![0; max_sum + 1];
        let mut next = vec![0; max_sum + 1];
        ways[0] = 1;
        for (i, &available) in remaining.iter().enumerate() {
            next.fill(0);
            for sum in 0..=max_sum {
                if ways[sum] == 0 {
                    continue;
                }
                for copies in 0..=available.min((max_sum - sum) / self.lengths[i]) {
                    let count = &mut next[sum + copies * self.lengths[i]];
                    *count = limit.min(*count + ways[sum]);
                }
            }
            std::mem::swap(&mut ways, &mut next);
        }
        ways
    }

    fn remaining_filling(&self, remaining: &[usize]) -> Counts {
        let mut filling = [0; MAX_LENGTH];
        for (i, &count) in remaining.iter().enumerate() {
            filling[i] = count as u8;
        }
        filling
    }

    // Suffix sums prune incomplete fillings; an exhausted budget never caches failure.
    fn enumerate_exact_row(
        &mut self,
        remaining: &mut [usize],
        active_rows: usize,
        depth: usize,
        selected_row: usize,
        index: usize,
        remaining_length: usize,
    ) -> bool {
        self.budget -= 1;
        if self.budget < 0 {
            self.budget_exhausted = true;
            return false;
        }
        if remaining_length == 0 {
            if self.exact(remaining, active_rows ^ (1 << selected_row), depth + 1) {
                let filling = self.row_fillings[depth];
                self.store_row(selected_row, &filling);
                return true;
            }
            return false;
        }
        if index == self.type_count {
            return false;
        }
        let available = remaining[index];
        for copies in (0..=available.min(remaining_length / self.lengths[index])).rev() {
            let rest = remaining_length - copies * self.lengths[index];
            if self.suffix[depth].get(index + 1, rest) {
                remaining[index] = available - copies;
                self.row_fillings[depth][index] = copies as u8;
                if self.enumerate_exact_row(
                    remaining,
                    active_rows,
                    depth,
                    selected_row,
                    index + 1,
                    rest,
                ) {
                    return true;
                }
                if self.budget_exhausted {
                    break;
                }
            }
        }
        remaining[index] = available;
        self.row_fillings[depth][index] = 0;
        false
    }

    // The complete fallback selects the first row with the fewest multiset fillings.
    // Complementary sums keep the counting table at most half the remaining length.
    fn exact(&mut self, remaining: &mut [usize], active_rows: usize, depth: usize) -> bool {
        self.budget -= 1;
        if self.budget < 0 {
            self.budget_exhausted = true;
            return false;
        }
        if active_rows & (active_rows - 1) == 0 {
            let filling = self.remaining_filling(remaining);
            self.store_row(active_rows.trailing_zeros() as usize, &filling);
            return true;
        }
        let key = self.failure_key(remaining, active_rows);
        if self.failed.contains(&key) {
            return false;
        }
        let mut total_length = 0;
        let mut max_sum = 0;
        for row in 0..self.row_count {
            if active_rows >> row & 1 != 0 {
                total_length += self.rows[row];
                max_sum = max_sum.max(self.rows[row]);
            }
        }
        max_sum = max_sum.min(total_length / 2);
        let filling_counts = self.count_fillings(remaining, max_sum, FILLING_COUNT_LIMIT);
        let mut selected_row = None;
        for row in 0..self.row_count {
            if active_rows >> row & 1 == 0 {
                continue;
            }
            if filling_counts[self.rows[row].min(total_length - self.rows[row])] == 0 {
                return false;
            }
            if self.rows[row] <= total_length / 2
                && selected_row.map_or(true, |previous: usize| {
                    filling_counts[self.rows[row]] < filling_counts[self.rows[previous]]
                })
            {
                selected_row = Some(row);
            }
        }
        let row = selected_row.unwrap();
        let target = self.rows[row];
        let mut suffix = SuffixSums::new(self.type_count + 1, target);
        for i in (0..self.type_count).rev() {
            suffix.prepend(i, self.lengths[i], remaining[i]);
        }
        self.suffix[depth] = suffix;
        self.row_fillings[depth].fill(0);
        if self.enumerate_exact_row(remaining, active_rows, depth, row, 0, target) {
            return true;
        }
        if !self.budget_exhausted {
            self.failed.insert(key);
        }
        false
    }

    // Dual prices turn column pricing into bounded subset sum.
    // Branching fixes whole fillings before the independent exact fallback.
    fn generate_columns(
        &mut self,
        remaining: &mut [usize],
        pricing_work: &mut usize,
        active_rows: usize,
        mut columns: Vec<Column>,
    ) -> bool {
        if active_rows & (active_rows - 1) == 0 {
            let filling = self.remaining_filling(remaining);
            self.store_row(active_rows.trailing_zeros() as usize, &filling);
            return true;
        }
        if *pricing_work > PRICING_WORK_LIMIT {
            return false;
        }
        let active_row_count = active_rows.count_ones() as usize;
        let mut max_sum = 0;
        let mut row_constraint = [0; MAX_ROWS];
        let mut constraint_index = 0;
        for (row, constraint) in row_constraint[..self.row_count].iter_mut().enumerate() {
            if active_rows >> row & 1 != 0 {
                *constraint = constraint_index;
                constraint_index += 1;
                max_sum = max_sum.max(self.rows[row]);
            }
        }
        columns.retain(|(row, filling)| {
            active_rows >> row & 1 != 0
                && (0..self.type_count).all(|i| usize::from(filling[i]) <= remaining[i])
        });
        let width = max_sum + 1;
        let mut minimum_cost = vec![0.0; (self.type_count + 1) * width];
        let mut chosen_count = vec![0u8; (self.type_count + 1) * width];
        let mut ship_prices = vec![0.0; self.type_count];
        let mut row_prices = vec![0.0; self.row_count];
        let mut column_weights = Vec::new();
        let mut feasible = false;
        for _ in 0..COLUMN_ITERATION_LIMIT {
            if *pricing_work >= PRICING_WORK_LIMIT {
                break;
            }
            *pricing_work += 1;
            let column_count = columns.len();
            let mut lp = LinearProgram::new(self.type_count + active_row_count, column_count);
            let rhs = lp.width - 1;
            for (i, &count) in remaining.iter().enumerate() {
                lp.set(i, rhs, count as f64);
            }
            for i in 0..active_row_count {
                lp.set(self.type_count + i, rhs, 1.0);
            }
            for (j, (row, filling)) in columns.iter().enumerate() {
                lp.set(self.type_count + row_constraint[*row], j, 1.0);
                lp.set(lp.constraint_count, j, -1.0);
                for (i, &copies) in filling[..self.type_count].iter().enumerate() {
                    lp.set(i, j, f64::from(copies));
                }
            }
            lp.solve();
            column_weights = vec![0.0; column_count];
            for i in 0..lp.constraint_count {
                if lp.basis[i] < column_count {
                    column_weights[lp.basis[i]] = lp.get(i, rhs).max(0.0);
                }
            }
            if lp.get(lp.constraint_count, rhs) >= active_row_count as f64 - FEASIBILITY_EPSILON {
                feasible = true;
                break;
            }
            for (i, price) in ship_prices.iter_mut().enumerate() {
                *price = lp.get(lp.constraint_count, column_count + i).max(0.0);
            }
            for row in 0..self.row_count {
                if active_rows >> row & 1 != 0 {
                    row_prices[row] = lp.get(
                        lp.constraint_count,
                        column_count + self.type_count + row_constraint[row],
                    );
                }
            }
            minimum_cost[..width].fill(INFINITE_PRICE);
            minimum_cost[0] = 0.0;
            for i in 0..self.type_count {
                let (previous_rows, next_rows) = minimum_cost.split_at_mut((i + 1) * width);
                let previous = &previous_rows[i * width..];
                let next = &mut next_rows[..width];
                next.copy_from_slice(previous);
                let choices = &mut chosen_count[(i + 1) * width..(i + 2) * width];
                choices.fill(0);
                for copies in 1..=remaining[i] {
                    let shift = copies * self.lengths[i];
                    let cost = copies as f64 * ship_prices[i];
                    for sum in shift..=max_sum {
                        let candidate = previous[sum - shift] + cost;
                        if candidate < next[sum] - PRICING_EPSILON {
                            next[sum] = candidate;
                            choices[sum] = copies as u8;
                        }
                    }
                }
            }
            let mut added = 0;
            for (row, &row_price) in row_prices.iter().enumerate() {
                if active_rows >> row & 1 == 0 {
                    continue;
                }
                if minimum_cost[self.type_count * width + self.rows[row]] + row_price
                    > 1.0 - SIMPLEX_EPSILON
                {
                    continue;
                }
                let mut filling = [0; MAX_LENGTH];
                let mut remaining_length = self.rows[row];
                for i in (1..=self.type_count).rev() {
                    let copies = chosen_count[i * width + remaining_length];
                    filling[i - 1] = copies;
                    remaining_length -= usize::from(copies) * self.lengths[i - 1];
                }
                if remaining_length != 0 {
                    continue;
                }
                if !columns
                    .iter()
                    .any(|column| column.0 == row && column.1 == filling)
                {
                    columns.push((row, filling));
                    added += 1;
                }
            }
            if added == 0 {
                return false;
            }
        }
        if !feasible {
            return false;
        }
        let mut selected_row = 0;
        let mut largest_weight = -1.0;
        for (j, column) in columns.iter().enumerate() {
            if column_weights[j] > largest_weight {
                largest_weight = column_weights[j];
                selected_row = column.0;
            }
        }
        let mut order: Vec<usize> = (0..columns.len())
            .filter(|&j| columns[j].0 == selected_row)
            .collect();
        order.sort_by(|&left, &right| {
            column_weights[right]
                .partial_cmp(&column_weights[left])
                .unwrap()
        });
        for j in order {
            let filling = columns[j].1;
            for i in 0..self.type_count {
                remaining[i] -= usize::from(filling[i]);
            }
            if self.generate_columns(
                remaining,
                pricing_work,
                active_rows ^ (1 << selected_row),
                columns.clone(),
            ) {
                self.store_row(selected_row, &filling);
                return true;
            }
            for i in 0..self.type_count {
                remaining[i] += usize::from(filling[i]);
            }
            if *pricing_work >= PRICING_WORK_LIMIT {
                break;
            }
        }
        false
    }

    fn solve(&mut self) {
        if self.greedy(INITIAL_GREEDY_ATTEMPTS) {
            return;
        }
        let mut remaining = self.counts.clone();
        if self.generate_columns(
            &mut remaining,
            &mut 0,
            (1 << self.row_count) - 1,
            Vec::new(),
        ) {
            return;
        }
        self.suffix.resize(self.row_count, SuffixSums::default());
        self.row_fillings.resize(self.row_count, [0; MAX_LENGTH]);
        self.failed.clear();
        // Double exact-search budgets and retry greedy orders between attempts.
        let mut limit = INITIAL_EXACT_BUDGET;
        loop {
            let mut remaining = self.counts.clone();
            self.budget_exhausted = false;
            self.budget = limit;
            if self.exact(&mut remaining, (1 << self.row_count) - 1, 0) {
                return;
            }
            if self.greedy(RETRY_GREEDY_ATTEMPTS) {
                return;
            }
            limit = (limit * 2).min(MAX_EXACT_BUDGET);
        }
    }
}

fn run() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    let mut position = 0;
    let mut next = || {
        while position < input.len() && input[position].is_ascii_whitespace() {
            position += 1;
        }
        if position == input.len() {
            return None;
        }
        let mut value = 0;
        while position < input.len() && input[position].is_ascii_digit() {
            value = value * 10 + usize::from(input[position] - b'0');
            position += 1;
        }
        Some(value)
    };
    let Some(ship_count) = next() else {
        return;
    };
    let Some(row_count) = next() else {
        return;
    };
    let ships: Vec<usize> = (0..ship_count).map(|_| next().unwrap()).collect();
    let rows: Vec<usize> = (0..row_count).map(|_| next().unwrap()).collect();
    let mut solver = Solver::new(&ships, rows);
    solver.solve();
    let mut output = String::new();
    for row in &solver.answer {
        writeln!(&mut output, "{}", row.len()).unwrap();
        for length in row {
            write!(&mut output, "{} ", length).unwrap();
        }
        output.push('\n');
    }
    io::stdout().lock().write_all(output.as_bytes()).unwrap();
}

fn main() {
    // Nested row/type recursion gets a dedicated stack on Windows.
    std::thread::Builder::new()
        .stack_size(STACK_SIZE)
        .spawn(run)
        .unwrap()
        .join()
        .unwrap();
}
