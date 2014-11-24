BEGIN;  

LOCK TABLE boat IN EXCLUSIVE MODE;

DELETE FROM boats_per_skipper;

INSERT INTO boats_per_skipper (
   SELECT skipper.id, count(boat.skipper_id)
   FROM skipper
   LEFT JOIN boat ON boat.skipper_id = skipper.id
   GROUP BY skipper.id );

COMMIT;
