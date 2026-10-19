use std::io::{self, Read};

struct Search<'a> {
    n: i64,
    start: Vec<i64>,
    rest: &'a [i64],
    shallowest: i64,
    deepest: i64,
}

impl Search<'_> {
    // a signing of the second half with this total and these lowest and
    // highest running sums fits after depth x exactly when
    // -low <= x <= n - high, and it ends at x + total
    fn walk(&mut self, i: usize, total: i64, low: i64, high: i64) {
        if i == self.rest.len() {
            let first = self.start.partition_point(|&x| x < -low);
            if first == self.start.len() || self.start[first] > self.n - high {
                return;
            }
            self.shallowest = self.shallowest.min(self.start[first] + total);
            let last = self.start.partition_point(|&x| x <= self.n - high) - 1;
            self.deepest = self.deepest.max(self.start[last] + total);
            return;
        }
        for u in [total + self.rest[i], total - self.rest[i]] {
            let (a, b) = (low.min(u), high.max(u));
            if b - a <= self.n {
                self.walk(i + 1, u, a, b);
            }
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|v| v.parse::<i64>().unwrap());
    let (n, s, k) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap() as usize);
    let data: Vec<i64> = it.take(k).collect();
    let moves = &data[..];
    let half = k / 2;
    // the depths the first half of the moves can reach without leaving
    // [0, n]; equal depths are kept once
    let mut start = vec![s];
    for &d in &moves[..half] {
        let mut next: Vec<i64> = Vec::with_capacity(2 * start.len());
        for &p in &start {
            if p + d <= n {
                next.push(p + d);
            }
            if p - d >= 0 {
                next.push(p - d);
            }
        }
        next.sort_unstable();
        next.dedup();
        start = next;
    }
    let mut search = Search { n, start, rest: &moves[half..], shallowest: n + 1, deepest: -1 };
    search.walk(0, 0, 0, 0);
    println!("{} {}", search.shallowest, search.deepest);
}
