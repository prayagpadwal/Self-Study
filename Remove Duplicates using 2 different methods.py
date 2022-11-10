# This approach uses pandas to remove duplicates, but since Leetcode
# complier doesn't support pandas, this solution would not suffice

import pandas as pd

try:
    list_user = []

    while True:
        list_user.append(int(input()))

except:
    print('original list =', list_user)

print(pd.Series(list_user).drop_duplicates().tolist())


# New attempt

try:
    list_user = []

    while True:
        list_user.append(int(input()))

except:
    print('original list =', list_user)

print(list(dict.fromkeys(list_user)))

