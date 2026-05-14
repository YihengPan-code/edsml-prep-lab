#question 1
print("Hello world!")

#question 2 
print("I'm a programmer.")
print('I\'m a programmer.')

#question 3
print("""
Good morning,
it's sunny and spring.
Time for some hiking.
""")

#question4(using %)
name="Bob"
height=1.755
print("%s is %.2f m tall"%(name,height))

#question4(using f)
print(f"{name} is {height:.2f} m tall")

#question5(new)
mae=0.8734
rmse=1.2456
print(f"{'MAE':<4} = {mae:.2f}")
print(f"{'RMSE':<4} = {rmse:.2f}")

#question6(new)
n_samples=1234567
print(f"Loaded {n_samples:,} rows")

#self practice
print(f"{1864874:e}\n")
print("%e" % 1864874)
