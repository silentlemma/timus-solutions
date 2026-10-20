use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write as IoWrite};

const MAX_FACTORS: usize = 7;

struct Input {
    data: Vec<u8>,
    cursor: usize,
}

impl Input {
    fn next(&mut self) -> usize {
        while self.cursor < self.data.len() && self.data[self.cursor] <= b' ' {
            self.cursor += 1;
        }
        let mut value = 0;
        while self.cursor < self.data.len() && self.data[self.cursor].is_ascii_digit() {
            value = value * 10 + (self.data[self.cursor] - b'0') as usize;
            self.cursor += 1;
        }
        value
    }
}

struct PrimeSets {
    offset: Vec<usize>,
    length: Vec<usize>,
    count: Vec<usize>,
    coordinate: Vec<usize>,
    bit: Vec<usize>,
    previous: Vec<usize>,
}

impl PrimeSets {
    fn locate(&self, prime: usize, position: usize) -> usize {
        let mut left = 1;
        let mut right = self.length[prime] + 1;
        while left < right {
            let middle = (left + right) / 2;
            if self.coordinate[self.offset[prime] + middle] < position {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        left
    }

    fn change(&mut self, prime: usize, mut index: usize, insert: bool) {
        while index <= self.length[prime] {
            if insert {
                self.bit[self.offset[prime] + index] += 1;
            } else {
                self.bit[self.offset[prime] + index] -= 1;
            }
            index += index & index.wrapping_neg();
        }
        if insert {
            self.count[prime] += 1;
        } else {
            self.count[prime] -= 1;
        }
    }

    fn prefix(&self, prime: usize, mut index: usize) -> usize {
        let mut result = 0;
        while index > 0 {
            result += self.bit[self.offset[prime] + index];
            index -= index & index.wrapping_neg();
        }
        result
    }

    fn select_node(&self, prime: usize, mut rank: usize) -> usize {
        let mut step = 1;
        while step * 2 <= self.length[prime] {
            step *= 2;
        }
        let mut index = 0;
        while step > 0 {
            let next = index + step;
            if next <= self.length[prime] && self.bit[self.offset[prime] + next] < rank {
                rank -= self.bit[self.offset[prime] + next];
                index = next;
            }
            step /= 2;
        }
        self.offset[prime] + index + 1
    }
}

struct SegmentTree {
    base: usize,
    maximum: Vec<usize>,
}

impl SegmentTree {
    fn new(length: usize) -> Self {
        let base = length.next_power_of_two();
        Self {
            base,
            maximum: vec![0; base * 2],
        }
    }

    fn set(&mut self, position: usize, value: usize) {
        let mut node = self.base + position - 1;
        self.maximum[node] = value;
        node /= 2;
        while node > 0 {
            self.maximum[node] = self.maximum[node * 2].max(self.maximum[node * 2 + 1]);
            node /= 2;
        }
    }

    fn first(
        &self,
        node: usize,
        left: usize,
        right: usize,
        query_left: usize,
        query_right: usize,
    ) -> usize {
        if right < query_left || left > query_right || self.maximum[node] < query_left {
            return 0;
        }
        if left == right {
            return left;
        }
        let middle = (left + right) / 2;
        let answer = self.first(node * 2, left, middle, query_left, query_right);
        if answer > 0 {
            answer
        } else {
            self.first(node * 2 + 1, middle + 1, right, query_left, query_right)
        }
    }
}

fn collect(
    position: usize,
    mut value: usize,
    spf: &[usize],
    raw: &mut [Vec<usize>],
    used: &mut Vec<usize>,
) {
    while value > 1 {
        let prime = spf[value];
        if raw[prime].is_empty() {
            used.push(prime);
        }
        raw[prime].push(position);
        while value % prime == 0 {
            value /= prime;
        }
    }
}

fn refresh(position: usize, members: &[usize], sets: &PrimeSets, tree: &mut SegmentTree) {
    let mut best = 0;
    for &node in &members[position * MAX_FACTORS..(position + 1) * MAX_FACTORS] {
        best = best.max(sets.previous[node]);
    }
    tree.set(position, best);
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut input = Input { data, cursor: 0 };
    let n = input.next();
    let q = input.next();
    let mut values = vec![0; n + 1];
    let mut maximum = 2;
    for value in values.iter_mut().skip(1) {
        *value = input.next();
        maximum = maximum.max(*value);
    }
    let mut operations = Vec::with_capacity(q);
    for _ in 0..q {
        let kind = input.next();
        let first = input.next();
        let second = input.next();
        if kind == 2 {
            maximum = maximum.max(second);
        }
        operations.push((kind, first, second));
    }
    let mut spf = vec![0; maximum + 1];
    for prime in 2..=maximum {
        if spf[prime] != 0 {
            continue;
        }
        spf[prime] = prime;
        if prime <= maximum / prime {
            for multiple in (prime * prime..=maximum).step_by(prime) {
                if spf[multiple] == 0 {
                    spf[multiple] = prime;
                }
            }
        }
    }
    let mut raw = vec![Vec::new(); maximum + 1];
    let mut used = Vec::new();
    for (position, &value) in values.iter().enumerate().skip(1) {
        collect(position, value, &spf, &mut raw, &mut used);
    }
    for &(kind, first, second) in &operations {
        if kind == 2 {
            collect(first, second, &spf, &mut raw, &mut used);
        }
    }
    let mut sets = PrimeSets {
        offset: vec![0; maximum + 1],
        length: vec![0; maximum + 1],
        count: vec![0; maximum + 1],
        coordinate: vec![0],
        bit: Vec::new(),
        previous: Vec::new(),
    };
    for &prime in &used {
        let mut positions = std::mem::take(&mut raw[prime]);
        positions.sort_unstable();
        positions.dedup();
        sets.offset[prime] = sets.coordinate.len() - 1;
        sets.length[prime] = positions.len();
        sets.coordinate.extend(positions);
    }
    drop(raw);
    sets.bit = vec![0; sets.coordinate.len()];
    sets.previous = vec![0; sets.coordinate.len()];
    let mut members = vec![0; (n + 1) * MAX_FACTORS];
    let mut last = vec![0; maximum + 1];
    let mut tree = SegmentTree::new(n);
    for (position, &initial) in values.iter().enumerate().skip(1) {
        let mut slot = position * MAX_FACTORS;
        let mut best = 0;
        let mut value = initial;
        while value > 1 {
            let prime = spf[value];
            let node = sets.offset[prime] + sets.locate(prime, position);
            members[slot] = node;
            sets.previous[node] = last[prime];
            sets.bit[node] = 1;
            best = best.max(last[prime]);
            last[prime] = position;
            sets.count[prime] += 1;
            slot += 1;
            while value % prime == 0 {
                value /= prime;
            }
        }
        tree.maximum[tree.base + position - 1] = best;
    }
    for &prime in &used {
        let offset = sets.offset[prime];
        for index in 1..=sets.length[prime] {
            let parent = index + (index & index.wrapping_neg());
            if parent <= sets.length[prime] {
                sets.bit[offset + parent] += sets.bit[offset + index];
            }
        }
    }
    for node in (1..tree.base).rev() {
        tree.maximum[node] = tree.maximum[node * 2].max(tree.maximum[node * 2 + 1]);
    }
    let mut output = String::new();
    for (kind, left, right) in operations {
        if kind == 1 {
            let position = tree.first(1, 1, tree.base, left, right);
            if position == 0 {
                writeln!(output, "-1").unwrap();
            } else {
                writeln!(
                    output,
                    "{} {}",
                    tree.maximum[tree.base + position - 1],
                    position
                )
                .unwrap();
            }
            continue;
        }
        let old_value = values[left];
        if old_value == right {
            continue;
        }
        let mut value = old_value;
        while value > 1 {
            let prime = spf[value];
            if right % prime != 0 {
                let index = sets.locate(prime, left);
                let node = sets.offset[prime] + index;
                let rank = sets.prefix(prime, index);
                if rank < sets.count[prime] {
                    let next = sets.select_node(prime, rank + 1);
                    sets.previous[next] = sets.previous[node];
                    refresh(sets.coordinate[next], &members, &sets, &mut tree);
                }
                sets.change(prime, index, false);
            }
            while value % prime == 0 {
                value /= prime;
            }
        }
        value = right;
        while value > 1 {
            let prime = spf[value];
            if old_value % prime != 0 {
                let index = sets.locate(prime, left);
                let node = sets.offset[prime] + index;
                let rank = sets.prefix(prime, index - 1);
                sets.previous[node] = if rank == 0 {
                    0
                } else {
                    sets.coordinate[sets.select_node(prime, rank)]
                };
                if rank < sets.count[prime] {
                    let next = sets.select_node(prime, rank + 1);
                    sets.previous[next] = left;
                    refresh(sets.coordinate[next], &members, &sets, &mut tree);
                }
                sets.change(prime, index, true);
            }
            while value % prime == 0 {
                value /= prime;
            }
        }
        values[left] = right;
        let mut slot = left * MAX_FACTORS;
        members[slot..slot + MAX_FACTORS].fill(0);
        value = right;
        while value > 1 {
            let prime = spf[value];
            members[slot] = sets.offset[prime] + sets.locate(prime, left);
            slot += 1;
            while value % prime == 0 {
                value /= prime;
            }
        }
        refresh(left, &members, &sets, &mut tree);
    }
    io::BufWriter::new(io::stdout())
        .write_all(output.as_bytes())
        .unwrap();
}
