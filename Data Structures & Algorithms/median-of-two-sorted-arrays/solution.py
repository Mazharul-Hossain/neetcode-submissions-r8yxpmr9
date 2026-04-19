            N_right = float("inf") if j == N_end else nums2[j]

            # nums2: [ ... j elements | rest ] so nums2[j-1] <= nums1[i]
            N_left = float("-inf") if j == 0 else nums2[j-1]
            M_right = float("inf") if i == M_end else nums1[i] 

            if M_left <= N_right and N_left <= M_right:
                if (M_end + N_end) % 2:
                    return max(M_left, N_left)
                return (max(M_left, N_left) + min(M_right, N_right)) / 2.0
            
            elif M_left > N_right:
                # An element from nums1 LEFT side is too big
                # it should actually be on the RIGHT side
                right = i - 1
            
            else:
                left = i + 1



