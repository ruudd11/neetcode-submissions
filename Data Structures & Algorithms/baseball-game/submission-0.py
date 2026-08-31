class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []

        for o in operations:
            if o not in {"+", "D", "C"}:
                rec.append(int(o))
            elif o == "+":
                rec.append(rec[-1] + rec[-2])
            elif o == "D":
                rec.append(rec[-1] * 2)
            elif o == "C":
                rec.pop()
        return sum(rec)

                
        
