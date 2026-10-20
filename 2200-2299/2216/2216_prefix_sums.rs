use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input
        .split_whitespace()
        .map(|value| value.parse::<usize>().unwrap());
    let floors = values.next().unwrap();
    let elevators = values.next().unwrap();
    let mut difference = vec![0_i32; floors + 1];
    for _ in 0..elevators {
        let left = values.next().unwrap();
        let right = values.next().unwrap();
        difference[left] += 1;
        difference[right] -= 1;
    }
    if floors == 1 {
        println!("{}", -1);
        return;
    }

    let mut crossing = 0;
    let mut answer = elevators as i32;
    // Every route crosses each gap; cover all elevators crossing the cheapest gap.
    for change in difference.iter().take(floors).skip(1) {
        crossing += change;
        answer = answer.min(crossing);
    }
    println!("{}", answer);
}
