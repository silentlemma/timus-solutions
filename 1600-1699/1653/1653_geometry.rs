use std::io::{self, Read};

const TINY: f64 = 1e-14;
const SAME: f64 = 1e-7; // equal edge lengths up to rounding
const DIM: usize = 3;
const PHI: f64 = 1.618_033_988_749_895; // the golden ratio

type Vec3 = [f64; DIM];
type Mat = [Vec3; DIM]; // rows

fn dot(a: Vec3, b: Vec3) -> f64 {
    a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
}

fn unit(v: Vec3) -> Vec3 {
    let n = dot(v, v).sqrt();
    [v[0] / n, v[1] / n, v[2] / n]
}

fn cross(a: Vec3, b: Vec3) -> Vec3 {
    [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
}

fn dist(a: Vec3, b: Vec3) -> f64 {
    let d = [a[0] - b[0], a[1] - b[1], a[2] - b[2]];
    dot(d, d).sqrt()
}

fn apply(m: &Mat, v: Vec3) -> Vec3 {
    [dot(m[0], v), dot(m[1], v), dot(m[2], v)]
}

fn compose(a: &Mat, b: &Mat) -> Mat {
    let mut r = [[0.0; DIM]; DIM];
    for i in 0..DIM {
        for j in 0..DIM {
            r[i][j] = (0..DIM).map(|k| a[i][k] * b[k][j]).sum();
        }
    }
    r
}

/// rotation by angle around axis, right-handed
fn rotation(axis: Vec3, angle: f64) -> Mat {
    let [x, y, z] = unit(axis);
    let (c, s) = (angle.cos(), angle.sin());
    let t = 1.0 - c;
    [
        [t * x * x + c, t * x * y - s * z, t * x * z + s * y],
        [t * x * y + s * z, t * y * y + c, t * y * z - s * x],
        [t * x * z - s * y, t * y * z + s * x, t * z * z + c],
    ]
}

fn solid(name: &str) -> Vec<Vec3> {
    let phi = PHI;
    let signs = [-1.0, 1.0];
    let mut pts: Vec<Vec3> = Vec::new();
    match name {
        "tetrahedron" => {
            pts.extend_from_slice(&[[1.0, 1.0, 1.0], [1.0, -1.0, -1.0], [-1.0, 1.0, -1.0]]);
            pts.push([-1.0, -1.0, 1.0]);
        }
        "octahedron" => {
            for i in 0..DIM {
                for s in [1.0, -1.0].iter() {
                    let mut p = [0.0; DIM];
                    p[i] = *s;
                    pts.push(p);
                }
            }
        }
        "icosahedron" => {
            for &a in &signs {
                for &b in &signs {
                    pts.push([0.0, a, b * phi]);
                    pts.push([a, b * phi, 0.0]);
                    pts.push([b * phi, 0.0, a]);
                }
            }
        }
        _ => {
            for &x in &signs {
                for &y in &signs {
                    for &z in &signs {
                        pts.push([x, y, z]);
                    }
                }
            }
            if name == "dodecahedron" {
                for &a in &signs {
                    for &b in &signs {
                        pts.push([0.0, a / phi, b * phi]);
                        pts.push([a / phi, b * phi, 0.0]);
                        pts.push([b * phi, 0.0, a / phi]);
                    }
                }
            }
        }
    }
    pts.into_iter().map(unit).collect()
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let mut guns = solid(words.next().unwrap());
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut edge = f64::MAX;
    for &a in &guns {
        for &b in &guns {
            let d = dist(a, b);
            if d > SAME {
                edge = edge.min(d);
            }
        }
    }
    // turn the solid so that one gun points along z and a neighbour lies in
    // the half-plane x >= 0 of Oxz; any choice is the same up to symmetry
    let z = guns[0];
    let near = *guns.iter().find(|&&g| (dist(g, z) - edge).abs() < SAME).unwrap();
    let along = dot(near, z);
    let x = unit([near[0] - along * z[0], near[1] - along * z[1], near[2] - along * z[2]]);
    let y = cross(z, x);
    for g in guns.iter_mut() {
        *g = unit([dot(*g, x), dot(*g, y), dot(*g, z)]);
    }
    let mut turn: Mat = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]];
    let mut total = 0.0;
    for _ in 0..n {
        let mut v = [0.0; DIM];
        for c in v.iter_mut() {
            *c = words.next().unwrap().parse().unwrap();
        }
        let target = unit([-v[0], -v[1], -v[2]]); // the ship comes from there
        let mut gun = apply(&turn, guns[0]);
        for &g in &guns {
            let turned = apply(&turn, g);
            if dot(turned, target) > dot(gun, target) {
                gun = turned;
            }
        }
        let angle = dot(gun, target).clamp(-1.0, 1.0).acos();
        total += angle;
        let axis = cross(gun, target);
        if angle > TINY && dot(axis, axis).sqrt() > TINY {
            // the shortest turn: around the axis normal to both directions
            turn = compose(&rotation(axis, angle), &turn);
        }
    }
    println!("{:.5}", total);
}
