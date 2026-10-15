use std::fmt::Write as _;
use std::io::{self, Read};

const LIMIT: f64 = 1e6;
const TIGHT: f64 = 1e-7; // a smaller slack counts as an equality

#[derive(Clone, Copy)]
struct Laser {
    x: i64,
    y: i64,
    u: i64,
    v: i64,
    w: i64,
}

fn bounds(z: &[f64]) -> (f64, f64) {
    z.iter().fold((f64::MAX, f64::MIN), |(lo, hi), &h| (lo.min(h), hi.max(h)))
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut nums = text.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let n = nums.next().unwrap() as usize;
    let mut lasers = Vec::with_capacity(n);
    for _ in 0..n {
        let mut next = || nums.next().unwrap();
        let (x, y, u, v, w) = (next(), next(), next(), next(), next());
        lasers.push(Laser { x, y, u, v, w });
    }
    let m = nums.next().unwrap() as usize;
    // z[hi] - z[lo] must exceed lift: the gap of the beams where they cross
    let mut edges = Vec::with_capacity(m);
    let mut out = vec![Vec::new(); n];
    for k in 0..m {
        let a = nums.next().unwrap() as usize - 1;
        let b = nums.next().unwrap() as usize - 1;
        let (la, lb) = (lasers[a], lasers[b]);
        let det = la.u * lb.v - la.v * lb.u;
        let (dx, dy) = (lb.x - la.x, lb.y - la.y);
        let top = lb.w * (la.v * dx - la.u * dy) - la.w * (dx * lb.v - dy * lb.u);
        edges.push((b, a, top as f64 / det as f64));
        out[b].push(k);
    }
    // longest paths from an imaginary source tied to every laser by 0.
    // Only lasers raised in the last round can raise others.
    let mut z = vec![0.0f64; n];
    let mut active: Vec<usize> = (0..n).collect();
    let mut mark = vec![false; n];
    for _ in 0..n {
        if active.is_empty() {
            break;
        }
        let mut raised = Vec::new();
        for &lo in &active {
            for &k in &out[lo] {
                let (_, hi, lift) = edges[k];
                if z[lo] + lift > z[hi] {
                    z[hi] = z[lo] + lift;
                    if !mark[hi] {
                        mark[hi] = true;
                        raised.push(hi);
                    }
                }
            }
        }
        for &h in &raised {
            mark[h] = false;
        }
        active = raised;
    }
    // equalities form an acyclic graph; a step per level of it makes them
    // strict, small enough to keep the other constraints and the bounds
    let mut tight = vec![Vec::new(); n];
    let mut indegree = vec![0; n];
    let mut slack_min: Option<f64> = None;
    for &(lo, hi, lift) in &edges {
        let slack = z[hi] - z[lo] - lift;
        if slack < TIGHT {
            tight[lo].push(hi);
            indegree[hi] += 1;
        } else if slack_min.map_or(true, |s| slack < s) {
            slack_min = Some(slack);
        }
    }
    let mut level = vec![0usize; n];
    let mut queue: Vec<usize> = (0..n).filter(|&i| indegree[i] == 0).collect();
    let mut head = 0;
    while head < queue.len() {
        let at = queue[head];
        head += 1;
        for &to in &tight[at] {
            level[to] = level[to].max(level[at] + 1);
            indegree[to] -= 1;
            if indegree[to] == 0 {
                queue.push(to);
            }
        }
    }
    let levels = *level.iter().max().unwrap();
    let mut step = 0.0;
    if levels > 0 {
        let (lo, hi) = bounds(&z);
        let mut room = 2.0 * LIMIT - (hi - lo);
        if let Some(s) = slack_min {
            room = room.min(s);
        }
        step = room / (2 * levels + 2) as f64;
    }
    for i in 0..n {
        z[i] += step * level[i] as f64;
    }
    let (lo, hi) = bounds(&z);
    let middle = (lo + hi) / 2.0;
    let mut text = String::new();
    for h in z {
        writeln!(text, "{:.10}", h - middle).unwrap();
    }
    print!("{}", text);
}
