use std::io::{self, Read};

const DECIMAL_SCALE: i64 = 1000000000000;
const PRECISION: usize = 12;

struct Line {
    dx: i64,
    dy: i64,
    c: i64,
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let mut lines = Vec::with_capacity(count);
    for _ in 0..count {
        let x1: i64 = tokens.next().unwrap().parse().unwrap();
        let y1: i64 = tokens.next().unwrap().parse().unwrap();
        let x2: i64 = tokens.next().unwrap().parse().unwrap();
        let y2: i64 = tokens.next().unwrap().parse().unwrap();
        let mut dx = x2 - x1;
        let mut dy = y2 - y1;
        if dx < 0 || (dx == 0 && dy < 0) {
            dx = -dx;
            dy = -dy;
        }
        lines.push(Line {
            dx,
            dy,
            c: dy * x1 - dx * y1,
        });
    }

    lines.sort_unstable_by(|a, b| (a.dy * b.dx).cmp(&(b.dy * a.dx)));

    let mut best_num = 0_i64;
    let mut best_den = 1_i64;
    // A farthest intersection belongs to neighboring directions in cyclic order.
    for i in 0..count {
        let a = &lines[i];
        let b = &lines[(i + 1) % count];
        let num = (a.dx * b.c - a.c * b.dx).abs() + (a.dy * b.c - a.c * b.dy).abs();
        let den = (a.dx * b.dy - a.dy * b.dx).abs();
        if num * best_den > best_num * den {
            best_num = num;
            best_den = den;
        }
    }

    let rounded = ((best_num % best_den) * DECIMAL_SCALE + best_den / 2) / best_den;
    let mut answer = (best_num / best_den + rounded / DECIMAL_SCALE).to_string();
    let remainder = rounded % DECIMAL_SCALE;
    if remainder != 0 {
        let fractional = format!("{:0width$}", remainder, width = PRECISION);
        answer.push('.');
        answer.push_str(fractional.trim_end_matches('0'));
    }
    println!("{}", answer);
}
