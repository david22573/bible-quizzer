package main

import (
	"bufio"
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"sync"
	"time"

	"github.com/joho/godotenv"
)

// Define structs for the request body
type RequestBody struct {
	Model    string    `json:"model"`
	Messages []Message `json:"messages"`
}

type Message struct {
	Role    string `json:"role"`
	Content string `json:"content"`
}

// Response struct for parsing the API response
type Response struct {
	Choices []struct {
		Message struct {
			Content string `json:"content"`
		} `json:"message"`
	} `json:"choices"`
}

// Function to make the HTTP request
func queryModel(ctx context.Context, wg *sync.WaitGroup, apiKey, model string, content string) string {
	defer wg.Done()
	url := "https://openrouter.ai/api/v1/chat/completions"
	requestBody := RequestBody{
		Model: model,
		Messages: []Message{
			{Role: "user", Content: content},
		},
	}

	jsonValue, err := json.Marshal(requestBody)
	if err != nil {
		panic(err)
	}

	req, err := http.NewRequestWithContext(ctx, "POST", url, bytes.NewBuffer(jsonValue))
	if err != nil {
		panic(err)
	}

	req.Header.Set("Authorization", fmt.Sprintf("Bearer %s", apiKey))
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	var response Response
	if err := json.Unmarshal(body, &response); err != nil {
		panic(err)
	}
	if len(response.Choices) > 0 {
		fmt.Println("Model: " + model)
		return response.Choices[0].Message.Content
	} else {
		return "No choices in response"
	}
}

// Main function
func main() {
	// Load .env file
	err := godotenv.Load()
	if err != nil {
		log.Fatalf("Error loading .env file: %s", err)
	}

	models := []string{
		"nousresearch/hermes-3-llama-3.1-405b",
		"meta-llama/llama-3.1-8b-instruct:free",
	}

	apiKey := os.Getenv("OPENROUTER_API_KEY")
	if apiKey == "" {
		log.Fatal("OPENROUTER_API_KEY not found in environment variables")
	}

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Minute)
	defer cancel()

	var wg sync.WaitGroup
	// get prompt from user in terminal
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter prompt: ")
	content, _ := reader.ReadString('\n')
	for _, model := range models {
		wg.Add(1)
		go func(model string) {
			res := queryModel(ctx, &wg, apiKey, model, content)
			fmt.Println(res)
		}(model)
	}

	wg.Wait()
}
