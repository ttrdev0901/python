#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE test (id integer,name varchar(10));
    INSERT INTO test (id, name) VALUES (1, 'sample');
EOSQL