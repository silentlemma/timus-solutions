use std::io::{self, Read};

const SCALE: i64 = 10_000_000_000; // ten digits after the point
const FULL_TURN: f64 = 360.0;
const VERTICES: usize = 3;
const ORDERS: [[usize; VERTICES]; 6] = [
    [0, 1, 2],
    [0, 2, 1],
    [1, 0, 2],
    [1, 2, 0],
    [2, 0, 1],
    [2, 1, 0],
];

type P = (i64, i64);

fn cross(o: P, a: P, b: P) -> i64 {
    (a.0 - o.0) * (b.1 - o.1) - (a.1 - o.1) * (b.0 - o.0)
}

fn length2(a: P, b: P) -> i64 {
    (a.0 - b.0).pow(2) + (a.1 - b.1).pow(2)
}

/// num / den with exactly ten digits after the point, rounded.
fn decimal(num: i64, den: i64) -> String {
    let (num, den) = if den < 0 { (-num, -den) } else { (num, den) };
    let a = num.abs();
    let (mut whole, rem) = (a / den, a % den);
    let mut part = (2 * rem * SCALE + den) / (2 * den);
    if part == SCALE {
        whole += 1;
        part = 0;
    }
    let sign = if num < 0 && (whole > 0 || part > 0) {
        "-"
    } else {
        ""
    };
    format!("{}{}.{:010}", sign, whole, part)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let point = |i: usize| (v[2 * i], v[2 * i + 1]);
    let target: [P; VERTICES] = [point(0), point(1), point(2)];
    let token: [P; VERTICES] = [point(VERTICES), point(VERTICES + 1), point(VERTICES + 2)];

    // a correspondence works when the sides match and the turn is the same
    // (the token cannot be flipped over)
    let fits: Vec<[P; VERTICES]> = ORDERS
        .iter()
        .map(|idx| [target[idx[0]], target[idx[1]], target[idx[2]]])
        .filter(|o| {
            length2(token[0], token[1]) == length2(o[0], o[1])
                && length2(token[0], token[2]) == length2(o[0], o[2])
                && length2(token[1], token[2]) == length2(o[1], o[2])
                && (cross(token[0], token[1], token[2]) > 0) == (cross(o[0], o[1], o[2]) > 0)
        })
        .collect();
    if fits.is_empty() {
        println!("0");
        return;
    }
    for o in &fits {
        let (dx, dy) = (o[0].0 - token[0].0, o[0].1 - token[0].1);
        if (1..VERTICES).all(|i| o[i].0 - token[i].0 == dx && o[i].1 - token[i].1 == dy) {
            println!("1 {} {}", decimal(dx, 1), decimal(dy, 1));
            return;
        }
    }

    let o = fits[0];
    let (ux, uy) = (token[1].0 - token[0].0, token[1].1 - token[0].1);
    let (wx, wy) = (o[1].0 - o[0].0, o[1].1 - o[0].1);
    let mut angle = ((ux * wy - uy * wx) as f64)
        .atan2((ux * wx + uy * wy) as f64)
        .to_degrees();
    if angle < 0.0 {
        angle += FULL_TURN;
    }

    // the centre is a vertex that stays, or it lies on the perpendicular
    // bisector of every vertex and its image: 2 d . c = |t|^2 - |s|^2
    let mut centre: Option<(String, String)> = None;
    for i in 0..VERTICES {
        if token[i] == o[i] {
            centre = Some((decimal(token[i].0, 1), decimal(token[i].1, 1)));
        }
    }
    if centre.is_none() {
        let a: Vec<i64> = (0..VERTICES).map(|i| 2 * (o[i].0 - token[i].0)).collect();
        let b: Vec<i64> = (0..VERTICES).map(|i| 2 * (o[i].1 - token[i].1)).collect();
        let e: Vec<i64> = (0..VERTICES)
            .map(|i| o[i].0.pow(2) + o[i].1.pow(2) - token[i].0.pow(2) - token[i].1.pow(2))
            .collect();
        'search: for i in 0..VERTICES {
            for j in i + 1..VERTICES {
                let det = a[i] * b[j] - a[j] * b[i];
                if det != 0 {
                    centre = Some((
                        decimal(e[i] * b[j] - e[j] * b[i], det),
                        decimal(a[i] * e[j] - a[j] * e[i], det),
                    ));
                    break 'search;
                }
            }
        }
    }
    let (cx, cy) = centre.unwrap();
    println!("2 {} {} {:.10}", cx, cy, angle);
}
