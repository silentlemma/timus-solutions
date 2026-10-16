use std::io::{self, Read};

const CORNERS: usize = 3;
const HEADER: usize = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let (mana, h, top) = (v[0], v[1], v[2]);
    let x: Vec<i64> = v[HEADER..].iter().step_by(2).cloned().collect();
    let y: Vec<i64> = v[HEADER + 1..].iter().step_by(2).cloned().collect();
    // after flying up, mana - h is left for the radius, and the field must
    // reach the nearest of the floor and the three walls
    let spare = mana - h;
    let mut ok = spare >= h;
    for i in 1..=CORNERS {
        if spare < 0 {
            break;
        }
        let j = i % CORNERS + 1;
        let (ux, uy) = (x[j] - x[i], y[j] - y[i]);
        let (wx, wy, wz) = (x[CORNERS + 1] - x[i], y[CORNERS + 1] - y[i], top);
        let (nx, ny, nz) = (uy * wz, -ux * wz, ux * wy - uy * wx);
        let reach = (nx * (x[0] - x[i]) + ny * (y[0] - y[i]) + nz * h) as i128;
        // the distance to the wall is reach / |normal|, compared exactly
        let length = (nx * nx + ny * ny + nz * nz) as i128;
        if reach * reach <= (spare * spare) as i128 * length {
            ok = true;
        }
    }
    println!("{}", if ok && spare >= 0 { "YES" } else { "NO" });
}
