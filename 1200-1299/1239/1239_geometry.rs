use std::io::{self, Read};

const EPS: f64 = 1e-9;
const FIELDS: usize = 4;
const RADIUS: usize = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    let g4: Vec<&[i64]> = v[1..].chunks(FIELDS).collect();
    let (x, y, z): (Vec<i64>, Vec<i64>, Vec<i64>) = (
        g4.iter().map(|c| c[0]).collect(),
        g4.iter().map(|c| c[1]).collect(),
        g4.iter().map(|c| c[2]).collect(),
    );
    // a ray along d touches ghost i when d.C_i >= L_i |d|, where L_i is the
    // length of a tangent from the gun: L_i^2 = |C_i|^2 - R_i^2
    let norm: Vec<i64> = (0..n)
        .map(|i| x[i] * x[i] + y[i] * y[i] + z[i] * z[i])
        .collect();
    let tan2: Vec<i64> = (0..n)
        .map(|i| norm[i] - g4[i][RADIUS] * g4[i][RADIUS])
        .collect();
    let tan: Vec<f64> = tan2.iter().map(|&a| (a as f64).sqrt()).collect();
    let dot: Vec<Vec<i64>> = (0..n)
        .map(|i| {
            (0..n)
                .map(|k| x[i] * x[k] + y[i] * y[k] + z[i] * z[k])
                .collect()
        })
        .collect();
    let mut best: Vec<usize> = Vec::new();
    // the ray through the centre of ghost i, tested exactly in integers
    for i in 0..n {
        let hit: Vec<usize> = (0..n)
            .filter(|&k| dot[i][k] * dot[i][k] >= tan2[k] * norm[i])
            .collect();
        if hit.len() > best.len() {
            best = hit;
        }
    }
    // rays touching two ghosts i and j: d = (a C_i + b C_j + c C_i x C_j) / det
    for i in 0..n {
        for j in i + 1..n {
            let g = dot[i][j];
            let det = norm[i] * norm[j] - g * g;
            if det == 0 {
                continue;
            }
            // 1 - |a C_i + b C_j|^2 = Q / det with Q = base + 2 g L_i L_j
            let base = det - tan2[i] * norm[j] - tan2[j] * norm[i];
            let p = tan2[i] * tan2[j];
            let gap = ((2 * g) * (2 * g)) as i128 * p as i128 - base as i128 * base as i128;
            if base < 0 && gap < 0 {
                continue; // the two outlines do not meet
            }
            let root = (p as f64).sqrt();
            let q = if base >= 0 {
                base as f64 + 2.0 * g as f64 * root
            } else {
                gap as f64 / (2.0 * g as f64 * root - base as f64)
            };
            // a det and b det, rationalised to avoid cancellation
            let na =
                (tan2[i] * norm[j]) as i128 * norm[j] as i128 - (tan2[j] * g) as i128 * g as i128;
            let nb =
                (tan2[j] * norm[i]) as i128 * norm[i] as i128 - (tan2[i] * g) as i128 * g as i128;
            let ad = na as f64 / (tan[i] * norm[j] as f64 + tan[j] * g as f64);
            let bd = nb as f64 / (tan[j] * norm[i] as f64 + tan[i] * g as f64);
            let cx = y[i] * z[j] - z[i] * y[j];
            let cy = z[i] * x[j] - x[i] * z[j];
            let cz = x[i] * y[j] - y[i] * x[j];
            let signs: &[f64] = if q > 0.0 { &[1.0, -1.0] } else { &[1.0] };
            for &sign in signs {
                let s = sign * q.sqrt();
                let hit: Vec<usize> = (0..n)
                    .filter(|&k| {
                        let t = (cx * x[k] + cy * y[k] + cz * z[k]) as f64;
                        let v = ad * dot[i][k] as f64 + bd * dot[j][k] as f64 + s * t;
                        k == i || k == j || v >= det as f64 * tan[k] * (1.0 - EPS)
                    })
                    .collect();
                if hit.len() > best.len() {
                    best = hit;
                }
            }
        }
    }
    let ids: Vec<String> = best.iter().map(|k| (k + 1).to_string()).collect();
    println!("{}\n{}", best.len(), ids.join(" "));
}
