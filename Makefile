build:
	go build -o prompt ./src/main/main.go

run:
	./prompt -p data/prompt.txt

test:
	go test ./ai