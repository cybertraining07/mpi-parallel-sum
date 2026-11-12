# Python MPI Parallel Sum Calculator

## Project Overview
A beginner parallel-computing project using Python,
mpi4py and MPICH to distribute calculations across
multiple processes.

## Technologies
- Python 3.12.7
- mpi4py 4.1.2
- MPICH 5.0.2
- Linux

## Project Objective
Calculate the sum of integers from 1 to 100 using
four parallel MPI processes.

## Execution
```bash
mpiexec -n 4 python parallel_sum.py

Results
- Process 0: 1225
- Process 1: 1250
- Process 2: 1275
- Process 3: 1300
- Final result: 5050
Concepts Demonstrated
- MPI process management
- Distributed workload
- Parallel execution
- MPI reduction
- Python scientific computing
Verification
The calculated result matched the expected result
of 5050.
