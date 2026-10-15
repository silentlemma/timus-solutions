use std::io::{self, Read};

const DIM: usize = 3;
const VERTICES: usize = 4;
const OPPOSITE: usize = 3;
// each face and the vertex opposite it
type Face = [usize; VERTICES];
const FACES: [Face; VERTICES] = [[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 3, 1], [1, 2, 3, 0]];

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let data: Vec<i64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let head = DIM * VERTICES;
    let v: Vec<&[i64]> = data[..head].chunks(DIM).collect();
    let n = data[head] as usize;
    let stars: Vec<&[i64]> = data[head + 1..head + 1 + DIM * n].chunks(DIM).collect();
    let normals: Vec<[i64; DIM]> = FACES
        .iter()
        .map(|face| {
            let diff = |p: usize, t: usize| v[face[p]][t] - v[face[0]][t];
            let u = [diff(1, 0), diff(1, 1), diff(1, 2)];
            let w = [diff(2, 0), diff(2, 1), diff(2, 2)];
            let c = [
                u[1] * w[2] - u[2] * w[1],
                u[2] * w[0] - u[0] * w[2],
                u[0] * w[1] - u[1] * w[0],
            ];
            // point the cross product, twice the face area long, away from the body
            let toward: i64 = (0..DIM).map(|t| c[t] * diff(OPPOSITE, t)).sum();
            if toward > 0 {
                [-c[0], -c[1], -c[2]]
            } else {
                c
            }
        })
        .collect();
    // a lit face gives area * intensity * cosine = (cross . star) / 2, and the
    // doubled total is a plain integer sum; the body is convex, so no shadows
    let total: i64 = normals
        .iter()
        .flat_map(|c| stars.iter().map(move |s| (c[0] * s[0] + c[1] * s[1] + c[2] * s[2]).max(0)))
        .sum();
    println!("{}.00000", total);
}
