use std::collections::BTreeSet;
use std::io;

const BASES: [u64; 12] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37];
const BATCH: usize = 64;
const MAX_CYCLE: usize = 1 << 16;

fn multiply(a: u64, b: u64, n: u64) -> u64 {
    (u128::from(a) * u128::from(b) % u128::from(n)) as u64
}

fn prime(n: u64) -> bool {
    for p in BASES {
        if n % p == 0 {
            return n == p;
        }
    }
    let twos = (n - 1).trailing_zeros();
    let odd = (n - 1) >> twos;
    for mut a in BASES {
        let mut value = 1;
        let mut exponent = odd;
        while exponent != 0 {
            if exponent & 1 != 0 {
                value = multiply(value, a, n);
            }
            a = multiply(a, a, n);
            exponent >>= 1;
        }
        if value == 1 {
            continue;
        }
        for _ in 1..twos {
            if value == n - 1 {
                break;
            }
            value = multiply(value, value, n);
        }
        if value != n - 1 {
            return false;
        }
    }
    true
}

fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn divisor(n: u64) -> u64 {
    for c in 1.. {
        let step = |a| (multiply(a, a, n) + c) % n;
        let (mut x, mut y, mut saved, mut factor) = (0, 2, 0, 1);
        let mut size = 1;
        while size <= MAX_CYCLE && factor == 1 {
            x = y;
            for _ in 0..size {
                y = step(y);
            }
            for start in (0..size).step_by(BATCH) {
                saved = y;
                let mut product = 1;
                for _ in 0..BATCH.min(size - start) {
                    y = step(y);
                    product = multiply(product, x.abs_diff(y), n);
                }
                factor = gcd(product, n);
                if factor != 1 {
                    break;
                }
            }
            size *= 2;
        }
        if factor == n {
            loop {
                saved = step(saved);
                factor = gcd(x.abs_diff(saved), n);
                if factor != 1 {
                    break;
                }
            }
        }
        if factor > 1 && factor < n {
            return factor;
        }
    }
    unreachable!()
}

fn square(n: u64) -> bool {
    let root = (n as f64).sqrt() as u64;
    root * root == n || (root + 1) * (root + 1) == n
}

const POWER_OF_FOUR: u64 = 4;
const LEGENDRE_MODULUS: u64 = 8;
const LEGENDRE_RESIDUE: u64 = 7;
const TWO_SQUARE_OBSTRUCTION: u64 = 3;
const THREE_SQUARES: u8 = 3;
const FOUR_SQUARES: u8 = 4;

fn collect(n: u64, odd: &mut BTreeSet<u64>) {
    if square(n) {
        return;
    }
    if prime(n) {
        if n % POWER_OF_FOUR == TWO_SQUARE_OBSTRUCTION && !odd.remove(&n) {
            odd.insert(n);
        }
        return;
    }
    let part = divisor(n);
    collect(part, odd);
    collect(n / part, odd);
}

fn solve(mut n: u64) -> u8 {
    if square(n) {
        return 1;
    }
    while n % POWER_OF_FOUR == 0 {
        n /= POWER_OF_FOUR;
    }
    if n % LEGENDRE_MODULUS == LEGENDRE_RESIDUE {
        return FOUR_SQUARES;
    }
    if n % 2 == 0 {
        n /= 2;
    }
    if n % POWER_OF_FOUR == TWO_SQUARE_OBSTRUCTION {
        return THREE_SQUARES;
    }
    for p in BASES {
        let mut odd = false;
        while n % p == 0 {
            n /= p;
            odd = !odd;
        }
        if odd && p % POWER_OF_FOUR == TWO_SQUARE_OBSTRUCTION {
            return THREE_SQUARES;
        }
    }
    let mut odd = BTreeSet::new();
    collect(n, &mut odd);
    if odd.is_empty() {
        2
    } else {
        THREE_SQUARES
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    println!("{}", solve(input.trim().parse().unwrap()));
}
