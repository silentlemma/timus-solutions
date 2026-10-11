use std::io::{self, Read};

const DIM: usize = 8;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let mut point = || -> Vec<i64> { (0..DIM).map(|_| it.next().unwrap()).collect() };
    let (a, b, c) = (point(), point(), point());
    let r = it.next().unwrap();
    let (mut length2, mut ca2, mut cb2, mut dot) = (0i64, 0i64, 0i64, 0i64);
    for i in 0..DIM {
        let (ab, ac, bc) = (b[i] - a[i], c[i] - a[i], c[i] - b[i]);
        length2 += ab * ab;
        ca2 += ac * ac;
        cb2 += bc * bc;
        dot += ab * ac;
    }
    // the segment enters the ball when the closest point of it to C lies
    // strictly inside; outside 0 <= t <= 1 the closest point is an end, and
    // both ends are outside: |AC|^2 |AB|^2 - (AB . AC)^2 < R^2 |AB|^2
    if length2 == 0 || dot <= 0 || dot >= length2 || ca2 * length2 - dot * dot >= r * r * length2 {
        println!("{:.2}", (length2 as f64).sqrt());
        return;
    }
    // otherwise, in the plane of A, B and C: a tangent from A, an arc of the
    // great circle and a tangent to B
    let (da, db, rf) = ((ca2 as f64).sqrt(), (cb2 as f64).sqrt(), r as f64);
    let cos = (ca2 + cb2 - length2) as f64 / (2.0 * da * db);
    let arc = cos.clamp(-1.0, 1.0).acos() - (rf / da).acos() - (rf / db).acos();
    let total = ((ca2 - r * r) as f64).sqrt() + ((cb2 - r * r) as f64).sqrt() + rf * arc;
    println!("{:.2}", total);
}
