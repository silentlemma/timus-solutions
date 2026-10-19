use std::cmp::Ordering;
use std::collections::{BTreeSet, HashMap};
use std::io::{self, Read};
use std::ops::Bound::{Included, Unbounded};

// an edge from its left end to its right end, or a fly when both ends meet
#[derive(Clone, Copy)]
struct Item {
    lx: i64,
    ly: i64,
    rx: i64,
    ry: i64,
    polygon: usize,
    top: bool, // the inside lies below the edge
}

impl Item {
    fn point(&self) -> bool {
        self.lx == self.rx
    }
}

// where s lies against t, both crossing the sweep line just right of its
// position: below, above, or equal for the same edge or a fly on it. The
// comparison uses the end of one that lies over the other.
fn side(s: &Item, t: &Item) -> Ordering {
    if t.point() || (!s.point() && s.lx < t.lx) {
        return side(t, s).reverse();
    }
    let (tx, ty) = (t.rx - t.lx, t.ry - t.ly);
    let mut c = tx * (s.ly - t.ly) - ty * (s.lx - t.lx);
    if c == 0 && !s.point() {
        // two edges of one polygon from a common left end
        c = tx * (s.ry - t.ly) - ty * (s.rx - t.lx);
    }
    c.cmp(&0)
}

impl PartialEq for Item {
    fn eq(&self, other: &Self) -> bool {
        side(self, other) == Ordering::Equal
    }
}

impl Eq for Item {}

impl PartialOrd for Item {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Item {
    fn cmp(&self, other: &Self) -> Ordering {
        side(self, other)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|v| v.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let flies: Vec<(i64, i64)> = (0..n).map(|_| (it.next().unwrap(), it.next().unwrap())).collect();
    let m = it.next().unwrap() as usize;
    let mut corners: HashMap<(i64, i64), usize> = HashMap::new(); // vertex -> polygon
    // x -> (low y, high y, polygon) of vertical edges
    let mut upright: HashMap<i64, Vec<(i64, i64, usize)>> = HashMap::new();
    let mut edges: Vec<Item> = Vec::new();
    for p in 0..m {
        let k = it.next().unwrap() as usize;
        let pts: Vec<(i64, i64)> =
            (0..k).map(|_| (it.next().unwrap(), it.next().unwrap())).collect();
        for i in 0..k {
            let (ax, ay) = pts[(i + k - 1) % k];
            let (bx, by) = pts[i];
            corners.insert((bx, by), p);
            if ax == bx {
                upright.entry(ax).or_default().push((ay.min(by), ay.max(by), p));
                continue;
            }
            // counter-clockwise: the inside is left of the edge, so an edge
            // running right to left has the inside below it
            let top = ax > bx;
            let (lx, ly, rx, ry) = if top { (bx, by, ax, ay) } else { (ax, ay, bx, by) };
            edges.push(Item { lx, ly, rx, ry, polygon: p, top });
        }
    }
    for spans in upright.values_mut() {
        spans.sort_unstable();
    }
    let mut starts: Vec<usize> = (0..edges.len()).collect();
    let mut ends = starts.clone();
    starts.sort_by_key(|&i| edges[i].lx);
    ends.sort_by_key(|&i| edges[i].rx);
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_by_key(|&i| flies[i].0);
    let mut active: BTreeSet<Item> = BTreeSet::new();
    let mut count = vec![0usize; m];
    let e = edges.len();
    let (mut si, mut ei) = (0, 0);
    for &f in &order {
        let (x, y) = flies[f];
        // sweep every event column up to x; in a column, edges ending there
        // leave before edges starting there come in
        loop {
            let mut column = x + 1;
            if si < e {
                column = column.min(edges[starts[si]].lx);
            }
            if ei < e {
                column = column.min(edges[ends[ei]].rx);
            }
            if column > x {
                break;
            }
            while ei < e && edges[ends[ei]].rx == column {
                active.remove(&edges[ends[ei]]);
                ei += 1;
            }
            while si < e && edges[starts[si]].lx == column {
                active.insert(edges[starts[si]]);
                si += 1;
            }
        }
        if let Some(&p) = corners.get(&(x, y)) {
            count[p] += 1;
            continue;
        }
        if let Some(spans) = upright.get(&x) {
            let j = spans.partition_point(|s| s.0 <= y);
            if j > 0 && spans[j - 1].1 >= y {
                count[spans[j - 1].2] += 1;
                continue;
            }
        }
        let fly = Item { lx: x, ly: y, rx: x, ry: y, polygon: 0, top: false };
        if let Some(edge) = active.range((Included(fly), Unbounded)).next() {
            if edge.top || side(&fly, edge) == Ordering::Equal {
                count[edge.polygon] += 1;
            }
        }
    }
    let out: Vec<String> = count.iter().map(|c| c.to_string()).collect();
    println!("{}", out.join("\n"));
}
