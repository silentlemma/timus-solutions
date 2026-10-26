use std::io::{self, Read, Write};
use std::time::{Duration, Instant};

// Three exact searches with growing time slices and perturbed orders, tried in
// turns until one places all ships: B (rows one at a time), C (B over the
// rare lengths only), D (C with residues modulo K checked exactly).
const MAX_SHIPS: usize = 100;
const MAX_ROWS: usize = 10;
const MAX_LEN: usize = 100;
const MAX_SUM: usize = 10001; // fewer than 100 ships of at most 100
const TIME_LIMIT_MILLIS: u64 = 900;
const TIME_LIMIT: Duration = Duration::from_millis(TIME_LIMIT_MILLIS);
const CLOCK_EVERY: i64 = 256; // nodes between looks at the clock
const WORD: usize = 64;
const WORDS: usize = (MAX_SUM + WORD - 1) / WORD;
const XS_A: u32 = 13; // xorshift32 shifts
const XS_B: u32 = 17;
const XS_C: u32 = 5;
const GOLDEN: u64 = 0x9E37_79B9_7F4A_7C15; // splitmix64 finalizer
const MIX1: u64 = 0xBF58_476D_1CE4_E5B9;
const MIX2: u64 = 0x94D0_49BB_1331_11EB;
const MIX_S1: u32 = 30;
const MIX_S2: u32 = 27;
const MIX_S3: u32 = 31;
const MEMO_BITS: u32 = 20;
const MEMO_SIZE: usize = 1 << MEMO_BITS;
const PROBES: usize = 8;
const CHECK_BITS: u32 = 21;
const CHECK_SIZE: usize = 1 << CHECK_BITS;
const CHECK_PROBES: usize = 4;
const MAX_CODES: f64 = 1e17; // the count vectors must fit in 64 bits
const QUERY_BUDGET: i64 = 100000;
const MAX_OVER: i32 = 5; // queries over budget before a check gives up
const ROW_RADIX: u64 = 16; // more than the rows
const SLOT_SHIFT: u32 = 8;
const SALT: u64 = 0x1234567;
const MAX_CHECKS: usize = 13;
const ROW_SALT: u64 = 0x51ED27;
const REMAINDER_SALT: u64 = 0xC0FFEE;
const TAG_SALT: u64 = 0x7A6;

fn mix(mut x: u64) -> u64 {
    x = x.wrapping_add(GOLDEN);
    x = (x ^ (x >> MIX_S1)).wrapping_mul(MIX1);
    x = (x ^ (x >> MIX_S2)).wrapping_mul(MIX2);
    x ^ (x >> MIX_S3)
}

fn get(b: &[u64], x: usize) -> bool {
    (b[x / WORD] >> (x % WORD)) & 1 != 0
}

fn one(b: &mut [u64]) {
    b.fill(0);
    b[0] = 1;
}

// dst = src | src << sh over the width of dst
fn shift_or(dst: &mut [u64], src: &[u64], sh: usize) {
    let (ws, bs) = (sh / WORD, sh % WORD);
    for i in (0..dst.len()).rev() {
        let mut x = src[i];
        if i >= ws {
            let j = i - ws;
            x |= src[j] << bs;
            if bs != 0 && j > 0 {
                x |= src[j - 1] >> (WORD - bs);
            }
        }
        dst[i] = x;
    }
}

fn shift_or_self(b: &mut [u64], sh: usize) {
    let src = b.to_vec();
    shift_or(b, &src, sh);
}

struct Clock {
    started: Instant,
    nodes: i64,
    attempt_end: Duration, // the time when the current attempt stops
    aborted: bool,
}

impl Clock {
    fn tick(&mut self) -> bool {
        self.nodes += 1;
        if self.nodes % CLOCK_EVERY == 0 && self.started.elapsed() > self.attempt_end {
            self.aborted = true;
            return false;
        }
        true
    }
}

// Failed states of the row searches, by a hash of the unused ships and the
// open rows; they do not depend on the order, so they survive restarts.
struct Memo {
    zobrist: [u64; MAX_LEN + 1], // a random key per ship length
    table: Vec<u64>,
}

