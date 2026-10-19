use std::io::{self, Read};

fn can_crash(
    length: i64,
    height: i64,
    gate_height: i64,
    speed: i64,
    gate_speed: i64,
    deceleration: i64,
) -> bool {
    let stopping_bound = gate_speed * (speed * speed + 2 * deceleration * length);
    let passing_bound = 2 * deceleration * speed * (gate_height - height);
    stopping_bound >= passing_bound
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input
        .split_whitespace()
        .map(|word| word.parse::<i64>().unwrap());
    let length = values.next().unwrap();
    let height = values.next().unwrap();
    let gate_height = values.next().unwrap();
    let speed = values.next().unwrap();
    let gate_speed = values.next().unwrap();
    let deceleration = values.next().unwrap();
    let crash = can_crash(length, height, gate_height, speed, gate_speed, deceleration);
    println!("{}", if crash { "Crash" } else { "Safe" });
}
