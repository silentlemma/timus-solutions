use std::collections::HashSet;
use std::io::{self, Read};

const CORNERS: usize = 3;

type P = (i64, i64);

fn cross(o: P, a: P, b: P) -> i64 {
    (a.0 - o.0) * (b.1 - o.1) - (a.1 - o.1) * (b.0 - o.0)
}

fn dot(n: P, p: P) -> i64 {
    n.0 * p.0 + n.1 * p.1
}

// convex hull, counterclockwise, without points on the edges
fn hull(mut pts: Vec<P>) -> Vec<P> {
    pts.sort();
    let mut h: Vec<P> = Vec::new();
    for &p in &pts {
        while h.len() >= 2 && cross(h[h.len() - 2], h[h.len() - 1], p) <= 0 {
            h.pop();
        }
        h.push(p);
    }
    let t = h.len() + 1;
    for &p in pts.iter().rev().skip(1) {
        while h.len() >= t && cross(h[h.len() - 2], h[h.len() - 1], p) <= 0 {
            h.pop();
        }
        h.push(p);
    }
    h.pop();
    h
}

// an open convex polygon: the places where the tanker hits a ship
struct Polygon {
    v: Vec<P>,
    bx: (i64, i64, i64, i64),
    axes: Vec<(P, i64, i64)>,
}

impl Polygon {
    fn new(v: Vec<P>) -> Polygon {
        let xs = v.iter().map(|p| p.0);
        let ys = v.iter().map(|p| p.1);
        let bx = (
            xs.clone().min().unwrap(),
            xs.max().unwrap(),
            ys.clone().min().unwrap(),
            ys.max().unwrap(),
        );
        let mut g = Polygon {
            v,
            bx,
            axes: Vec::new(),
        };
        for i in 0..g.v.len() {
            let (a, b) = (g.v[i], g.v[(i + 1) % g.v.len()]);
            let n = (b.1 - a.1, a.0 - b.0);
            let (lo, hi) = g.project(n);
            g.axes.push((n, lo, hi));
        }
        g
    }

    fn project(&self, n: P) -> (i64, i64) {
        let d = self.v.iter().map(|&p| dot(n, p));
        (d.clone().min().unwrap(), d.max().unwrap())
    }

    // whether p is strictly inside
    fn holds(&self, p: P) -> bool {
        (0..self.v.len()).all(|i| cross(self.v[i], self.v[(i + 1) % self.v.len()], p) > 0)
    }

    // whether the segment pq crosses the inside: no axis separates them,
    // neither an edge normal nor the normal of pq itself
    fn blocks(&self, p: P, q: P) -> bool {
        let (x0, x1, y0, y1) = self.bx;
        if p.0.max(q.0) <= x0 || p.0.min(q.0) >= x1 || p.1.max(q.1) <= y0 || p.1.min(q.1) >= y1 {
            return false;
        }
        for &(n, lo, hi) in &self.axes {
            let (a, b) = (dot(n, p), dot(n, q));
            if a.max(b) <= lo || a.min(b) >= hi {
                return false;
            }
        }
        let n = (q.1 - p.1, p.0 - q.0);
        let c = dot(n, p);
        let (lo, hi) = self.project(n);
        lo < c && c < hi
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let nums: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let mut it = nums.into_iter();
    let mut next = || it.next().unwrap();
    let (dx, dy) = (next(), next());
    let tanker: Vec<P> = (0..CORNERS).map(|_| (next(), next())).collect();
    let goal = (next(), next());
    let n = next() as usize;
    let ships: Vec<Vec<P>> = (0..n)
        .map(|_| (0..CORNERS).map(|_| (next(), next())).collect())
        .collect();
    // the tanker is placed by its first corner; offsets of all corners
    let start = tanker[0];
    let offsets: Vec<P> = tanker
        .iter()
        .map(|t| (t.0 - start.0, t.1 - start.1))
        .collect();
    let xlo = -offsets.iter().map(|o| o.0).min().unwrap();
    let xhi = dx - offsets.iter().map(|o| o.0).max().unwrap();
    let ylo = -offsets.iter().map(|o| o.1).min().unwrap();
    let yhi = dy - offsets.iter().map(|o| o.1).max().unwrap();
    let polygons: Vec<Polygon> = ships
        .iter()
        .map(|ship| {
            let sums = ship
                .iter()
                .flat_map(|s| offsets.iter().map(move |o| (s.0 - o.0, s.1 - o.1)));
            Polygon::new(hull(sums.collect()))
        })
        .collect();
    let free = |p: P| {
        xlo <= p.0 && p.0 <= xhi && ylo <= p.1 && p.1 <= yhi && !polygons.iter().any(|g| g.holds(p))
    };
    if !free(goal) {
        println!("-1");
        return;
    }
    if goal == start {
        println!("0.000");
        return;
    }
    // shortest paths bend only at corners of the forbidden polygons
    let mut points = vec![start, goal];
    let mut seen = HashSet::new();
    for g in &polygons {
        for &v in &g.v {
            if free(v) && seen.insert(v) {
                points.push(v);
            }
        }
    }
    let m = points.len();
    let mut dist = vec![f64::INFINITY; m];
    let mut done = vec![false; m];
    dist[0] = 0.0;
    loop {
        let i = match (0..m)
            .filter(|&j| !done[j] && dist[j].is_finite())
            .min_by(|&a, &b| dist[a].partial_cmp(&dist[b]).unwrap())
        {
            Some(i) if i != 1 => i,
            _ => break,
        };
        done[i] = true;
        let p = points[i];
        for j in 0..m {
            let q = points[j];
            if done[j] || q == p {
                continue;
            }
            let nd = dist[i] + ((q.0 - p.0) as f64).hypot((q.1 - p.1) as f64);
            if nd < dist[j] && !polygons.iter().any(|g| g.blocks(p, q)) {
                dist[j] = nd;
            }
        }
    }
    if dist[1].is_finite() {
        println!("{:.3}", dist[1]);
    } else {
        println!("-1");
    }
}