impl Memo {
    fn known(&self, k: u64) -> bool {
        let p = (k >> (WORD as u32 - MEMO_BITS)) as usize;
        for t in 0..PROBES {
            let e = self.table[(p + t) % MEMO_SIZE];
            if e == k {
                return true;
            }
            if e == 0 {
                return false;
            }
        }
        false
    }

    fn remember(&mut self, k: u64) {
        let p = (k >> (WORD as u32 - MEMO_BITS)) as usize;
        for t in 0..PROBES {
            let e = &mut self.table[(p + t) % MEMO_SIZE];
            if *e == 0 || *e == k {
                *e = k;
                return;
            }
        }
        self.table[(p + (k % PROBES as u64) as usize) % MEMO_SIZE] = k;
    }
}

// For strategy D: ships not divisible by modulus fall into classes by residue.
// Rows b.. can only be completed if the remaining class counts split among
// them so that each row gets its length modulo it: a DP over (row, counts).
#[derive(Clone)]
struct Residues {
    modulus: usize,
    classes: usize,
    m: usize,
    residue: [usize; MAX_LEN], // classes by count, the largest last
    count: [usize; MAX_LEN],
    radix: [u64; MAX_LEN],
    target: [usize; MAX_ROWS], // row lengths modulo the modulus
    order_salt: u64,
    full: u64,
    ops: i64,
    budget: i64,
    broken: bool,    // the current query is over budget: "feasible"
    over_count: i32, // queries over budget in this attempt
}

impl Residues {
    // the classes for modulus k; None if the count vectors do not fit in 64 bits
    fn new(k: usize, ships: &[usize], m: usize) -> Option<Residues> {
        let mut per_residue = [0usize; MAX_LEN];
        for &x in ships {
            if x % k != 0 {
                per_residue[x % k] += 1;
            }
        }
        let mut list: Vec<(usize, usize)> = (1..k)
            .filter(|&r| per_residue[r] > 0)
            .map(|r| (per_residue[r], r))
            .collect();
        list.sort();
        let mut z = Residues {
            modulus: k,
            classes: 0,
            m,
            residue: [0; MAX_LEN],
            count: [0; MAX_LEN],
            radix: [0; MAX_LEN],
            target: [0; MAX_ROWS],
            order_salt: 0,
            full: (1u64 << k) - 1,
            ops: 0,
            budget: QUERY_BUDGET,
            broken: false,
            over_count: 0,
        };
        let (mut total, mut s) = (1.0f64, 1u64);
        for (cnt, r) in list {
            z.residue[z.classes] = r;
            z.count[z.classes] = cnt;
            z.radix[z.classes] = s;
            z.classes += 1;
            total *= (cnt + 1) as f64;
            if total > MAX_CODES {
                return None;
            }
            s *= (cnt + 1) as u64;
        }
        Some(z)
    }

    fn rotate(&self, x: u64, s: usize) -> u64 {
        if s == 0 {
            x
        } else {
            ((x << s) | (x >> (self.modulus - s))) & self.full
        }
    }

    fn over_budget(&mut self) -> bool {
        self.ops += 1;
        if self.ops > self.budget {
            self.broken = true;
        }
        self.broken
    }

    // Row b takes c of class j and of the classes after it (rest: the counts
    // left, r: the residue so far, reach[j]: residues the classes j.. give).
    #[allow(clippy::too_many_arguments)]
    fn split(
        &mut self,
        checked: &mut [u64],
        b: usize,
        rest: &[usize],
        reach: &[u64],
        code: u64,
        j: usize,
        r: usize,
        taken: u64,
    ) -> bool {
        if self.over_budget() {
            return true;
        }
        let md = self.modulus;
        let need = (self.target[b] + md - r) % md;
        if (reach[j] >> need) & 1 == 0 {
            return false;
        }
        if j == self.classes {
            return self.feasible(checked, b + 1, code - taken);
        }
        if j == self.classes - 1 {
            // the last class: its count is fixed modulo the modulus
            for c in 0..=rest[j].min(md - 1) {
                if c * self.residue[j] % md != need {
                    continue;
                }
                let mut cc = c;
                while cc <= rest[j] {
                    if self.over_budget()
                        || self.feasible(checked, b + 1, code - taken - cc as u64 * self.radix[j])
                        || self.broken
                    {
                        return true;
                    }
                    cc += md;
                }
            }
            return false;
        }
        for c in 0..=rest[j] {
            let next_r = (r + c * self.residue[j]) % md;
            if self.split(
                checked,
                b,
                rest,
                reach,
                code,
                j + 1,
                next_r,
                taken + c as u64 * self.radix[j],
            ) || self.broken
            {
                return true;
            }
        }
        false
    }

