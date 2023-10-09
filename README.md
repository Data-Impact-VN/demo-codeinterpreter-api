# CodeInterpreter API demo

This is a demo for [Code Interpreter API](https://github.com/shroominic/codeinterpreter-api) to check if these requirements can be statisfied:

_(Sample generated charts can be found at `./out` folder)_

- Generate a chart from an user prompt and a csv file

> Answer: Possible

- Generate a chart with text description from an user prompt and a csv file

> Answer: Possible

- Generate a chart with text description from an user prompt and a numpy file

> Answer: NOT possible
>
> - If a npy file provided, it will return "It seems that the dataset you uploaded is empty or does not contain any data. Please make sure the dataset file is correct and contains valid data."
>
> - If a npz file provided, it will timeout

- Check what graph can create ?

> Answer: We can create any type of chart, as long as we give a clear instruction.
>
> A good instruction should be: "Analyze this dataset and plot `{type_of_chart}` about `{interested_topic}` using `{column_name(s)}`".

- Can we customize graph or not ?

> Answer: We can't customize the produced image, since it is raw png file(s).
>
> We can only customize the result by changing the prompt.

### Project Setup

_You can choose either pipenv or just use virtualenv or directly._

If using directly

```
pip install -r requirements.txt
cp .env.example .env   --> add your OPEN_API_KEY
```

If using `pipenv`

```
pipenv shell
pipenv install
cp .env.example .env   --> add your OPEN_API_KEY
```

If using `virtualenv`

```
virtualenv venv
source venv/bin/activate
cp .env.example .env   --> add your OPEN_API_KEY
```

### Usage

Generate chart using dataset files in `/in` directory

```
make start
```

Clean generated output

```
make clean
```

To change prompt or file, modify `src/main.py`
