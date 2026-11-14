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
// Days elapsed since September 1.
const MONTHS: [(&str, i32); 4] = [
    ("September", 0),
    ("October", 30),
    ("November", 61),
    ("December", 91),
];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let weekday = words.next().unwrap();
    let month = words.next().unwrap();
    let mut numbers = words.map(|word| word.parse::<i32>().unwrap());
    let (day, minimum, maximum) = (
        numbers.next().unwrap(),
        numbers.next().unwrap(),
        numbers.next().unwrap(),
    );
    let start = DAYS.iter().position(|&day| day == weekday).unwrap() + 1;
    let offset = MONTHS.iter().find(|&&(name, _)| name == month).unwrap().1;
    let week = DAYS.len() as i32;
    let training = offset + day - 2;
    let (regular, extra) = (training / week, training % week);
    // Extra weekdays occur once more than the others.
    for count in 1..=week {
        let low = 0.max(count - (week - extra)).max(minimum - count * regular);
        let high = count.min(extra).min(maximum - count * regular);
        if low <= high {
            println!("{count}");
            for i in (0..low).chain(extra..extra + count - low) {
                println!("{}", DAYS[(start + i as usize) % DAYS.len()]);
            }
            return;
        }
    }
    println!("Impossible");
}
