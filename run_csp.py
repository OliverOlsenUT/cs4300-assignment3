from cs4300_csp_parser import parse_cs4300
from cs4300_csp import solve_backtracking

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python run_csp.py <problem.csp> (-m enable MRV)")
        sys.exit(1)
    csp = parse_cs4300(sys.argv[1])

    if "-m" in sys.argv:
        enable_mrv = True
    else:
        enable_mrv = False
    
    any_sol = False
    for i, sol in enumerate(solve_backtracking(csp, use_mrv=enable_mrv), 1):
        any_sol = True
        print(f"Solution #{i}: {sol}")
    if not any_sol:
        print("No solutions.")
