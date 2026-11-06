use std::io::{self, Read};

const NAMES: [u8; 4] = *b"pVnT";
const SCALE: [i64; 4] = [1000, 1000, 8314, 8314];
const DECIMALS: i64 = 1_000_000;

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut tokens = text.split_ascii_whitespace();
    let mut value = [None; NAMES.len()];
    while let Some(name) = tokens.next() {
        let index = NAMES
            .iter()
            .position(|&item| item == name.as_bytes()[0])
            .unwrap();
        tokens.next(); // equals sign
        value[index] = Some(tokens.next().unwrap().parse::<i64>().unwrap());
    }
    let missing = value.iter().position(Option::is_none).unwrap();
    // The missing quantity's coefficient comes from its own side of pV = nRT.
    let divisor = SCALE[missing] * value[missing ^ 1].unwrap();
    let other = missing ^ 2;
    let numerator = SCALE[other] * value[other].unwrap() * value[other ^ 1].unwrap();
    if divisor == 0 && numerator == 0 {
        println!("undefined");
    } else if divisor == 0 || (numerator == 0 && missing % 2 == 1) {
        println!("error");
    } else {
        let rounded = (numerator * DECIMALS + divisor / 2) / divisor;
        println!(
            "{} = {}.{:06}",
            char::from(NAMES[missing]),
            rounded / DECIMALS,
            rounded % DECIMALS
        );
    }
}
