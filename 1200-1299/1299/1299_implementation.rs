use std::io::{self, Read};

const STEP: i64 = 100; // energy spent on one move or turn, at most
const SHOT: i64 = 20; // ammunition spent on one shot, at most

const PER_ENEMY: i64 = 20; // ammunition the defence wants for each enemy
const STRENGTH: i64 = 3; // the attack needs three times the strength of the enemy

const AIM: i64 = 5; // the angle within which a guard, defence or retreat fires
const CHARGE_AIM: i64 = 10; // the angle within which an advance fires
const COURSE: i64 = 20; // the patrol turns when it is off course by more than this

const HALF_TURN: i64 = 180;

struct Robot {
    energy: i64,
    ammo: i64,
    enemies: i64,
    enemy_power: i64,
    angle: i64,
}

impl Robot {
    fn step(&self, direction: &str) -> String {
        format!("{} {}", direction, STEP.min(self.energy))
    }

    fn fire(&self) -> String {
        format!("FIRE {}", SHOT.min(self.ammo))
    }

    // positive angles lie to the left
    fn turn(&self, towards: i64) -> String {
        self.step(if towards > 0 { "LEFT" } else { "RIGHT" })
    }

    fn guard(&self) -> String {
        if self.enemies == 0 {
            "STOP".to_string()
        } else if self.angle.abs() < AIM {
            self.fire()
        } else {
            self.turn(self.angle)
        }
    }

    fn retreat(&self) -> String {
        if self.enemies == 0 || self.angle.abs() >= AIM {
            self.step("BACKWARD")
        } else {
            self.fire()
        }
    }

    fn defence(&self) -> String {
        if self.enemies * PER_ENEMY >= self.ammo {
            self.retreat()
        } else {
            self.guard()
        }
    }

    fn attack(&self, own: i64, own_power: i64) -> String {
        if own * own_power <= self.enemies * self.enemy_power * STRENGTH {
            self.retreat()
        } else if self.enemies == 0 || self.angle.abs() >= CHARGE_AIM {
            self.step("FRONT")
        } else {
            self.fire()
        }
    }

    fn patrol(&self, deviation: i64) -> String {
        if self.enemies > 0 {
            return self.defence();
        }
        // the robot may drive either way, so it heads for the point with
        // its front or its back, whichever needs the smaller turn
        let back = if deviation > 0 {
            deviation - HALF_TURN
        } else {
            deviation + HALF_TURN
        };
        if back.abs() < deviation.abs() {
            if back.abs() <= COURSE {
                self.step("BACKWARD")
            } else {
                self.turn(back)
            }
        } else if deviation.abs() <= COURSE {
            self.step("FRONT")
        } else {
            self.turn(deviation)
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let mut number = || words.next().unwrap().to_string();
    let energy = number().parse().unwrap();
    let ammo = number().parse().unwrap();
    let mode = number();
    let enemies = number().parse().unwrap();
    let enemy_power = number().parse().unwrap();
    let angle = number().parse().unwrap();
    let robot = Robot {
        energy,
        ammo,
        enemies,
        enemy_power,
        angle,
    };
    let command = match mode.as_str() {
        "G" => robot.guard(),
        "D" => robot.defence(),
        "A" => {
            let own = number().parse().unwrap();
            let own_power = number().parse().unwrap();
            robot.attack(own, own_power)
        }
        _ => robot.patrol(number().parse().unwrap()),
    };
    println!("{}", command);
}
