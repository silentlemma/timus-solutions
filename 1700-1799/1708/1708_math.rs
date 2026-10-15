use std::collections::HashMap;
use std::io::{self, Read, Write};

const LONGEST: usize = 15; // no minimal forbidden multiset is longer for bases up to 36
const SHIFT: u32 = 6; // bits per digit in a word code
const DIGIT_MASK: u128 = (1 << SHIFT) - 1;
const LENGTH_AT: u32 = 92; // the length sits above the 90 bits of the word
const STAR: u64 = 15; // a pattern count meaning "any number of this digit"

const FIELD: usize = 4; // bits per count in a packed vector
const FIELDS: usize = 16; // counts per 64-bit word
const WORDS: usize = 3;
const COUNT_MASK: u64 = (1 << FIELD) - 1;
const MIX_1: u64 = 0x9e37_79b9_7f4a_7c15;
const MIX_2: u64 = 0xbf58_476d_1ce4_e5b9;
const MIX_3: u64 = 0x94d0_49bb_1331_11eb;
const MIX_SHIFT_1: u32 = 30;
const MIX_SHIFT_2: u32 = 27;
const MIX_SHIFT_3: u32 = 31;
const LOAD_DEN: usize = 2; // the hash table is kept at most half full
const KEY_AT: u32 = 32; // a table slot keeps the key above the index
const WORD_BITS: u32 = 64;
const ESTIMATE_DIV: usize = 2; // about base^4 / 2 least words exist
const DIGITS: &[u8] = b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

fn mix(x: u64) -> u64 {
    let mut x = x.wrapping_add(MIX_1);
    x = (x ^ (x >> MIX_SHIFT_1)).wrapping_mul(MIX_2);
    x = (x ^ (x >> MIX_SHIFT_2)).wrapping_mul(MIX_3);
    x ^ (x >> MIX_SHIFT_3)
}

// the least number of a pair: (length << LENGTH_AT) | sorted digits, SHIFT
// bits each, so that comparing the numbers compares length first
fn encode(length: usize, word: u128) -> u128 {
    (length as u128) << LENGTH_AT | word
}

// open addressing from a pair key to the index of its least word: a slot
// holds (key + 1) << KEY_AT | index, and 0 marks an empty one
struct Table {
    slots: Vec<u64>,
    bits: u32,
    used: usize,
}

impl Table {
    fn new(expected: usize) -> Table {
        let mut bits = 1;
        while (1usize << bits) < expected * LOAD_DEN {
            bits += 1;
        }
        Table { slots: vec![0; 1 << bits], bits, used: 0 }
    }

    fn slot(&self, key: u32) -> usize {
        let mask = self.slots.len() - 1;
        let mut pos = ((key as u64).wrapping_mul(MIX_1) >> (WORD_BITS - self.bits)) as usize;
        while self.slots[pos] != 0 && self.slots[pos] >> KEY_AT != key as u64 + 1 {
            pos = (pos + 1) & mask;
        }
        pos
    }

    fn get(&self, key: u32) -> i32 {
        let s = self.slots[self.slot(key)];
        if s == 0 {
            -1
        } else {
            s as u32 as i32
        }
    }

    fn put(&mut self, key: u32, value: i32) {
        if (self.used + 1) * LOAD_DEN > self.slots.len() {
            let old = std::mem::replace(&mut self.slots, Vec::new());
            self.bits += 1;
            self.slots = vec![0; old.len() * 2];
            for s in old {
                if s != 0 {
                    let pos = self.slot((s >> KEY_AT) as u32 - 1);
                    self.slots[pos] = s;
                }
            }
        }
        let pos = self.slot(key);
        self.slots[pos] = (key as u64 + 1) << KEY_AT | value as u32 as u64;
        self.used += 1;
    }
}

// counts of the digits 1 .. m, FIELD bits each, with the set of nonzero
// counts and their total
#[derive(Clone, Copy, Default)]
struct Counts {
    w: [u64; WORDS],
    mask: u64,
    sum: u32,
}

