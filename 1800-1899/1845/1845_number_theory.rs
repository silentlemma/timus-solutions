use std::io::{self, Read};

#[derive(Clone, Copy, PartialEq)]
struct Gauss {
    re: i64,
    im: i64,
}

fn sub(a: Gauss, b: Gauss) -> Gauss {
    Gauss { re: a.re - b.re, im: a.im - b.im }
}

fn mul(a: Gauss, b: Gauss) -> Gauss {
    Gauss { re: a.re * b.re - a.im * b.im, im: a.re * b.im + a.im * b.re }
}

// x / y rounded to the nearest Gaussian integer in both parts
fn quotient(x: Gauss, y: Gauss) -> Gauss {
    let n = y.re * y.re + y.im * y.im;
    let re = x.re * y.re + x.im * y.im;
    let im = x.im * y.re - x.re * y.im;
    Gauss { re: (2 * re + n).div_euclid(2 * n), im: (2 * im + n).div_euclid(2 * n) }
}

// what is left of x after taking away the nearest multiple of p: its norm
// is at most half the norm of p
fn remainder(x: Gauss, p: Gauss) -> Gauss {
    sub(x, mul(p, quotient(x, p)))
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|v| v.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let mut a: Vec<Vec<Gauss>> = (0..n)
        .map(|_| {
            (0..n).map(|_| Gauss { re: it.next().unwrap(), im: it.next().unwrap() }).collect()
        })
        .collect();
    let p = Gauss { re: it.next().unwrap(), im: it.next().unwrap() };
    for row in a.iter_mut() {
        for x in row.iter_mut() {
            *x = remainder(*x, p);
        }
    }
    let zero = Gauss { re: 0, im: 0 };
    // elimination modulo p: the Euclidean algorithm on the Gaussian
    // integers clears each column below the diagonal with row operations,
    // which keep the determinant; the entries of the column only shrink
    let mut det = Gauss { re: 1, im: 0 };
    for k in 0..n {
        for i in k + 1..n {
            while a[i][k] != zero {
                let q = quotient(a[k][k], a[i][k]);
                a[k][k] = sub(a[k][k], mul(q, a[i][k]));
                for j in k + 1..n {
                    a[k][j] = remainder(sub(a[k][j], mul(q, a[i][j])), p);
                }
                a.swap(k, i);
                det = Gauss { re: -det.re, im: -det.im };
            }
        }
        det = remainder(mul(det, a[k][k]), p);
    }
    println!("{} {}", det.re, det.im);
}
