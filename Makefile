all:
	@echo "You can use this:"
	@echo "    make docker-up"
	@echo "    make docker-down"

docker-up:
	docker run --name=ticketo-postgres -p 5432:5432 -v /var/lib/postgresql/data:/var/lib/postgresql/data -e POSTGRES_PASSWORD=1 -d postgres
	docker run --name=ticketo-memcache -p 11211:11211 -d memcached

docker-down:
	docker stop ticketo-postgres
	docker stop ticketo-memcache
	docker rm ticketo-postgres
	docker rm ticketo-memcache
