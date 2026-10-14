use std::f64::consts::PI;
use std::io::{self, Read};

const TAU: f64 = 2.0 * PI;
const EPS: f64 = 1e-12; // events closer than this in angle happen together
const PERCENT: i64 = 100;
const HALF: f64 = 0.5;
const MOST_HITS: usize = 5; // an arrow stops after the fifth cow
const ENTER: u8 = 0; // at one angle, rays start touching before they stop
const LEAVE: u8 = 1;

/// The angle in [0, 2 pi); a tiny negative angle may round up to 2 pi.
fn norm(a: f64) -> f64 {
    let a = a.rem_euclid(TAU);
    if a >= TAU {
        0.0
    } else {
        a
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut it = text
        .split_ascii_whitespace()
        .map(|w| w.parse::<f64>().unwrap());
    let mut next_number = || it.next().unwrap();
    let n = next_number() as usize;
    let k = next_number() as usize;
    let p = next_number() as i64;
    let (r, vx, vy) = (next_number(), next_number(), next_number());
    // expected hits of an arrow whose ray meets m cows, kept exact as integers
    // in units of 1 / 100^4: each further cow adds p / 100 of the last addition
    let scale = PERCENT.pow(MOST_HITS as u32 - 1);
    let mut gain = vec![0i64; n + 1];
    let mut term = scale;
    for m in 1..=n {
        gain[m] = gain[m - 1] + if m <= MOST_HITS { term } else { 0 };
        if m < MOST_HITS {
            term = term / PERCENT * p;
        }
    }
    let turn: Vec<f64> = (0..k)
        .map(|i| norm((i as f64 / (k - 1) as f64 - HALF).atan()))
        .collect();
    // the angle a seen by arrow i: the events of one arrow come in this order
    let turned = |a: f64, i: usize| {
        if a >= turn[i] {
            a - turn[i]
        } else {
            a - turn[i] + TAU
        }
    };
    // rays meet a cow at angles within asin(R / d) of its centre, and
    // each arrow sees the same angular intervals turned back by its offset
    let mut base: Vec<(f64, u8)> = Vec::with_capacity(2 * n);
    let mut count = vec![0usize; k];
    for _ in 0..n {
        let (x, y) = (next_number() - vx, next_number() - vy);
        let centre = y.atan2(x);
        let width = (r / x.hypot(y)).min(1.0).asin();
        let (lo, hi) = (norm(centre - width), norm(centre + width));
        base.push((lo, ENTER));
        base.push((hi, LEAVE));
        // the intervals that wrap hold the angle 0 of the arrow
        for i in 0..k {
            if turned(lo, i) > turned(hi, i) {
                count[i] += 1;
            }
        }
    }
    base.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let size = 2 * n;
    // arrow i takes the sorted events from cut[i] on, wrapping around once
    let cut: Vec<usize> = turn
        .iter()
        .map(|&t| base.partition_point(|e| e.0 < t))
        .collect();
    let mut used = vec![0usize; k];
    let at = |used: &[usize], i: usize| base[(cut[i] + used[i]) % size];
    // the arrow whose next event comes first, or none when all are done
    let pick = |used: &[usize]| {
        let mut choice: Option<(f64, u8, usize)> = None;
        for i in 0..k {
            if used[i] == size {
                continue;
            }
            let (a, kind) = at(used, i);
            let key = (turned(a, i), kind, i);
            if choice.map_or(true, |c| (key.0, key.1) < (c.0, c.1)) {
                choice = Some(key);
            }
        }
        choice
    };
    let (mut best, mut best_angle) = (-1i64, 0.0);
    let mut total: i64 = count.iter().map(|&c| gain[c]).sum();
    let mut next = pick(&used);
    let first = next.unwrap().0;
    let mut leaving = Vec::new();
    while let Some((x, _, _)) = next {
        leaving.clear();
        while let Some((a, kind, i)) = next {
            if a - x > EPS {
                break;
            }
            if kind == ENTER {
                total += gain[count[i] + 1] - gain[count[i]];
                count[i] += 1;
            } else {
                leaving.push(i);
            }
            used[i] += 1;
            next = pick(&used);
        }
        // at the angle itself, touching counts: new cows join, none leave yet
        let point = total;
        for &i in &leaving {
            count[i] -= 1;
            total -= gain[count[i] + 1] - gain[count[i]];
        }
        // after the last event the stretch runs on past 2 pi to the first one
        let following = next.map_or(TAU + first, |e| e.0);
        // an open stretch is safer than a single tangent angle, so it wins ties
        if following - x > EPS && total >= best {
            best = total;
            best_angle = (x + following) / 2.0;
        }
        if point > best {
            best = point;
            best_angle = x;
        }
    }
    println!(
        "The best shot at ({:.10};{:.10}) gives Vasya {:.4} average hits.",
        best_angle.cos(),
        best_angle.sin(),
        best as f64 / scale as f64
    );
}
