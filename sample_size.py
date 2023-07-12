import math
from scipy.stats import norm
from scipy.special import erfinv

# Given values
p1 = 0.0392  # Baseline conversion rate
d = 0.00196  # Minimum detectable effect
alpha = 0.05  # Significance level
beta = 0.2  # 1 - Statistical power

# Calculating critical values
z_alpha_2 = abs(math.sqrt(2) * erfinv(2 * alpha - 1))
z_beta = abs(math.sqrt(2) * erfinv(2 * beta - 1))

# Calculating pooled probability
p_bar = p1 + d / 2

# Calculating sample size
n = ((z_alpha_2 * math.sqrt(2 * p_bar * (1 - p_bar)) + z_beta *
     math.sqrt(p1 * (1 - p1) + (p1 + d) * (1 - (p1 + d)))) / d) ** 2
# Rounding up to the nearest whole number because you can't have a fraction of a sample
n = math.ceil(n)

print(f"The required sample size is approximately {n} in each group.")