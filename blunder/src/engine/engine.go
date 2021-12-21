package engine

import (
	"fmt"
	"os"

	"github.com/aurelienspnll/coding-game/blunder/src/robot"
	"github.com/aurelienspnll/coding-game/blunder/src/world"
)

type Engine struct {
	robot   robot.Robot
	world   world.World
	arrived bool
	turn    int
}

func NewEngine(robot robot.Robot, world world.World) *Engine {
	e := new(Engine)
	e.robot = robot
	e.world = world
	e.arrived = false
	e.turn = 0
	return e
}

func (e *Engine) PrintWorldAndRobot() {
	for i := 0; i < e.world.GetHeight(); i++ {
		for j := 0; j < e.world.GetWidth(); j++ {
			if i == e.robot.GetPosX() && j == e.robot.GetPosY() {
				print("R")
			} else {
				print(e.world.GetTab()[i*e.world.GetWidth()+j])
			}
		}
		println()
	}
}

func (e *Engine) NextRobotPos() (int, int) {
	switch e.robot.GetCurrentDirection() {
	case "S":
		return e.robot.GetPosX() + 1, e.robot.GetPosY()
	case "E":
		return e.robot.GetPosX(), e.robot.GetPosY() + 1
	case "N":
		return e.robot.GetPosX() - 1, e.robot.GetPosY()
	case "W":
		return e.robot.GetPosX(), e.robot.GetPosY() - 1
	case "blocked":
		fmt.Fprintln(os.Stderr, "Blunder is blocked")
		os.Exit(1)
	}
	return -1, -1
}

func (e *Engine) MoveRobot(nextPosX int, nextPosY int) bool {
	switch e.world.GetBox(nextPosX, nextPosY) {
	case "#": // World borders
		return false
	case "X":
		if e.robot.IsDrunk() {
			e.robot.Move(nextPosX, nextPosY)
			e.world.BreakObstacle(nextPosX, nextPosY)
			return true
		} else {
			return false
		}
	case "@":
		e.robot.Move(nextPosX, nextPosY)
		return true
	case "$":
		e.robot.Move(nextPosX, nextPosY)
		// The end
		e.arrived = true
		return true
	case "S", "E", "N", "W":
		e.robot.Move(nextPosX, nextPosY)
		e.robot.SetCurrentDirection(e.world.GetBox(nextPosX, nextPosY))
		return true
	case "B":
		e.robot.Move(nextPosX, nextPosY)
		e.robot.DrinkBeer()
		return true
	case "I":
		e.robot.Move(nextPosX, nextPosY)
		e.robot.CircuitInverter()
		return true
	case "T":
		x, y := e.world.GetOtherTeleporter(nextPosX, nextPosY)
		e.robot.Move(x, y)
		return true
	case " ":
		e.robot.Move(nextPosX, nextPosY)
		return true
	}
	return false
}

func (e *Engine) Play() {
	for {
		e.turn++
		// fmt.Fprintf(os.Stdout, "Turn n %d: \n", e.turn)
		x, y := e.NextRobotPos()
		if x == -1 && y == -1 {
			return
		} else {
			hasMove := e.MoveRobot(x, y)
			if !hasMove {
				e.robot.ChangeDirection()
				e.robot.IncreaseCurrentDirectionIndex()
				// fmt.Fprintf(os.Stdout, "Blunder can not move to %d ; %d", x, y)
			} else {
				e.robot.ResetCurrentDirectionIndex()
				// e.PrintWorldAndRobot()
				if e.robot.IsLooping() {
					fmt.Fprintln(os.Stdout, "LOOP")
					return
				}
			}
		}
		if e.arrived {
			for _, v := range e.robot.GetMovement() {
				fmt.Fprintln(os.Stdout, v)
			}
			return
		}
	}
}
