
# 🤖 AI Document Understanding and Question Answering

This project aims to provide AI-powered document understanding and question answering services. Leveraging advanced models such as Google's Gemini and a high-performance vector database like Pinecone, the system efficiently processes and analyzes text data to provide accurate and insightful answers to inquiries.

## 🚀 Features

- **Advanced AI Models:** Utilizes Google's Gemini model for document understanding and question answering.
- **Efficient Vector Database:** Employs Pinecone for high-performance vector storage and retrieval.
- **Document Processing:** Processes text documents to extract relevant information and generate embeddings.
- **Question Answering:** Provides accurate answers to user queries based on the content of the documents.
- **Scalable Infrastructure:** Utilizes serverless Pinecone indexing for scalable and cost-effective storage and retrieval.

## 💻 Installation

To run ExploraAi locally, follow these steps:


1. Clone the repository to your local machine:

```
https://github.com/KushanManahara/AI-Powered-Document-Understanding-and-Question-Answering-Specialist.git
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Set up your Google GeminiAIAPI key, Pinecone API key and Pinecone environment by creating a .env file and adding your API key:
```
echo "GOOELE_API_KEY = <your_api_key_here> >> .env
echo "PINECONE_API_KEY = <your_api_key_here> >> .env
echo "PINECODE_ENV" = <your_api_key_here> >> .env
```
or you can add that api key directly into your .env file


You're all set! Start exploring Gimhara ChatBot.


## 🛠️ Getting Started

To get started with Gimhara ChatBot, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the Streamlit app using `python3 main.py`.



## 🚀 Usage

1. Prepare your text data and place it in the `data` directory.
2. Run the main script to initialize the Pinecone index, process the documents, and perform question answering
```
python3 main.py

```


3. Access the results through the generated Markdown file.

## 🔑 Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`GOOGLE_API_KEY`
`PINECONE_API_KEY`
`PINECODE_ENV`
## 📚 Lessons Learned

During the development of the AI Document Understanding and Question Answering project, several valuable lessons were learned and challenges were encountered:

### Integration with Google Generative AI Model

- **Gemini Model Integration**: Integrating with the Gemini AI model from Google required a deep understanding of the model's capabilities and the API's authentication process. Configuring the API key and effectively handling responses from the Gemini model were critical for successful integration.

### Pinecone Vector Database Integration

- **Pinecone Vector Database**: Integrating with Pinecone for vector storage and retrieval provided efficient handling of document embeddings. Understanding Pinecone's indexing and query mechanisms optimized the performance of the document search functionality.

### Streamlit Application Development

- **Streamlit Development**: Developing the Streamlit application involved mastering the creation of interactive widgets, handling user input effectively, and displaying dynamic content. Understanding Streamlit's layout and functionality was pivotal in creating a user-friendly and responsive interface.

### Python Programming

- **Proficiency in Python**: Extensive use of the Python programming language was necessary for implementing the document processing pipeline, managing Pinecone indexing, and handling user interactions. Leveraging Python libraries streamlined various aspects of application development.

### User Interaction and Experience

- **Designing Intuitive User Interaction**: Crafting an intuitive user interaction flow required thoughtful consideration of user queries, robust error handling, and providing informative feedback. Balancing simplicity and functionality was paramount to ensuring a positive user experience.

### Testing and Debugging

- **Thorough Testing**: Rigorous testing with diverse inputs and scenarios was instrumental in identifying potential issues, such as handling errors during Pinecone queries, managing state across document processing, and ensuring consistent behavior across different user queries.

### Documentation and Best Practices

- **Comprehensive Documentation**: Documenting the project's architecture, implementation details, and usage instructions facilitated collaboration and ensured the reproducibility of results. Adhering to best practices in software engineering and AI development promoted code maintainability and scalability.

## 🤝 Contributing

We welcome contributions from the community to enhance ExploraAi. If you're interested in contributing, please follow these guidelines:

- Fork the repository and create a new branch for your feature or bug fix.
- Ensure your code follows the project's coding standards.
- Submit a pull request detailing your changes and their purpose.

## 🧑‍💼 About Me
### Kushan Manahara

I'm a final year undergraduate student pursuing Computer Engineering at the University of Peradeniya. My passion lies in research, AI development, and automation. I thrive on exploring new technologies and pushing the boundaries of what's possible in the realm of artificial intelligence.

Whether it's diving into the intricacies of machine learning algorithms or crafting seamless user experiences through full stack development, I'm driven by a relentless curiosity and a desire to make meaningful contributions to the field of technology.

Feel free to reach out if you'd like to collaborate on exciting projects or discuss ideas at the intersection of technology and innovation.

Connect with me on [LinkedIn]([Your_LinkedIn_Profile_URL](https://www.linkedin.com/in/kushan-manahara/))
## 💡 Skills
- **Full Stack Development**
- **LLM Development** (Large Language Models)
- **ML Development** (Machine Learning)
- **Web Automation**
- **AI Development** (Artificial Intelligence)

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://kushan-portfollio.vercel.app/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kushan-manahara/)

## ✍️ Authors
- [@KushanManahara](https://github.com/KushanManahara/)
## 🎖️ Badges
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)