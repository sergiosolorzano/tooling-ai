#Project Description: 
Miscellaneous ai projects that prototype the use of AI and machine learning to enhance predictive results.

You may find useful code or an approach here but the README may not be well explained and the code likely requires refactoring, sorry but these are prototypes.
However, I'll specify if a project works or does not and I will provide a video running a project.

##Projects included:
1. vectordb/gpt-embeddings: Vectorize documents in Pinecone vector db for LLM queries: Works at the time uploaded.
  - Project downloads the [Bank of England's Monetary Policy pdf Report November 2023](https://www.bankofengland.co.uk/-/media/boe/files/monetary-policy-report/2023/november/monetary-policy-report-november-2023.pdf)
    <img width="593" alt="image" src="https://github.com/sergiosolorzano/tooling-ai/assets/24430655/7623fe4b-b62e-4453-b7f2-adf4a60efdee">

  - Chunk the pdf pages to vectorize each page
  - Vectorizes each page in Pinecone
  - User asks chat-gpt-3.5 a question about the document and specifies N number of embeddings (pdf pages) relevant to the question and use these to contextualize its response

  You can also see the Video [here](https://vimeo.com/886124664?share=copy).

  Special thanks to @Roulin for the clear instructions in the blog(https://betterprogramming.pub/enhancing-chatgpt-with-infinite-external-memory-using-vector-database-and-chatgpt-retrieval-plugin-b6f4ea16ab8) fail this link here(https://drive.google.com/file/d/1XQPwsg1pvsni_aT6386vrTTAqzjvgAy0/view?usp=sharing). No need to add a how-to here.

    

    