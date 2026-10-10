use std::io::{self, Read, Write};

const SAFE: f64 = 0.1;
const INF: f64 = 1e300;
const SAME: f64 = 1e-9;

type Pt = (f64, f64);

// A place on a boundary: edge index and position along that edge.
type Pos = (usize, f64);

struct Polygon {
    v: Vec<Pt>, // corners
    d: Vec<Pt>, // the edge vectors leaving them
    cx: f64,
    cy: f64,
    r: f64,
}

// The nearest point of the edges to p if closer than best; updates best
// (squared distance) and where.
fn point_edges(p: Pt, poly: &Polygon, best: &mut f64, place: &mut Pos) -> bool {
    let mut found = false;
    for i in 0..poly.v.len() {
        let (wx, wy) = (p.0 - poly.v[i].0, p.1 - poly.v[i].1);
        let (dx, dy) = poly.d[i];
        let d2 = dx * dx + dy * dy;
        let t = wx * dx + wy * dy;
        let (q, t) = if t <= 0.0 {
            (wx * wx + wy * wy, 0.0)
        } else if t >= d2 {
            ((wx - dx) * (wx - dx) + (wy - dy) * (wy - dy), 1.0)
        } else {
            let c = wx * dy - wy * dx;
            (c * c / d2, t / d2)
        };
        if q < *best {
            *best = q;
            *place = (i, t);
            found = true;
        }
    }
    found
}

// Squared distance between two polygons and where it is reached on each.
fn poly_poly(a: &Polygon, b: &Polygon) -> (f64, Pos, Pos) {
    let mut best = INF;
    let (mut on_a, mut on_b) = ((0, 0.0), (0, 0.0));
    for side in 0..2 {
        let (own, other) = if side == 1 { (b, a) } else { (a, b) };
        for (k, &p) in own.v.iter().enumerate() {
            let mut there = (0, 0.0);
            if point_edges(p, other, &mut best, &mut there) {
                let here = (k, 0.0);
                if side == 1 {
                    on_a = there;
                    on_b = here;
                } else {
                    on_a = here;
                    on_b = there;
                }
            }
        }
    }
    (best, on_a, on_b)
}

fn at(poly: &Polygon, p: Pos) -> Pt {
    (
        poly.v[p.0].0 + poly.d[p.0].0 * p.1,
        poly.v[p.0].1 + poly.d[p.0].1 * p.1,
    )
}

// Corners passed going along the boundary from src to dst, in the
// direction with fewer of them.
fn walk(poly: &Polygon, src: Pos, dst: Pos, path: &mut Vec<Pt>) {
    let k = poly.v.len();
    let mut fwd = (dst.0 + k - src.0) % k;
    let mut back = (src.0 + k - dst.0) % k;
    if fwd == 0 && dst.1 < src.1 {
        fwd = k;
    }
    if back == 0 && dst.1 > src.1 {
        back = k;
    }
    if fwd <= back {
        for s in 0..fwd {
            path.push(poly.v[(src.0 + 1 + s) % k]);
        }
    } else {
        for s in 0..back {
            path.push(poly.v[(src.0 + k - s) % k]);
        }
    }
}

