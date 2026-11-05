def wer(reference_text: str, hypothesis_text: str) -> dict:
    ref = reference_text.strip().split()
    hyp = hypothesis_text.strip().split()
    
    ref_len = len(ref)
    hyp_len = len(hyp)

    if ref_len == 0:
        return {
            "WER": 0.0,
            "S": 0,
            "D": 0,
            "I": hyp_len,
            "N": 0
        }   
    
    dp = [[0] * (hyp_len + 1) for _ in range(ref_len + 1)]
    for i in range(ref_len + 1):
        dp[i][0] = i
    for j in range(hyp_len + 1):
        dp[0][j] = j
        
    for i in range(1, ref_len + 1):
        for j in range(1, hyp_len + 1):
            if ref[i - 1] == hyp[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                sub = dp[i - 1][j - 1] + 1 
                dele = dp[i - 1][j] + 1
                ins = dp[i][j - 1] + 1
                dp[i][j] = min(sub, dele, ins)

    S, D, I, C = 0, 0, 0, 0
    i, j = ref_len, hyp_len
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and ref[i - 1] == hyp[j - 1]:
            C += 1
            i -= 1
            j -= 1
        else:
            choices = []
            if i > 0 and j > 0:
                choices.append((dp[i - 1][j - 1], 'S', i - 1, j - 1))
            if i > 0:
                choices.append((dp[i - 1][j], 'D', i - 1, j))
            if j > 0:
                choices.append((dp[i][j - 1], 'I', i, j - 1))
                
            if choices:
                min_choice = min(choices, key=lambda x: x[0])
                op = min_choice[1]
                if op == 'S':
                    S += 1
                elif op == 'D':
                    D += 1
                elif op == 'I':
                    I += 1
                i, j = min_choice[2], min_choice[3]
            else:
                break
                
    N = ref_len
    wer_value = (S + D + I) / N if N > 0 else 0.0
    
    return {
        "WER": round(wer_value, 4),
        "S": S,
        "D": D,
        "I": I,
        "N": N
    }