use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|x| x.parse::<i32>().unwrap());
    let k = it.next().unwrap();
    let n = it.next().unwrap() as usize;
    // the light lets k cars through, but never more than are waiting
    let jam = it.take(n).fold(0, |jam, cars| (jam + cars - k).max(0));
    println!("{}", jam);
}
