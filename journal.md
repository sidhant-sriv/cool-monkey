# `django-admin startproject coolmonkey`

Right now I basically need to start the backend for the project cycle. Essentially just take some text data in json format from client. 
For now just take the string and save it in a text file.

Ok so fuck the text file. Now I need to take the text prompt and do something with it. 
Should I make a separate function that makes request to an API with some params or should I just make a whole ass inference API.
I get to dockerize the API and make like a microservice thing.

I don't fucking know let's just try to find an API first. I think I'll just do the separate function thing.

OK so I did some random bullshit. 
I'm using the palm 2 API. Thank fuck for that. 
I wonder if they have an embeddings API. 
Anyway. Now that we can get the script for the reel, we can start with the following

- Voiceover generation
- Editing the prompt made on frontend
- Getting DALLE or Stable diffusion to generate some images based on the prompt
- Putting all of these things together. (I genuinely have no idea how to do the video thing so I'm feeling kinda fucked rn)

Need to figure out handler for the regenerate button. 
Also need to make some edits to the prompt itself so that its cleaner.