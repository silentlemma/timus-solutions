use std::io::{self, BufRead};

// coordinates differ by at most 2000000; products and cross products fit in 64 bits.
struct Point {
    x: i32,
    y: i32,
    index: usize,
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let mut line = String::new();
    input.read_line(&mut line).unwrap();
    let n: usize = line.trim().parse().unwrap();
    let mut points: Vec<Point> = Vec::with_capacity(n);
    // the lowest point (the leftmost of the lowest) sees all others within
    // half a turn, so they can be sorted by angle with cross products
    let mut pivot = 0;
    for i in 0..n {
        line.clear();
        input.read_line(&mut line).unwrap();
        let mut values = line.split_ascii_whitespace();
        let x = values.next().unwrap().parse().unwrap();
        let y = values.next().unwrap().parse().unwrap();
        points.push(Point { x, y, index: i + 1 });
        if (y, x) < (points[pivot].y, points[pivot].x) {
            pivot = i;
        }
    }
    let origin = points.swap_remove(pivot);
    for point in &mut points {
        point.x -= origin.x;
        point.y -= origin.y;
    }
    points.sort_unstable_by(|a, b| {
        let cross = i64::from(a.x) * i64::from(b.y) - i64::from(a.y) * i64::from(b.x);
        0.cmp(&cross)
    });
    // the middle one leaves (n - 2) / 2 points on each side of the line
    println!("{} {}", origin.index, points[(n - 2) / 2].index);
}