    fn feasible(&mut self, checked: &mut [u64], b: usize, code: u64) -> bool {
        if self.broken {
            return true;
        }
        let mut rest = [0usize; MAX_LEN];
        let mut c = code;
        for j in 0..self.classes {
            rest[j] = (c % (self.count[j] + 1) as u64) as usize;
            c /= (self.count[j] + 1) as u64;
        }
        if b == self.m - 1 {
            let r =
                (0..self.classes).fold(0, |r, j| (r + rest[j] * self.residue[j]) % self.modulus);
            return r == self.target[b];
        }
        let key =
            mix(self.order_salt ^ mix(code.wrapping_mul(ROW_RADIX).wrapping_add(b as u64))) & !1;
        let p = (key >> (WORD as u32 - CHECK_BITS)) as usize;
        for t in 0..CHECK_PROBES {
            let e = checked[(p + t) % CHECK_SIZE];
            if e & !1 == key {
                return e & 1 != 0;
            }
        }
        let mut reach = [0u64; MAX_LEN + 1];
        reach[self.classes] = 1;
        for j in (0..self.classes).rev() {
            for t in 0..=rest[j].min(self.modulus - 1) {
                reach[j] |= self.rotate(reach[j + 1], t * self.residue[j] % self.modulus);
            }
            self.ops += rest[j].min(self.modulus) as i64 + 1;
        }
        if self.ops > self.budget {
            self.broken = true;
            return true;
        }
        let ok = self.split(checked, b, &rest, &reach, code, 0, 0, 0);
        if self.broken {
            return true;
        }
        let mut q = (p + ((key >> SLOT_SHIFT) % CHECK_PROBES as u64) as usize) % CHECK_SIZE;
        for t in 0..CHECK_PROBES {
            if checked[(p + t) % CHECK_SIZE] == 0 {
                q = (p + t) % CHECK_SIZE;
                break;
            }
        }
        checked[q] = key | ok as u64;
        ok
    }

    fn full_code(&self) -> u64 {
        (0..self.classes)
            .map(|j| self.count[j] as u64 * self.radix[j])
            .sum()
    }

    // a query from a search: limited effort, "feasible" when it runs out
    fn query(&mut self, checked: &mut [u64], clock: &Clock, b: usize, code: u64) -> bool {
        if self.over_count > MAX_OVER || clock.started.elapsed() > clock.attempt_end {
            return true;
        }
        self.ops = 0;
        self.broken = false;
        let ok = self.feasible(checked, b, code);
        self.over_count += self.broken as i32;
        ok
    }

    // a new attempt with these row lengths, in search order
    fn set_rows(&mut self, lens: &[usize]) {
        self.order_salt = mix(SALT + self.modulus as u64);
        for (b, &l) in lens.iter().enumerate() {
            self.target[b] = l % self.modulus;
            self.order_salt = mix(self.order_salt ^ l as u64);
        }
        self.over_count = 0;
        self.budget = QUERY_BUDGET;
    }
}

// Strategies B, C, D: rows are filled one at a time; inside a row each ship
// is taken or skipped (equal ships skipped together). Ships kept..n are
// deferred: a row only needs a remainder they make, and they go in last.
struct RowSearch {
    n: usize,
    m: usize,
    kept: usize,
    v: Vec<usize>,
    len: Vec<usize>,
    place: Vec<usize>,
    remainder: Vec<usize>,
    used: Vec<bool>,
    tag: u64, // which lengths are deferred (0: none)
    ships_hash: u64,
    remainder_hash: u64,
    width: usize,
    sums: Vec<Vec<u64>>, // [row * (MAX_SHIPS + 1) + pos]: sums of unused ships pos.. (+ deferred)
    deferred_sums: Vec<u64>,
    checks: Vec<usize>, // indices into the residue pool; valid: closed rows are complete
    cls: Vec<Vec<i32>>, // the class of ship i in check t, -1 if divisible
    code: [u64; MAX_CHECKS], // mixed-radix codes of the unused class counts
}

