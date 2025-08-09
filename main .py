import random
import datetime
import math
import re
import requests # Import the requests library for web searches

class EnhancedAI:
    def __init__(self):
        self.conversation_history = []
        self.user_name = None
        self.context = {}

    def get_ai_response(self, user_input):
        user_input = user_input.strip()
        original_input = user_input
        user_input_lower = user_input.lower()

        # Store conversation history
        self.conversation_history.append({"user": original_input, "timestamp": datetime.datetime.now()})

        # Web search functionality
        if user_input_lower.startswith("search:"):
            query = user_input[7:].strip() # Extract the search query
            return self.perform_web_search(query)

        # Name learning and personalization
        if self.user_name is None and ("my name is" in user_input_lower or "i'm" in user_input_lower or "i am" in user_input_lower):
            name_match = re.search(r"(?:my name is|i'm|i am)\s+(\w+)", user_input_lower)
            if name_match:
                self.user_name = name_match.group(1).title()
                return f"Nice to meet you, {self.user_name}! I'll remember your name. How can I help you today?"

        # Greeting responses with personalization
        if any(word in user_input_lower for word in ["hi", "hello", "hey", "greetings"]):
            greeting = f"Hello{f', {self.user_name}' if self.user_name else ''}!"
            responses = [
                f"{greeting} I'm an enhanced AI assistant. How can I help you today?",
                f"{greeting} I'm here to assist you with coding, math, questions, and much more!",
                f"{greeting} I'm your AI companion ready to help. What would you like to explore?"
            ]
            return random.choice(responses)

        # Math calculations
        if any(word in user_input_lower for word in ["calculate", "math", "plus", "minus", "times", "divided", "+", "-", "*", "/"]):
            return self.handle_math(user_input)

        # Enhanced coding capability responses
        elif any(word in user_input_lower for word in ["code", "programming", "python", "javascript", "java", "c++", "html", "css"]):
            responses = [
                "I'm excellent at coding! I can help with Python, JavaScript, Java, C++, HTML, CSS, and many other languages. I can write code, debug, explain algorithms, review code quality, and help with best practices. What coding challenge are you working on?",
                "Absolutely! I'm proficient in multiple programming languages and can assist with:\n• Writing clean, efficient code\n• Debugging and troubleshooting\n• Code reviews and optimization\n• Algorithm design\n• Best practices and design patterns\nWhat programming task can I help you with?",
                "Yes! I love helping with code! Whether you need help building applications, solving algorithms, learning new concepts, or debugging issues, I'm here to help. What programming language or project are you working with?"
            ]
            return random.choice(responses)

        # Simple game requests
        elif "game" in user_input_lower:
            if "car" in user_input_lower or "racing" in user_input_lower:
                return "I can help you create a simple car game! Would you like me to create a basic text-based racing game, or are you thinking of something with graphics using pygame or HTML5 canvas? Let me know what kind of car game you have in mind!"
            else:
                return "I'd love to help you create a game! What type of game are you thinking of? Some options I can help with:\n• Text-based games (like adventure or trivia)\n• Simple arcade games with pygame\n• Web games with HTML5/JavaScript\n• Card games or board games\nWhat sounds interesting to you?"

        # Time and date
        elif any(word in user_input_lower for word in ["time", "date", "today", "now"]):
            now = datetime.datetime.now()
            return f"The current time is {now.strftime('%I:%M %p')} and today's date is {now.strftime('%A, %B %d, %Y')}."

        # Weather (simulated since we don't have real API)
        elif "weather" in user_input_lower:
            weather_conditions = ["sunny", "cloudy", "partly cloudy", "rainy", "clear"]
            temp = random.randint(65, 85)
            condition = random.choice(weather_conditions)
            return f"I don't have access to real weather data, but I can simulate: It's currently {condition} and {temp}°F. For real weather updates, I'd recommend checking a weather app or website!"

        # Enhanced AI-related questions
        elif any(word in user_input_lower for word in ["ai", "artificial intelligence", "machine learning", "neural network"]):
            responses = [
                "I'm an AI assistant powered by language models! I can help with coding, answer questions, solve problems, have conversations, and assist with learning. I'm designed to be helpful, informative, and engaging. What would you like to know about AI or how I can help you?",
                "As an AI, I use machine learning to understand and respond to your messages. I can assist with programming, mathematics, creative writing, problem-solving, and general knowledge questions. I'm continuously learning from our conversation to provide better help. How can I assist you today?",
                "I'm an artificial intelligence designed to be your helpful assistant! I can code, calculate, explain concepts, help with projects, and have meaningful conversations. While I'm not perfect, I strive to be accurate and useful. What AI capabilities are you curious about?"
            ]
            return random.choice(responses)

        # Help requests with enhanced information
        elif "help" in user_input_lower:
            help_text = f"""I'm here to help{f', {self.user_name}' if self.user_name else ''}! Here's what I can assist you with:

🔧 **Programming & Development**
• Write code in multiple languages
• Debug and optimize existing code
• Explain programming concepts
• Help with algorithms and data structures

🧮 **Mathematics & Calculations**
• Solve equations and word problems
• Perform calculations
• Explain mathematical concepts

🔍 **Web Search**
• Search the internet for information
• Use 'search: your query' to find answers
• Get definitions, facts, and explanations

💡 **General Assistance**
• Answer questions on various topics
• Help with creative projects
• Provide explanations and tutorials
• Have engaging conversations

🎮 **Fun Features**
• Create simple games
• Tell jokes or stories
• Help with creative writing

Just tell me what you need help with, and I'll do my best to assist you!"""
            return help_text

        # Jokes
        elif "joke" in user_input_lower:
            jokes = [
                "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
                "Why don't scientists trust atoms? Because they make up everything!",
                "How do you comfort a JavaScript bug? You console it! 😄",
                "Why did the Python programmer break up with the Java programmer? Because Java was too verbose!",
                "What's a computer's favorite snack? Microchips! 🍪"
            ]
            return random.choice(jokes)

        # Conversation history
        elif "history" in user_input_lower or "remember" in user_input_lower:
            if len(self.conversation_history) > 1:
                return f"I remember our conversation! We've exchanged {len(self.conversation_history)} messages so far. I can recall what we've discussed if you need me to reference something specific."
            else:
                return "This is the beginning of our conversation! I'll remember what we discuss as we continue chatting."




        # Enhanced default responses with context awareness
        else:
            if len(self.conversation_history) > 3:
                responses = [
                    f"I'm not sure I understand that{f', {self.user_name}' if self.user_name else ''}. Could you please rephrase or provide more details?",
                    "That's interesting! Could you tell me more about what you're looking for? I'm here to help with coding, math, questions, or just chatting!",
                    "I'd like to help, but I need a bit more context. Are you looking for help with programming, need information about something, or want to try something fun?",
                ]
            else:
                responses = [
                    "I'm not sure I understand that. Could you please rephrase your question?",
                    "That's interesting! Could you tell me more about what you're looking for?",
                    "I'd like to help, but I need a bit more context. What specifically are you trying to do?",
                    "I'm here to assist! Could you clarify what you'd like help with? I can help with coding, math, questions, and more!"
                ]
            return random.choice(responses)

    def handle_math(self, user_input):
        """Handle mathematical calculations and problems"""
        try:
            # Extract numbers and basic operations
            numbers = re.findall(r'-?\d+\.?\d*', user_input)

            if len(numbers) >= 2:
                a, b = float(numbers[0]), float(numbers[1])

                if any(op in user_input.lower() for op in ["plus", "+", "add"]):
                    result = a + b
                    return f"{a} + {b} = {result}"
                elif any(op in user_input.lower() for op in ["minus", "-", "subtract"]):
                    result = a - b
                    return f"{a} - {b} = {result}"
                elif any(op in user_input.lower() for op in ["times", "*", "multiply"]):
                    result = a * b
                    return f"{a} × {b} = {result}"
                elif any(op in user_input.lower() for op in ["divided", "/", "divide"]):
                    if b != 0:
                        result = a / b
                        return f"{a} ÷ {b} = {result}"
                    else:
                        return "I can't divide by zero! That would break mathematics! 😅"
                elif "power" in user_input.lower() or "^" in user_input:
                    result = a ** b
                    return f"{a} raised to the power of {b} = {result}"

            elif len(numbers) == 1:
                num = float(numbers[0])
                if "square root" in user_input.lower() or "sqrt" in user_input.lower():
                    if num >= 0:
                        result = math.sqrt(num)
                        return f"The square root of {num} = {result}"
                    else:
                        return "I can't calculate the square root of a negative number (in real numbers)!"
                elif "factorial" in user_input.lower():
                    if num >= 0 and num == int(num):
                        result = math.factorial(int(num))
                        return f"The factorial of {int(num)} = {result}"
                    else:
                        return "Factorial is only defined for non-negative integers!"

            # Try to evaluate simple expressions safely
            safe_expr = re.sub(r'[^0-9+\-*/.() ]', '', user_input)
            if safe_expr and any(char in safe_expr for char in ['+', '-', '*', '/']):
                try:
                    result = eval(safe_expr)
                    return f"{safe_expr} = {result}"
                except:
                    pass

            return "I can help with math! Try asking me to add, subtract, multiply, divide numbers, or calculate square roots and factorials. For example: 'What's 15 + 27?' or 'Calculate the square root of 64'"

        except Exception as e:
            return "I had trouble with that calculation. Could you try rephrasing it? For example: 'What's 5 + 3?' or 'Calculate 10 times 7'"

    def perform_web_search(self, query):
        """Performs a web search using free APIs"""
        if not query.strip():
            return "Please provide a search query after 'search:'"

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        
        try:
            # First try Wikipedia API for general information
            wiki_search_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{requests.utils.quote(query)}"
            response = requests.get(wiki_search_url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('extract') and len(data['extract']) > 20 and 'disambiguation' not in data.get('type', ''):
                    title = data.get('title', query)
                    extract = data['extract']
                    page_url = data.get('content_urls', {}).get('desktop', {}).get('page', '')
                    
                    result = f"🔍 **{title}**\n\n{extract}"
                    if page_url:
                        result += f"\n\n🌐 Source: {page_url}"
                    return result

        except Exception:
            pass

        try:
            # Try Wikipedia search API for broader results
            search_url = "https://en.wikipedia.org/w/api.php"
            search_params = {
                'action': 'query',
                'format': 'json',
                'list': 'search',
                'srsearch': query,
                'srlimit': 3
            }
            
            response = requests.get(search_url, params=search_params, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if 'query' in data and 'search' in data['query'] and len(data['query']['search']) > 0:
                    results = []
                    for i, item in enumerate(data['query']['search'][:3]):
                        title = item.get('title', 'No title')
                        snippet = item.get('snippet', 'No description available').replace('<span class="searchmatch">', '').replace('</span>', '')
                        page_url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
                        
                        result_text = f"**{i+1}. {title}**\n{snippet}"
                        results.append(result_text)
                    
                    result = f"🔍 Search Results for '{query}':\n\n" + "\n\n".join(results)
                    result += f"\n\n🌐 Source: Wikipedia"
                    return result

        except Exception:
            pass

        try:
            # Try free DuckDuckGo instant answer API
            ddg_url = "https://api.duckduckgo.com/"
            ddg_params = {
                'q': query,
                'format': 'json',
                'no_html': '1',
                'skip_disambig': '1'
            }
            
            response = requests.get(ddg_url, params=ddg_params, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                # Check for abstract
                if data.get('Abstract') and len(data['Abstract']) > 20:
                    abstract = data['Abstract']
                    heading = data.get('Heading', query)
                    source = data.get('AbstractSource', 'DuckDuckGo')
                    url = data.get('AbstractURL', '')
                    
                    result = f"🔍 **{heading}**\n\n{abstract}"
                    if url:
                        result += f"\n\n🌐 Source: {url}"
                    else:
                        result += f"\n\n🌐 Source: {source}"
                    return result
                
                # Check for definition
                if data.get('Definition') and len(data['Definition']) > 10:
                    definition = data['Definition']
                    source = data.get('DefinitionSource', 'DuckDuckGo')
                    url = data.get('DefinitionURL', '')
                    
                    result = f"🔍 **Definition of {query}**\n\n{definition}"
                    if url:
                        result += f"\n\n🌐 Source: {url}"
                    else:
                        result += f"\n\n🌐 Source: {source}"
                    return result

        except Exception:
            pass

        # Final fallback
        return f"🔍 I couldn't find specific information about '{query}' right now. The search APIs might be temporarily unavailable or the query might need to be more specific.\n\nTry:\n• Using different keywords\n• Being more specific\n• Asking me directly - I might know about it!"

    


def main():
    ai = EnhancedAI()
    print("🤖 Enhanced AI Assistant: Hello! I'm your upgraded AI assistant with improved capabilities!")
    print("I can help with coding, math, conversations, and much more. Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit", "bye", "goodbye"]:
            farewell = f"Goodbye{f', {ai.user_name}' if ai.user_name else ''}! It was great chatting with you. Have a wonderful day! 👋"
            print(f"🤖 Enhanced AI: {farewell}")
            break

        if user_input.strip():
            response = ai.get_ai_response(user_input)
            print(f"🤖 Enhanced AI: {response}")
        else:
            print("🤖 Enhanced AI: Please say something! I'm here and ready to help! 😊")

if __name__ == "__main__":
    main()
