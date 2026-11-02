# Python with AI & Machine Learning Course Overview Chatbot
# This chatbot provides a detailed syllabus and feature overview of the course.

def get_response(message):
    # Convert the message to lowercase and remove extra spaces
    message = message.lower().strip()
    
    # Store course sections, modules, and their detailed responses
    responses = {
        "hello": "Hello! Welcome to the 'Python with AI & Machine Learning' course chatbot. Type 'overview' or 'help' to explore!",
        "hi": "Hi! Nice to meet you. Ask me about any module, tools, or course features.",
        
        "overview": (
            "Course Title: PYTHON WITH AI & MACHINE LEARNING\n"
            "Tagline: From Basics to AI Power – Build, Analyze, Predict & Innovate[cite: 1]\n"
            "This course spans 12 comprehensive modules covering everything from Python fundamentals to building advanced AI-driven applications."
        ),
        
        "modules": (
            "Here are the 12 Modules included in this course:\n"
            "1. Python Fundamentals\n"
            "2. Control Statements\n"
            "3. Data Structures\n"
            "4. Functions & Modules\n"
            "5. Object-Oriented Programming (OOP)\n"
            "6. File & Exception Handling\n"
            "7. Python Libraries\n"
            "8. Data Analysis\n"
            "9. Machine Learning\n"
            "10. Artificial Intelligence\n"
            "11. Mini Projects\n"
            "12. Final Project\n"
            "Type 'module 1' through 'module 12' to see specific details!"
        ),
        
        "module 1": (
            "Module 1: PYTHON FUNDAMENTALS[cite: 1]\n"
            "- Introduction to Python\n"
            "- Installation & IDE Setup\n"
            "- Variables & Data Types\n"
            "- Operators\n"
            "- Input & Output\n"
            "- Type Casting\n"
            "- Comments & Indentation"
        ),
        
        "module 2": (
            "Module 2: CONTROL STATEMENTS[cite: 1]\n"
            "- If, Else, Elif\n"
            "- Nested If\n"
            "- Match Case\n"
            "- While Loop\n"
            "- For Loop\n"
            "- Break, Continue & Pass"
        ),
        
        "module 3": (
            "Module 3: DATA STRUCTURES[cite: 1]\n"
            "- Strings\n"
            "- Lists [1, 2, 3]\n"
            "- Tuples (1, 2, 3)\n"
            "- Sets {1, 2, 3}\n"
            "- Dictionaries {'a': 1, 'b': 2}\n"
            "- String Methods"
        ),
        
        "module 4": (
            "Module 4: FUNCTIONS & MODULES[cite: 1]\n"
            "- User-defined Functions\n"
            "- Lambda Functions\n"
            "- Recursion\n"
            "- Modules & Packages\n"
            "- Import & from...import\n"
            "- Virtual Environment (venv)"
        ),
        
        "module 5": (
            "Module 5: OBJECT-ORIENTED PROGRAMMING (OOP)[cite: 1]\n"
            "- Classes & Objects\n"
            "- Constructors\n"
            "- Inheritance\n"
            "- Polymorphism\n"
            "- Encapsulation\n"
            "- Abstraction"
        ),
        
        "module 6": (
            "Module 6: FILE & EXCEPTION HANDLING[cite: 1]\n"
            "- Reading & Writing Files\n"
            "- CSV Files\n"
            "- JSON Files\n"
            "- Try, Except, Finally\n"
            "- Custom Exceptions"
        ),
        
        "module 7": (
            "Module 7: PYTHON LIBRARIES[cite: 1]\n"
            "- NumPy: Numerical Computing\n"
            "- Pandas: Data Handling\n"
            "- Matplotlib: Data Visualization\n"
            "- Scikit-learn: Machine Learning Library"
        ),
        
        "module 8": (
            "Module 8: DATA ANALYSIS[cite: 1]\n"
            "- Import Datasets\n"
            "- Data Cleaning\n"
            "- Data Filtering\n"
            "- Missing Values\n"
            "- GroupBy\n"
            "- Data Visualization\n"
            "- Correlation"
        ),
        
        "module 9": (
            "Module 9: MACHINE LEARNING[cite: 1]\n"
            "- Introduction to ML & Types of Machine Learning\n"
            "- Data Preprocessing & Train-Test Split\n"
            "- Linear Regression & Logistic Regression\n"
            "- Decision Tree, Random Forest & KNN\n"
            "- Model Evaluation (Accuracy, Precision & Recall)"
        ),
        
        "module 10": (
            "Module 10: ARTIFICIAL INTELLIGENCE[cite: 1]\n"
            "- Introduction to AI & AI Applications\n"
            "- Prompt Engineering\n"
            "- AI Productivity Tools\n"
            "- Working with ChatGPT\n"
            "- AI Ethics\n"
            "- Building AI-based Python Applications"
        ),
        
        "module 11": (
            "Module 11: MINI PROJECTS[cite: 1]\n"
            "- Student Result Analysis\n"
            "- Sales Prediction\n"
            "- House Price Prediction\n"
            "- Email Spam Detection\n"
            "- Movie Recommendation System\n"
            "- AI Chatbot (Basic)\n"
            "- Face Detection"
        ),
        
        "module 12": (
            "Module 12: FINAL PROJECT[cite: 1]\n"
            "- End-to-End AI & Machine Learning Project\n"
            "- Project Documentation\n"
            "- GitHub Upload\n"
            "- Project Presentation"
        ),
        
        "tools": (
            "Tools & Technologies Covered[cite: 1]:\n"
            "- Python, Jupyter Notebook, VS Code\n"
            "- NumPy, Pandas, Matplotlib, Scikit-learn\n"
            "- Git, GitHub, ChatGPT"
        ),
        
        "features": (
            "Key Course Features[cite: 1]:\n"
            "- 100% Practical Training & Live Projects\n"
            "- AI-Based Assignments & Doubt Solving Sessions\n"
            "- Interview Preparation & Resume Building\n"
            "- GitHub Portfolio & Placement Assistance\n"
            "- Internship Certificate & Project Certificate"
        ),
        
        "help": (
            "Available Commands:\n"
            "- 'overview': Get a summary of the course\n"
            "- 'modules': List all 12 modules\n"
            "- 'module 1' to 'module 12': View details of a specific module\n"
            "- 'tools': View tools and technologies\n"
            "- 'features': View key course highlights\n"
            "- 'bye': Exit the chatbot"
        )
    }

    # Return the matching response if the message exists
    if message in responses:
        return responses[message]
    # Check for a few alternative greetings
    elif message in ["hey", "good morning", "good evening"]:
        return "Hello! What would you like to know about the AI & ML course?"
    elif "module" in message:
        return "Please specify a module number between 1 and 12 (e.g., 'module 1', 'module 9')."
    # Respond when no rule matches
    else:
        return "Sorry, I do not understand that message yet. Type 'help' to see what you can ask."

# Display a welcome message
print("PyBot: Hello! Welcome to Python with AI & Machine Learning Course Advisor.")
print("PyBot: Type 'overview' to see course summary or 'help' for example commands.")
print("PyBot: Type 'bye' to end the chat.")

# Keep chatting until the user exits
while True:
    user_message = input("You: ").strip()
    
    # Stop the loop if the user types bye
    if user_message.lower() == "bye":
        print("PyBot: Goodbye! Have a great learning journey.")
        break
        
    # Get and display the chatbot's response
    reply = get_response(user_message)
    print("PyBot:", reply)