impl Counts {
    fn get(&self, i: usize) -> u64 {
        (self.w[i / FIELDS] >> (i % FIELDS * FIELD)) & COUNT_MASK
    }

    fn put(&mut self, i: usize, c: u64) {
        let shift = i % FIELDS * FIELD;
        self.sum = self.sum + c as u32 - self.get(i) as u32;
        self.w[i / FIELDS] = (self.w[i / FIELDS] & !(COUNT_MASK << shift)) | c << shift;
        if c != 0 {
            self.mask |= 1 << i;
        } else {
            self.mask &= !(1 << i);
        }
    }

    fn without(mut self, i: usize) -> Counts {
        self.put(i, 0);
        self
    }
}

// whether every count of g is at most that of f
fn below(g: &Counts, f: &Counts) -> bool {
    let mut rest = g.mask;
    while rest != 0 {
        let i = rest.trailing_zeros() as usize;
        if g.get(i) > f.get(i) {
            return false;
        }
        rest &= rest - 1;
    }
    true
}

// vectors sorted by their sets of nonzero counts, to find quickly whether one
// of them lies below a given vector
struct Index {
    items: Vec<Counts>,
    supports: Vec<u64>, // the distinct sets, increasing
    begin: Vec<usize>,  // items of supports[s] are begin[s] .. begin[s + 1] - 1
}

impl Index {
    fn new(mut items: Vec<Counts>) -> Index {
        items.sort_by_key(|v| v.mask);
        let mut supports = Vec::new();
        let mut begin = Vec::new();
        for i in 0..items.len() {
            if i == 0 || items[i].mask != items[i - 1].mask {
                supports.push(items[i].mask);
                begin.push(i);
            }
        }
        begin.push(items.len());
        Index { items, supports, begin }
    }

    fn in_group(&self, s: usize, f: &Counts) -> bool {
        self.items[self.begin[s]..self.begin[s + 1]].iter().any(|g| below(g, f))
    }

    // whether some item lies below f: by the subsets of its support or by a
    // scan of the supports, whichever is shorter
    fn covers(&self, f: &Counts) -> bool {
        if (1u64 << f.mask.count_ones()) < self.supports.len() as u64 {
            let mut sub = f.mask;
            loop {
                if let Ok(s) = self.supports.binary_search(&sub) {
                    if self.in_group(s, f) {
                        return true;
                    }
                }
                if sub == 0 {
                    return false;
                }
                sub = (sub - 1) & f.mask;
            }
        }
        (0..self.supports.len()).any(|s| self.supports[s] & !f.mask == 0 && self.in_group(s, f))
    }
}

// the minimal vectors: one that lies below another has a smaller total, so
// the vectors are taken by total, and those of one total are checked only
// against the smaller ones
fn minimal(mut vectors: Vec<Counts>) -> Vec<Counts> {
    vectors.sort_by_key(|v| (v.sum, v.w));
    let mut kept: Vec<Counts> = Vec::new();
    let mut smaller = Index::new(Vec::new());
    let mut i = 0;
    while i < vectors.len() {
        let mut j = i;
        let mut grown = false;
        while j < vectors.len() && vectors[j].sum == vectors[i].sum {
            let repeat = j > i && vectors[j].w == vectors[j - 1].w;
            if !repeat && !smaller.covers(&vectors[j]) {
                kept.push(vectors[j]);
                grown = true;
            }
            j += 1;
        }
        if grown && j < vectors.len() {
            smaller = Index::new(kept.clone());
        }
        i = j;
    }
    kept
}

// consecutive nodes start, start + 1, ..., start + count - 1
#[derive(Clone, Copy)]
struct Run {
    start: u32,
    count: u32,
}

