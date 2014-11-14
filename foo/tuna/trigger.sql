--
-- Add a comment for each book
--
--
-- Functions appellées par les triggers
--
CREATE OR REPLACE FUNCTION tuna_book_insert() RETURNS TRIGGER AS $BODY$
DECLARE 
  editoraid integer;
  editorbid integer;
BEGIN 
  SELECT id INTO editoraid FROM tuna_editor ORDER BY random() LIMIT 1;
  SELECT id INTO editorbid FROM tuna_editor WHERE NOT id = editoraid ORDER BY random() LIMIT 1;

  INSERT INTO tuna_sinopsis (book_id, text) VALUES (NEW.id, md5(random()::text) );
  INSERT INTO tuna_editor_books (book_id, editor_id) VALUES (NEW.id, editoraid );
  INSERT INTO tuna_editor_books (book_id, editor_id) VALUES (NEW.id, editorbid );
  RETURN NEW;
END;
$BODY$ LANGUAGE plpgsql;


--
-- Declaration des triggers
--
CREATE TRIGGER book_insert_trigger
    AFTER INSERT ON tuna_book
    FOR EACH ROW
    EXECUTE PROCEDURE tuna_book_insert();
