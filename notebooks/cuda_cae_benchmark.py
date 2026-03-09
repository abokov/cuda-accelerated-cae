import cupy as cp
import numpy as np
import time

def solve_physics_system(size, use_gpu=False):
    if use_gpu:
        # Generate a massive system of equations on the GPU
        A = cp.random.random((size, size), dtype=cp.float32)
        b = cp.random.random((size, 1), dtype=cp.float32)
        cp.cuda.Stream.null.synchronize() # Ensure GPU is ready
        start = time.time()
        
        # Solve Ax = b using CUDA-accelerated LAPACK
        x = cp.linalg.solve(A, b)
        
        cp.cuda.Stream.null.synchronize() # Wait for kernels to finish
        return time.time() - start
    else:
        # Generate the same system on the CPU
        A = np.random.random((size, size)).astype(np.float32)
        b = np.random.random((size, 1)).astype(np.float32)
        start = time.time()
        
        # Solve Ax = b using standard CPU BLAS/LAPACK
        x = np.linalg.solve(A, b)
        return time.time() - start

# Matrix size (Simulation complexity)
sim_size = 15000 

print(f"🚀 Running Simulation Benchmark (Complexity: {sim_size}x{sim_size})...")

cpu_time = solve_physics_system(sim_size, use_gpu=False)
print(f"🐢 CPU Runtime: {cpu_time:.4f} seconds")

gpu_time = solve_physics_system(sim_size, use_gpu=True)
print(f"⚡ GPU Runtime: {gpu_time:.4f} seconds")

print(f"\n🔥 Total Speedup: {cpu_time/gpu_time:.1f}x")
