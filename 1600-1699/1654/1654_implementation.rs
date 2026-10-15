use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    // a letter equal to the one before it cancels that one: removing the
    // inserted pairs in any order leaves the same text
    let mut stack: Vec<u8> = Vec::new();
    for &c in text.trim().as_bytes() {
        if stack.last() == Some(&c) {
            stack.pop();
        } else {
            stack.push(c);
        }
    }
    println!("{}", String::from_utf8(stack).unwrap());
}
