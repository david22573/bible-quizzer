run:
	@go build -o bin/main.exe src/main/main.go
	@bin/main.exe -p ./data/prompt.txt

test:
	go test ./ai