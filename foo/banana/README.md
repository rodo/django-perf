Bench usage of select_related
=============================

print Apple.objects.filter(pk=1).select_related('color')

djangofoo=# explain SELECT "banana_apple"."id", "banana_apple"."name",
"banana_apple"."alpha", "banana_apple"."color_id",
"banana_apple"."fruit_id", "banana_apple"."variety_id",
"banana_color"."id", "banana_color"."name", "banana_color"."code",
"banana_color"."epsilon", "banana_fruit"."id",
"banana_fruit"."family", "banana_fruit"."beta", "banana_variety"."id",
"banana_variety"."name", "banana_variety"."beta",
"banana_variety"."code", "banana_variety"."owner_id",
"banana_owner"."id", "banana_owner"."name", "banana_owner"."country"
FROM "banana_apple" INNER JOIN "banana_color" ON (
"banana_apple"."color_id" = "banana_color"."id" ) INNER JOIN
"banana_fruit" ON ( "banana_apple"."fruit_id" = "banana_fruit"."id" )
INNER JOIN "banana_variety" ON ( "banana_apple"."variety_id" =
"banana_variety"."id" ) INNER JOIN "banana_owner" ON (
"banana_variety"."owner_id" = "banana_owner"."id" ) WHERE
"banana_apple"."id" = 1  LIMIT 21
djangofoo-# ;
                                                   QUERY PLAN                                                   
----------------------------------------------------------------------------------------------------------------
 Limit  (cost=5.69..29.40 rows=1 width=1780)
   ->  Nested Loop  (cost=5.69..29.40 rows=1 width=1780)
         ->  Nested Loop  (cost=5.55..28.96 rows=1 width=1594)
               ->  Nested Loop  (cost=5.41..20.79 rows=1 width=988)
                     ->  Hash Join  (cost=5.26..12.61 rows=1 width=390)
                           Hash Cond: (banana_color.id = banana_apple.color_id)
                           ->  Seq Scan on banana_color (cost=0.00..6.70 rows=170 width=175)
                           ->  Hash  (cost=5.25..5.25 rows=1 width=215)
                                 ->  Seq Scan on banana_apple
                                 (cost=0.00..5.25 rows=1 width=215)
                                       Filter: (id = 1)
                     ->  Index Scan using banana_fruit_pkey on
                     banana_fruit  (cost=0.14..8.16 rows=1 width=598)
                           Index Cond: (id = banana_apple.fruit_id)
               ->  Index Scan using banana_variety_pkey on
               banana_variety  (cost=0.14..8.16 rows=1 width=606)
                     Index Cond: (id = banana_apple.variety_id)
         ->  Index Scan using banana_owner_pkey on banana_owner
         (cost=0.14..0.43 rows=1 width=186)
               Index Cond: (id = banana_variety.owner_id)
(16 rows)


print Apple.objects.filter(pk=1).select_related('color')


djangofoo=# explain SELECT "banana_apple"."id", "banana_apple"."name",
"banana_apple"."alpha", "banana_apple"."color_id",
"banana_apple"."fruit_id", "banana_apple"."variety_id",
"banana_color"."id", "banana_color"."name", "banana_color"."code",
"banana_color"."epsilon" FROM "banana_apple" INNER JOIN "banana_color"
ON ( "banana_apple"."color_id" = "banana_color"."id" ) WHERE
"banana_apple"."id" = 1;
                                QUERY PLAN                                
--------------------------------------------------------------------------
 Hash Join  (cost=5.26..12.61 rows=1 width=390)
   Hash Cond: (banana_color.id = banana_apple.color_id)
   ->  Seq Scan on banana_color  (cost=0.00..6.70 rows=170 width=175)
   ->  Hash  (cost=5.25..5.25 rows=1 width=215)
         ->  Seq Scan on banana_apple  (cost=0.00..5.25 rows=1
         width=215)
               Filter: (id = 1)
(6 rows)

