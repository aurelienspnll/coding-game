package main

import (
	"bufio"
	"fmt"
	"os"

	"github.com/aurelienspnll/coding-game/blunder/src/engine"
	"github.com/aurelienspnll/coding-game/blunder/src/robot"
	"github.com/aurelienspnll/coding-game/blunder/src/world"
)

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var L, C int
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &L, &C)

	worldDef := ""
	for scanner.Scan() {
		worldDef += scanner.Text()
	}
	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	w := world.NewWorld(L, C, worldDef)
	// w.PrintWorld()
	posX, posY := w.GetStartPos()
	r := robot.NewRobot(posX, posY)
	e := engine.NewEngine(*r, *w)
	// e.PrintWorldAndRobot()
	e.Play()

}
