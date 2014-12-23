Tests on djorm-array
====================

djangofoo=# select count(*) from grid_gridforeign ;select count(*) from grid_grid ; count  

 count 
-------
     0
(1 row)

 count 
-------
     0
(1 row)

                                                QUERY PLAN                                                 
-----------------------------------------------------------------------------------------------------------
 Seq Scan on public.grid_grid  (cost=0.00..15.62 rows=1 width=4) (actual time=0.001..0.001 rows=0 loops=1)
   Output: id
   Filter: (grid_grid.tags @> '{17439}'::integer[])
 Planning time: 0.397 ms
 Execution time: 0.011 ms
(5 rows)

                                                QUERY PLAN                                                 
-----------------------------------------------------------------------------------------------------------
 Seq Scan on public.grid_grid  (cost=0.00..15.62 rows=1 width=4) (actual time=0.001..0.001 rows=0 loops=1)
   Output: id
   Filter: (grid_grid.old ~~ '%,17439,%'::text)
 Planning time: 0.350 ms
 Execution time: 0.024 ms
(5 rows)

                                                                          QUERY PLAN                                                                           
---------------------------------------------------------------------------------------------------------------------------------------------------------------
 Index Only Scan using grid_gridforeign_tag_grid_id_idx on public.grid_gridforeign  (cost=0.15..8.17 rows=1 width=4) (actual time=0.013..0.013 rows=0 loops=1)
   Output: grid_id
   Index Cond: (grid_gridforeign.tag = 17439)
   Heap Fetches: 0
 Planning time: 0.226 ms
 Execution time: 0.051 ms
(6 rows)

 count 
-------
  2000
(1 row)

 count 
-------
 21016
(1 row)

                                                 QUERY PLAN                                                 
------------------------------------------------------------------------------------------------------------
 Seq Scan on public.grid_grid  (cost=0.00..68.35 rows=23 width=4) (actual time=0.039..0.918 rows=2 loops=1)
   Output: id
   Filter: (grid_grid.tags @> '{17439}'::integer[])
   Rows Removed by Filter: 1998
 Planning time: 0.343 ms
 Execution time: 0.929 ms
(6 rows)

                                                 QUERY PLAN                                                 
------------------------------------------------------------------------------------------------------------
 Seq Scan on public.grid_grid  (cost=0.00..68.35 rows=19 width=4) (actual time=0.018..0.914 rows=2 loops=1)
   Output: id
   Filter: (grid_grid.old ~~ '%,17439,%'::text)
   Rows Removed by Filter: 1998
 Planning time: 0.335 ms
 Execution time: 0.936 ms
(6 rows)

                                                                          QUERY PLAN                                                                           
---------------------------------------------------------------------------------------------------------------------------------------------------------------
 Index Only Scan using grid_gridforeign_tag_grid_id_idx on public.grid_gridforeign  (cost=0.29..8.30 rows=1 width=4) (actual time=0.028..0.034 rows=2 loops=1)
   Output: grid_id
   Index Cond: (grid_gridforeign.tag = 17439)
   Heap Fetches: 2
 Planning time: 0.322 ms
 Execution time: 0.076 ms
(6 rows)

 count 
-------
 10000
(1 row)

 count  
--------
 105077
(1 row)

                                                 QUERY PLAN                                                 
------------------------------------------------------------------------------------------------------------
 Seq Scan on public.grid_grid  (cost=0.00..348.09 rows=5 width=4) (actual time=0.039..4.298 rows=8 loops=1)
   Output: id
   Filter: (grid_grid.tags @> '{17439}'::integer[])
   Rows Removed by Filter: 9992
 Planning time: 0.334 ms
 Execution time: 4.312 ms
(6 rows)

                                                 QUERY PLAN                                                 
------------------------------------------------------------------------------------------------------------
 Seq Scan on public.grid_grid  (cost=0.00..348.09 rows=1 width=4) (actual time=0.021..4.531 rows=8 loops=1)
   Output: id
   Filter: (grid_grid.old ~~ '%,17439,%'::text)
   Rows Removed by Filter: 9992
 Planning time: 0.294 ms
 Execution time: 4.552 ms
(6 rows)

                                                               QUERY PLAN                                                                
-----------------------------------------------------------------------------------------------------------------------------------------
 Bitmap Heap Scan on public.grid_gridforeign  (cost=4.33..22.99 rows=5 width=4) (actual time=0.035..0.072 rows=8 loops=1)
   Output: grid_id
   Recheck Cond: (grid_gridforeign.tag = 17439)
   Heap Blocks: exact=8
   ->  Bitmap Index Scan on grid_gridforeign_tag_grid_id_idx  (cost=0.00..4.33 rows=5 width=0) (actual time=0.018..0.018 rows=8 loops=1)
         Index Cond: (grid_gridforeign.tag = 17439)
 Planning time: 0.221 ms
 Execution time: 0.091 ms
(8 rows)