struct Shared {
    clock: Clock,
    memo: Memo,
    pool: Vec<Residues>,
    checked: Vec<u64>,
}

impl RowSearch {
    fn new() -> RowSearch {
        RowSearch {
            n: 0,
            m: 0,
            kept: 0,
            v: vec![0; MAX_SHIPS],
            len: vec![0; MAX_ROWS],
            place: vec![0; MAX_SHIPS],
            remainder: vec![0; MAX_ROWS],
            used: vec![false; MAX_SHIPS],
            tag: 0,
            ships_hash: 0,
            remainder_hash: 0,
            width: 1,
            sums: vec![vec![0; WORDS]; MAX_ROWS * (MAX_SHIPS + 1)],
            deferred_sums: vec![0; WORDS],
            checks: Vec::new(),
            cls: vec![vec![0; MAX_SHIPS]; MAX_CHECKS],
            code: [0; MAX_CHECKS],
        }
    }

    fn take(&mut self, sh: &Shared, pos: usize, add: bool) {
        for (t, &z) in self.checks.iter().enumerate() {
            if self.cls[t][pos] >= 0 {
                let d = sh.pool[z].radix[self.cls[t][pos] as usize];
                self.code[t] = if add {
                    self.code[t].wrapping_add(d)
                } else {
                    self.code[t].wrapping_sub(d)
                };
            }
        }
    }

    fn sums_at(&self, b: usize, pos: usize) -> &[u64] {
        &self.sums[b * (MAX_SHIPS + 1) + pos][..self.width]
    }

    fn place_deferred(&mut self, sh: &mut Shared, sub: &mut RowSearch) -> bool {
        let count = self.n - self.kept;
        sub.n = count;
        sub.kept = count;
        sub.m = self.m;
        sub.checks.clear();
        sub.v[..count].copy_from_slice(&self.v[self.kept..self.n]);
        sub.len[..self.m].copy_from_slice(&self.remainder[..self.m]);
        if !sub.run(sh, None, 0) {
            return false;
        }
        let kept = self.kept;
        self.place[kept..kept + count].copy_from_slice(&sub.place[..count]);
        true
    }

    fn fill(
        &mut self,
        sh: &mut Shared,
        mut sub: Option<&mut RowSearch>,
        b: usize,
        mut pos: usize,
        r: usize,
    ) -> bool {
        if !sh.clock.tick() {
            return false;
        }
        while pos < self.kept && self.used[pos] {
            pos += 1;
        }
        if r == 0 || pos >= self.kept {
            // row b is done; the rest comes from deferred ships
            if r > 0 && (self.kept == self.n || !get(&self.deferred_sums[..self.width], r)) {
                return false;
            }
            self.remainder[b] = r;
            let deferred = self.kept < self.n;
            if deferred {
                self.remainder_hash = self.remainder_hash.wrapping_add(mix(r as u64));
            }
            let ok = self.open(sh, sub, b + 1);
            if deferred {
                self.remainder_hash = self.remainder_hash.wrapping_sub(mix(r as u64));
            }
            return ok;
        }
        let x = self.v[pos];
        if x <= r && get(self.sums_at(b, pos + 1), r - x) {
            self.used[pos] = true;
            self.place[pos] = b;
            self.ships_hash = self.ships_hash.wrapping_sub(sh.memo.zobrist[x]);
            self.take(sh, pos, false);
            if self.fill(sh, sub.as_deref_mut(), b, pos + 1, r - x) {
                return true;
            }
            self.used[pos] = false;
            self.ships_hash = self.ships_hash.wrapping_add(sh.memo.zobrist[x]);
            self.take(sh, pos, true);
            if sh.clock.aborted {
                return false;
            }
        }
        let mut q = pos + 1; // skip ship x and all its copies
        while q < self.kept && self.v[q] == x {
            q += 1;
        }
        get(self.sums_at(b, q), r) && self.fill(sh, sub, b, q, r)
    }