fn toward(f: Pt, p: Pt, len: f64) -> Pt {
    let d = (p.0 - f.0).hypot(p.1 - f.1);
    (f.0 + (p.0 - f.0) * len / d, f.1 + (p.1 - f.1) * len / d)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let mut num = || it.next().unwrap().parse::<f64>().unwrap();
    let mouse = (num(), num());
    let cheese = (num(), num());
    let n = num() as usize;
    let mut polys = Vec::new();
    for _ in 0..n {
        let k = num() as usize;
        let mut v: Vec<Pt> = (0..k).map(|_| (num(), num())).collect();
        let cx = v.iter().map(|p| p.0 / k as f64).sum::<f64>();
        let cy = v.iter().map(|p| p.1 / k as f64).sum::<f64>();
        // the corners may come in any order, so sort them around the centre
        v.sort_by(|p, q| {
            let ap = (p.1 - cy).atan2(p.0 - cx);
            let aq = (q.1 - cy).atan2(q.0 - cx);
            ap.partial_cmp(&aq).unwrap()
        });
        let d = (0..k)
            .map(|j| (v[(j + 1) % k].0 - v[j].0, v[(j + 1) % k].1 - v[j].1))
            .collect();
        let r = v
            .iter()
            .map(|p| (p.0 - cx).hypot(p.1 - cy))
            .fold(0.0, f64::max);
        polys.push(Polygon { v, d, cx, cy, r });
    }

    // nodes 0..n-1 are the safe zones around the furniture, n the mouse and
    // n + 1 the cheese; an edge costs the dangerous length between them
    let to_point = |p: Pt, poly: &Polygon| {
        let mut best = INF;
        point_edges(p, poly, &mut best, &mut (0, 0.0));
        (best.sqrt() - SAFE).max(0.0)
    };
    let (start, goal) = (n, n + 1);
    let mut dist = vec![INF; n + 2];
    let mut parent = vec![0; n + 2];
    let mut done = vec![false; n + 2];
    dist[start] = 0.0;
    loop {
        let mut u = usize::MAX;
        for v in 0..n + 2 {
            if !done[v] && (u == usize::MAX || dist[v] < dist[u]) {
                u = v;
            }
        }
        if u == goal {
            break;
        }
        done[u] = true;
        for v in 0..n + 2 {
            if done[v] {
                continue;
            }
            let w = if v == goal && u == start {
                (mouse.0 - cheese.0).hypot(mouse.1 - cheese.1)
            } else if v == goal {
                to_point(cheese, &polys[u])
            } else if u == start {
                to_point(mouse, &polys[v])
            } else {
                let (a, b) = (&polys[u], &polys[v]);
                let gap = (a.cx - b.cx).hypot(a.cy - b.cy) - a.r - b.r - 2.0 * SAFE;
                if dist[u] + gap >= dist[v] {
                    continue;
                }
                poly_poly(a, b).0.sqrt() - 2.0 * SAFE
            };
            if dist[u] + w < dist[v] {
                dist[v] = dist[u] + w;
                parent[v] = u;
            }
        }
    }
    let mut route = vec![goal];
    while *route.last().unwrap() != start {
        route.push(parent[*route.last().unwrap()]);
    }
    route.reverse();

    let mut path = vec![mouse];
    if route.len() == 2 {
        path.push(cheese);
    } else {
        // step from the mouse onto the nearest point of the first piece
        let first = &polys[route[1]];
        let mut q = INF;
        let mut here = (0, 0.0);
        point_edges(mouse, first, &mut q, &mut here);
        let foot = at(first, here);
        if q.sqrt() > SAFE {
            path.push(toward(foot, mouse, SAFE));
        }
        path.push(foot);
        for i in 1..route.len() - 2 {
            let (a, b) = (&polys[route[i]], &polys[route[i + 1]]);
            let (_, out_pos, in_pos) = poly_poly(a, b);
            let (fa, fb) = (at(a, out_pos), at(b, in_pos));
            walk(a, here, out_pos, &mut path);
            path.extend([fa, toward(fa, fb, SAFE), toward(fb, fa, SAFE), fb]);
            here = in_pos;
        }
        let last = &polys[route[route.len() - 2]];
        let mut q = INF;
        let mut end = (0, 0.0);
        point_edges(cheese, last, &mut q, &mut end);
        let foot = at(last, end);
        walk(last, here, end, &mut path);
        path.push(foot);
        if q.sqrt() > SAFE {
            path.push(toward(foot, cheese, SAFE));
        }
        path.push(cheese);
    }

    let mut out = vec![path[0]];
    for &p in &path[1..] {
        let prev = *out.last().unwrap();
        if (p.0 - prev.0).hypot(p.1 - prev.1) > SAME {
            out.push(p);
        }
    }
    if out.len() == 1 {
        out.push(*path.last().unwrap());
    }
    let mut s = format!("{}\n", out.len());
    for p in &out {
        s += &format!("{:.9} {:.9}\n", p.0, p.1);
    }
    io::stdout().write_all(s.as_bytes()).unwrap();
}
