use std::io::{self, Read};

const TRIANGLE: usize = 3;
const CORNERS: usize = 4;
const CLOSED: usize = 5;
#[derive(Clone, Copy)]
struct Point {
    x: i64,
    y: i64,
}
fn cross(a: Point, b: Point, p: Point) -> i64 {
    (b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x)
}
fn same_sum(a: Point, b: Point, c: Point, d: Point) -> bool {
    a.x + b.x == c.x + d.x && a.y + b.y == c.y + d.y
}
fn parallelogram(p: &[Point]) -> bool {
    same_sum(p[0], p[1], p[2], p[TRIANGLE])
        || same_sum(p[0], p[2], p[1], p[TRIANGLE])
        || same_sum(p[0], p[TRIANGLE], p[1], p[2])
}
fn solve(points: &[Point]) -> String {
    let n = points.len();
    if n <= TRIANGLE {
        return n.to_string();
    }
    for i in 0..TRIANGLE {
        for j in i + 1..TRIANGLE {
            let mut outside = 0;
            for &p in points {
                if cross(points[i], points[j], p) != 0 {
                    outside += 1;
                    if outside > 1 {
                        break;
                    }
                }
            }
            if outside <= 1 {
                return n.to_string();
            }
        }
    }
    if n == CORNERS {
        return if parallelogram(points) {
            CLOSED.to_string()
        } else {
            "oo".to_string()
        };
    }
    if n == CLOSED {
        for center in 0..n {
            let mut others = Vec::with_capacity(CORNERS);
            let (mut sx, mut sy) = (0, 0);
            for (i, &p) in points.iter().enumerate() {
                if i != center {
                    others.push(p);
                    sx += p.x;
                    sy += p.y;
                }
            }
            if parallelogram(&others)
                && sx == CORNERS as i64 * points[center].x
                && sy == CORNERS as i64 * points[center].y
            {
                return CLOSED.to_string();
            }
        }
    }
    "oo".to_string()
}
fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let points: Vec<Point> = (0..n)
        .map(|_| Point {
            x: words.next().unwrap().parse().unwrap(),
            y: words.next().unwrap().parse().unwrap(),
        })
        .collect();
    println!("{}", solve(&points));
}
