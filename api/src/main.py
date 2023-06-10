from fastapi import FastAPI
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

#This code is used to build the API. It takes a username as input and returns a list of recommended movies for that user.

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this to the appropriate origin URL for production
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/health-check")
async def root():
    return {"message": "Api is working"}

@app.get("/recommend-movies/{username}")
async def predict(username: str):
    # Load the model
    path = os.path.abspath("pickle")
    model = pd.read_pickle(path + "/titles.pkl")

    try:
        # Get the cluster of the user
        user_cluster = model[model['username'] == username]['cluster'].values[0]
        # Get the list of users in the same cluster, but not the same user
        cluster_df = model[model['cluster'] == user_cluster]
        cluster_df = cluster_df[cluster_df['username'] != username]

        # Get the titles of the users in the cluster
        titles = []

        for i in range(4, 10):
            title = cluster_df.columns[i]
            title = title.replace("15", "").replace("\n", "").replace("\\", "").replace("'", "").replace("", "")
            titles.append(title)
    except:
        titles = ["User not found"]    

    # Create a JSON response with the titles array
    response = {"titles": list(set(titles))}
    return JSONResponse(content=response)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4567)