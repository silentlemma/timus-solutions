use std::io::{self, Read};

const MAX_WEIGHT: usize = 130000;
const DECIMAL: usize = 10;

fn number(input: &mut impl Iterator<Item = u8>) -> usize {
    let mut value = 0;
    let mut started = false;
    for byte in input {
        if byte.is_ascii_digit() {
            value = value * DECIMAL + usize::from(byte - b'0');
            started = true;
        } else if started {
            break;
        }
    }
    value
}

fn gcd(mut a: usize, mut b: usize) -> usize {
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().bytes().map_while(Result::ok);
    let size = number(&mut input);
    let mut positions = vec![0u32; MAX_WEIGHT + 1];
    let (mut min_weight, mut max_weight) = (MAX_WEIGHT, 0);
    for i in 1..=size {
        let weight = number(&mut input);
        positions[weight] = i as u32;
        min_weight = min_weight.min(weight);
        max_weight = max_weight.max(weight);
    }
    let (mut rank, mut up, mut down) = (0, 0, 0);
    for &position in &positions[min_weight..=max_weight] {
        if position == 0 {
            continue;
        }
        let position = position as usize;
        rank += 1;
        up = gcd(up, position.abs_diff(rank));
        down = gcd(down, position.abs_diff(size + 1 - rank));
        if up == 1 && down == 1 {
            break;
        }
    }
    let step = if up == 0 || down == 0 {
        size
    } else {
        up.max(down)
    };
    println!("{}", step - 1);
}
