use std::io::{self, Read};

const DIM: usize = 3;

fn cross(u: [f64; DIM], v: [f64; DIM]) -> [f64; DIM] {
    [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let mut next = || words.next().unwrap();
    let (a, b) = (next(), next());
    let p: Vec<i64> = (0..DIM).map(|_| next()).collect();
    let d: Vec<i64> = (0..DIM).map(|i| next() - p[i]).collect();
    // the elbow's axis is parallel to the rail and across both segments, so the
    // shoulder, the elbow and the claw lie in the plane through the shoulder
    // across the rail, and the claw sits at the rail's point h nearest to it
    let c = [p[1] * d[2] - p[2] * d[1], p[2] * d[0] - p[0] * d[2], p[0] * d[1] - p[1] * d[0]];
    let dd: i64 = d.iter().map(|x| x * x).sum();
    let num: i64 = c.iter().map(|x| x * x).sum(); // |h|^2 = num / dd, exactly

    // the bend (the angle opposite h) is not acute and the triangle closes:
    // a^2 + b^2 <= |h|^2 <= (a + b)^2
    if (a * a + b * b) * dd > num || num > (a + b) * (a + b) * dd {
        println!("No solution.");
        return;
    }
    let t = -((0..DIM).map(|i| p[i] * d[i]).sum::<i64>() as f64) / dd as f64;
    let r = (num as f64 / dd as f64).sqrt();
    let mut e1 = [0.0; DIM];
    let mut unit = [0.0; DIM];
    for i in 0..DIM {
        e1[i] = (p[i] as f64 + t * d[i] as f64) / r;
        unit[i] = d[i] as f64 / (dd as f64).sqrt();
    }
    let e2 = cross(unit, e1);
    // the elbow is at distance a from the shoulder and b from h
    let (fa, fb) = (a as f64, b as f64);
    let along = (fa * fa - fb * fb + r * r) / (2.0 * r);
    let side = (fa * fa - along * along).max(0.0).sqrt();
    let bend = ((fa * fa + fb * fb - r * r) / (2.0 * fa * fb)).clamp(-1.0, 1.0).acos();
    let elbow: Vec<String> =
        (0..DIM).map(|i| format!("{:.15}", along * e1[i] + side * e2[i])).collect();
    println!("{} {:.15}", elbow.join(" "), bend);
}
