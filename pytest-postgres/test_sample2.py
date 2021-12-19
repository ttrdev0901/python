from pytest_postgresql import factories

postgresql_in_docker = factories.postgresql_noproc()
postgresql = factories.postgresql("postgresql_in_docker", dbname="test")


def test_postgres_docker(postgresql):
    """Run test."""
    cur = postgresql.cursor()
    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    postgresql.commit()
    cur.close()