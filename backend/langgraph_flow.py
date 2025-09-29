from langgraph.graph import Graph

def run_flow(user_message):
    graph = Graph()

    # Simple flow: user input → AI response
    def reply_node(inputs):
        import google.generativeai as genai
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(inputs["msg"])
        return {"output": response.text}

    graph.add_node("reply", reply_node)
    graph.set_entry_point("reply")

    result = graph.run({"msg": user_message})
    return result["output"]
