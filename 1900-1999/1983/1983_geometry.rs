use std::io::{self, Read};

const DIMENSIONS: usize = 3;
const RADIUS: i64 = 100;
type IntVector = [i64; DIMENSIONS];

fn dot(a: IntVector, b: IntVector) -> i64 {
    a.iter().zip(b.iter()).map(|(x, y)| x * y).sum()
}

fn cross(a: IntVector, b: IntVector) -> IntVector {
    [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ]
}

fn area(points: [IntVector; DIMENSIONS]) -> f64 {
    let mut first = [0; DIMENSIONS];
    let mut second = [0; DIMENSIONS];
    for i in 0..DIMENSIONS {
        first[i] = points[1][i] - points[0][i];
        second[i] = points[2][i] - points[0][i];
    }
    let normal = cross(first, second);
    let norm_squared = dot(normal, normal);
    let offset = dot(normal, points[0]);
    let residual = RADIUS * RADIUS * norm_squared - offset * offset;
    if residual <= 0 {
        return 0.0;
    }
    let radius_squared = residual as f64 / norm_squared as f64;
    let mut axis = [0.0; DIMENSIONS];
    let mut unit_normal = [0.0; DIMENSIONS];
    for i in 0..DIMENSIONS {
        axis[i] = first[i] as f64 / (dot(first, first) as f64).sqrt();
        unit_normal[i] = normal[i] as f64 / (norm_squared as f64).sqrt();
    }
    let other = [
        unit_normal[1] * axis[2] - unit_normal[2] * axis[1],
        unit_normal[2] * axis[0] - unit_normal[0] * axis[2],
        unit_normal[0] * axis[1] - unit_normal[1] * axis[0],
    ];
    let mut projected = [[0.0; 2]; DIMENSIONS];
    for i in 0..DIMENSIONS {
        for j in 0..DIMENSIONS {
            projected[i][0] += points[i][j] as f64 * axis[j];
            projected[i][1] += points[i][j] as f64 * other[j];
        }
    }
    let mut total = 0.0;
    for i in 0..DIMENSIONS {
        let following = (i + 1) % DIMENSIONS;
        let mut delta = [0; DIMENSIONS];
        for j in 0..DIMENSIONS {
            delta[j] = points[following][j] - points[i][j];
        }
        let quadratic = dot(delta, delta);
        let linear = dot(points[i], delta);
        let constant = dot(points[i], points[i]) - RADIUS * RADIUS;
        let discriminant = linear * linear - quadratic * constant;
        let mut cuts = vec![0.0, 1.0];
        let (mut low, mut high) = (1.0, 0.0);
        if discriminant > 0 {
            let stable = -(linear as f64) - (discriminant as f64).sqrt().copysign(linear as f64);
            low = stable / quadratic as f64;
            high = constant as f64 / stable;
            if low > high {
                std::mem::swap(&mut low, &mut high);
            }
            if low > 0.0 && low < 1.0 {
                cuts.push(low);
            }
            if high > 0.0 && high < 1.0 {
                cuts.push(high);
            }
        }
        cuts.sort_by(|a, b| a.partial_cmp(b).unwrap());
        let (x, y) = (projected[i][0], projected[i][1]);
        let (dx, dy) = (projected[following][0] - x, projected[following][1] - y);
        for pair in cuts.windows(2) {
            let (left, right) = (pair[0], pair[1]);
            let (ax, ay) = (x + left * dx, y + left * dy);
            let (bx, by) = (x + right * dx, y + right * dy);
            let signed = ax * by - ay * bx;
            let middle = (left + right) / 2.0;
            total += if low < middle && middle < high {
                signed
            } else {
                radius_squared * signed.atan2(ax * bx + ay * by)
            };
        }
    }
    total.abs() / 2.0
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let mut points = [[0; DIMENSIONS]; DIMENSIONS];
    for point in &mut points {
        for value in point {
            *value = tokens.next().unwrap().parse().unwrap();
        }
    }
    println!("{:.10}", area(points));
}
