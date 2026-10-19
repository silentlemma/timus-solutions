use std::io::{self, Read};

const ROLE_COUNT: usize = 3;

fn transform(sentence: &str) -> String {
    let lowered = sentence.to_ascii_lowercase();
    let opening = b"{([";
    let closing = b"})]";
    let mut results = Vec::new();
    for clause in lowered.split(',') {
        let bytes = clause.as_bytes();
        let mut phrases = vec![String::new(); ROLE_COUNT];
        let mut prefix = String::new();
        let mut i = 0;
        while i < bytes.len() {
            if let Some(role) = opening.iter().position(|&c| c == bytes[i]) {
                let mut end = i + 1;
                while bytes[end] != closing[role] {
                    end += 1;
                }
                phrases[role] = clause[i + 1..end].to_owned();
                i = end + 1;
            } else if bytes[i].is_ascii_lowercase() {
                let begin = i;
                while i < bytes.len() && bytes[i].is_ascii_lowercase() {
                    i += 1;
                }
                prefix = clause[begin..i].to_owned();
            } else {
                i += 1;
            }
        }
        let phrase = phrases.join(" ");
        results.push(if prefix.is_empty() {
            phrase
        } else {
            prefix + " " + &phrase
        });
    }
    let mut answer = results.join(", ").into_bytes();
    answer[0].make_ascii_uppercase();
    String::from_utf8(answer).unwrap()
}
fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    println!("{}", transform(input.trim()));
}
