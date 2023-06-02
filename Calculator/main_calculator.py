from Calculator.multiplication import multiply
from Calculator.subtraction import subtract
from Calculator.addition import add
from Calculator.division import divide


if __name__ == "__main__":
    operations = {1: add, 2: subtract, 3: multiply, 4: divide}
    while True:
        try:
            operation = input("Enter operation or 0 to exit: ( Add = 1, Subtract = 2, multiply = 3, Divide = 4): ")
            assert isinstance(int(operation), int)
            if operation == "0":
                break
            operation = operations[int(operation)]
            nums = input("Enter list of numbers: ")
            nums = nums.split(" ")
            for num in nums:
                assert float(num)
            nums = list(map(lambda item: float(item), nums))
            print(f"Result = {operation(nums)}")
        except AssertionError:
            print("All entries must be digit")
        except ValueError:
            print("All entries must be digit")
        except KeyError:
            print("Operation not found")


