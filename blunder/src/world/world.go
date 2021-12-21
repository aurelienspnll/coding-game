package world

type World struct {
	height int
	width  int
	tab    []string
}

func NewWorld(height int, width int, tab string) *World {
	w := new(World)
	w.height = height
	w.width = width
	for _, val := range tab {
		w.tab = append(w.tab, string(val))
	}
	return w
}

func (w *World) PrintWorld() {
	for i := 0; i < w.height; i++ {
		for j := 0; j < w.width; j++ {
			print(w.tab[i*w.width+j])
		}
		println()
	}
}

func (w *World) GetStartPos() (int, int) {
	for i := 0; i < w.height; i++ {
		for j := 0; j < w.width; j++ {
			if w.tab[i*w.width+j] == "@" {
				return i, j
			}
		}
	}
	return -1, -1
}

func (w *World) GetOtherTeleporter(x int, y int) (int, int) {
	for i := 0; i < w.height; i++ {
		for j := 0; j < w.width; j++ {
			if w.tab[i*w.width+j] == "T" && (i != x || j != y) {
				return i, j
			}
		}
	}
	return -1, -1
}

func (w *World) BreakObstacle(x int, y int) {
	w.tab[x*w.width+y] = " "
}

func (w *World) GetBox(x int, y int) string {
	return w.tab[x*w.width+y]
}

func (w *World) GetHeight() int {
	return w.height
}

func (w *World) GetWidth() int {
	return w.width
}

func (w *World) GetTab() []string {
	return w.tab
}
