from fastapi import FastAPI
import httpx

app = FastAPI()

# Base URL for JokeAPI
JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any"

@app.get("/")
def read_root():
    return {"message": "Welcome to the Random Joke Generator!"}

@app.get("/joke")
async def get_joke():
    """
    Fetch a random joke from the JokeAPI.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(JOKE_API_URL)
        if response.status_code == 200:
            joke_data = response.json()
            # Handle single-part and two-part jokes
            if joke_data.get("type") == "single":
                return {"joke": joke_data.get("joke")}
            elif joke_data.get("type") == "twopart":
                return {
                    "setup": joke_data.get("setup"),
                    "delivery": joke_data.get("delivery"),
                }
        else:
            return {"error": "Failed to fetch a joke. Please try again later."}
