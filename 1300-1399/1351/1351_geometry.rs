use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let mut next = || it.next().unwrap();
    let (reach, rx, ry, lx, ly) = (next(), next(), next(), next(), next());
    let n = next();
    let mut out = String::new();
    for _ in 0..n {
        let (x, y) = (next(), next());
        // inside the sector means left of the right border and right of the
        // left one, borders included; the sector is narrower than a half turn
        let (right, left) = (rx * y - ry * x, x * ly - y * lx);
        let inside = right >= 0 && left >= 0;
        // a border's extension behind the gun is out; for a sector of zero
        // width, both borders along one ray, no other test rejects it
        let behind = (right == 0 && rx * x + ry * y < 0) || (left == 0 && lx * x + ly * y < 0);
        out.push_str(if inside && !behind && x * x + y * y <= reach * reach {
            "YES\n"
        } else {
            "NO\n"
        });
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
