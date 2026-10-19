use std::io::{self, Read, Write};

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

// atom 0 at the origin, atom p at (a, b); every other atom follows from its
// distances to these two up to a reflection in the line through them, and
// the first atom off that line picks the side by flip
fn place(d: &[Vec<i64>], p: usize, a: i64, b: i64, flip: bool) -> Option<Vec<(i64, i64)>> {
    let n = d.len();
    let big = a * a + b * b;
    let signs = if flip { [-1, 1] } else { [1, -1] };
    let mut at = vec![(0i64, 0i64); n];
    for i in 1..n {
        let twice = d[0][i] - d[p][i] + big; // twice the dot product with (a, b)
        if twice % 2 != 0 {
            return None;
        }
        let dot = twice / 2;
        let square = big * d[0][i] - dot * dot; // the cross product, squared
        if square < 0 {
            return None;
        }
        let cross = isqrt(square);
        if cross * cross != square {
            return None;
        }
        let mut done = false;
        for &sign in signs.iter() {
            let nx = a * dot + b * sign * cross;
            let ny = b * dot - a * sign * cross;
            if nx % big != 0 || ny % big != 0 {
                continue;
            }
            let (x, y) = (nx / big, ny / big);
            let fits = (0..i).all(|j| {
                let (dx, dy) = (x - at[j].0, y - at[j].1);
                dx * dx + dy * dy == d[i][j]
            });
            if fits {
                at[i] = (x, y);
                done = true;
                break;
            }
        }
        if !done {
            return None;
        }
    }
    Some(at)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let d: Vec<Vec<i64>> = (0..n).map(|_| (0..n).map(|_| it.next().unwrap()).collect()).collect();
    let mut out = String::new();
    let p = (1..n).find(|&i| d[0][i] != 0);
    let p = match p {
        Some(p) => p,
        None => {
            // everything sits at the origin
            if d.iter().all(|row| row.iter().all(|&v| v == 0)) {
                for _ in 0..n {
                    out.push_str("0 0\n");
                }
            } else {
                out.push_str("Impossible\n");
            }
            io::stdout().write_all(out.as_bytes()).unwrap();
            return;
        }
    };
    let big = d[0][p];
    // the symmetries of the grid bring atom p to (a, b) with 0 <= a <= b
    let mut a = 0i64;
    while 2 * a * a <= big {
        let b = isqrt(big - a * a);
        if a * a + b * b == big {
            for &flip in [false, true].iter() {
                if let Some(at) = place(&d, p, a, b, flip) {
                    for (x, y) in at {
                        out.push_str(&format!("{} {}\n", x, y));
                    }
                    io::stdout().write_all(out.as_bytes()).unwrap();
                    return;
                }
            }
        }
        a += 1;
    }
    println!("Impossible");
}
