use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    // a word is a run of letters; anything else ends it
    let words = text.split(|c: char| !c.is_ascii_lowercase());
    let (mut trams, mut trolleys) = (0, 0);
    for w in words {
        if w == "tram" {
            trams += 1;
        } else if w == "trolleybus" {
            trolleys += 1;
        }
    }
    let answer = if trams > trolleys {
        "Tram driver"
    } else if trolleys > trams {
        "Trolleybus driver"
    } else {
        "Bus driver"
    };
    println!("{}", answer);
}
