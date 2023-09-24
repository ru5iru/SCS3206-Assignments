if __name__ == "__main__":
    num_vertices = 2000 
    density = 0.5       
    sparsity = 0.5 

    from graph.graph import Graph
    from kruskal.kruskal import Kruskal
    from prim.lazy_prim import LazyPrim
    from prim.eager_prim import EagerPrim
    from random_graph.random_graph import generate_dense_graph, generate_sparse_graph   
    
    # Generate random dense graph with adjacency matrix
    dense_graph_matrix = generate_dense_graph(num_vertices, density, use_matrix=True)

    # Generate random dense graph with adjacency list
    dense_graph_list = generate_dense_graph(num_vertices, density, use_matrix=False)

    # Generate random sparse graph with adjacency matrix
    sparse_graph_matrix = generate_sparse_graph(num_vertices, sparsity, use_matrix=True)

    # Generate random sparse graph with adjacency list
    sparse_graph_list = generate_sparse_graph(num_vertices, sparsity, use_matrix=False)

    print("\nVertices:", num_vertices, "\tDensity:", density, "\tSparsity:", sparsity)
    print("")

    # Kruskal's | Dense Graph | Matrix
    import time
    start_time = time.time()
    kruskal_matrix = Kruskal(dense_graph_matrix)
    mst_kruskal_matrix = kruskal_matrix.find_mst()
    end_time = time.time()
    print("Algorithm: Kruskal's [dense graph, matrix] Execution Time:", end_time - start_time, "seconds")

    # Kruskal's | Dense Graph | List
    start_time = time.time()
    kruskal_list = Kruskal(dense_graph_list)
    mst_kruskal_list = kruskal_list.find_mst()
    end_time = time.time()
    print("Algorithm: Kruskal's [dense graph, list] Execution Time:", end_time - start_time, "seconds")
    
    # Kruskal's | Sparse Graph | Matrix
    start_time = time.time()
    kruskal_matrix = Kruskal(sparse_graph_matrix)
    mst_kruskal_matrix = kruskal_matrix.find_mst()
    end_time = time.time()
    print("Algorithm: Kruskal's [sparse graph, matrix] Execution Time:", end_time - start_time, "seconds")

    # Kruskal's | Sparse Graph | List
    start_time = time.time()
    kruskal_list = Kruskal(sparse_graph_list)
    mst_kruskal_list = kruskal_list.find_mst()
    end_time = time.time()
    print("Algorithm: Kruskal's [sparse graph, list] Execution Time:", end_time - start_time, "seconds")



    # Lazy Prim's | Dense Graph | Matrix
    start_time = time.time()
    lazy_prim_matrix = LazyPrim(dense_graph_matrix)
    mst_lazy_prim_matrix = lazy_prim_matrix.find_mst()
    end_time = time.time()
    print("Algorithm: Lazy Prim's [dense graph, matrix] Execution Time:", end_time - start_time, "seconds")
    
    # Lazy Prim's | Dense Graph | List
    start_time = time.time()
    lazy_prim_list = LazyPrim(dense_graph_list)
    mst_lazy_prim_list = lazy_prim_list.find_mst()
    end_time = time.time()
    print("Algorithm: Lazy Prim's [dense graph, list] Execution Time:", end_time - start_time, "seconds")
    
    # Lazy Prim's | Sparse Graph | Matrix
    start_time = time.time()
    lazy_prim_matrix = LazyPrim(sparse_graph_matrix)
    mst_lazy_prim_matrix = lazy_prim_matrix.find_mst()
    end_time = time.time()
    print("Algorithm: Lazy Prim's [sparse graph, matrix] Execution Time:", end_time - start_time, "seconds")
    
    # Lazy Prim's | Sparse Graph | List
    start_time = time.time()
    lazy_prim_list = LazyPrim(sparse_graph_list)
    mst_lazy_prim_list = lazy_prim_list.find_mst()
    end_time = time.time()
    print("Algorithm: Lazy Prim's [sparse graph, list] Execution Time:", end_time - start_time, "seconds")
    


    # Eager Prim's | Dense Graph | Matrix
    start_time = time.time()
    eager_prim_matrix = EagerPrim(dense_graph_matrix)
    mst_eager_prim_matrix = eager_prim_matrix.find_mst()
    end_time = time.time()
    print("Algorithm: Eager Prim's [dense graph, matrix] Execution Time:", end_time - start_time, "seconds")
    
    # Eager Prim's | Dense Graph | List
    start_time = time.time()
    eager_prim_list = EagerPrim(dense_graph_list)
    mst_eager_prim_list = eager_prim_list.find_mst()
    end_time = time.time()
    print("Algorithm: Eager Prim's [dense graph, list] Execution Time:", end_time - start_time, "seconds")
    
    # Eager Prim's | Sparse Graph | Matrix
    start_time = time.time()
    eager_prim_matrix = EagerPrim(sparse_graph_matrix)
    mst_eager_prim_matrix = eager_prim_matrix.find_mst()
    end_time = time.time()
    print("Algorithm: Eager Prim's [sparse graph, matrix] Execution Time:", end_time - start_time, "seconds")
    
    # Eager Prim's | Sparse Graph | List
    start_time = time.time()
    eager_prim_list = EagerPrim(sparse_graph_list)
    mst_eager_prim_list = eager_prim_list.find_mst()
    end_time = time.time()
    print("Algorithm: Eager Prim's [sparse graph, list] Execution Time:", end_time - start_time, "seconds")
