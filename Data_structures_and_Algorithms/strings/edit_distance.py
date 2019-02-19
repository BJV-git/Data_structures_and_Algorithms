# so if equal we dont bother else we try to find the 1+ min(either delete or insert of replace)

def editdic(a,b):
    ans={}
    def solve(i,j):
        if i<0: return j+1
        if j<0: return i+1

        if ans.get((i,j)) is None:
            ans[(i,j)] = solve(i-1,j-1) if a[i] == b[j] else 1+min(solve(i-1,j-1), solve(i-1,j), solve(i,j-1))
        return ans[(i, j)]
    return solve(len(a)-1, len(b)-1)