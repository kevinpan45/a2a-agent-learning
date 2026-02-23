class A2ASpecAgent:
    """
    Simple A2A spec agent for demonstration purposes.
    Implements basic send, receive, and process message functionality.
    """
    def __init__(self, name):
        self.name = name
        self.inbox = []

    def send_message(self, recipient, message):
        """Send a message to another agent."""
        recipient.receive_message({
            'from': self.name,
            'to': recipient.name,
            'content': message
        })

    def receive_message(self, message):
        """Receive a message and add it to the inbox."""
        self.inbox.append(message)

    def process_messages(self):
        """Process all messages in the inbox."""
        while self.inbox:
            msg = self.inbox.pop(0)
            print(f"{self.name} received message from {msg['from']}: {msg['content']}")

# Example usage:
if __name__ == "__main__":
    agent1 = A2ASpecAgent("Agent1")
    agent2 = A2ASpecAgent("Agent2")

    agent1.send_message(agent2, "Hello, Agent2!")
    agent2.process_messages()

    agent2.send_message(agent1, "Hi, Agent1! How are you?")
    agent1.process_messages()
