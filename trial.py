docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_tax" \
  -v /c:/Users/User/OneDrive/Desktop/DE_Zoomcamp/docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5431:5432 \
  postgres:13

#Command to run pgAdmin in docker
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL='admin@admin.com' \
  -e PGADMIN_DEFAULT_PASSWORD='root' \
  -p 8080:80 \
  dpage/pgadmin4


#Run on network
docker network create pg-network2

docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_tax" \
  -v /c:/Users/User/OneDrive/Desktop/DE_Zoomcamp/docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5431:5432 \
  --network=pg-network2 \
  --name pg-database \
  postgres:13

docker run -it \
  -e PGADMIN_DEFAULT_EMAIL='admin@admin.com' \
  -e PGADMIN_DEFAULT_PASSWORD='root' \
  -p 8080:80 \
  --network=pg-network2 \
  --name pgadmin \
  dpage/pgadmin4

docker build -t taxi_ingest:v001 .

docker run taxi_ingest:v001 \
  