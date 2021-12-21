package robot

import (
	"fmt"
	"os"
)

type Robot struct {
	posX                  int
	posY                  int
	invert                bool
	drunk                 bool
	currentDirection      string
	direction             [4]string
	currentDirectionIndex int
	potentialLoop         bool
	loop                  bool
	memory                []string
	movement              []string
}

func NewRobot(posX int, posY int) *Robot {
	b := new(Robot)
	b.posX = posX
	b.posY = posY
	b.invert = false
	b.drunk = false
	b.currentDirection = "S"
	b.direction = [4]string{"S", "E", "N", "W"}
	b.currentDirectionIndex = 0
	b.potentialLoop = false
	b.loop = false
	return b
}

func (r *Robot) Move(x int, y int) {
	r.posX = x
	r.posY = y
	r.movement = append(r.movement, r.GetCurrentDirectionString())
	r.MemorizeMovement()
}

func GetOppositeDirection(direction string) string {
	switch direction {
	case "S":
		return "N"
	case "E":
		return "W"
	case "N":
		return "S"
	case "W":
		return "E"
	}
	return "error"
}

// Memorize movement and return if the robot is looping
func (r *Robot) MemorizeMovement() {
	if len(r.memory) == 0 {
		r.memory = append(r.memory, r.currentDirection)
	} else {
		if r.memory[0] == r.currentDirection { // The robot continues his path
			r.memory = append(r.memory, r.currentDirection)
		} else if r.memory[0] == GetOppositeDirection(r.currentDirection) { // The robot comes back
			r.memory = append(r.memory, r.currentDirection)
			r.IsStuckInLoop()
		} else { // The robot can't be in loop in this case
			r.memory = nil
			r.memory = append(r.memory, r.currentDirection) // It starts his new journey
		}
	}
}

func (r *Robot) CleanInitialDirectionFromMemory(oppositeDirectionCount int, oppositeDirection string) {
	r.memory = nil
	for i := 0; i < oppositeDirectionCount; i++ {
		r.memory = append(r.memory, oppositeDirection)
	}
}

func (r *Robot) IsStuckInLoop() {
	initialDirection := r.memory[0]
	initialDirectionCount := 0
	oppositeDirection := GetOppositeDirection(initialDirection)
	oppositeDirectionCount := 0
	for _, val := range r.memory {
		if val == initialDirection {
			initialDirectionCount++
		} else if val == oppositeDirection {
			oppositeDirectionCount++
		} else {
			fmt.Fprintln(os.Stdout, "Memory is compromised...")
		}
	}
	if initialDirectionCount == oppositeDirectionCount {
		if r.potentialLoop {
			r.loop = true
		} else {
			r.potentialLoop = true
			r.CleanInitialDirectionFromMemory(oppositeDirectionCount, oppositeDirection)
		}
	}
}

func (r *Robot) GetCurrentDirectionString() string {
	switch r.currentDirection {
	case "S":
		return "SOUTH"
	case "E":
		return "EAST"
	case "N":
		return "NORTH"
	case "W":
		return "WEST"
	}
	return "error"
}

// func (r *Robot) GetCurrentDirectionIndex() int {
// 	return r.currentDirectionIndex
// }

func (r *Robot) ChangeDirection() {
	if r.currentDirectionIndex >= 0 && r.currentDirectionIndex < len(r.direction) {
		if r.invert {
			r.currentDirection = r.direction[len(r.direction)-(r.currentDirectionIndex+1)]
		} else {
			r.currentDirection = r.direction[r.currentDirectionIndex]
		}
	} else {
		r.currentDirection = "blocked"
	}
}

func (r *Robot) IncreaseCurrentDirectionIndex() {
	r.currentDirectionIndex++
}

func (r *Robot) ResetCurrentDirectionIndex() {
	r.currentDirectionIndex = 0
}

func (r *Robot) SetCurrentDirection(direction string) {
	r.currentDirection = direction
}

func (r *Robot) GetCurrentDirection() string {
	return r.currentDirection
}

func (r *Robot) GetMovement() []string {
	return r.movement
}

func (r *Robot) GetPosX() int {
	return r.posX
}

func (r *Robot) GetPosY() int {
	return r.posY
}

func (r *Robot) IsInvert() bool {
	return r.invert
}

func (r *Robot) IsDrunk() bool {
	return r.drunk
}

func (r *Robot) DrinkBeer() {
	r.drunk = !r.drunk
}

func (r *Robot) CircuitInverter() {
	r.invert = !r.invert
}

func (r *Robot) IsLooping() bool {
	return r.loop
}
