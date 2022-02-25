def max_profit_recursive(capacity, weights, profits, idx=0):
    if idx == len(weights):
        return 0
    if weights[idx] > capacity:
        return max_profit_recursive(capacity, weights, profits, idx+1)
    else:
        return max(max_profit_recursive(capacity, weights, profits, idx+1),
                   profits[idx] + max_profit_recursive(capacity-weights[idx], weights, profits, idx+1))