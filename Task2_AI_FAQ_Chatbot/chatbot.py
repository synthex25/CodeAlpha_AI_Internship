from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = [
    "What is artificial intelligence?",
    "Define artificial intelligence",
    "What is machine learning?",
    "Types of machine learning",
    "What is deep learning?",
    "Difference between AI and machine learning",
    "Difference between machine learning and deep learning",
    "What is NLP?",
    "What is computer vision?",
    "Applications of artificial intelligence",
    "Advantages of artificial intelligence",
    "Disadvantages of artificial intelligence",
    "Is AI dangerous?",
    "What is Python?",
    "Why Python is used for AI?",
    "What is a chatbot?",
    "How does a chatbot work?",
    "What are neural networks?",
    "What is data science?",
    "Future of artificial intelligence"
]

answers = [
    "Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence.",
    "Artificial intelligence refers to machines that can think, learn, and make decisions like humans.",
    "Machine learning is a subset of AI that allows systems to learn from data automatically.",
    "Types of machine learning include supervised, unsupervised, and reinforcement learning.",
    "Deep learning is a branch of machine learning that uses multi-layered neural networks.",
    "AI is the broader concept, while machine learning is a method used to achieve AI.",
    "Machine learning uses algorithms, while deep learning uses neural networks with many layers.",
    "Natural Language Processing enables machines to understand and interpret human language.",
    "Computer vision allows machines to interpret and analyze images and videos.",
    "AI is used in healthcare, finance, education, robotics, self-driving cars, and chatbots.",
    "AI increases efficiency, reduces human error, and automates repetitive tasks.",
    "AI can be costly, may reduce jobs, and can be risky if misused.",
    "AI is not dangerous if developed ethically and used responsibly.",
    "Python is a simple and powerful programming language widely used in AI.",
    "Python has rich libraries, simplicity, and strong community support for AI development.",
    "A chatbot is an AI system that communicates with users using text or voice.",
    "Chatbots process user input, analyze intent, and generate suitable responses.",
    "Neural networks are computing systems inspired by the human brain.",
    "Data science involves extracting insights from structured and unstructured data.",
    "The future of AI includes automation, intelligent systems, and human-AI collaboration."
]


print("=== AI FAQ Chatbot ===")
print("Ask me anything about AI")
print("Type 'exit' to quit\n")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye! 👋")
        break

    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)

    best_index = similarity.argmax()
    best_score = similarity[0][best_index]

    if best_score < 0.1:
        print("Bot: Sorry, I don't have information on that yet.")
    else:
        print("\nBot:", answers[best_index], "\n")
