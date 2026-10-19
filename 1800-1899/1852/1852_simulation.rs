use std::collections::HashMap;
use std::io::{self, Read};

const DIMENSIONS: usize = 3;
type Vec3 = [i32; DIMENSIONS];

const NAMES: &[u8] = b"UDLRFB";
// the outward normal of every face, in the order of NAMES
const FACES: [Vec3; 6] = [[0, 1, 0], [0, -1, 0], [-1, 0, 0], [1, 0, 0], [0, 0, 1], [0, 0, -1]];

fn dot(a: &Vec3, b: &Vec3) -> i32 {
    a.iter().zip(b).map(|(x, y)| x * y).sum()
}

// a quarter turn of v about the axis a: counter-clockwise seen from the tip
// of a for sign 1, clockwise for sign -1
fn turn(v: &Vec3, a: &Vec3, sign: i32) -> Vec3 {
    let cross = [a[1] * v[2] - a[2] * v[1], a[2] * v[0] - a[0] * v[2], a[0] * v[1] - a[1] * v[0]];
    let along = dot(a, v);
    let mut r = [0; DIMENSIONS];
    for k in 0..r.len() {
        r[k] = sign * cross[k] + a[k] * along;
    }
    r
}

fn gcd(a: u64, b: u64) -> u64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let moves = input.trim().as_bytes();
    // a sticker is a cubie position with every coordinate in -1..1 and the
    // outward normal of a face that cubie touches
    let mut stickers: Vec<(Vec3, Vec3)> = Vec::new();
    for x in -1..=1 {
        for y in -1..=1 {
            for z in -1..=1 {
                for n in FACES.iter() {
                    if dot(&[x, y, z], n) == 1 {
                        stickers.push(([x, y, z], *n));
                    }
                }
            }
        }
    }
    let index: HashMap<(Vec3, Vec3), usize> =
        stickers.iter().enumerate().map(|(i, &s)| (s, i)).collect();
    let count = stickers.len();
    // the place every sticker moves to under each letter
    let mut table: Vec<Vec<usize>> = vec![Vec::new(); 1 << u8::BITS];
    for (f, a) in FACES.iter().enumerate() {
        for sign in [1, -1] {
            let letter = if sign == 1 { NAMES[f] } else { NAMES[f].to_ascii_lowercase() };
            table[letter as usize] = stickers
                .iter()
                .enumerate()
                .map(|(i, (p, n))| {
                    if dot(p, a) == 1 {
                        index[&(turn(p, a, sign), turn(n, a, sign))]
                    } else {
                        i
                    }
                })
                .collect();
        }
    }
    // where each sticker ends up after the whole sequence
    let mut place: Vec<usize> = (0..count).collect();
    for &c in moves {
        let to = &table[c as usize];
        for p in place.iter_mut() {
            *p = to[*p];
        }
    }
    // the sequence returns the cube after the lcm of the cycle lengths
    let mut order = 1u64;
    let mut seen = vec![false; count];
    for start in 0..count {
        let (mut length, mut i) = (0u64, start);
        while !seen[i] {
            seen[i] = true;
            i = place[i];
            length += 1;
        }
        if length > 0 {
            order = order / gcd(order, length) * length;
        }
    }
    println!("{}", order - 1);
}
