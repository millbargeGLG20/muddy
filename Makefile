build:
	docker build -t muddy:latest .

run:
	docker run --name muddy -d -p 5000:5000 -e API_TOKEN=$(API_TOKEN) -e ZIP_CODE=$(ZIP_CODE) muddy
	docker ps

logs:
	docker logs -f muddy

clean:
	# docker system prune -af
	docker stop muddy
	docker rm muddy
