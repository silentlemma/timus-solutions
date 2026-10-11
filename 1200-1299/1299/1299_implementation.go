package main

import "fmt"

const (
	step     = 100 // energy spent on one move or turn, at most
	shot     = 20  // ammunition spent on one shot, at most
	perEnemy = 20  // ammunition the defence wants for each enemy
)

const (
	strength  = 3  // the attack needs three times the strength of the enemy
	aim       = 5  // the angle within which a guard, defence or retreat fires
	chargeAim = 10 // the angle within which an advance fires
)

const (
	course   = 20 // the patrol turns when it is off course by more than this
	halfTurn = 180
)

var energy, ammo, enemies, enemyPower, angle int

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func move(direction string) string {
	return fmt.Sprintf("%s %d", direction, min(step, energy))
}

func fire() string {
	return fmt.Sprintf("FIRE %d", min(shot, ammo))
}

// positive angles lie to the left
func turn(towards int) string {
	if towards > 0 {
		return move("LEFT")
	}
	return move("RIGHT")
}

func guard() string {
	if enemies == 0 {
		return "STOP"
	}
	if abs(angle) < aim {
		return fire()
	}
	return turn(angle)
}

func retreat() string {
	if enemies == 0 || abs(angle) >= aim {
		return move("BACKWARD")
	}
	return fire()
}

func defence() string {
	if enemies*perEnemy >= ammo {
		return retreat()
	}
	return guard()
}

func attack(own, ownPower int) string {
	if own*ownPower <= enemies*enemyPower*strength {
		return retreat()
	}
	if enemies == 0 || abs(angle) >= chargeAim {
		return move("FRONT")
	}
	return fire()
}

func patrol(deviation int) string {
	if enemies > 0 {
		return defence()
	}
	// the robot may drive either way, so it heads for the point with
	// its front or its back, whichever needs the smaller turn
	back := deviation + halfTurn
	if deviation > 0 {
		back = deviation - halfTurn
	}
	if abs(back) < abs(deviation) {
		if abs(back) <= course {
			return move("BACKWARD")
		}
		return turn(back)
	}
	if abs(deviation) <= course {
		return move("FRONT")
	}
	return turn(deviation)
}

func main() {
	var mode string
	fmt.Scan(&energy, &ammo, &mode, &enemies, &enemyPower, &angle)
	switch mode {
	case "G":
		fmt.Println(guard())
	case "D":
		fmt.Println(defence())
	case "A":
		var own, ownPower int
		fmt.Scan(&own, &ownPower)
		fmt.Println(attack(own, ownPower))
	default:
		var deviation int
		fmt.Scan(&deviation)
		fmt.Println(patrol(deviation))
	}
}
