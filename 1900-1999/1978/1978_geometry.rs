use std::io::{self, Read, Write};

const INDEX_BITS: usize = 10;
const INDEX_MASK: usize = (1 << INDEX_BITS) - 1;
const OUTPUT_DIGITS: usize = 10;

fn record(best: &mut [i64], k: usize, mut a: i64, mut b: i64, tx: i64, ty: i64) {
    best[k] = best[k].max(a * a + b * b);
    a = tx - a;
    b = ty - b;
    let complement = best.len() - 1 - k;
    best[complement] = best[complement].max(a * a + b * b);
}

fn solve(points: &[(i64, i64)]) -> Vec<i64> {
    let n = points.len();
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_unstable_by_key(|&i| (-points[i].1, points[i].0, i));
    let mut position = vec![0; n];
    let mut px = vec![0; n + 1];
    let mut py = vec![0; n + 1];
    let mut best = vec![0; n + 1];
    for (i, &id) in order.iter().enumerate() {
        position[id] = i;
        px[i + 1] = px[i] + points[id].0;
        py[i + 1] = py[i] + points[id].1;
    }
    let (tx, ty) = (px[n], py[n]);
    for k in 0..=n {
        record(&mut best, k, px[k], py[k], tx, ty);
    }
    let mut events = Vec::with_capacity(n * (n - 1) / 2);
    for i in 0..n {
        for j in 0..i {
            if points[i].1 == points[j].1 {
                continue;
            }
            let high = if points[i].1 > points[j].1 { i } else { j };
            let low = i + j - high;
            events.push((high << INDEX_BITS) | low);
        }
    }
    let compare = |a: usize, b: usize| {
        let (ah, al) = (points[a >> INDEX_BITS], points[a & INDEX_MASK]);
        let (bh, bl) = (points[b >> INDEX_BITS], points[b & INDEX_MASK]);
        ((al.0 - ah.0) * (bh.1 - bl.1)).cmp(&((bl.0 - bh.0) * (ah.1 - al.1)))
    };
    events.sort_unstable_by(|&a, &b| compare(a, b));
    let mut ends = vec![None; n];
    let mut starts = Vec::with_capacity(n);
    let mut intervals: Vec<(usize, usize)> = Vec::with_capacity(n);
    let mut at = 0;
    while at < events.len() {
        let mut after = at + 1;
        while after < events.len() && compare(events[at], events[after]).is_eq() {
            after += 1;
        }
        if after == at + 1 {
            let (a, b) = (
                position[events[at] >> INDEX_BITS],
                position[events[at] & INDEX_MASK],
            );
            let left = a.min(b);
            let (first, second) = (order[left], order[left + 1]);
            order.swap(left, left + 1);
            position[first] = left + 1;
            position[second] = left;
            let k = left + 1;
            px[k] += points[second].0 - points[first].0;
            py[k] += points[second].1 - points[first].1;
            record(&mut best, k, px[k], py[k], tx, ty);
        } else {
            starts.clear();
            intervals.clear();
            for &code in &events[at..after] {
                let (mut a, mut b) = (position[code >> INDEX_BITS], position[code & INDEX_MASK]);
                if a > b {
                    std::mem::swap(&mut a, &mut b);
                }
                if ends[a].is_none() {
                    starts.push(a);
                }
                ends[a] = Some(ends[a].unwrap_or(0).max(b));
            }
            starts.sort_unstable();
            for &left in &starts {
                let right = ends[left].take().unwrap();
                if let Some(last) = intervals.last_mut() {
                    if left <= last.1 {
                        last.1 = last.1.max(right);
                        continue;
                    }
                }
                intervals.push((left, right));
            }
            for &(left, right) in &intervals {
                order[left..=right].reverse();
                let (mut a, mut b) = (px[left], py[left]);
                for i in left..=right {
                    let id = order[i];
                    position[id] = i;
                    a += points[id].0;
                    b += points[id].1;
                    px[i + 1] = a;
                    py[i + 1] = b;
                    if i < right {
                        record(&mut best, i + 1, a, b, tx, ty);
                    }
                }
            }
        }
        at = after;
    }
    best[1..].to_vec()
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut input = text.split_whitespace();
    let n: usize = match input.next() {
        Some(s) => s.parse().unwrap(),
        None => return,
    };
    let points: Vec<(i64, i64)> = (0..n)
        .map(|_| {
            (
                input.next().unwrap().parse().unwrap(),
                input.next().unwrap().parse().unwrap(),
            )
        })
        .collect();
    let mut out = io::BufWriter::new(io::stdout().lock());
    for value in solve(&points) {
        writeln!(
            out,
            "{:.precision$}",
            (value as f64).sqrt(),
            precision = OUTPUT_DIGITS
        )
        .unwrap();
    }
}