    fn open(&mut self, sh: &mut Shared, sub: Option<&mut RowSearch>, b: usize) -> bool {
        if b == self.m {
            return self.place_deferred(sh, sub.unwrap());
        }
        if b == self.m - 1 {
            // the last row takes all the ships left
            let mut s = 0;
            for i in 0..self.kept {
                if !self.used[i] {
                    s += self.v[i];
                    self.place[i] = b;
                }
            }
            if self.kept == self.n {
                return true;
            }
            if s > self.len[b] || !get(&self.deferred_sums[..self.width], self.len[b] - s) {
                return false;
            }
            self.remainder[b] = self.len[b] - s;
            return self.place_deferred(sh, sub.unwrap());
        }
        let mut rows_hash = self.tag;
        for c in b..self.m {
            rows_hash = rows_hash.wrapping_add(mix(self.len[c] as u64 + ROW_SALT));
        }
        let key = mix(self.ships_hash ^ mix(rows_hash))
            .wrapping_add(mix(self.remainder_hash ^ REMAINDER_SALT))
            | 1;
        if sh.memo.known(key) {
            return false;
        }
        for t in 0..self.checks.len() {
            let z = self.checks[t];
            let Shared {
                pool,
                checked,
                clock,
                ..
            } = sh;
            if !pool[z].query(checked, clock, b, self.code[t]) {
                sh.memo.remember(key);
                return false;
            }
        }
        let base = b * (MAX_SHIPS + 1);
        let w = self.width;
        if self.kept == self.n {
            one(&mut self.sums[base + self.kept][..w]);
        } else {
            let (d, s) = (&self.deferred_sums, &mut self.sums[base + self.kept]);
            s[..w].copy_from_slice(&d[..w]);
        }
        for i in (0..self.kept).rev() {
            let (head, tail) = self.sums.split_at_mut(base + i + 1);
            let (dst, src) = (&mut head[base + i][..w], &tail[0][..w]);
            if self.used[i] {
                dst.copy_from_slice(src);
            } else {
                shift_or(dst, src, self.v[i]);
            }
        }
        for c in b..self.m {
            if !get(self.sums_at(b, 0), self.len[c]) {
                sh.memo.remember(key);
                return false;
            }
        }
        let ok = self.fill(sh, sub, b, 0, self.len[b]);
        if !ok && !sh.clock.aborted {
            sh.memo.remember(key);
        }
        ok
    }

    fn run(&mut self, sh: &mut Shared, sub: Option<&mut RowSearch>, tag: u64) -> bool {
        self.tag = tag;
        self.width = self.len[..self.m].iter().max().unwrap() / WORD + 1;
        self.ships_hash = 0;
        self.remainder_hash = 0;
        for t in 0..self.checks.len() {
            self.code[t] = sh.pool[self.checks[t]].full_code();
        }
        self.used[..self.n].fill(false);
        for i in 0..self.kept {
            self.ships_hash = self.ships_hash.wrapping_add(sh.memo.zobrist[self.v[i]]);
        }
        if self.kept < self.n {
            let w = self.width;
            one(&mut self.deferred_sums[..w]);
            for i in self.kept..self.n {
                shift_or_self(&mut self.deferred_sums[..w], self.v[i]);
            }
        }
        self.open(sh, sub, 0)
    }
}

struct Rng(u32);

impl Rng {
    fn next(&mut self) -> u32 {
        self.0 ^= self.0 << XS_A;
        self.0 ^= self.0 >> XS_B;
        self.0 ^= self.0 << XS_C;
        self.0
    }

    fn next64(&mut self) -> u64 {
        let high = self.next() as u64;
        high << (WORD / 2) | self.next() as u64
    }
}

