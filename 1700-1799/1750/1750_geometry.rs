use std::fmt::Write as _;
use std::io::{self, Read};

type P = (i64, i64);

// the coordinates of S, T, A, B and C
const FIELDS: usize = 10;
// a turn: the point before, the corner, the point after
const TURN: usize = 3;

fn cross(o: P, a: P, b: P) -> i64 {
    (a.0 - o.0) * (b.1 - o.1) - (a.1 - o.1) * (b.0 - o.0)
}
fn vec(a: P, b: P) -> P {
    (b.0 - a.0, b.1 - a.1)
}
fn turn(u: P, w: P) -> i64 {
    u.0 * w.1 - u.1 * w.0
}
fn dot(u: P, w: P) -> i64 {
    u.0 * w.0 + u.1 * w.1
}

// whether the ray w lies in the closed sector turning left from u to v
fn within(u: P, v: P, w: P) -> bool {
    let c = turn(u, v);
    if c > 0 {
        turn(u, w) >= 0 && turn(w, v) >= 0
    } else if c < 0 {
        !(turn(v, w) > 0 && turn(w, u) > 0)
    } else {
        turn(u, w) >= 0
    }
}

// rays from the bend b towards x and y stay on one side of the ravine
fn same_side_at_bend(a: P, b: P, c: P, x: P, y: P) -> bool {
    let (u, v, p, q) = (vec(b, a), vec(b, c), vec(b, x), vec(b, y));
    if turn(u, v) == 0 && dot(u, v) > 0 {
        return true; // b is a free tip
    }
    (within(u, v, p) && within(u, v, q)) || (within(v, u, p) && within(v, u, q))
}

fn strictly_inside(p: P, a: P, b: P) -> bool {
    cross(a, b, p) == 0 && dot(vec(p, a), vec(p, b)) < 0
}

fn crosses(p: P, q: P, a: P, b: P) -> bool {
    cross(p, q, a) * cross(p, q, b) < 0 && cross(a, b, p) * cross(a, b, q) < 0
}

fn allowed(path: &[P], a: P, b: P, c: P) -> bool {
    for w in path.windows(2) {
        let (p, q) = (w[0], w[1]);
        if crosses(p, q, a, b) || crosses(p, q, b, c) {
            return false;
        }
        // going straight through the bend must not change sides there
        if strictly_inside(b, p, q) && !same_side_at_bend(a, b, c, p, q) {
            return false;
        }
    }
    for w in path.windows(TURN) {
        let (x, v, y) = (w[0], w[1], w[w.len() - 1]);
        if v == b && !same_side_at_bend(a, b, c, x, y) {
            return false;
        }
        // an end of the ravine lying inside the other piece is no corner
        if v == a && strictly_inside(a, b, c) && cross(b, c, x) * cross(b, c, y) < 0 {
            return false;
        }
        if v == c && strictly_inside(c, a, b) && cross(a, b, x) * cross(a, b, y) < 0 {
            return false;
        }
    }
    true
}

// every order of every subset of the corners
fn orders(left: &[usize], chosen: &mut Vec<usize>, out: &mut Vec<Vec<usize>>) {
    out.push(chosen.clone());
    for i in 0..left.len() {
        let mut rest = left.to_vec();
        let k = rest.remove(i);
        chosen.push(k);
        orders(&rest, chosen, out);
        chosen.pop();
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let mut routes = Vec::new();
    orders(&[0, 1, 2], &mut Vec::new(), &mut routes);
    let mut out = String::new();
    for test in v[1..].chunks(FIELDS).take(v[0] as usize) {
        let mut pts = test.chunks(2).map(|c| (c[0], c[1]));
        let mut next = || pts.next().unwrap();
        let (s, e, a, b, c) = (next(), next(), next(), next(), next());
        let corner = [a, b, c];
        // a shortest way bends only at points of the ravine, at most once at
        // each of A, B and C; the shortest allowed candidate is the answer
        let mut best = f64::INFINITY;
        for route in &routes {
            let mut path = vec![s];
            path.extend(route.iter().map(|&k| corner[k]));
            path.push(e);
            let size: f64 = path
                .windows(2)
                .map(|w| ((w[1].0 - w[0].0) as f64).hypot((w[1].1 - w[0].1) as f64))
                .sum();
            if size < best && allowed(&path, a, b, c) {
                best = size;
            }
        }
        writeln!(out, "{:.6}", best).unwrap();
    }
    print!("{}", out);
}
