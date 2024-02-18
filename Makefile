IMAGE_NAME=chuikyo-notify
CONTAINER_NAME=chuikyo-notify-container

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -it --name $(CONTAINER_NAME) --rm $(IMAGE_NAME)

stop:
	docker stop $(CONTAINER_NAME)

clean:
	docker rmi $(IMAGE_NAME)

.PHONY: build run stop clean