// patterns over the first n digits, a trie of (parent, count) nodes, where
// the patterns of one solved set are a few runs of consecutive nodes
struct Patterns {
    nodes: Vec<u32>, // (parent << FIELD) | count; node 0 is empty
    stars: Vec<u32>,
    memo: HashMap<u64, usize>,
    runs: Vec<Run>,
    first_run: Vec<usize>, // the runs of result i are first_run[i] .. first_run[i + 1] - 1
}

impl Patterns {
    fn new(digits: usize) -> Patterns {
        let mut p = Patterns {
            nodes: vec![0],
            stars: vec![0],
            memo: HashMap::new(),
            runs: Vec::new(),
            first_run: vec![0],
        };
        for _ in 0..digits {
            let node = p.extend(*p.stars.last().unwrap(), STAR);
            p.stars.push(node);
        }
        p
    }

    fn extend(&mut self, parent: u32, count: u64) -> u32 {
        self.nodes.push(parent << FIELD | count as u32);
        (self.nodes.len() - 1) as u32
    }

    fn members(&self, result: usize) -> Vec<u32> {
        let mut out = Vec::new();
        for run in &self.runs[self.first_run[result]..self.first_run[result + 1]] {
            out.extend(run.start..run.start + run.count);
        }
        out
    }

    fn decode(&self, mut node: u32, n: usize) -> Counts {
        let mut p = Counts::default();
        for i in (0..n).rev() {
            let c = self.nodes[node as usize] as u64 & COUNT_MASK;
            p.w[i / FIELDS] |= c << (i % FIELDS * FIELD);
            if c != 0 {
                p.mask |= 1 << i;
            }
            node = self.nodes[node as usize] >> FIELD;
        }
        p
    }

