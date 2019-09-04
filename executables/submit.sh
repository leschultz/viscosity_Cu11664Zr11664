#!/bin/sh
#SBATCH --partition=univ2
#SBATCH --time=7-00:00:00		# run time in days-hh:mm:ss
#SBATCH --nodes=2			# require 2 nodes
#SBATCH --ntasks-per-node=16            # (by default, "ntasks"="cpus")
#SBATCH --mem-per-cpu=4000		# RAM per CPU core, in MB (default 4 GB/core)
#SBATCH --error=job.%J.err
#SBATCH --output=job.%J.out

#SBATCH --mail-user=lsschultz@wisc.edu
#SBATCH --mail-type=END

module load mpi/gcc/openmpi/3.1.1-GCC-7.3.0-2.30

./exec_runs
