use std::io::{self, Read, Write};

fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn power(mut base: u64, mut exponent: u64, modulus: u64) -> u64 {
    let mut result = 1;
    while exponent > 0 {
        if exponent & 1 != 0 {
            result = result * base % modulus;
        }
        base = base * base % modulus;
        exponent >>= 1;
    }
    result
}

struct Group {
    prime: u64,
    full: u64,
    factors: Vec<u64>,
}

impl Group {
    fn new(prime: u64) -> Self {
        let full = prime - 1;
        let mut remaining = full;
        let mut factors = Vec::new();
        let mut factor = 2;
        while factor * factor <= remaining {
            if remaining % factor == 0 {
                factors.push(factor);
                while remaining % factor == 0 {
                    remaining /= factor;
                }
            }
            factor += 1;
        }
        if remaining > 1 {
            factors.push(remaining);
        }
        Self {
            prime,
            full,
            factors,
        }
    }

    // The known subgroup has index limit; only its missing factors need testing.
    fn subgroup_order(&self, value: u64, mut limit: u64) -> u64 {
        if value == 1 {
            return self.full / limit;
        }
        if value == self.prime - 1 {
            return self.full / gcd(limit, self.full / 2);
        }
        let mut order = self.full;
        for &factor in &self.factors {
            while limit % factor == 0 {
                let candidate = order / factor;
                if power(value, candidate, self.prime) != 1 {
                    break;
                }
                order = candidate;
                limit /= factor;
            }
        }
        order
    }
}

struct GcdTree {
    base: usize,
    full: u64,
    data: Vec<u64>,
}

impl GcdTree {
    fn new(values: &[u64], group: &Group) -> Self {
        let base = values.len().next_power_of_two();
        let mut data = vec![group.full; base * 2];
        for i in 1..values.len() {
            data[base + i] = group.full / group.subgroup_order(values[i], group.full);
        }
        for i in (1..base).rev() {
            data[i] = gcd(data[i * 2], data[i * 2 + 1]);
        }
        Self {
            base,
            full: group.full,
            data,
        }
    }

    fn set(&mut self, mut position: usize, mut value: u64) {
        position += self.base;
        if self.data[position] == value {
            return;
        }
        self.data[position] = value;
        position /= 2;
        while position > 0 {
            value = gcd(self.data[position * 2], self.data[position * 2 + 1]);
            if self.data[position] == value {
                break;
            }
            self.data[position] = value;
            position /= 2;
        }
    }

    fn query(&self, mut left: usize, mut right: usize) -> u64 {
        left += self.base;
        right += self.base;
        let mut result = self.full;
        while left < right && result > 1 {
            if left & 1 != 0 {
                result = gcd(result, self.data[left]);
                left += 1;
            }
            if right & 1 != 0 {
                right -= 1;
                result = gcd(result, self.data[right]);
            }
            left /= 2;
            right /= 2;
        }
        result
    }
}

struct Fenwick {
    prime: u64,
    data: Vec<u64>,
}

impl Fenwick {
    fn new(size: usize, prime: u64) -> Self {
        Self {
            prime,
            data: vec![1; size + 1],
        }
    }

    fn multiply(&mut self, mut position: usize, value: u64) {
        while position < self.data.len() {
            self.data[position] = self.data[position] * value % self.prime;
            position += position & position.wrapping_neg();
        }
    }

    fn prefix(&self, mut position: usize) -> u64 {
        let mut result = 1;
        while position > 0 {
            result = result * self.data[position] % self.prime;
            position &= position - 1;
        }
        result
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let prime: u64 = tokens.next().unwrap().parse().unwrap();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let q: usize = tokens.next().unwrap().parse().unwrap();
    let original: Vec<u64> = (0..n)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let group = Group::new(prime);
    let mut prefix = vec![1; n + 1];
    for i in 0..n {
        prefix[i + 1] = prefix[i] * original[i] % prime;
    }
    let mut difference = vec![1; n];
    let mut inverse = power(prefix[n], prime - 2, prime);
    // Batch inversion forms all adjacent ratios with one modular exponentiation.
    for i in (0..n).rev() {
        let inverse_value = inverse * prefix[i] % prime;
        if i + 1 < n {
            difference[i + 1] = original[i + 1] * inverse_value % prime;
        }
        inverse = inverse * original[i] % prime;
    }
    let mut indices = GcdTree::new(&difference, &group);
    let mut multipliers = Fenwick::new(n, prime);
    let mut output = String::new();
    for _ in 0..q {
        let kind: u64 = tokens.next().unwrap().parse().unwrap();
        let left = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
        let right: usize = tokens.next().unwrap().parse().unwrap();
        if kind == 1 {
            let value: u64 = tokens.next().unwrap().parse().unwrap();
            if value == 1 {
                continue;
            }
            multipliers.multiply(left + 1, value);
            if left > 0 {
                difference[left] = difference[left] * value % prime;
                let index = group.full / group.subgroup_order(difference[left], group.full);
                indices.set(left, index);
            }
            if right < n {
                let inverse_value = power(value, prime - 2, prime);
                multipliers.multiply(right + 1, inverse_value);
                difference[right] = difference[right] * inverse_value % prime;
                let index = group.full / group.subgroup_order(difference[right], group.full);
                indices.set(right, index);
            }
        } else {
            let index = indices.query(left + 1, right);
            let mut answer = group.full;
            if index > 1 {
                let value = original[left] * multipliers.prefix(left + 1) % prime;
                answer = group.subgroup_order(value, index);
            }
            output.push_str(&answer.to_string());
            output.push('\n');
        }
    }
    io::stdout().write_all(output.as_bytes()).unwrap();
}
