
def main():
    n = eval(input("Enter number of disks: "))
    # Find the solution recursively
    move_total = moveDisks(n, "A", "B", "C")
    print("The moves are:", move_total)
    

# The function for finding the solution to move n disks
# from fromTower to toTower with auxTower

def moveDisks(n, fromTower, toTower, auxTower):

    if n == 1:
        return 1
    else:
        return (
            moveDisks(n - 1, fromTower, auxTower, toTower)
            + 1
            + moveDisks(n - 1, auxTower, toTower, fromTower)
        )

main() # Call the main function