const MOD_MIN: usize = 2; // moduli for D
const MOD_MAX: usize = 50;
const SMALL_MOD_MAX: usize = 6; // B also checks moduli up to this
const TOP_MODS: usize = 4;
const SCORE_SCALE: i64 = 100;
const SLOTS: usize = 5; // B, B with rows ascending, C, D, B again
const SHARE: usize = 4; // a modulus must divide a quarter of the ships
const STRATEGY_B: usize = 0;
const STRATEGY_C: usize = 1;
const STRATEGY_D: usize = 2;
// B gets three slots of five: the hardest tests need its row-by-row search.
const SLOT_STRATEGY: [usize; SLOTS] = [STRATEGY_B, STRATEGY_B, STRATEGY_C, STRATEGY_D, STRATEGY_B];
const RARE_LEVELS: usize = 3; // C: "rare" means at most 1..3 copies
const KEY_SCALE: u32 = 1000; // ship order keys
const MAX_NOISE: usize = 30;
const RARE_FIRST: i64 = 1_000_000_000;
const FIRST_SLICE: f64 = 0.003; // seconds
const SLICE_GROWTH: f64 = 1.6;
const MAX_GROWTH: i32 = 20;
const SEED: u32 = 2463534242;

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let nums: Vec<usize> = text
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, m) = (nums[0], nums[1]);
    let ships = nums[2..2 + n].to_vec();
    let row_len = nums[2 + n..2 + n + m].to_vec();
    let mut rng = Rng(SEED);
    let mut sh = Shared {
        clock: Clock {
            started: Instant::now(),
            nodes: 0,
            attempt_end: Duration::ZERO,
            aborted: false,
        },
        memo: Memo {
            zobrist: [0; MAX_LEN + 1],
            table: vec![0; MEMO_SIZE],
        },
        pool: Vec::new(),
        checked: vec![0; CHECK_SIZE],
    };
    let mut copies = [0usize; MAX_LEN + 1];
    for &x in &ships {
        copies[x] += 1;
    }
    for x in 0..=MAX_LEN {
        sh.memo.zobrist[x] = rng.next64();
    }
    let sane = row_len.iter().all(|&l| l > 0 && l < MAX_SUM);

    // moduli for D from two rankings: many multiples of a large k, and the
    // fewest non-multiples (say all ships even but one odd ship per row)
    let (mut by_score, mut by_few): (Vec<(i64, usize)>, Vec<(i64, usize)>) =
        (Vec::new(), Vec::new());
    for k in MOD_MIN..=MOD_MAX {
        let d = ships.iter().filter(|&&x| x % k == 0).count();
        if d < n && d >= MOD_MIN.max(n / SHARE) {
            by_score.push((-((d * k) as i64), k));
            by_few.push(((n - d) as i64 * SCORE_SCALE - k as i64, k));
        }
    }
    by_score.sort();
    by_few.sort();
    let mut d_mods: Vec<usize> = Vec::new();
    for c in 0..TOP_MODS {
        for list in [&by_score, &by_few] {
            if c < list.len() && !d_mods.contains(&list[c].1) {
                d_mods.push(list[c].1);
            }
        }
    }
    // residue checks: D's moduli, plus small ones that B checks with them
    let mut d_checks: Vec<Option<usize>> = vec![None; d_mods.len()];
    let mut mods = d_mods.clone();
    for k in MOD_MIN..=SMALL_MOD_MAX {
        if !mods.contains(&k) {
            mods.push(k);
        }
    }
    for (c, &k) in mods.iter().enumerate() {
        if let Some(z) = Residues::new(k, &ships, m).filter(|z| z.classes > 0) {
            if c < d_mods.len() {
                d_checks[c] = Some(sh.pool.len());
            }
            sh.pool.push(z);
        }
    }
    let b_checks: Vec<usize> = (0..sh.pool.len()).collect();

    let mut main_search = RowSearch::new();
    let mut sub_search = RowSearch::new();
    let mut ship_id = vec![0usize; n];
    let mut row_id: Vec<usize> = (0..m).collect();
    let mut placed = vec![0usize; n];
    let mut solved = false;
    let mut attempt = 0;
    while sane && !solved {
        let (slot, round) = (attempt % SLOTS, attempt / SLOTS);
        attempt += 1;
        let mut strategy = SLOT_STRATEGY[slot];
        let rows_up = slot == 1;
        let rare_level = 1 + round % RARE_LEVELS;
        let ci = if d_mods.is_empty() {
            None
        } else {
            Some(round % d_mods.len())
        };
        let k_mod = ci.map_or(0, |c| d_mods[c]);
        let mut rare = [false; MAX_LEN + 1];
        for x in 1..=MAX_LEN {
            rare[x] = if strategy == STRATEGY_C {
                copies[x] <= rare_level
            } else {
                strategy == STRATEGY_D && k_mod != 0 && x % k_mod != 0
            };
        }
        if strategy == STRATEGY_D && k_mod == 0 {
            strategy = STRATEGY_B;
        }
        let kept = ships.iter().filter(|&&x| rare[x]).count();
        if (strategy == STRATEGY_C || strategy == STRATEGY_D) && (kept == 0 || kept == n) {
            strategy = STRATEGY_B;
        }

        // ship order: B longest first, C and D rare lengths first,
        // later rounds add noise, equal lengths stay together
        let mut length_key = [0i64; MAX_LEN + 1];
        for x in 1..=MAX_LEN {
            length_key[x] = x as i64 * KEY_SCALE as i64;
            if round > 0 {
                length_key[x] +=
                    (rng.next() % (KEY_SCALE * MAX_NOISE.min(round + 1) as u32)) as i64;
            }
            if (strategy == STRATEGY_C || strategy == STRATEGY_D) && rare[x] {
                length_key[x] += RARE_FIRST;
            }
        }
        let mut order: Vec<usize> = (0..n).collect();
        order.sort_by(|&p, &q| {
            (length_key[ships[q]], ships[q], p).cmp(&(length_key[ships[p]], ships[p], q))
        });
        let v: Vec<usize> = order.iter().map(|&i| ships[i]).collect();
        ship_id.copy_from_slice(&order);
        // rows: longest first in round 0, then random; shortest first for the
        // second B slot and for D in even rounds (the last row absorbs the rest)
        row_id = (0..m).collect();
        if rows_up || (strategy == STRATEGY_D && round % 2 == 0) {
            row_id.sort_by_key(|&j| row_len[j]);
        } else if round == 0 {
            row_id.sort_by_key(|&j| std::cmp::Reverse(row_len[j]));
        } else {
            for j in (1..m).rev() {
                let k = rng.next() as usize % (j + 1);
                row_id.swap(j, k);
            }
        }

        sh.clock.nodes = 0;
        sh.clock.aborted = false;
        let slice = FIRST_SLICE * SLICE_GROWTH.powi((round as i32).min(MAX_GROWTH));
        sh.clock.attempt_end =
            (sh.clock.started.elapsed() + Duration::from_secs_f64(slice)).min(TIME_LIMIT);
        let lens: Vec<usize> = row_id.iter().map(|&j| row_len[j]).collect();
        let (kept_here, checks): (usize, Vec<usize>) = match strategy {
            STRATEGY_B => (
                n,
                if (round + slot) % 2 == 0 {
                    b_checks.clone()
                } else {
                    Vec::new()
                },
            ),
            STRATEGY_C => (kept, Vec::new()),
            _ => (kept, ci.and_then(|c| d_checks[c]).into_iter().collect()),
        };
        let s = &mut main_search;
        s.n = n;
        s.m = m;
        s.kept = kept_here;
        s.v[..n].copy_from_slice(&v);
        s.len[..m].copy_from_slice(&lens);
        for (t, &z) in checks.iter().enumerate() {
            let r = &mut sh.pool[z];
            let mut class_of = [-1i32; MAX_LEN];
            for j in 0..r.classes {
                class_of[r.residue[j]] = j as i32;
            }
            for i in 0..n {
                s.cls[t][i] = class_of[v[i] % r.modulus];
            }
            r.set_rows(&lens);
        }
        s.checks = checks;
        let mut tag = 0;
        if kept_here < n {
            let mut is_rare = [false; MAX_LEN + 1];
            for &x in &v[..kept_here] {
                is_rare[x] = true;
            }
            tag = TAG_SALT;
            for x in 1..=MAX_LEN {
                if is_rare[x] {
                    tag = mix(tag ^ x as u64);
                }
            }
        }
        solved = s.run(&mut sh, Some(&mut sub_search), tag);
        if solved {
            placed.copy_from_slice(&s.place[..n]);
        }
        if !solved && sh.clock.started.elapsed() > TIME_LIMIT {
            break;
        }
    }

    let mut rows: Vec<Vec<String>> = vec![Vec::new(); m];
    for i in 0..n {
        rows[row_id[placed[i]]].push(ships[ship_id[i]].to_string());
    }
    let mut out = String::new();
    for row in &rows {
        out.push_str(&format!("{}\n{}\n", row.len(), row.join(" ")));
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
