use std::io::{self, Read};

fn fits(first: u128, second: u128, height: u128, circumference: u128) -> bool {
    if first > circumference {
        return false;
    }
    if second <= height {
        return true;
    }
    let area = first * second;
    let capacity = height * circumference;
    if capacity < area {
        return false;
    }
    let residual = capacity - area;
    residual * residual >= first * first * (circumference * circumference - first * first)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let width: u128 = tokens.next().unwrap().parse().unwrap();
    let height: u128 = tokens.next().unwrap().parse().unwrap();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let mut output = String::new();
    for _ in 0..count {
        let cylinder_height: u128 = tokens.next().unwrap().parse().unwrap();
        let circumference: u128 = tokens.next().unwrap().parse().unwrap();
        let possible = fits(width, height, cylinder_height, circumference)
            || fits(height, width, cylinder_height, circumference);
        output.push_str(if possible {
            "Block the hole\n"
        } else {
            "Too small\n"
        });
    }
    print!("{}", output);
}
