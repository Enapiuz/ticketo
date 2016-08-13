CREATE ROLE ticketo LOGIN PASSWORD '1'
   VALID UNTIL 'infinity';

CREATE DATABASE ticketo
  WITH ENCODING='UTF8'
       OWNER=ticketo
       CONNECTION LIMIT=-1;


CREATE TABLE public.tickets
(
  id          INTEGER NOT NULL DEFAULT nextval('tickets_id_seq' :: REGCLASS),
  create_date DATE    NOT NULL,
  change_date DATE    NOT NULL,
  topic       TEXT    NOT NULL,
  content     TEXT,
  email       TEXT,
  state       INTEGER NOT NULL,
  CONSTRAINT id_primary PRIMARY KEY (id)
);

CREATE TABLE public.ticket_comments
(
  id          INTEGER NOT NULL DEFAULT nextval('ticket_comments_id_seq' :: REGCLASS),
  ticket_id   INTEGER NOT NULL,
  create_date DATE    NOT NULL,
  email       TEXT    NOT NULL,
  content     TEXT    NOT NULL,
  CONSTRAINT ticket_id_foreign FOREIGN KEY (ticket_id)
  REFERENCES public.tickets (id) MATCH SIMPLE
  ON UPDATE CASCADE ON DELETE CASCADE
);
