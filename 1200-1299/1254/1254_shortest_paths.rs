use std::cmp::Ordering;
use std::collections::{BinaryHeap, HashMap};
use std::io::{self, Read};

const ROOT2: f64 = std::f64::consts::SQRT_2;

// a heap entry: the A* key (walked plus estimated length) and a cell
#[derive(PartialEq)]
struct Entry(f64, usize);

impl Eq for Entry {}

impl Ord for Entry {
    fn cmp(&self, other: &Self) -> Ordering {
        other.0.partial_cmp(&self.0).unwrap()
    }
}

impl PartialOrd for Entry {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let mut num = || words.next().unwrap();
    let (n, m): (usize, usize) = (num().parse().unwrap(), num().parse().unwrap());
    let k: usize = num().parse().unwrap();
    let v: f64 = num().parse().unwrap();
    // cells over a grid with a border of buildings, so no move needs a
    // bounds check
    let w = n + 2;
    let mut free = vec![false; (m + 2) * w];
    for r in 1..=m {
        for (c, ch) in num().bytes().take(n).enumerate() {
            free[r * w + c + 1] = ch == b'.';
        }
    }
    let mut cell = || {
        let x: usize = num().parse().unwrap();
        let y: usize = num().parse().unwrap();
        y * w + x
    };
    let mut at = cell();
    free[at] = true; // John stands there, whatever the map shows
                     // a step along a side costs 1, along a diagonal sqrt 2, and a diagonal
                     // may pass a building's corner
    let iw = w as isize;
    let steps = [1, -1, iw, -iw, iw + 1, iw - 1, -iw + 1, -iw - 1];
    let costs = [1.0, 1.0, 1.0, 1.0, ROOT2, ROOT2, ROOT2, ROOT2];
    // parts of the town joined by moves, so an unreachable bomb costs nothing
    let mut part = vec![0usize; free.len()];
    for c in 0..free.len() {
        if !free[c] || part[c] != 0 {
            continue;
        }
        part[c] = c + 1;
        let mut stack = vec![c];
        while let Some(a) = stack.pop() {
            for &s in &steps {
                let b = (a as isize + s) as usize;
                if free[b] && part[b] == 0 {
                    part[b] = c + 1;
                    stack.push(b);
                }
            }
        }
    }
    let mut dist = vec![0.0f64; free.len()];
    // shortest walk by A*, with the octile distance as an estimate that
    // never exceeds the true length
    let mut walk = |from: usize, to: usize| -> f64 {
        let guess = |c: usize| {
            let (dy, dx) = ((c / w).abs_diff(to / w), (c % w).abs_diff(to % w));
            dx.max(dy) as f64 + (ROOT2 - 1.0) * dx.min(dy) as f64
        };
        dist.iter_mut().for_each(|d| *d = f64::INFINITY);
        dist[from] = 0.0;
        let mut q = BinaryHeap::new();
        q.push(Entry(guess(from), from));
        loop {
            let Entry(key, c) = q.pop().unwrap();
            if c == to {
                return dist[to];
            }
            if key > dist[c] + guess(c) {
                continue;
            }
            for i in 0..steps.len() {
                let b = (c as isize + steps[i]) as usize;
                let d = dist[c] + costs[i];
                if free[b] && d < dist[b] {
                    dist[b] = d;
                    q.push(Entry(d + guess(b), b));
                }
            }
        }
    };
    let mut known: HashMap<(usize, usize), f64> = HashMap::new();
    let mut total = 0.0;
    for _ in 0..k {
        let target = cell();
        // an unreachable bomb is skipped and John stays where he is
        if part[target] != part[at] {
            continue;
        }
        let d = match known.get(&(at, target)) {
            Some(&d) => d,
            None => walk(at, target),
        };
        known.insert((at, target), d);
        known.insert((target, at), d);
        total += d;
        at = target;
    }
    println!("{:.2}", total / v);
}
