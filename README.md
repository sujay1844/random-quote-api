# Random quote API

This is an API that returns a random quote.

It uses `flask` for API endpoints.

There are 3 versions of the API:
1. `pandas`
2. `sqlite`
3. `redis`

# Usage

To run this,
- Install `python`
- Download and extract this project from [here](https://github.com/sujay1844/random-quote-api/archive/refs/heads/main.zip)
- Open a terminal/cmd in `random-quote-api-main` folder and run,
```bash
pip install -r requirements.txt
```
- To run the `pandas` version,
```bash
python random-quote-api-pandas.py
```
- To run the `sqlite` version,
```bash
python random-quote-api-sqlite.py
```
- To run the `redis` version,
```bash
docker compose up -d
python random-quote-api-redis.py
```
- Open http://localhost:8080 in your browser to get a random quote

# Credits

The dataset used in this project was obtained from [here](https://github.com/ShivaliGoel/Quotes-500K).
