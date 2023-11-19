# Project Description: 
Miscellaneous ai projects that prototype the use of AI and machine learning to enhance predictive results.

You may find useful code or an approach here but the README may not be well explained and the code likely requires refactoring, sorry but these are prototypes.
However, I'll specify if a project works or does not and I will provide a video running a project.

# Projects included:
## 1. vectordb/gpt-embeddings: Vectorize documents in Pinecone vector db for LLM queries: 
  - Works at the time uploaded
  - Project downloads the [Bank of England's Monetary Policy pdf Report November 2023](https://www.bankofengland.co.uk/-/media/boe/files/monetary-policy-report/2023/november/monetary-policy-report-november-2023.pdf)
    <img width="569" alt="image" src="https://github.com/sergiosolorzano/tooling-ai/assets/24430655/88d17ae1-83ae-4d25-b5e7-6fa4e4216c68">

  - Chunk the pdf pages to vectorize each page
  - Vectorizes each page in Pinecone
  - User asks chat-gpt-3.5 a question about the document and specifies N number of embeddings (pdf pages) relevant to the question and use these to contextualize its response
  - Key feature: it uses a [GPT Retrieval Plugin](https://github.com/openai/chatgpt-retrieval-plugin), a recently released tool from OpenAI, which serves as our database interface handling all chunkings, embedding model calls, and vector database interaction.

  You can also see the Video [here](https://vimeo.com/886124664?share=copy).

<video src="https://github.com/sergiosolorzano/tooling-ai/assets/24430655/21bbd8d1-8749-43c7-b1fc-a7729d7f7f2a" controls="controls" muted="muted" playsinline="playsinline">
      </video>

  Special thanks to @Roulin for the clear instructions in the [blog](https://betterprogramming.pub/enhancing-chatgpt-with-infinite-external-memory-using-vector-database-and-chatgpt-retrieval-plugin-b6f4ea16ab8) fail this link [here](https://drive.google.com/file/d/1XQPwsg1pvsni_aT6386vrTTAqzjvgAy0/view?usp=sharing).

## 2. classification/ada_and_randomforest: Mail Spam Classification using OpenAI
  - Vectorize mail dataset with OpenAI's text-embedding-ada-002
  - Train a random forest classification model with these embedding vectors (features) and labels (mail is spam or ham type)
  - Test the model and report stats

    (oai310env) sergio@Home-Win11:~/my-repos/tooling-ai/classification/ada_and_randomforest$ ./classify_ada_rndforest.py

    OUTPUT                                               TEXT                                          embedding  class_embeddings
0      ham  go until jurong point crazy available only in ...  [-0.004949026275426149, -0.025076890364289284,...                 0
1      ham                           ok lar joking wif u oni   [-0.0046631754375994205, -0.015035536140203476...                 0
2      ham       u dun say so early hor u c already then say   [0.014811056666076183, -0.014046785421669483, ...                 0
3      ham  nah i don t think he goes to usf he lives arou...  [0.00585900479927659, 0.0007614285568706691, -...                 0
5      ham  even my brother is not like to speak with me t...  [-0.010946870781481266, -0.02851772867143154, ...                 0
4     spam  freemsg hey there darling it s been week s now...  [-0.02513720840215683, -0.018801702186465263, ...                 1
9     spam  xxxmobilemovieclub to use your credit click th...  [-0.016372570767998695, -0.0069217374548316, 0...                 1
13    spam  england v macedonia dont miss the goals team n...  [-0.013056539930403233, -0.001103076385334134,...                 1
28    spam  thanks for your subscription to ringtone uk yo...  [-0.017348436638712883, -0.019642658531665802,...                 1

    Start to train the model.
    Time elapsed to train the model for 50 mails: 0 minutes, 0 seconds, 48 milliseconds

              precision    recall  f1-score   support

           0       0.75      1.00      0.86         3
           1       1.00      0.86      0.92         7

    accuracy                           0.90        10
   macro avg       0.88      0.93      0.89        10
weighted avg       0.93      0.90      0.90        10
    
