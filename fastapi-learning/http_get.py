import httpx

def main():
    response = httpx.get("https://jsonplaceholder.typicode.com/todos/1", timeout=5)
    print(response.status_code)
    print(response.json())

if __name__ == "__main__":
    main()