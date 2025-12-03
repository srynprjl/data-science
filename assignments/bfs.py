from typing import Optional, Tuple
State = Tuple[int, int]

CAP_A = 3
CAP_B = 4

class Node:
    STATE: State
    PARENT: Optional["Node"]
    ACTION: Optional[str]
    PATH_COST: int

    def fill_a(state: State) -> State:
        a, b = state
        return CAP_A, b

    def fill_b(state: State) -> State:
        a, b = state
        return a, CAP_B

    def empty_a(state: State) -> State:
        a, b = state
        return 0, a

    def empty_b(state: State) -> State:
        a, b = state
        return a, 0

