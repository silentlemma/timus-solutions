use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let mut next = || it.next().unwrap();
    let (a, b, c) = (next(), next(), next());
    let (x, y, z) = (next(), next(), next());
    // the dual lands first cover what the red and blue lands miss, and every
    // land left over pays for the mana of any color
    let missing = (x - a).max(0) + (y - b).max(0);
    if missing <= c && a + b + c >= x + y + z {
        println!("It is a kind of magic");
    } else {
        println!("There are no miracles in life");
    }
}
