use std::fmt::Write;
use std::io::{self, Read};

const TREE_FACTOR: usize = 4;

fn radii(s: &[u8], odd_cap: usize, even_cap: usize) -> (Vec<usize>, Vec<usize>) {
    let n = s.len();
    let (mut odd, mut even) = (vec![0; n], vec![0; n]);
    let (mut left, mut right) = (0_isize, -1_isize);
    for i in 0..n {
        let mut d = if i as isize > right {
            1
        } else {
            odd[(left + right - i as isize) as usize].min((right - i as isize + 1) as usize)
        };
        while d < odd_cap && i >= d && i + d < n && s[i - d] == s[i + d] {
            d += 1;
        }
        odd[i] = d;
        if (i + d) as isize - 1 > right {
            left = i as isize - d as isize + 1;
            right = (i + d) as isize - 1;
        }
    }
    left = 0;
    right = -1;
    for i in 0..n {
        let mut d = if i as isize > right {
            0
        } else {
            even[(left + right - i as isize + 1) as usize].min((right - i as isize + 1) as usize)
        };
        while d < even_cap && i > d && i + d < n && s[i - d - 1] == s[i + d] {
            d += 1;
        }
        even[i] = d;
        if (i + d) as isize - 1 > right {
            left = i as isize - d as isize;
            right = (i + d) as isize - 1;
        }
    }
    (odd, even)
}

struct Characters {
    n: usize,
    tag: Vec<u8>,
}
impl Characters {
    fn new(s: &[u8]) -> Self {
        let mut tree = Self {
            n: s.len(),
            tag: vec![0; TREE_FACTOR * s.len()],
        };
        tree.build(1, 0, s.len(), s);
        tree
    }
    fn build(&mut self, v: usize, a: usize, b: usize, s: &[u8]) {
        if b - a == 1 {
            self.tag[v] = s[a];
            return;
        }
        let mid = (a + b) / 2;
        self.build(2 * v, a, mid, s);
        self.build(2 * v + 1, mid, b, s);
        if self.tag[2 * v] == self.tag[2 * v + 1] {
            self.tag[v] = self.tag[2 * v];
        }
    }
    fn assign(&mut self, v: usize, a: usize, b: usize, left: usize, right: usize, c: u8) {
        if left <= a && b <= right {
            self.tag[v] = c;
            return;
        }
        let mid = (a + b) / 2;
        let old = self.tag[v];
        if old != 0 {
            self.tag[2 * v] = old;
            self.tag[2 * v + 1] = old;
            self.tag[v] = 0;
        }
        if left < mid {
            self.assign(2 * v, a, mid, left, right, c);
        }
        if mid < right {
            self.assign(2 * v + 1, mid, b, left, right, c);
        }
        if self.tag[2 * v] == self.tag[2 * v + 1] {
            self.tag[v] = self.tag[2 * v];
        }
    }
    fn collect(&self, v: usize, a: usize, b: usize, left: usize, right: usize, out: &mut Vec<u8>) {
        if self.tag[v] != 0 {
            let count = b.min(right) - a.max(left);
            out.resize(out.len() + count, self.tag[v]);
            return;
        }
        let mid = (a + b) / 2;
        if left < mid {
            self.collect(2 * v, a, mid, left, right, out);
        }
        if mid < right {
            self.collect(2 * v + 1, mid, b, left, right, out);
        }
    }
    fn extract(&self, left: usize, right: usize) -> Vec<u8> {
        let mut out = Vec::with_capacity(right - left);
        self.collect(1, 0, self.n, left, right, &mut out);
        out
    }
}

