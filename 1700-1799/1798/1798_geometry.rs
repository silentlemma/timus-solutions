use std::io::{self, Read};

const QUARTERS: i64 = 4;

fn isqrt(v: i64) -> i64 {
    let mut r = (v as f64).sqrt() as i64;
    while r * r > v {
        r -= 1;
    }
    while (r + 1) * (r + 1) <= v {
        r += 1;
    }
    r
}

// the sum of isqrt(n - x*x) over x = 0 .. m, where 2*m*m <= n, found by
// walking from m to the left along the upper hull of the lattice points
// in the disk; a vector (a, b) moves a columns left and b rows up
fn column_sum(n: i64, m: i64) -> i64 {
    let inside = |px: i64, py: i64| px >= 0 && px * px + py * py <= n;
    let (mut x, mut y) = (m, isqrt(n - m * m));
    let mut total = y;
    let mut stack: Vec<(i64, i64)> = vec![(1, 0), (1, 1)];
    while x > 0 {
        let (mut a1, mut b1) = stack.pop().unwrap();
        while inside(x - a1, y + b1) {
            // the columns x - a1 .. x - 1 lie under this hull edge
            total += a1 * y + (a1 - 1) * (b1 - 1) / 2 + b1;
            x -= a1;
            y += b1;
        }
        if x - a1 < 0 {
            break;
        }
        let (mut a2, mut b2) = (a1, b1);
        loop {
            (a1, b1) = *stack.last().unwrap();
            if inside(x - a1, y + b1) {
                break;
            }
            (a2, b2) = (a1, b1);
            stack.pop();
        }
        loop {
            let (a12, b12) = (a1 + a2, b1 + b2);
            let nx = x - a12;
            if nx < 0 {
                break;
            }
            if inside(nx, y + b12) {
                stack.push((a12, b12));
                (a1, b1) = (a12, b12);
            } else {
                // from the outside point nx, steps of (a1, b1) rise at least
                // as fast as the circle, so no inside point lies between
                let rise = (b1 * b1) as i128 * (n - nx * nx) as i128;
                if rise >= (a1 * a1) as i128 * (nx * nx) as i128 {
                    break;
                }
                (a2, b2) = (a12, b12);
            }
        }
    }
    total + (0..x).map(|column| isqrt(n - column * column)).sum::<i64>()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let radius: i64 = input.trim().parse().unwrap();
    // slab (x, y) of the first quarter burns when its nearest corner is
    // strictly inside the circle: x*x + y*y <= radius^2 - 1
    let n = radius * radius - 1;
    let m = isqrt(n / 2);
    let total = column_sum(n, m);
    // points with x < y twice, then the diagonal once
    let quarter = 2 * (total - m * (m + 1) / 2) + m + 1;
    println!("{}", QUARTERS * quarter);
}
