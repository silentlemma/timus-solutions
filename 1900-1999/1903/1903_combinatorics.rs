use std::io::{self, Read};

const MODULUS: u64 = 1_000_000_007;

fn power(mut base: u64, mut exponent: u64) -> u64 {
    let mut result = 1;
    while exponent > 0 {
        if exponent & 1 != 0 {
            result = result * base % MODULUS;
        }
        base = base * base % MODULUS;
        exponent /= 2;
    }
    result
}

struct Binomial {
    factorial: Vec<u64>,
    inverse: Vec<u64>,
}

impl Binomial {
    fn new(maximum: usize) -> Self {
        let mut factorial = vec![1; maximum + 1];
        let mut inverse = vec![1; maximum + 1];
        for i in 1..=maximum {
            factorial[i] = factorial[i - 1] * i as u64 % MODULUS;
        }
        inverse[maximum] = power(factorial[maximum], MODULUS - 2);
        for i in (1..=maximum).rev() {
            inverse[i - 1] = inverse[i] * i as u64 % MODULUS;
        }
        Self { factorial, inverse }
    }

    fn choose(&self, total: usize, take: usize) -> u64 {
        if take > total {
            return 0;
        }
        self.factorial[total] * self.inverse[take] % MODULUS * self.inverse[total - take] % MODULUS
    }

    fn bad(&self, others: usize, selected: usize, pool: usize, threshold: usize) -> u64 {
        let mut result = 0;
        for count in threshold..=pool.min(selected - 1) {
            result += self.choose(pool, count) * self.choose(others - pool, selected - 1 - count)
                % MODULUS;
            result %= MODULUS;
        }
        result
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input
        .split_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let n = tokens.next().unwrap();
    let selected = tokens.next().unwrap();
    let classes: Vec<_> = (0..n).map(|_| tokens.next().unwrap()).collect();
    let identified = tokens.next().unwrap() - 1;
    let position = tokens.next().unwrap();
    let lower = classes.iter().filter(|&&x| x < classes[identified]).count();
    let greater = classes.iter().filter(|&&x| x > classes[identified]).count();
    let others = n - 1;
    let combinations = Binomial::new(others);
    let mut answer = combinations.choose(others, selected - 1);
    answer = (answer + MODULUS - combinations.bad(others, selected, lower, position)) % MODULUS;
    answer = (answer + MODULUS
        - combinations.bad(others, selected, greater, selected - position + 1))
        % MODULUS;
    println!("{}", answer);
}
