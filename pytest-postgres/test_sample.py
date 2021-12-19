import pytest
from pytest_postgresql import factories
import psycopg

# def is_postgres_ready(docker_ip):
#     try:
#         psycopg.connect(
#                     user="postgres",
#                     password="password",
#                     host=docker_ip,
#                     dbname="test",
#                     port=5432,
#                     connection_timeout=5
#                     )
#         return True
#     except:
#         return False

# @pytest.fixture(scope="session")
# def database_service(docker_ip, docker_services):
#     docker_services.wait_until_responsive(
#         timeout=30.0, pause=0.1, check=lambda: is_postgres_ready(docker_ip)
#     )
#     return

postgresql_in_docker = factories.postgresql_noproc()
postgresql = factories.postgresql("postgresql_in_docker", dbname="test")

def test_function(postgresql):
    cur = postgresql.cursor()
    cur.execute("select * from test")
    res = cur.fetchall()

    print(res)

