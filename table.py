from cs4300_csp_parser import parse_cs4300
from cs4300_csp import solve_backtracking

if __name__ == "__main__":
    problems = ["sudoku_4x4_inst1.csp", "sudoku_4x4_inst2.csp", "sudoku_4x4_inst3.csp", "./examples/send_more_money_strict_add10.csp"]
    
    print("|Instance|Uses MRV|Steps|Solution(s)|")
    print("|--------|--------|-----|-----------|")
    for p in problems:
        csp = parse_cs4300(p)
        for a in [True, False]:
            sols = list(solve_backtracking(csp, use_mrv=a))
            
            print(f"|{p}|{a}|(enter from the above info)|{sols}|")
