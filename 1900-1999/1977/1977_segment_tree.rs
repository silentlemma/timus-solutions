use std::io::{self, Read, Write};

const HALF: f64 = 0.5;
const BOUNDARIES_PER_EVENT: usize = 3;
const OUTPUT_PRECISION: usize = 17;

struct Event {
    time: i32,
    first: i32,
    second: i32,
    enforce: bool,
}
struct EnergyTree {
    xs: Vec<i32>,
    total: Vec<f64>,
    low: Vec<f64>,
    high: Vec<f64>,
    cleared: Vec<bool>,
}
impl EnergyTree {
    fn new(xs: Vec<i32>) -> Self {
        let nodes = 2 * (xs.len() - 1) - 1;
        Self {
            xs,
            total: vec![0.0; nodes],
            low: vec![0.0; nodes],
            high: vec![0.0; nodes],
            cleared: vec![false; nodes],
        }
    }
    fn apply(&mut self, node: usize, length: i32, first: f64, last: f64) {
        self.total[node] += (first + last) * HALF * f64::from(length);
        self.low[node] += first;
        self.high[node] += last;
    }
    fn push(&mut self, node: usize, left: usize, middle: usize, right: usize) {
        let child = node + 1;
        let other = node + 2 * (middle - left);
        if self.cleared[node] {
            self.total[child] = 0.0;
            self.low[child] = 0.0;
            self.high[child] = 0.0;
            self.total[other] = 0.0;
            self.low[other] = 0.0;
            self.high[other] = 0.0;
            self.cleared[child] = true;
            self.cleared[other] = true;
            self.cleared[node] = false;
        }
        let first = self.low[node];
        let last = self.high[node];
        if first == 0.0 && last == 0.0 {
            return;
        }
        let length = self.xs[right] - self.xs[left];
        let a = self.xs[middle] - self.xs[left];
        let b = length - a;
        if first == last {
            self.apply(child, a, first, first);
            self.apply(other, b, first, first);
        } else {
            let denominator = f64::from(length - 1);
            let left_last = (first * f64::from(b) + last * f64::from(a - 1)) / denominator;
            let right_first = (first * f64::from(b - 1) + last * f64::from(a)) / denominator;
            self.apply(child, a, first, left_last);
            self.apply(other, b, right_first, last);
        }
        self.low[node] = 0.0;
        self.high[node] = 0.0;
    }
    fn add(
        &mut self,
        node: usize,
        left: usize,
        right: usize,
        begin: usize,
        end: usize,
        origin: i32,
        direction: i32,
        scale: f64,
    ) {
        if begin <= left && right <= end {
            let first = scale * f64::from(origin + direction * self.xs[left]);
            let last = scale * f64::from(origin + direction * (self.xs[right] - 1));
            self.apply(node, self.xs[right] - self.xs[left], first, last);
            return;
        }
        let middle = (left + right) / 2;
        self.push(node, left, middle, right);
        if begin < middle {
            self.add(node + 1, left, middle, begin, end, origin, direction, scale);
        }
        let other = node + 2 * (middle - left);
        if end > middle {
            self.add(other, middle, right, begin, end, origin, direction, scale);
        }
        self.total[node] = self.total[node + 1] + self.total[other];
    }
    fn take(&mut self, node: usize, left: usize, right: usize, begin: usize, end: usize) -> f64 {
        if begin <= left && right <= end {
            let answer = self.total[node];
            self.total[node] = 0.0;
            self.low[node] = 0.0;
            self.high[node] = 0.0;
            self.cleared[node] = true;
            return answer;
        }
        let middle = (left + right) / 2;
        self.push(node, left, middle, right);
        let mut answer = 0.0;
        if begin < middle {
            answer += self.take(node + 1, left, middle, begin, end);
        }
        let other = node + 2 * (middle - left);
        if end > middle {
            answer += self.take(other, middle, right, begin, end);
        }
        self.total[node] = self.total[node + 1] + self.total[other];
        answer
    }
}
fn number(input: &mut std::str::SplitWhitespace<'_>) -> i32 {
    input.next().unwrap().parse().unwrap()
}
fn solve(input: &mut std::str::SplitWhitespace<'_>, out: &mut impl Write) {
    let length = number(input);
    let rate = number(input);
    let count = number(input) as usize;
    let mut events = Vec::with_capacity(count);
    let mut xs = Vec::with_capacity(BOUNDARIES_PER_EVENT * count + 2);
    xs.extend([1, length + 1]);
    for _ in 0..count {
        let time = number(input);
        let enforce = input.next().unwrap() == "enforce";
        let first = number(input);
        let second = number(input);
        events.push(Event {
            time,
            first,
            second,
            enforce,
        });
        if enforce {
            xs.extend([first - second + 1, first + 1, first + second]);
        } else {
            xs.extend([first, second + 1]);
        }
    }
    xs.sort_unstable();
    xs.dedup();
    let leaves = xs.len() - 1;
    let mut tree = EnergyTree::new(xs);
    let mut previous = 0;
    let mut reserve = 0.0;
    for e in events {
        let growth = f64::from(rate) * f64::from(e.time - previous);
        if growth != 0.0 {
            tree.apply(0, length, growth, growth);
        }
        previous = e.time;
        if e.enforce {
            if reserve == 0.0 {
                continue;
            }
            let begin = e.first - e.second + 1;
            let middle = e.first + 1;
            let end = e.first + e.second;
            let a = tree.xs.binary_search(&begin).unwrap();
            let b = tree.xs.binary_search(&middle).unwrap();
            let c = tree.xs.binary_search(&end).unwrap();
            let scale = reserve / (f64::from(e.second) * f64::from(e.second));
            tree.add(0, 0, leaves, a, b, 1 - begin, 1, scale);
            if b < c {
                tree.add(0, 0, leaves, b, c, end, -1, scale);
            }
            reserve = 0.0;
        } else {
            let a = tree.xs.binary_search(&e.first).unwrap();
            let b = tree.xs.binary_search(&(e.second + 1)).unwrap();
            reserve += tree.take(0, 0, leaves, a, b);
            writeln!(out, "{:.precision$}", reserve, precision = OUTPUT_PRECISION).unwrap();
        }
    }
}
fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut input = text.split_whitespace();
    let stdout = io::stdout();
    let mut out = io::BufWriter::new(stdout.lock());
    solve(&mut input, &mut out);
}
