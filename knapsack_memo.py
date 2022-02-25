def knapsack_memo(capacity, weights, profits):
    memo = {}
    
    def recurse(idx, remaining):
        key = (idx, remaining)
        if key in memo:
            return memo[key]
        elif idx == len(weights):
            memo[key] = 0
        elif weights[idx] > remaining:
            memo[key] = recurse(idx+1, remaining)
        else:
            memo[key] = max(recurse(idx+1, remaining), 
                            profits[idx] + recurse(idx+1, remaining-weights[idx]))
        return memo[key] 
        
    return recurse(0, capacity)