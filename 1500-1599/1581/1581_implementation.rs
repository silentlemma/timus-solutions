use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let numbers: Vec<u32> = words.take(n).map(|w| w.parse().unwrap()).collect();
    // each run of equal numbers is said as its length and then the number
    let mut out = Vec::new();
    let mut i = 0;
    while i < n {
        let mut j = i;
        while j < n && numbers[j] == numbers[i] {
            j += 1;
        }
        out.push((j - i).to_string());
        out.push(numbers[i].to_string());
        i = j;
    }
    println!("{}", out.join(" "));
}
