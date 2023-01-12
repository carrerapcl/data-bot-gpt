# data-bot-gpt
POC of a chatbot to translate natural language into SQL queries about a set of documented tables using GPT.

## Set up

Create a `.env` file in the root folder to store your environment variables. Here you can add the following line to define your OpenAI API key:

```
export OPENAI_KEY = "<your_key>"
```

And then add `.env` to the `.gitignore` file so your keys stay safe.

7:05 yarn install