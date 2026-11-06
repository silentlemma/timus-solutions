use std::io::{self, Read};

const TEAM_SIZE: i32 = 3;

fn number(input: &mut impl Iterator<Item = u8>) -> i32 {
    let first = input.find(|byte| byte.is_ascii_digit()).unwrap();
    let mut value = i32::from(first - b'0');
    for byte in input.take_while(u8::is_ascii_digit) {
        value = value * 10 + i32::from(byte - b'0');
    }
    value
}

fn pairs(count: i32) -> i32 {
    count * (count - 1) / 2
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().bytes().map(Result::unwrap);
    let (total, special) = (number(&mut input), number(&mut input));
    let first = i32::from((0..special).any(|_| number(&mut input) == 1));
    let (s, o) = (special - first, total - special - (1 - first));
    // Leave at least one special person per remaining team.
    let maximum = special - total / TEAM_SIZE + 1;
    let mut answer = 0;
    if first == 1 && maximum >= 1 {
        answer += pairs(o);
    }
    if maximum > first {
        answer += s * o;
    }
    if maximum > first + 1 {
        answer += pairs(s);
    }
    println!("{}", answer);
}
