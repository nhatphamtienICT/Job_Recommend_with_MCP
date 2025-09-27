#Extract content from pdf

import fitz #PyMuPDF

import os #load api key
from dotenv import load_dotenv
from openai import OpenAI
from apify_client import ApifyClient
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

#apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(),filetype = "pdf")

    for page in doc:
        text += page.get_text()
    return text

def ask_openai(prompt, max_tokens = 500):
    response = client.chat.completions.create(
        model= "gpt-4o",
        messages=[
            {
            "role":"user",
            "content":prompt
            }
        ],
        temperature=0.5,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content


# #Fetch LinkedIN jobs based on search query and location
# def fetch_linkedin_jobs(search_query, location="india", rows=60):
#     run_input = {
#         "title": search_query,
#         "location":location,
#         "rows": rows,
#         "proxy": {
#             "useApifyProxy": True,
#             "apifyProxyGroups": ["RESIDENTIAL"],
#         }
#     }
#     # Run the Actor and wait for it to finish
#     run = apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
#     jobs= list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
#     return jobs



# #Fetch Naukri jobs based on search query and location
# def fetch_naukri_jobs(search_query, location="india", rows=60):
#     run_input = {
#         "keyword": search_query,
#         "maxJobs": 60,
#         "freshness":"all",
#         "sortBy":"relevance",
#         "experience":"all",
# }

# # Run the Actor and wait for it to finish
#     run = apify_client.actor("wsrn5gy5C4EDeYCcD").call(run_input=run_input)
#     jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
#     return jobs
    



