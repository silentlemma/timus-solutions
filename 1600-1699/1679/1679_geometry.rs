use std::io::{self, Read, Write};

// whether one side of some inscribed square passes through both points:
// a side lies on a line at distance R / sqrt(2) from the centre, and the
// disc cuts exactly the side out of that line
fn same_side(r: i64, x1: i64, y1: i64, x2: i64, y2: i64) -> bool {
    if x1 == x2 && y1 == y2 {
        return 2 * (x1 * x1 + y1 * y1) >= r * r;
    }
    let cross = x1 * y2 - y1 * x2;
    let (dx, dy) = (x1 - x2, y1 - y2);
    2 * cross * cross == r * r * (dx * dx + dy * dy)
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut it = text.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let t = it.next().unwrap();
    let mut out = String::new();
    for _ in 0..t {
        let mut next = || it.next().unwrap();
        let (r, x1, y1, x2, y2) = (next(), next(), next(), next(), next());
        // the second point on the same, the opposite or an adjacent side:
        // turning it by 0, 180, 90 or -90 degrees brings it onto the first one's side
        let ok = same_side(r, x1, y1, x2, y2)
            || same_side(r, x1, y1, -x2, -y2)
            || same_side(r, x1, y1, -y2, x2)
            || same_side(r, x1, y1, y2, -x2);
        out.push_str(if ok { "YES\n" } else { "NO\n" });
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
