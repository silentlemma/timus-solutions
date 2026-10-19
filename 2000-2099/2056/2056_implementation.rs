use std::io::{self, Read};

const LOW_MARK: i32 = 3;
const TOP_MARK: i32 = 5;
const DOUBLED_THRESHOLD: i32 = 9;

fn classify(count: i32, total: i32, lowest: i32) -> &'static str {
    if lowest == LOW_MARK {
        return "None";
    }
    if lowest == TOP_MARK {
        return "Named";
    }
    if 2 * total >= DOUBLED_THRESHOLD * count {
        return "High";
    }
    "Common"
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut fields = input
        .split_whitespace()
        .map(|word| word.parse::<i32>().unwrap());
    let count = fields.next().unwrap();
    let mut total = 0;
    let mut lowest = TOP_MARK;
    for _ in 0..count {
        let grade = fields.next().unwrap();
        total += grade;
        lowest = lowest.min(grade);
    }
    println!("{}", classify(count, total, lowest));
}
