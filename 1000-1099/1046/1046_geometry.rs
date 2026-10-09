use std::io::{self, Read};
use std::ops::{Add, Div, Mul, Sub};

const ROUNDING: f64 = 0.005;

#[derive(Clone, Copy)]
struct C(f64, f64);

impl Add for C {
    type Output = C;
    fn add(self, o: C) -> C {
        C(self.0 + o.0, self.1 + o.1)
    }
}

impl Sub for C {
    type Output = C;
    fn sub(self, o: C) -> C {
        C(self.0 - o.0, self.1 - o.1)
    }
}

impl Mul for C {
    type Output = C;
    fn mul(self, o: C) -> C {
        C(self.0 * o.0 - self.1 * o.1, self.0 * o.1 + self.1 * o.0)
    }
}

impl Div for C {
    type Output = C;
    fn div(self, o: C) -> C {
        let d = o.0 * o.0 + o.1 * o.1;
        C(
            (self.0 * o.0 + self.1 * o.1) / d,
            (self.1 * o.0 - self.0 * o.1) / d,
        )
    }
}

// a value that would print as -0.00 is printed as 0.00
fn clean(v: f64) -> f64 {
    if v.abs() < ROUNDING {
        0.0
    } else {
        v
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut num = || it.next().unwrap().parse::<f64>().unwrap();
    let apex: Vec<C> = (0..n).map(|_| C(num(), num())).collect();
    let turn: Vec<C> = (0..n)
        .map(|_| {
            let t = num().to_radians();
            C(t.cos(), t.sin())
        })
        .collect();
    // a step turns z around M[i] by its angle, z -> w z + (1 - w) M[i], and going
    // around the polygon composes the steps into z -> a z + b that fixes A[0]
    let one = C(1.0, 0.0);
    let (mut a, mut b) = (one, C(0.0, 0.0));
    for i in 0..n {
        a = turn[i] * a;
        b = turn[i] * b + (one - turn[i]) * apex[i];
    }
    // the angles never add up to a multiple of 360, so a != 1
    let mut z = b / (one - a);
    let mut out = String::new();
    for i in 0..n {
        out.push_str(&format!("{:.2} {:.2}\n", clean(z.0), clean(z.1)));
        z = apex[i] + turn[i] * (z - apex[i]);
    }
    print!("{}", out);
}
