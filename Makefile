create_image_server:
	docker build -f server.Dockerfile -t app_server .
run_container_server:
	docker run -d -p 8001:4000 --rm --name app_server app_server
stop_container_server:
	docker stop app_server
remove_image_server:
	docker rmi app_server

upd_server:
	docker stop app_server
	docker rmi app_server
	docker build -f server.Dockerfile -t app_server .
	docker run -d -p 8001:4000 --rm --name app_server app_server
run_server:
	docker build -f server.Dockerfile -t app_server .
	docker run -d -p 8001:4000 --rm --name app_server app_server
stop_server:
	docker stop app_server
	docker rmi app_server


create_image_client:
	docker build -f client.Dockerfile -t app_client .
run_container_client:
	docker run -d -p 80:3000 --rm --name app_client app_client
stop_container_client:
	docker stop app_client
remove_image_client:
	docker rmi app_client

upd_client:
	docker stop app_client
	docker rmi app_client
	docker build -f client.Dockerfile -t app_client .
	docker run -d -p 80:3000 --rm --name app_client app_client
run_client:
	docker build -f client.Dockerfile -t app_client .
	docker run -d -p 80:3000 --rm --name app_client app_client
stop_client:
	docker stop app_client
	docker rmi app_client

run_app:
	docker build -f client.Dockerfile -t app_client .
	docker run -d -p 80:3000 --rm --name app_client app_client
	docker build -f server.Dockerfile -t app_server .
	docker run -d -p 8001:4000 --rm --name app_server app_server

stop_app:
	docker stop app_server
	docker rmi app_server
	docker stop app_client
	docker rmi app_client
