# Minimal package structure example (as a comment, not code)
# my_pkg/
#     __init__.py
#     core.py
# pyproject.toml
# or setup.cfg/setup.py
#


#   Error handling and debugging ---------------------------------------------->

def safe_div(a, b):
    try: 
        return a/b
    except ZeroDivisionError:
        return float('inf')
    else:
        print("No error!")
    finally:
        print("Done.")

print(safe_div(10, 2))
print(safe_div(1, 0))    

#Raising Errors -------------------------------------------------
def withdraw(balance, amt):
    if amt > balance:
        raise ValueError("Insufficient funds")
    return balance - amt

try:
    withdraw(100, 150)
except ValueError as e:
    print("Error:", e)


      