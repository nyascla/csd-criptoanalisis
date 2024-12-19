from src.brute_force import brute_force
from src.bsgs import bsgs
from src.diffie_hellman import diffie_hellman
from src.indexcal import indexcalculus
from src.pollard_rho import pollard_rho


def a():
    brute_force.test()
    bsgs.test()
    pollard_rho.test()
    indexcalculus.test()
    diffie_hellman.test()


if __name__ == "__main__":
    indexcalculus.test(32, 10)

