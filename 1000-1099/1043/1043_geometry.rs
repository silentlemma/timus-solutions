use std::io::{self, Read};

// all comparisons are exact: the center is (ux / d, uy / d) and the radius
// times d is the square root of rho2
struct Circle {
    d: i128,
    rho2: i128,
}

impl Circle {
    // the sign of alpha - gamma * sqrt(rho2)
    fn sign_minus(&self, alpha: i128, gamma: i128) -> i128 {
        if gamma == 0 {
            alpha.signum()
        } else if gamma > 0 {
            if alpha <= 0 {
                -1
            } else {
                (alpha * alpha - gamma * gamma * self.rho2).signum()
            }
        } else if alpha >= 0 {
            1
        } else {
            (gamma * gamma * self.rho2 - alpha * alpha).signum()
        }
    }

    fn at_least_rho(&self, t: i128) -> bool {
        t >= 0 && t * t >= self.rho2
    }

    // the smallest integer k with k >= (u + sqrt(rho2)) / d
    fn ceil_plus(&self, u: i128) -> i128 {
        let estimate = (u as f64 + (self.rho2 as f64).sqrt()) / self.d as f64;
        let mut k = estimate.floor() as i128 - 2;
        while !self.at_least_rho(k * self.d - u) {
            k += 1;
        }
        k
    }

    // the largest integer k with k <= (u - sqrt(rho2)) / d
    fn floor_minus(&self, u: i128) -> i128 {
        let estimate = (u as f64 - (self.rho2 as f64).sqrt()) / self.d as f64;
        let mut k = estimate.ceil() as i128 + 2;
        while !self.at_least_rho(u - k * self.d) {
            k -= 1;
        }
        k
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i128>().unwrap());
    let mut next = || it.next().unwrap();
    let (ax, ay) = (next(), next());
    let (bx, by) = (next(), next());
    let (cx, cy) = (next(), next());
    let (a2, b2, c2) = (ax * ax + ay * ay, bx * bx + by * by, cx * cx + cy * cy);
    let mut d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by));
    let mut ux = a2 * (by - cy) + b2 * (cy - ay) + c2 * (ay - by);
    let mut uy = a2 * (cx - bx) + b2 * (ax - cx) + c2 * (bx - ax);
    if d < 0 {
        d = -d;
        ux = -ux;
        uy = -uy;
    }
    let rho2 = (ax * d - ux).pow(2) + (ay * d - uy).pow(2);
    let circle = Circle { d, rho2 };
    // an extreme point of the circle is on the arc when it lies on the same side
    // of the chord AB as C; side(P) * d = alpha - gamma * sqrt(rho2)
    let (ex, ey) = (bx - ax, by - ay);
    let side_c = (ex * (cy - ay) - ey * (cx - ax)).signum();
    let alpha = ex * (uy - ay * d) - ey * (ux - ax * d);
    let (mut lo_x, mut hi_x) = (ax.min(bx), ax.max(bx));
    let (mut lo_y, mut hi_y) = (ay.min(by), ay.max(by));
    if circle.sign_minus(alpha, ey) == side_c {
        hi_x = hi_x.max(circle.ceil_plus(ux));
    }
    if circle.sign_minus(alpha, -ey) == side_c {
        lo_x = lo_x.min(circle.floor_minus(ux));
    }
    if circle.sign_minus(alpha, -ex) == side_c {
        hi_y = hi_y.max(circle.ceil_plus(uy));
    }
    if circle.sign_minus(alpha, ex) == side_c {
        lo_y = lo_y.min(circle.floor_minus(uy));
    }
    println!("{}", (hi_x - lo_x) * (hi_y - lo_y));
}
