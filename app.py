import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(question),
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            max_tokens=2400
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(question):
    return """Create a syntactically correct Snowflake SQL query that answers the question asked about dbt data models that are documented in the schema.yml file below.
<Start of schema.yml>
models:
  - name: mpas_item_location
    description: MPAS Item Locations
    columns:
      - name: ITEM_ID
        description: "Unique identifier of each item"
        tests:
          - not_null
      - name: TERMINAL_ID
        description: "Unique identifier for those items that are terminals, also known as TID"
      - name: TERMINAL_SERIAL_NUMBER
        description: "Another type of unique identifier for those items that are terminals, also known as TID"
      - name: TERMINAL_STATUS
        description: ""
      - name: LOCATION_ID
        description: ""
      - name: LOCATION_DESCRIPTION
        description: ""
      - name: CONNECTION_TYPE
        description: ""
      - name: LOCATION_NAME
        description: ""
      - name: CITY
        description: ""
      - name: STREET
        description: ""
      - name: ZIP
        description: ""
      - name: COUNTRY
        description: ""
      - name: LOCATION_OUTLET_ID
        description: ""
      - name: SALTPAY_GUID
        description: ""
      - name: DEFAULT_WAREHOUSE_ID
        description: ""
      - name: WAREHOUSE
        description: ""
      - name: INSTALLATION_CODE
        description: ""
      - name: INSTALLATION_ID
        description: ""
      - name: INSTALLATION_DATE
        description: ""
      - name: MID
        description: ""
      - name: LOCATION_BRANCH_ID
        description: ""
      - name: LOCATION_COMPANY_ID
        description: ""
      - name: COMPANY_NAME
        description: ""
      - name: COMPANY_CREATED_AT
        description: ""
      - name: COMPANY_CONTACT_ID
        description: ""
      - name: COMPANY_IDENTIFICATION_NUMBER
        description: ""
      - name: COMPANY_COUNTRY_CODE
        description: ""
      - name: PROJECT_ID
        description: ""
      - name: PROJECT_CODE
        description: ""
      - name: PROJECT_NAME
        description: ""
      - name: PROJECT_COUNTRY_CODE
        description: ""
      - name: PROJECT_INSTITUTION_ID
        description: ""
      - name: INSTALLATION_STATUS_ID
        description: ""
      - name: INSTALLATION_STATUS
        description: ""
      - name: PRODUCT_ID
        description: ""
      - name: PRODUCT_NAME
        description: ""
      - name: SYSTEM_TYPE
        description: ""
      - name: TERMINAL_TYPE
        description: ""
      - name: SOFTWARE_VERSION
        description: ""
      - name: ACQUIRER
        description: ""
      - name: COMPANY_STATUS
        description: ""
      - name: PROJECT_STATUS
        description: ""
      - name: ITEM_ACTIVITY_STATUS
        description: ""
<End of schema.yml>
Question: How many terminals do we have in stock in Hungary?
SQL: SELECT COUNT(terminal_id) AS N_TERMINALS FROM mpas_item_location WHERE INSTALLATION_ID IS NULL AND PROJECT_COUNTRY_CODE = 'HUN'
Question: How many terminals do we have active in the UK?
SQL: SELECT COUNT(terminal_id) AS N_TERMINALS FROM mpas_item_location WHERE INSTALLATION_ID IS NOT NULL AND PROJECT_COUNTRY_CODE = 'GBR'
Question: {}
SQL:""".format(
        question.capitalize()
    )