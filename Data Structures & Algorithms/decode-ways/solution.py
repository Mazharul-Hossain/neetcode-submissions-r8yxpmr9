        dp = [0 for _ in range(N + 1)]
        # Step 4: Base cases
        # starts by 1 combination
        dp[N] = 1
        # print(dp)
        # Step 2: Define state (MOST IMPORTANT)
        # Let dp[i] represent how much we can steal at house i - 1?
        # print(s)
            

        s = list(s)
        s = list(map(int, s))
        # decisions between index i and j depend on previous subproblems.
        N = len(s)

        # Step 5: Order of computation
        # We compute from left --> right because we can take compute substrings only once
        for i in range(N - 1, -1, -1):
            # Step 3: Recurrence (transition)
            # At each step, I have one choices:
            # palindrom and previous also palindrom
            # print(i + 1, j - 1)
            if s[i] == 0:
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if i + 1 < N and (s[i] == 1 or (s[i] == 2 and s[i + 1] <= 6)):
                    dp[i] += dp[i + 2]

            
            # print(dp)
            # print()

        # Step 6: Optimization