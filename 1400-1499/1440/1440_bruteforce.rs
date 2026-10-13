use std::io::{self, Read};

const DAYS: [&str; 7] = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
];
// the months and the days from September 1 to the first day of each of them
const MONTHS: [(&str, usize); 4] = [
    ("September", 0),
    ("October", 30),
    ("November", 61),
    ("December", 91),
];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace();
    let (first, month) = (it.next().unwrap(), it.next().unwrap());
    let mut number = || it.next().unwrap().parse::<usize>().unwrap();
    let (day, a, b) = (number(), number(), number());
    let week = DAYS.len();
    let start = DAYS.iter().position(|&d| d == first).unwrap();
    let offset = MONTHS.iter().find(|m| m.0 == month).unwrap().1;
    let matchday = offset + day - 1; // September 1 is day 0
    let mut count = vec![0usize; week]; // training days from September 2 to the eve of the match
    for i in 1..matchday {
        count[(start + i) % week] += 1;
    }
    for mask in 1..1usize << week {
        let chosen: Vec<usize> = (0..week).filter(|d| mask >> d & 1 == 1).collect();
        let total: usize = chosen.iter().map(|&d| count[d]).sum();
        if a <= total && total <= b {
            println!("{}", chosen.len());
            for d in chosen {
                println!("{}", DAYS[d]);
            }
            return;
        }
    }
    println!("Impossible");
}
