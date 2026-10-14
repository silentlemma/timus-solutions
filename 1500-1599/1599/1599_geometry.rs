use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut it = s
        .split_ascii_whitespace()
        .map(|x| x.parse::<i64>().unwrap());
    let n = match it.next() {
        Some(v) => v as usize,
        None => return,
    };
    let mut pts = Vec::with_capacity(n);
    for _ in 0..n {
        let x = it.next().unwrap();
        let y = it.next().unwrap();
        pts.push((x, y));
    }
    let m = it.next().unwrap() as usize;
    let mut out = String::new();
    for _ in 0..m {
        let (px, py) = (it.next().unwrap(), it.next().unwrap());
        let mut turns = 0;
        let mut on_edge = false;
        for i in 0..n {
            let (ax, ay) = pts[i];
            let (bx, by) = pts[(i + 1) % n];
            // each product is below 4 10^18, so the difference fits in 64 bits
            let cross = (bx - ax) * (py - ay) - (by - ay) * (px - ax);
            if cross == 0
                && ax.min(bx) <= px
                && px <= ax.max(bx)
                && ay.min(by) <= py
                && py <= ay.max(by)
            {
                on_edge = true;
                break;
            }
            if ay <= py && py < by {
                // upwards past the point on its left: one more turn
                if cross > 0 {
                    turns += 1;
                }
            } else if by <= py && py < ay {
                // downwards past the point on its right: one turn less
                if cross < 0 {
                    turns -= 1;
                }
            }
        }
        if on_edge {
            out.push_str("EDGE\n");
        } else {
            writeln!(out, "{}", turns).unwrap();
        }
    }
    print!("{}", out);
}
