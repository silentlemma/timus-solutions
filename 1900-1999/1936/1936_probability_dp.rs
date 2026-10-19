use std::io::{self, Read};

const GESTURE_COUNT: f64 = 3.0;
const OUTPUT_DIGITS: usize = 12;

fn expected_rounds(count: usize) -> f64 {
    let mut expected = vec![0.0; count + 1];
    let mut power_three = 1.0;
    let mut power_two = 2.0;
    for players in 2..=count {
        power_three *= GESTURE_COUNT;
        power_two *= 2.0;
        let mut weighted_successors = 0.0;
        let mut combination = 1.0;
        for survivors in 1..players {
            combination = combination * (players - survivors + 1) as f64 / survivors as f64;
            weighted_successors += combination * expected[survivors];
        }
        expected[players] = (power_three + weighted_successors) / (power_two - 2.0);
    }
    expected[count]
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let count = input.trim().parse::<usize>().unwrap();
    println!("{:.*}", OUTPUT_DIGITS, expected_rounds(count));
}
