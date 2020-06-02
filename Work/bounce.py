# bounce.py
#
# Exercise 1.5

start_height = 100.
N_bounces = 10
frac = 0.6

height = start_height

for i in range(N_bounces):
    height = height * frac
    bounce_idx = i + 1

    print(bounce_idx, round(height, 4))
