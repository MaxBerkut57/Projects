import httpx


BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 5


def get_todo(todo_id):
    try:
        response = httpx.get(f"{BASE_URL}/todos/{todo_id}", timeout=TIMEOUT)
        response.raise_for_status()
        return response.status_code, response.json()
    except httpx.HTTPStatusError as e:
        print(f"Код {e.response.status_code}")
        return None
    except httpx.TimeoutException:
        print(f"Сервер не ответил за {TIMEOUT} секунд")
        return None
    except httpx.RequestError:
        print("не удалось подключиться к серверу")
        return None


def create_post(title, body):
    try:
        response = httpx.post(f"{BASE_URL}/posts", json={"title": title, "body": body},
                              timeout=TIMEOUT)
        response.raise_for_status()
        return response.status_code, response.json()
    except httpx.HTTPStatusError as e:
        print(f"Код {e.response.status_code}")
        return None
    except httpx.TimeoutException:
        print(f"Сервер не ответил за {TIMEOUT} секунд")
        return None
    except httpx.RequestError:
        print("не удалось подключиться к серверу")
        return None


def main():
    response = get_todo(todo_id=1)
    print(response)
    response = get_todo(todo_id=9999)
    response = create_post("abc", "{'abc' = 123}")
    print(response)


if __name__ == "__main__":
    main()