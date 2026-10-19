use std::io::{self, Read};

const DIM: usize = 3;

type Vec3 = [i128; DIM]; // the mixed product reaches 5 * 10^19

fn sub(u: Vec3, v: Vec3) -> Vec3 {
    [u[0] - v[0], u[1] - v[1], u[2] - v[2]]
}

fn dot(u: Vec3, v: Vec3) -> i128 {
    u.iter().zip(v.iter()).map(|(a, b)| a * b).sum()
}

fn cross(u: Vec3, v: Vec3) -> Vec3 {
    [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i128> = input.split_whitespace().map(|t| t.parse().unwrap()).collect();
    let p: Vec<Vec3> = v.chunks(DIM).map(|c| [c[0], c[1], c[2]]).collect();
    let (ab, cd, ac) = (sub(p[1], p[0]), sub(p[DIM], p[2]), sub(p[2], p[0]));
    // the turn is a right angle, the two lines meet, the turning point
    // P = A + t AB with t = (AC . AB) / |AB|^2 is not before B, and C is not
    // before P on the second line, (C - P) . CD = AC . CD >= 0
    let ok = dot(ab, cd) == 0
        && dot(ac, cross(ab, cd)) == 0
        && dot(ac, ab) >= dot(ab, ab)
        && dot(ac, cd) >= 0;
    println!("{}", if ok { "Valid" } else { "Invalid" });
}
