<p align="center">
  <a href="https://github.com/lavague-ai/LaVague/stargazers"><img src="https://img.shields.io/github/stars/lavague-ai/LaVague.svg?style=for-the-badge" alt="Stargazers"></a>
  <a href="https://github.com/lavague-ai/LaVague/issues"><img src="https://img.shields.io/github/issues/lavague-ai/LaVague.svg?style=for-the-badge" alt="Issues"></a>
  <a href="https://github.com/lavague-ai/LaVague/network/members"><img src="https://img.shields.io/github/forks/lavague-ai/LaVague.svg?style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/lavague-ai/LaVague/graphs/contributors"><img src="https://img.shields.io/github/contributors/lavague-ai/LaVague.svg?style=for-the-badge" alt="Contributors"></a>
</p>
</br>

<div align="center">
  <img src="static/logo.png" width=140px: alt="LaVague Logo">
  <h1>Welcome to LaVague</h1>

<h4 align="center">
 <a href="https://discord.gg/SDxn9KpqX9" target="_blank">
    <!-- markdown-link-check-disable -->
    <img src="https://dcbadge.vercel.app/api/server/SDxn9KpqX9?compact=true" height='35px' alt="Join our Discord server!">
    <!-- markdown-link-check-enable -->
  </a>
  <a href="https://docs.lavague.ai/en/latest/"><img src="https://img.shields.io/badge/📄-docs-000000?style=for-the-badge&colorA=09c&colorB=555" height='35px' alt="Docs"></a>
</h4>
  <p>A Large Action Model framework for developing AI Web Agents
</p>
<h1></h1>
</div>

## 🏄‍♀️  What is LaVague?

LaVague is an **open-source Large Action Model framework** which aims to leverage **advanced AI techniques** (RAG, Few-shot learning, Chain of Thought) to develop effective AI Web Agents.

Our web agents take an objective, such as "Print installation steps for Hugging Face's Diffusers library Thought:" and performs the required actions to achieve this goal by leveraging our two core components:

- A **World Model** to break down an objective, such as "" into instructions for step-by-step web actions
- An **Action Engine** which uses to “compile” these instructions into automation code, by leveraging **Selenium** or **Playwright** & execute them

## 🚀 Getting Started

You can download the LaVague PyPi package with:

```bash
pip install lavague
```
You can then leverage our library to automate web actions based on natural language objectives:

```python
from lavague.agents import WebAgent
from lavague.actionEngine import ActionEngine
from lavague.wordModel import WorldModel

agent = WebAgent(ActionEngine(), WorldModel())
agent.get("https://huggingface.co/docs")
agent.run("Go on the quicktour of PEFT")
```
For more informatio on this example and how to use LaVague Core, see our [quick-tour](https://docs.lavague.ai/en/latest/docs/get-started/quick-tour/).

> Note, these examples use our default OpenAI API configuration and you will need to set the OPENAI_API_KEY variable in your local environment with a valid API key for these to work. For different API integrations, see our [ActionEngine integrations]().

For an end-to-end example of LaVague in a Google Colab, see our [quick-tour notebook](https://colab.research.google.com/github/lavague-ai/lavague/blob/main/docs/docs/get-started/quick-tour-notebook/quick-tour.ipynb)

## 🙋 Contributing

We would love your help and support on our quest to build a robust and reliable Large Action Model for web automation.

To avoid having multiple people working on the same things & being unable to merge your work, we have outlined the following contribution process:

1) 📢 We outline tasks on our [`backlog`](https://github.com/orgs/lavague-ai/projects/1/views/3): we recommend you check out issues with the [`help-wanted`](https://github.com/lavague-ai/LaVague/labels/help%20wanted) labels & [`good first issue`](https://github.com/lavague-ai/LaVague/labels/good%20first%20issue) labels
2) 🙋‍♀️ If you are interested in working on one of these tasks, comment on the issue! 
3) 🤝 We will discuss with you and assign you the task with a [`community assigned`](https://github.com/lavague-ai/LaVague/labels/community-assigned) label 
4) 💬 We will then be available to discuss this task with you
5) ⬆️ You should submit your work as a PR
6) ✅ We will review & merge your code or request changes/give feedback

Please check out our [`contributing guide`](./contributing.md) for a more detailed guide.

If you want to ask questions, contribute, or have proposals, please come on our [`Discord`](https://discord.gg/SDxn9KpqX9) to chat!

## 🗺️ Roadmap

TO keep up to date with our project backlog [here](https://github.com/orgs/lavague-ai/projects/1/views/2).

### 🚨 Disclaimer

Note, this project executes LLM-generated code using `exec`. This is not considered a safe practice. We therefore recommend taking extra care when using LaVague (such as running LaVague in a sandboxed environment)!
