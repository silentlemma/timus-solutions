use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let word = input.split_ascii_whitespace().next().unwrap().as_bytes();
    // the added part is never empty, so look for the longest palindromic
    // suffix of the word without its first letter
    let tail = &word[1..];
    let mut text: Vec<u8> = tail.iter().rev().cloned().collect();
    text.push(b'#');
    text.extend_from_slice(tail);
    let mut border = vec![0usize; text.len()];
    for i in 1..text.len() {
        let mut k = border[i - 1];
        while k > 0 && text[i] != text[k] {
            k = border[k - 1];
        }
        if text[i] == text[k] {
            k += 1;
        }
        border[i] = k;
    }
    let longest = if tail.is_empty() {
        0
    } else {
        border[text.len() - 1]
    };
    let mut out = word.to_vec();
    out.extend(word[..word.len() - longest].iter().rev());
    println!("{}", String::from_utf8(out).unwrap());
}
