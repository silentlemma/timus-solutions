use std::collections::HashMap;
use std::io::{self, Read, Write};
use std::ops::{Add, Mul, Sub};

const MOD: i64 = 1_000_000_007;
const OTHER_MOD: i64 = 1_000_000_009;
const BASE: i64 = 911_382_323;
const WORD_BITS: usize = 64;
const CACHE_LIMIT: usize = 1024;

#[derive(Clone, Copy, Default, PartialEq, Eq, Hash)]
struct Fingerprint(i64, i64);

impl Add for Fingerprint {
    type Output = Self;
    fn add(self, rhs: Self) -> Self {
        Self((self.0 + rhs.0) % MOD, (self.1 + rhs.1) % OTHER_MOD)
    }
}

impl Sub for Fingerprint {
    type Output = Self;
    fn sub(self, rhs: Self) -> Self {
        Self(
            (self.0 - rhs.0 + MOD) % MOD,
            (self.1 - rhs.1 + OTHER_MOD) % OTHER_MOD,
        )
    }
}

impl Mul for Fingerprint {
    type Output = Self;
    fn mul(self, rhs: Self) -> Self {
        Self(self.0 * rhs.0 % MOD, self.1 * rhs.1 % OTHER_MOD)
    }
}

struct Positions {
    low: Vec<u64>,
    middle: Vec<u64>,
    top: u64,
}

impl Positions {
    fn new(n: usize) -> Self {
        let blocks = n / WORD_BITS + 1;
        let mut result = Self {
            low: vec![0; blocks],
            middle: vec![0; blocks / WORD_BITS + 1],
            top: 0,
        };
        result.insert(0);
        result
    }

    fn highest(bits: u64) -> usize {
        WORD_BITS - 1 - bits.leading_zeros() as usize
    }

    fn below(bit: usize) -> u64 {
        if bit == 0 {
            0
        } else {
            u64::MAX >> (WORD_BITS - bit)
        }
    }

    fn insert(&mut self, position: usize) {
        let block = position / WORD_BITS;
        let group = block / WORD_BITS;
        self.low[block] |= 1 << (position % WORD_BITS);
        self.middle[group] |= 1 << (block % WORD_BITS);
        self.top |= 1 << group;
    }

    fn erase(&mut self, position: usize) {
        let block = position / WORD_BITS;
        let group = block / WORD_BITS;
        self.low[block] &= !(1 << (position % WORD_BITS));
        if self.low[block] == 0 {
            self.middle[group] &= !(1 << (block % WORD_BITS));
            if self.middle[group] == 0 {
                self.top &= !(1 << group);
            }
        }
    }

    fn predecessor(&self, position: usize) -> usize {
        let mut block = position / WORD_BITS;
        let mut bits = self.low[block] & (u64::MAX >> (WORD_BITS - 1 - position % WORD_BITS));
        if bits == 0 {
            let mut group = block / WORD_BITS;
            let mut groups = self.middle[group] & Self::below(block % WORD_BITS);
            if groups == 0 {
                group = Self::highest(self.top & Self::below(group));
                groups = self.middle[group];
            }
            block = group * WORD_BITS + Self::highest(groups);
            bits = self.low[block];
        }
        block * WORD_BITS + Self::highest(bits)
    }
}

struct Solver {
    n: usize,
    hashes: Vec<Fingerprint>,
    power: Vec<Fingerprint>,
    values: Vec<Fingerprint>,
    fenwick: Vec<Fingerprint>,
    following: Vec<usize>,
    sources: Vec<usize>,
    primes: Vec<usize>,
    positions: Positions,
    whole: Fingerprint,
    multipliers: HashMap<usize, Fingerprint>,
    cache: HashMap<Fingerprint, usize>,
}

impl Solver {
    fn new(n: usize, text: &[u8]) -> Self {
        let mut hashes = vec![Fingerprint::default(); text.len() + 1];
        let mut power = vec![Fingerprint(1, 1); n + 1];
        for i in 0..n {
            power[i + 1] = power[i] * Fingerprint(BASE, BASE);
        }
        for (i, &character) in text.iter().enumerate() {
            let value = i64::from(character);
            hashes[i + 1] = hashes[i] * Fingerprint(BASE, BASE) + Fingerprint(value, value);
        }
        let whole = hashes[n];
        let mut values = vec![Fingerprint::default(); n + 1];
        let mut fenwick = values.clone();
        values[0] = whole;
        let mut index = 1;
        while index <= n {
            fenwick[index] = whole;
            index *= 2;
        }
        let mut primes = Vec::new();
        let mut remaining = n;
        let mut divisor = 2;
        while divisor * divisor <= remaining {
            if remaining % divisor == 0 {
                primes.push(divisor);
                while remaining % divisor == 0 {
                    remaining /= divisor;
                }
            }
            divisor += 1;
        }
        if remaining > 1 {
            primes.push(remaining);
        }
        Self {
            n,
            hashes,
            power,
            values,
            fenwick,
            following: vec![n; n + 1],
            sources: vec![0; n + 1],
            primes,
            positions: Positions::new(n),
            whole,
            multipliers: HashMap::new(),
            cache: HashMap::new(),
        }
    }

