from scipy import stats

# Significance level
alpha = 0.05
# One-sample t-test
sample_data = [12, 15, 14, 10, 13, 14, 15, 16, 14, 13]
population_mean = 13
t_stat_one, pvalue = stats.ttest_1samp(sample_data, population_mean)
print("One-sample t-test:")
print(f"T-statistic = {t_stat_one:.4f}")
print(f"P-value = {pvalue:.4f}")
if pvalue < alpha:
    print(
        "Conclusion: Reject the null hypothesis. There is a significant difference from the population mean.\n"
    )
else:
    print(
        "Conclusion: Fail to reject the null hypothesis. No significant difference from the population mean.\n"
    )
# Two-sample independent t-test
group1 = [23, 21, 19, 24, 25]
group2 = [27, 29, 26, 30, 28]
t_stat_two, pvalue_two = stats.ttest_ind(group1, group2, equal_var=True)
print("Two-sample t-test (Independent samples, equal variance):")
print(f"T-statistic = {t_stat_two:.4f}")
print(f"P-value = {pvalue_two:.4f}")
if pvalue_two < alpha:
    print(
        "Conclusion: Reject the null hypothesis. There is a significant difference between the group means."
    )
else:
    print(
        "Conclusion: Fail to reject the null hypothesis.No significant difference between the group means."
    )
