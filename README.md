# LL(1) parser

It is a top down parser that handles certain class of grammars called LL(1) grammar.

## Run locally

Clone the repo locally and follow the steps in the terminal to install the requirements.

### For Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### For Windows

```bash
python -m venv venv
source venv\Scripts\activate.bat
pip install -r requirements.txt
```

To run the parser, run the following:

```bash
flask run
```

Then navigate to `http://localhost:5000` in your web browser.

## Grammar

The given grammar: <br>
![image](https://user-images.githubusercontent.com/52276876/206690050-c6c75f77-9592-4d7b-a7c9-c8f648dda257.png)

## Steps

The following steps are required to parse the input string with respect to the grammar:

### 1. Remove left recursion (if present) from the grammar

![image](https://user-images.githubusercontent.com/52276876/206690742-dc1b2c37-995c-4577-aa9f-472eb187c667.png)

### 2. Left factor the grammar (if required)

![image](https://user-images.githubusercontent.com/52276876/206690928-98f661ea-ca86-4fa5-a893-dc5fd717d6d3.png)

### 3. Find First and Follow from the given grammar

![image](https://user-images.githubusercontent.com/52276876/206690969-f8606cb9-92c5-49b4-b137-0db4a2b9178c.png)

### 4. Generate Parse Table using the First/Follow sets and the grammar

![image](https://user-images.githubusercontent.com/52276876/206691050-fd51abdf-858f-40bf-83bd-073b48fdb586.png)

### 5. Parse the given input string using parse table

![image](https://user-images.githubusercontent.com/52276876/206691309-81dd0c7b-9d94-4300-bf1c-18002fc1aa13.png)
