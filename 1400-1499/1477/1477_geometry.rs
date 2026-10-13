use std::collections::HashSet;
use std::io::{self, Read};

const AXES: usize = 3;
type Vec3 = [i64; AXES];

fn cross(a: &Vec3, b: &Vec3) -> Vec3 {
    [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ]
}

fn dot(a: &Vec3, b: &Vec3) -> i64 {
    a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
}

fn gcd(a: i64, b: i64) -> i64 {
    let (mut a, mut b) = (a.abs(), b.abs());
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    let points: Vec<Vec3> = v[1..]
        .chunks(AXES)
        .take(n)
        .map(|c| [c[0], c[1], c[2]])
        .collect();

    // every plane through the origin and two non-parallel points, once
    let mut normals: HashSet<Vec3> = HashSet::new();
    for i in 0..n {
        for j in i + 1..n {
            let c = cross(&points[i], &points[j]);
            let mut g = gcd(gcd(c[0], c[1]), c[2]);
            if g == 0 {
                continue;
            }
            if *c.iter().find(|&&x| x != 0).unwrap() < 0 {
                g = -g;
            }
            normals.insert([c[0] / g, c[1] / g, c[2] / g]);
        }
    }

    let mut best = 1; // a single airplane is always visible
    for normal in &normals {
        let (mut above, mut below) = (0, 0);
        let mut circle: Vec<Vec3> = Vec::new();
        for p in &points {
            let s = dot(normal, p);
            if s > 0 {
                above += 1;
            } else if s < 0 {
                below += 1;
            } else {
                circle.push(*p);
            }
        }
        // a slight tilt shows the points of the circle in its best open half:
        // its edge passes through one of them, which a tilt adds as well
        let mut half = 0;
        for z in &circle {
            let edge = cross(normal, z);
            let ahead = circle.iter().filter(|p| dot(&edge, p) > 0).count();
            let behind = circle.iter().filter(|p| dot(&edge, p) < 0).count();
            half = half.max(ahead.max(behind) + 1);
        }
        best = best.max(above.max(below) + half);
    }
    println!("{}", best);
}