struct Counts {
    total: Vec<u32>,
    tag: Vec<u8>,
}
impl Counts {
    fn new(values: &[u32]) -> Self {
        let mut tree = Self {
            total: vec![0; TREE_FACTOR * values.len()],
            tag: vec![0; TREE_FACTOR * values.len()],
        };
        tree.build(1, 0, values.len(), values);
        tree
    }
    fn pull(&mut self, v: usize) {
        self.total[v] = self.total[2 * v] + self.total[2 * v + 1];
        self.tag[v] = if self.tag[2 * v] == self.tag[2 * v + 1] {
            self.tag[2 * v]
        } else {
            0
        };
    }
    fn build(&mut self, v: usize, a: usize, b: usize, values: &[u32]) {
        if b - a == 1 {
            self.total[v] = values[a];
            self.tag[v] = (values[a] + 1) as u8;
            return;
        }
        let mid = (a + b) / 2;
        self.build(2 * v, a, mid, values);
        self.build(2 * v + 1, mid, b, values);
        self.pull(v);
    }
    fn replace(
        &mut self,
        v: usize,
        a: usize,
        b: usize,
        left: usize,
        right: usize,
        value: Option<u32>,
        values: &[u32],
    ) {
        if (value.is_some() && left <= a && b <= right) || b - a == 1 {
            let chosen = value.unwrap_or_else(|| values[a - left]);
            self.total[v] = (b - a) as u32 * chosen;
            self.tag[v] = (chosen + 1) as u8;
            return;
        }
        let mid = (a + b) / 2;
        let old = self.tag[v];
        if old != 0 {
            self.total[2 * v] = (mid - a) as u32 * (old - 1) as u32;
            self.total[2 * v + 1] = (b - mid) as u32 * (old - 1) as u32;
            self.tag[2 * v] = old;
            self.tag[2 * v + 1] = old;
            self.tag[v] = 0;
        }
        if left < mid {
            self.replace(2 * v, a, mid, left, right, value, values);
        }
        if mid < right {
            self.replace(2 * v + 1, mid, b, left, right, value, values);
        }
        self.pull(v);
    }
    fn query(&self, v: usize, a: usize, b: usize, left: usize, right: usize) -> u32 {
        if left <= a && b <= right {
            return self.total[v];
        }
        if self.tag[v] != 0 {
            return (self.tag[v] - 1) as u32 * (b.min(right) - a.max(left)) as u32;
        }
        let mid = (a + b) / 2;
        let mut answer = 0;
        if left < mid {
            answer += self.query(2 * v, a, mid, left, right);
        }
        if mid < right {
            answer += self.query(2 * v + 1, mid, b, left, right);
        }
        answer
    }
}

struct Solver {
    n: usize,
    k: usize,
    odd_cap: usize,
    even_cap: usize,
    characters: Characters,
    counts: Counts,
}
impl Solver {
    fn new(text: &[u8], k: usize) -> Self {
        let (odd, even) = radii(text, (k + 1) / 2, k / 2);
        let values: Vec<u32> = odd.iter().zip(even).map(|(a, b)| (a + b) as u32).collect();
        Self {
            n: text.len(),
            k,
            odd_cap: (k + 1) / 2,
            even_cap: k / 2,
            characters: Characters::new(text),
            counts: Counts::new(&values),
        }
    }
    fn repair(&mut self, left: usize, right: usize) {
        if left >= right {
            return;
        }
        let start = left.saturating_sub(self.even_cap);
        let end = (right - 1 + self.odd_cap).min(self.n);
        let (odd, even) = radii(
            &self.characters.extract(start, end),
            self.odd_cap,
            self.even_cap,
        );
        let values: Vec<u32> = (left..right)
            .map(|i| (odd[i - start] + even[i - start]) as u32)
            .collect();
        self.counts
            .replace(1, 0, self.n, left, right, None, &values);
    }
    fn assign(&mut self, left: usize, right: usize, c: u8) {
        self.characters.assign(1, 0, self.n, left, right + 1, c);
        let a = left.saturating_sub(self.odd_cap - 1);
        let b = (right + self.even_cap + 1).min(self.n);
        let x = left + self.even_cap;
        let end = (right + 2).saturating_sub(self.odd_cap);
        if x < end {
            self.counts
                .replace(1, 0, self.n, x, end, Some(self.k as u32), &[]);
            self.repair(a, x);
            self.repair(end, b);
        } else {
            self.repair(a, b);
        }
    }
    fn partial(&self, left: usize, right: usize, first: usize, last: usize) -> u32 {
        let (odd, even) = radii(
            &self.characters.extract(left, right),
            self.odd_cap,
            self.even_cap,
        );
        (first..last).map(|i| (odd[i] + even[i]) as u32).sum()
    }
    fn query(&self, left: usize, right: usize) -> u32 {
        let length = right - left + 1;
        if length < self.k {
            return self.partial(left, right + 1, 0, length);
        }
        let mut answer =
            self.counts
                .query(1, 0, self.n, left + self.even_cap, right + 2 - self.odd_cap);
        if self.even_cap > 0 {
            answer += self.partial(left, left + self.k - 1, 0, self.even_cap);
        }
        if self.odd_cap > 1 {
            answer += self.partial(right + 2 - self.k, right + 1, self.even_cap, self.k - 1);
        }
        answer
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let text = tokens.next().unwrap().as_bytes();
    let k: usize = tokens.next().unwrap().parse().unwrap();
    let mut model = Solver::new(text, k);
    let q: usize = tokens.next().unwrap().parse().unwrap();
    let mut out = String::new();
    for _ in 0..q {
        let kind = tokens.next().unwrap();
        let left = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
        let right = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
        if kind == "1" {
            model.assign(left, right, tokens.next().unwrap().as_bytes()[0]);
        } else {
            writeln!(&mut out, "{}", model.query(left, right)).unwrap();
        }
    }
    print!("{}", out);
}
