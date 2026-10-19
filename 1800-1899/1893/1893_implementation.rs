use std::io::{self, Read};

const PREMIUM_LAST: usize = 2;
const BUSINESS_LAST: usize = 20;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let seat = input.trim();
    let row: usize = seat[..seat.len() - 1].parse().unwrap();
    let letter = seat.as_bytes()[seat.len() - 1];
    let (right_window, aisles): (u8, &[u8]) = if row <= PREMIUM_LAST {
        (b'D', b"BC")
    } else if row <= BUSINESS_LAST {
        (b'F', b"BCDE")
    } else {
        (b'K', b"CDGH")
    };
    let answer = if letter == b'A' || letter == right_window {
        "window"
    } else if aisles.contains(&letter) {
        "aisle"
    } else {
        "neither"
    };
    println!("{answer}");
}
