use std::fmt::Write as _;
use std::io::{self, Read};

const FULL: f64 = 360.0;
const MINUTES: f64 = 60.0;
const EPS: f64 = 1e-9;
const FIELDS: usize = 3; // azimuth, distance, speed

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let nums: Vec<f64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let (a, w, n) = (nums[0], nums[1], nums[2] as usize);
    let mut first = Vec::new(); // ships right in front of the gun, shot at once
    let mut ships: Vec<(f64, f64, usize)> = Vec::new(); // angle, deadline, number
    for (k, ship) in nums[FIELDS..].chunks(FIELDS).take(n).enumerate() {
        let (b, d, v) = (ship[0], ship[1], ship[2]);
        let deadline = (d - 1.0) / v * MINUTES; // when the ship reaches one mile
        let turn = (b - a).rem_euclid(FULL);
        if turn <= EPS || FULL - turn <= EPS {
            first.push(k + 1);
        } else {
            ships.push((turn, deadline, k + 1));
        }
    }
    ships.sort_by(|x, y| x.0.partial_cmp(&y.0).unwrap());
    let m = ships.len();
    let size = m + 1;
    // the turning rate in degrees a minute
    let rate = FULL * w;
    // the shot ships form an arc around the start: i taken turning left
    // (from the end of the sorted list), j turning right; left and right
    // keep the earliest time with the gun at that end of the arc
    let mut left = vec![f64::INFINITY; size * size];
    let mut right = vec![f64::INFINITY; size * size];
    let mut came_left = vec![0usize; size * size]; // the side before
    let mut came_right = vec![0usize; size * size];
    left[0] = 0.0;
    right[0] = 0.0;
    for i in 0..size {
        for j in 0..m.saturating_sub(i) {
            let here = i * size + j;
            let (tl, tr) = (left[here], right[here]);
            if tl.is_infinite() && tr.is_infinite() {
                continue;
            }
            let at_left = if i > 0 { FULL - ships[m - i].0 } else { 0.0 };
            let at_right = if j > 0 { ships[j - 1].0 } else { 0.0 };
            let next = ships[j].0; // the next ship turning right
            let there = here + 1;
            let moves =
                [(tr + (next - at_right) / rate, 1), (tl + (at_left + next) / rate, 0)];
            for &(t, side) in &moves {
                if t <= ships[j].1 + EPS && t + EPS < right[there] {
                    right[there] = t;
                    came_right[there] = side;
                }
            }
            let next = FULL - ships[m - i - 1].0; // the next ship turning left
            let there = here + size;
            let moves =
                [(tl + (next - at_left) / rate, 0), (tr + (at_right + next) / rate, 1)];
            for &(t, side) in &moves {
                if t <= ships[m - i - 1].1 + EPS && t + EPS < left[there] {
                    left[there] = t;
                    came_left[there] = side;
                }
            }
        }
    }
    // ending at the left end wins ties, then the fewest ships taken leftwards
    let mut best = f64::INFINITY;
    let mut side = 0;
    for (s, at) in [&left, &right].iter().enumerate() {
        for i in 0..size {
            if at[i * size + m - i] < best {
                best = at[i * size + m - i];
                side = s;
            }
        }
    }
    if best.is_infinite() {
        println!("Impossible");
        return;
    }
    let at = if side == 1 { &right } else { &left };
    let mut i = (0..size).find(|&i| (at[i * size + m - i] - best).abs() <= EPS).unwrap();
    let mut j = m - i;
    let mut order = Vec::new();
    while i > 0 || j > 0 {
        let here = i * size + j;
        if side == 1 {
            order.push(ships[j - 1].2);
            side = came_right[here];
            j -= 1;
        } else {
            order.push(ships[m - i].2);
            side = came_left[here];
            i -= 1;
        }
    }
    let mut out = format!("{:.3}\n", best);
    for k in first.iter().chain(order.iter().rev()) {
        writeln!(out, "{}", k).unwrap();
    }
    print!("{}", out);
}
