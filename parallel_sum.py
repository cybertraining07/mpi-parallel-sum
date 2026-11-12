from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

numbers = list(range(1, 101))

# Divide the numbers among processes
local_numbers = numbers[rank::size]

# Calculate each process's partial sum
local_sum = sum(local_numbers)

# Combine all partial sums
total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

print(f"Process {rank}: partial sum = {local_sum}")

if rank == 0:
    print(f"\nFinal total sum = {total_sum}")
    print("Expected result = 5050")
