# MusuRAG

## Requirements

Install [python](https://www.python.org/downloads/)

Get an [OpenAI API key](https://platform.openai.com/api-keys)

## Install the project

Clone the project 

```bash
git clone git@github.com:Musubi42/MusuRAG.git
```

Install the dependencies

Set the venv
For Fish :

```bash
source venv/bin/activate.fish
```

For other bash and zsh

```bash
source mon_env/bin/activate
```

Package installation

```bash
pip install -r requirements.txt
```

## Setup the environment variables

Create a `.env` file from the `.env.example`

```bash
cp .env.example .env
```

Add your `OpenAi API KEY` instead of the placeholder, something like this :

```bash
OPENAI_API_KEY="sk-..."
```

## Setup your RAG base knowledge

To test the RAG there is a sample in the `data_example` folder.

To use your own data put your text, image, code file in the `data` folder.

Change the input folder in the `starter.py`, by `data`

```python
documents = SimpleDirectoryReader("data_example").load_data()
```

## Run the RAG

To simply start the RAG :

```bash
python starter.py
```

If you want to easily work on your project you can use the `start.sh` script.
Nodemon work too with python file.

Install `nodemon` globally :
```bash
npm i -g nodemon
```

Make the script executable :
```bash
chmod +x ./start.sh
```

Start it :
```bash
./start.sh
```


