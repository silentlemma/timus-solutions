use std::io::{self, Read};

type Point = (i64, i64);

fn cross(o: Point, a: Point, b: Point) -> i64 {
    (a.0 - o.0) * (b.1 - o.1) - (a.1 - o.1) * (b.0 - o.0)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    let pts: Vec<Point> = v[1..]
        .chunks_exact(2)
        .take(n)
        .map(|c| (c[0], c[1]))
        .collect();
    // A is the lowest point and B the next one on the hull, so every other
    // point lies on the left of AB and sees it under an angle below 180
    let a = *pts.iter().min_by_key(|p| (p.1, p.0)).unwrap();
    let rest: Vec<Point> = pts.iter().copied().filter(|&p| p != a).collect();
    let mut b = rest[0];
    for &p in &rest {
        if cross(a, b, p) < 0 {
            b = p;
        }
    }
    // the angle APB grows as its cotangent dot / cross falls; the products
    // reach 10^33, hence 128 bits
    let key = |p: Point| -> (i128, i128) {
        let dot = (a.0 - p.0) * (b.0 - p.0) + (a.1 - p.1) * (b.1 - p.1);
        (dot as i128, cross(p, a, b) as i128)
    };
    let mut others: Vec<(Point, (i128, i128))> = rest
        .iter()
        .copied()
        .filter(|&p| p != b)
        .map(|p| (p, key(p)))
        .collect();
    let mid = others.len() / 2;
    others.select_nth_unstable_by(mid, |x, y| {
        let ((dx, cx), (dy, cy)) = (x.1, y.1);
        (dy * cx).cmp(&(dx * cy))
    });
    // points seeing AB under a larger angle than C lie inside the circle ABC
    let c = others[mid].0;
    println!("{} {}\n{} {}\n{} {}", a.0, a.1, b.0, b.1, c.0, c.1);
}
