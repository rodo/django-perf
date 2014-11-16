--
--
--
--
DROP TABLE IF EXISTS manga_category__catid_counter;

CREATE TABLE manga_category__catid_counter (
    catid int,
    counter int);


BEGIN;

DELETE FROM manga_category__catid_counter;

LOCK TABLE manga_category IN EXCLUSIVE MODE;

INSERT INTO manga_category__catid_counter (
    SELECT catid, count(catid) 
    FROM manga_category
    GROUP BY catid );

COMMIT;

--
-- Functions appellées par les triggers
--

CREATE OR REPLACE FUNCTION manga_category_insert() RETURNS TRIGGER AS $BODY$
BEGIN 
  UPDATE manga_category__catid_counter SET counter = counter + 1 WHERE catid = NEW.catid;
  RETURN NEW;
END;
$BODY$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION manga_category_delete() RETURNS TRIGGER AS $BODY$
BEGIN 
  UPDATE manga_category__catid_counter SET counter = counter - 1 WHERE catid = OLD.catid;
  RETURN NEW;
END;
$BODY$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION manga_category_update() RETURNS TRIGGER AS $BODY$
BEGIN 
  IF NEW.catid != OLD.catid THEN
  UPDATE manga_category__catid_counter SET counter = counter + 1 WHERE catid = NEW.catid;
  UPDATE manga_category__catid_counter SET counter = counter - 1 WHERE catid = OLD.catid;
  END IF;
  RETURN NEW;
END;
$BODY$ LANGUAGE plpgsql;

--
-- Declaration des triggers
--

CREATE TRIGGER manga_category_insert_trigger
    AFTER INSERT ON manga_category
    FOR EACH ROW
    EXECUTE PROCEDURE manga_category_insert();

CREATE TRIGGER manga_category_delete_trigger
    AFTER DELETE ON manga_category
    FOR EACH ROW
    EXECUTE PROCEDURE manga_category_delete();

CREATE TRIGGER manga_category_update_trigger
    AFTER UPDATE ON manga_category
    FOR EACH ROW
    EXECUTE PROCEDURE manga_category_update();
