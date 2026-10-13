use std::io::{self, Read};

const TINY: f64 = 1e-9; // a torque this small is no torque at all
const TURN: f64 = 360.0;
const HALF_UNIT: f64 = 5e-9; // half of the last printed digit

const DIM: usize = 3;

type Vec3 = [f64; DIM];

fn unit(lon: f64, lat: f64) -> Vec3 {
    let (lon, lat) = (lon.to_radians(), lat.to_radians());
    [lat.cos() * lon.cos(), lat.cos() * lon.sin(), lat.sin()]
}

fn cross(a: Vec3, b: Vec3) -> Vec3 {
    [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ]
}

fn dot(a: Vec3, b: Vec3) -> f64 {
    a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
}

fn angles(v: Vec3) -> (f64, f64) {
    let length = dot(v, v).sqrt();
    let lat = (v[2] / length).max(-1.0).min(1.0).asin().to_degrees();
    let mut lon = (v[1].atan2(v[0]).to_degrees() + TURN) % TURN;
    if lon >= TURN - HALF_UNIT {
        lon = 0.0; // it would print as 360
    }
    (lon + 0.0, lat + 0.0) // no negative zeros
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<f64>().unwrap());
    let mut next = || it.next().unwrap();
    let radius = next();
    next(); // the mass does not matter
    let (mast, thrust, count) = (next(), next(), next() as usize);
    let arm = radius + mast; // the engines sit on masts above the surface
    let mut torque: Vec3 = [0.0; DIM];
    for _ in 0..count {
        let (lon, lat, dlon, dlat) = (next(), next(), next(), next());
        let t = cross(unit(lon, lat), unit(dlon, dlat));
        for k in 0..DIM {
            torque[k] += arm * thrust * t[k];
        }
    }
    let size = dot(torque, torque).sqrt();
    if size < TINY {
        println!("{:.8} {:.8} {:.8} {:.8} {:.8}", 0.0, 0.0, 0.0, 0.0, 0.0);
        return;
    }
    // a force f at p turns the station by p x f, at most |p| |f|; so the
    // least thrust |T| / |p| needs p across the torque T and f = p x T / |p|^2
    let axis = [torque[0] / size, torque[1] / size, torque[2] / size];
    let axes: [Vec3; DIM] = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]];
    let mut pick = axes[0];
    for &e in axes.iter() {
        if dot(e, axis).abs() < dot(pick, axis).abs() {
            pick = e;
        }
    }
    let d = dot(pick, axis);
    let place = [
        pick[0] - d * axis[0],
        pick[1] - d * axis[1],
        pick[2] - d * axis[2],
    ];
    let push = cross(place, torque);
    let (lon, lat) = angles(place);
    let (dlon, dlat) = angles(push);
    println!(
        "{:.8} {:.8} {:.8} {:.8} {:.8}",
        lon,
        lat,
        dlon,
        dlat,
        size / arm
    );
}
