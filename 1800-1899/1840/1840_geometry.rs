use std::f64::consts::PI;
use std::io::{self, Read};

const TOP: f64 = 10.0; // the speed limit; both accelerations are limited by 1
const EPS: f64 = 1e-12;

// fastest run over a piece entered at v0 and left at v1: speed up,
// perhaps cruise at the cap, slow down
fn piece_time((length, cap): (f64, f64), v0: f64, v1: f64) -> f64 {
    if length <= EPS {
        return 0.0;
    }
    let (up, down) = ((cap * cap - v0 * v0) / 2.0, (cap * cap - v1 * v1) / 2.0);
    if up + down <= length {
        return (cap - v0) + (cap - v1) + (length - up - down) / cap;
    }
    let peak = (length + (v0 * v0 + v1 * v1) / 2.0).sqrt();
    (peak - v0) + (peak - v1)
}

struct Segment {
    ax: f64,
    ay: f64,
    bx: f64,
    by: f64,
    ux: f64,
    uy: f64,
    length: f64,
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<f64>().unwrap());
    let n = match it.next() {
        Some(v) => v as usize,
        None => return,
    };
    let segs: Vec<Segment> = (0..n)
        .map(|_| {
            let mut next = || it.next().unwrap();
            let (ax, ay, bx, by) = (next(), next(), next(), next());
            let length = (bx - ax).hypot(by - ay);
            Segment { ax, ay, bx, by, ux: (bx - ax) / length, uy: (by - ay) / length, length }
        })
        .collect();
    let mut extra = vec![0.0; n];
    let mut arcs = Vec::new();
    for i in 0..n.saturating_sub(1) {
        let (cur, next) = (&segs[i], &segs[i + 1]);
        let (dx, dy) = (next.ax - cur.bx, next.ay - cur.by);
        let sin = cur.ux * next.uy - cur.uy * next.ux;
        let cos = cur.ux * next.ux + cur.uy * next.uy;
        let (radius, angle);
        if sin.abs() > EPS {
            // the lines meet t past the end of this segment and back before
            // the start of the next one; the arc touches both lines at the
            // same distance from that point, as far as it can
            let t = (dx * next.uy - dy * next.ux) / sin;
            let back = -(dx * cur.uy - dy * cur.ux) / sin;
            let nearest = t.min(back);
            extra[i] += t - nearest;
            extra[i + 1] += back - nearest;
            if nearest.abs() <= EPS {
                arcs.push((0.0, 0.0));
                continue;
            }
            radius = nearest.abs() * (1.0 + cos) / sin.abs();
            let turn = sin.abs().atan2(cos);
            // a meeting point behind forces the long way around the circle
            angle = if nearest > 0.0 { turn } else { 2.0 * PI - turn };
        } else {
            // opposite directions: a half circle across the gap
            let along = dx * cur.ux + dy * cur.uy;
            let across = -dx * cur.uy + dy * cur.ux;
            if along > 0.0 {
                extra[i] += along;
            } else {
                extra[i + 1] -= along;
            }
            radius = across.abs() / 2.0;
            angle = PI;
        }
        arcs.push((radius * angle, TOP.min(radius.sqrt())));
    }
    let mut pieces = Vec::new();
    for i in 0..n {
        pieces.push((segs[i].length + extra[i], TOP));
        if i + 1 < n {
            pieces.push(arcs[i]);
        }
    }
    // the speed where pieces meet: what acceleration from the start and
    // braking before the end allow, within the caps on both sides
    let m = pieces.len();
    let mut reach = vec![0.0f64; m + 1];
    let mut stop = vec![0.0f64; m + 1];
    for i in 0..m {
        reach[i + 1] = pieces[i].1.min((reach[i] * reach[i] + 2.0 * pieces[i].0).sqrt());
    }
    for i in (0..m).rev() {
        stop[i] = pieces[i].1.min((stop[i + 1] * stop[i + 1] + 2.0 * pieces[i].0).sqrt());
    }
    let total: f64 = (0..m)
        .map(|i| piece_time(pieces[i], reach[i].min(stop[i]), reach[i + 1].min(stop[i + 1])))
        .sum();
    println!("{:.10}", total);
}
