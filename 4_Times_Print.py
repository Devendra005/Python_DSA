# Print 4 times "Devedra" using recursion 

def func(count):
    if count > 4:
        return
    print("Devendra")
    func(count+1)
func(1)