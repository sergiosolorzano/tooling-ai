# Project Description: 
<div align="center">

[![DeepWiki](https://img.shields.io/badge/DeepWiki-sergiosolorzano%2Ftooling--ai-blue.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAyCAYAAAAnWDnqAAAAAXNSR0IArs4c6QAAA05JREFUaEPtmUtyEzEQhtWTQyQLHNak2AB7ZnyXZMEjXMGeK/AIi+QuHrMnbChYY7MIh8g01fJoopFb0uhhEqqcbWTp06/uv1saEDv4O3n3dV60RfP947Mm9/SQc0ICFQgzfc4CYZoTPAswgSJCCUJUnAAoRHOAUOcATwbmVLWdGoH//PB8mnKqScAhsD0kYP3j/Yt5LPQe2KvcXmGvRHcDnpxfL2zOYJ1mFwrryWTz0advv1Ut4CJgf5uhDuDj5eUcAUoahrdY/56ebRWeraTjMt/00Sh3UDtjgHtQNHwcRGOC98BJEAEymycmYcWwOprTgcB6VZ5JK5TAJ+fXGLBm3FDAmn6oPPjR4rKCAoJCal2eAiQp2x0vxTPB3ALO2CRkwmDy5WohzBDwSEFKRwPbknEggCPB/imwrycgxX2NzoMCHhPkDwqYMr9tRcP5qNrMZHkVnOjRMWwLCcr8ohBVb1OMjxLwGCvjTikrsBOiA6fNyCrm8V1rP93iVPpwaE+gO0SsWmPiXB+jikdf6SizrT5qKasx5j8ABbHpFTx+vFXp9EnYQmLx02h1QTTrl6eDqxLnGjporxl3NL3agEvXdT0WmEost648sQOYAeJS9Q7bfUVoMGnjo4AZdUMQku50McDcMWcBPvr0SzbTAFDfvJqwLzgxwATnCgnp4wDl6Aa+Ax283gghmj+vj7feE2KBBRMW3FzOpLOADl0Isb5587h/U4gGvkt5v60Z1VLG8BhYjbzRwyQZemwAd6cCR5/XFWLYZRIMpX39AR0tjaGGiGzLVyhse5C9RKC6ai42ppWPKiBagOvaYk8lO7DajerabOZP46Lby5wKjw1HCRx7p9sVMOWGzb/vA1hwiWc6jm3MvQDTogQkiqIhJV0nBQBTU+3okKCFDy9WwferkHjtxib7t3xIUQtHxnIwtx4mpg26/HfwVNVDb4oI9RHmx5WGelRVlrtiw43zboCLaxv46AZeB3IlTkwouebTr1y2NjSpHz68WNFjHvupy3q8TFn3Hos2IAk4Ju5dCo8B3wP7VPr/FGaKiG+T+v+TQqIrOqMTL1VdWV1DdmcbO8KXBz6esmYWYKPwDL5b5FA1a0hwapHiom0r/cKaoqr+27/XcrS5UwSMbQAAAABJRU5ErkJggg==)](https://deepwiki.com/sergiosolorzano/tooling-ai)

</div>
Miscellaneous ai projects that prototype the use of AI and machine learning to enhance predictive results.

You may find useful code or an approach here but the README may not be well explained and the code likely requires refactoring, sorry but these are prototypes.
However, I'll specify if a project works or does not and I will provide a video running a project.

<p><div align="center">Git digest for performing LLM ingestion: ./gitingest/classification_digest.txt.txt and ./gitingest/vector_db_digest.txt</div></p>

<p align="center">
<img width="150" alt="star" src="https://github.com/sergiosolorzano/ai_gallery/assets/24430655/3c0b02ea-9b11-401a-b6f5-c61b69ad651b">
</p>

---------------------------------------------

# Projects included:
## 1. vectordb/gpt-embeddings: Vectorize documents in Pinecone vector db for LLM queries: 
  - Works at the time uploaded
  - Project downloads the [Bank of England's Monetary Policy pdf Report November 2023](https://www.bankofengland.co.uk/-/media/boe/files/monetary-policy-report/2023/november/monetary-policy-report-november-2023.pdf)
    <img width="569" alt="image" src="https://github.com/sergiosolorzano/tooling-ai/assets/24430655/88d17ae1-83ae-4d25-b5e7-6fa4e4216c68">

  - Chunk the pdf pages to vectorize each page
  - Vectorizes each page in Pinecone using the GPT Retrieval Plugin with web framework FastAPI(https://blog.devgenius.io/getting-started-with-fast-api-c7e52e68685f). The OpenAI released tool [GPT Retrieval Plugin](https://github.com/openai/chatgpt-retrieval-plugin) serves as our database interface handling all chunkings, embedding model calls, and vector database interaction.
  - User asks chat-gpt-3.5 a question about the document and specifies N number of embeddings (pdf pages) relevant to the question and use these to contextualize its response

  You can also see the app execution video [here](https://vimeo.com/886124664?share=copy).

<video src="https://github.com/sergiosolorzano/tooling-ai/assets/24430655/21bbd8d1-8749-43c7-b1fc-a7729d7f7f2a" controls="controls" muted="muted" playsinline="playsinline">
      </video>

  Special thanks to @Roulin for the clear instructions in the [blog](https://betterprogramming.pub/enhancing-chatgpt-with-infinite-external-memory-using-vector-database-and-chatgpt-retrieval-plugin-b6f4ea16ab8) fail this link [here](https://drive.google.com/file/d/1XQPwsg1pvsni_aT6386vrTTAqzjvgAy0/view?usp=sharing).

## 2. classification/ada_and_randomforest: Mail Spam Classification using OpenAI embeddings and a Random Forest Classification model
  - Vectorize mail [dataset](https://www.kaggle.com/code/sergiosolorzano/email-spam-filter/edit) with OpenAI's text-embedding-ada-002
  - Train a random forest classification model with these embedding vectors (features) and labels (mail is spam or ham type)
  - Test the model and report stats

    (oai310env) sergio@Home-Win11:~/my-repos/tooling-ai/classification/ada_and_randomforest$ ./classify_ada_rndforest.py

<img width="1010" alt="image" src="https://github.com/sergiosolorzano/tooling-ai/assets/24430655/2ac3ddf7-b147-4a78-bf9f-1ff1015b4a87">

    Start to train the model.
    Time elapsed to train the model for 50 mails: 0 minutes, 0 seconds, 48 milliseconds

              precision    recall  f1-score   support

           0       0.75      1.00      0.86         3
           1       1.00      0.86      0.92         7

    accuracy                           0.90        10
   macro avg       0.88      0.93      0.89        10
weighted avg       0.93      0.90      0.90        10

  Special thanks to Kaggle for the dataset and the [Geeks for Greeks community](https://www.geeksforgeeks.org/spam-classification-using-openai/) for the clear instructions

<br>If you find this helpful you can buy me a coffee :)
   
<a href="https://www.buymeacoffee.com/sergiosolorzano" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
      
