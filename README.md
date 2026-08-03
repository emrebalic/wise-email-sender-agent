# Wise Email Sender Agent

A small agentic AI project built with the OpenAI Agents SDK to explore how multiple AI agents can collaborate to solve a task.

The workflow is simple: three specialized writer agents generate wisdom-inspired emails from different perspectives (philosophy, history, and literature). A manager agent evaluates the drafts, selects the best one, and sends it automatically using Resend.

## What I Learned

This project was mainly a learning experience to better understand modern agentic AI systems.

Built a multi-agent workflow using the OpenAI Agents SDK.

Explored both code-based orchestration and LLM-based orchestration. In my experience, code orchestration is more predictable and reliable, while LLM orchestration provides greater flexibility and autonomy. For this project, I intentionally chose LLM orchestration to better understand its strengths and limitations.

Experimented with handoffs, but found that they reduced control over the workflow more than I wanted. Using a single manager agent with specialized tools felt like a better fit for this use case.

Learned how to use Structured Outputs so each writer agent returns a consistent Python object instead of unstructured text, making the workflow much easier to process programmatically.

Implemented email delivery with both SMTP and Resend. I ultimately chose Resend because it offers a cleaner developer experience and is better suited for modern applications.

Overall, this project gave me a much better understanding of agent orchestration, tool calling, structured outputs, and designing reliable AI workflows. It also highlighted the trade-offs between deterministic software orchestration and autonomous LLM-driven decision making.

bu kısım aynı şekilde kalsın devamında hangi toolları kullandığımıza , hangi writer toollarımız olduğuna ve onların içeriğinin ne olduğuna ve genel akışa da değin

## Tools & Workflow

The project is built around a manager agent that orchestrates three specialized writer tools. Each writer focuses on generating a wisdom-inspired email from a different perspective.

### Writer Tools

- **Philosopher Writer**
  - Generates emails inspired by philosophy, ethics, metaphysics, and famous philosophical ideas.

- **Historian Writer**
  - Generates emails based on historical events, influential figures, and lessons from history.

- **Literature Writer**
  - Generates emails inspired by classic literature, novels, and timeless stories.

Each writer returns its output as a **structured Python object**, allowing the manager agent to compare the generated emails in a consistent format.

### Email Manager

The manager agent is responsible for orchestrating the entire workflow. It:

- Calls each writer tool exactly once.
- Evaluates all generated emails.
- Selects the strongest draft.
- Converts the selected draft into plain text and HTML.
- Sends the final email using the `send_email_tool`.

### Email Delivery

The `send_email_tool` is responsible only for email delivery. It receives the final subject, plain-text body, and HTML body from the manager agent and sends the email through **Resend**.
