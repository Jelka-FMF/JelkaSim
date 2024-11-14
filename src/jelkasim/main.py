from .simulator import Simulation

from subprocess import Popen, PIPE
import sys
import os
import time
from jelka_validator import DataReader


if __name__ == "__main__":
    # Popen(["-m", "writer.py"], executable=sys.executable, stdout=PIPE)
    # Popen(["writer.exe"], stdout=PIPE)
    print(os.getcwd())
    print(sys.executable)
    with Popen([sys.executable, "test/basic.py"], stdout=PIPE) as p:
        sim = Simulation()
        dr = DataReader(p.stdout.read1)  # type: ignore
        dr.update()
        # assert dr.header is not None
        sim.init()
        time.sleep(1)
        while sim.running:
            c = next(dr)
            assert all(c[i] == c[0] for i in range(len(c)))
            dr.user_print()
            sim.set_colors(dict(zip(range(len(c)), c)))
            sim.frame()
        sim.quit()