    // the index of the result: patterns whose union is the set of count vectors
    // over the first n digits above none of gens, a set of minimal vectors; the
    // last digit takes each fixed count below the largest one, then any count
    fn solve(&mut self, gens: &[Counts], n: usize) -> usize {
        let mut key = mix(n as u64).wrapping_add(gens.len() as u64);
        for g in gens {
            let h = mix(g.w[0])
                ^ mix(g.w[1].wrapping_add(MIX_1)).wrapping_mul(MIX_3)
                ^ mix(g.w[2].wrapping_add(MIX_2));
            key = key.wrapping_add(h);
        }
        if let Some(&found) = self.memo.get(&key) {
            return found;
        }
        let mut result: Vec<Run> = Vec::new();
        if gens.is_empty() {
            result.push(Run { start: self.stars[n], count: 1 });
        } else if gens[0].mask != 0 {
            let last = n - 1;
            let top = gens.iter().map(|g| g.get(last)).max().unwrap();
            // levels[k]: the minimal gens that apply with k copies of the last
            // digit; as gens are minimal, a newcomer with k copies never lies
            // above an earlier one, and the last level serves any count
            let mut levels: Vec<Vec<Counts>> = Vec::new();
            for k in 0..=top {
                let fresh: Vec<Counts> =
                    gens.iter().filter(|g| g.get(last) == k).map(|g| g.without(last)).collect();
                let mut level: Vec<Counts> = Vec::new();
                if let Some(previous) = levels.last() {
                    let newcomers = Index::new(fresh.clone());
                    level.extend(previous.iter().filter(|f| !newcomers.covers(f)));
                }
                level.extend(fresh);
                levels.push(level);
            }
            let open = Index::new(levels.pop().unwrap());
            for (k, level) in levels.iter().enumerate() {
                let k = k as u64;
                let sub = self.solve(level, last);
                let mut run = Run { start: self.nodes.len() as u32, count: 0 };
                for node in self.members(sub) {
                    // a prefix allowed with any count is already covered below
                    if open.covers(&self.decode(node, last)) {
                        self.extend(node, k);
                        run.count += 1;
                    }
                }
                result.push(run);
            }
            let sub = self.solve(&open.items, last);
            let mut run = Run { start: self.nodes.len() as u32, count: 0 };
            for node in self.members(sub) {
                self.extend(node, STAR);
                run.count += 1;
            }
            result.push(run);
        }
        self.runs.extend(result);
        self.first_run.push(self.runs.len());
        let index = self.first_run.len() - 2;
        self.memo.insert(key, index);
        index
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let base: usize = text.trim().parse().unwrap();
    let m = base - 1;
    // the least number of every pair (sum of digits, sum of squares) with at most
    // LONGEST digits: digits are appended in increasing order, and adding the
    // same digits to two words keeps their order, so the best per pair suffices
    let width = (LONGEST * m * m + 1) as u32;
    let estimate = base * base * base * base / ESTIMATE_DIV + 1;
    let mut least: Vec<(u128, u32)> = Vec::with_capacity(estimate);
    least.push((0, 0));
    let mut table = Table::new(estimate);
    table.put(0, 0);
    for d in 1..base {
        let step = d as u32 * width + (d * d) as u32;
        let count = least.len();
        for i in 0..count {
            let (value, mut key) = least[i];
            let length = (value >> LENGTH_AT) as usize;
            let mut word = value ^ encode(length, 0);
            for grown in length + 1..=LONGEST {
                key += step;
                word = word << SHIFT | d as u128;
                let candidate = encode(grown, word);
                let at = table.get(key);
                if at < 0 {
                    table.put(key, least.len() as i32);
                    least.push((candidate, key));
                } else if candidate < least[at as usize].0 {
                    least[at as usize].0 = candidate;
                }
            }
        }
    }
    // a minimal forbidden multiset is not the least of its pair, while every
    // multiset with one digit fewer is; without its largest digit it is one
    // of the least words, so each least word is grown by one digit at its end
    let mut forbidden: Vec<Counts> = Vec::new();
    let least_of = |key: u32| least[table.get(key) as usize].0;
    for &(value, key) in &least {
        let length = (value >> LENGTH_AT) as usize;
        if length == 0 || length >= LONGEST {
            continue;
        }
        let word = value ^ encode(length, 0);
        let digits: Vec<usize> = (0..length)
            .map(|i| ((word >> (SHIFT as usize * (length - 1 - i))) & DIGIT_MASK) as usize)
            .collect();
        for add in digits[length - 1]..base {
            let grown_key = key + (add * width as usize + add * add) as u32;
            if least_of(grown_key) == encode(length + 1, word << SHIFT | add as u128) {
                continue;
            }
            let mut is_minimal = true;
            for i in 0..length {
                let drop = digits[i];
                if drop == add || (i > 0 && digits[i - 1] == drop) {
                    continue;
                }
                let mut rest: u128 = 0;
                for (j, &d) in digits.iter().enumerate() {
                    if j != i {
                        rest = rest << SHIFT | d as u128;
                    }
                }
                rest = rest << SHIFT | add as u128;
                let shorter_key = grown_key - (drop * width as usize + drop * drop) as u32;
                if least_of(shorter_key) != encode(length, rest) {
                    is_minimal = false;
                    break;
                }
            }
            if is_minimal {
                let mut f = Counts::default();
                for &d in digits.iter().chain(std::iter::once(&add)) {
                    let c = f.get(d - 1);
                    f.put(d - 1, c + 1);
                }
                forbidden.push(f);
            }
        }
    }
    drop(least);
    drop(table);
    let mut patterns = Patterns::new(m);
    let top = patterns.solve(&minimal(forbidden), m);
    let mut lines: Vec<String> = Vec::new();
    for node in patterns.members(top) {
        let p = patterns.decode(node, m);
        let mut line = String::new();
        for i in 0..m {
            let ch = DIGITS[i + 1] as char;
            let c = p.get(i);
            if c == STAR {
                line.push(ch);
                line.push('*');
            } else {
                line.extend(std::iter::repeat(ch).take(c as usize));
            }
        }
        lines.push(line);
    }
    lines.sort();
    let mut out = io::BufWriter::new(io::stdout());
    for line in &lines {
        writeln!(out, "{}", line).unwrap();
    }
}
