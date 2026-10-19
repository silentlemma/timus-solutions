use std::io::{self, Read};

const SCALE: i32 = 1000;
const FRACTION_DIGITS: usize = 3;

fn scaled(token: &str) -> i32 {
    let (mut sign, mut fraction, mut digits) = (1, 0, 0);
    let mut after_point = false;
    for symbol in token.bytes() {
        match symbol {
            b'-' => sign = -1,
            b'+' => (),
            b'.' => after_point = true,
            _ if after_point => {
                fraction = fraction * 10 + i32::from(symbol - b'0');
                digits += 1;
            }
            _ => (),
        }
    }
    while digits < FRACTION_DIGITS {
        fraction *= 10;
        digits += 1;
    }
    sign * fraction
}

fn best_group(points: &[(i32, i32)]) -> (i32, i32) {
    let mut counts = vec![0; (SCALE * SCALE) as usize];
    let (mut best_count, mut best_norm) = (0, 0);
    for &(x, y) in points {
        let (rx, ry) = (x.rem_euclid(SCALE), y.rem_euclid(SCALE));
        let code = (rx * SCALE + ry) as usize;
        counts[code] += 1;
        let count = counts[code];
        let (dx, dy) = (rx.min(SCALE - rx), ry.min(SCALE - ry));
        let norm = dx * dx + dy * dy;
        if count > best_count || (count == best_count && norm < best_norm) {
            best_count = count;
            best_norm = norm;
        }
    }
    (best_count, best_norm)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let size = words.next().unwrap().parse::<usize>().unwrap();
    let points: Vec<(i32, i32)> = (0..size)
        .map(|_| (scaled(words.next().unwrap()), scaled(words.next().unwrap())))
        .collect();
    let (count, norm) = best_group(&points);
    println!("{} {:.9}", count, f64::from(norm).sqrt() / f64::from(SCALE));
}