    // Static slices are weighted by their positions in the current string.
    fn fingerprint(&self, source: usize, left: usize, right: usize) -> Fingerprint {
        let length = right - left;
        (self.hashes[source + length] - self.hashes[source] * self.power[length])
            * self.power[self.n - right]
    }

    fn set_value(&mut self, position: usize, value: Fingerprint) {
        let old = self.values[position];
        let mut index = position + 1;
        // Each raw Fenwick sum fits in a signed 64-bit integer.
        while index <= self.n {
            self.fenwick[index].0 += value.0 - old.0;
            self.fenwick[index].1 += value.1 - old.1;
            index += index & index.wrapping_neg();
        }
        self.values[position] = value;
    }

    fn replace(&mut self, begin: usize, end: usize, source: usize) {
        let start = self.positions.predecessor(begin);
        let mut position = start;
        let mut removed = Fingerprint::default();
        while position < end {
            let left = position.max(begin);
            let right = self.following[position].min(end);
            removed = removed
                + if left == position && right == self.following[position] {
                    self.values[position]
                } else {
                    self.fingerprint(self.sources[position] + left - position, left, right)
                };
            position = self.following[position];
        }
        let replacement = self.fingerprint(source, begin, end);
        let delta = replacement - removed;
        if delta == Fingerprint::default() && end <= self.following[start] {
            return;
        }
        self.whole = self.whole + delta;
        position = start;
        while position < end {
            let stop = self.following[position];
            let old_source = self.sources[position];
            if position < begin {
                self.set_value(position, self.fingerprint(old_source, position, begin));
                self.following[position] = begin;
            } else if position != begin {
                self.set_value(position, Fingerprint::default());
                self.positions.erase(position);
            }
            if end < stop {
                self.sources[end] = old_source + end - position;
                self.following[end] = stop;
                self.set_value(end, self.fingerprint(self.sources[end], end, stop));
                self.positions.insert(end);
            }
            position = stop;
        }
        self.sources[begin] = source;
        self.following[begin] = end;
        self.set_value(begin, replacement);
        self.positions.insert(begin);
    }

    fn prefix(&self, length: usize) -> Fingerprint {
        let position = self.positions.predecessor(length - 1);
        let mut value = Fingerprint::default();
        let mut index = position;
        while index != 0 {
            value.0 += self.fenwick[index].0;
            value.1 += self.fenwick[index].1;
            index &= index - 1;
        }
        value.0 %= MOD;
        value.1 %= OTHER_MOD;
        value
            + if self.following[position] == length {
                self.values[position]
            } else {
                self.fingerprint(self.sources[position], position, length)
            }
    }

    fn answer(&mut self) -> usize {
        if let Some(&answer) = self.cache.get(&self.whole) {
            return answer;
        }
        let mut period = self.n;
        let repeated = self.power[self.n] - Fingerprint(1, 1);
        // Remove prime factors while the shorter prefix still generates the string.
        for &prime in &self.primes {
            while period % prime == 0 {
                let candidate = period / prime;
                let multiplier = *self.multipliers.entry(candidate).or_insert_with(|| {
                    (self.power[candidate] - Fingerprint(1, 1)) * self.power[self.n - candidate]
                });
                if self.whole * multiplier != self.prefix(candidate) * repeated {
                    break;
                }
                period = candidate;
            }
        }
        let result = self.n * period;
        if self.cache.len() == CACHE_LIMIT {
            self.cache.clear();
        }
        self.cache.insert(self.whole, result);
        result
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let m: usize = tokens.next().unwrap().parse().unwrap();
    let q: usize = tokens.next().unwrap().parse().unwrap();
    let mut text = tokens.next().unwrap().as_bytes().to_vec();
    let mut starts = vec![0; m + 1];
    let mut lengths = vec![0; m + 1];
    lengths[0] = n;
    for index in 1..=m {
        let part = tokens.next().unwrap().as_bytes();
        starts[index] = text.len();
        lengths[index] = part.len();
        text.extend_from_slice(part);
    }
    let mut solver = Solver::new(n, &text);
    let mut output = io::BufWriter::new(io::stdout().lock());
    writeln!(output, "{}", solver.answer()).unwrap();
    for _ in 0..q {
        let begin = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
        let index: usize = tokens.next().unwrap().parse().unwrap();
        solver.replace(begin, begin + lengths[index], starts[index]);
        writeln!(output, "{}", solver.answer()).unwrap();
    }
}
