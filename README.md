# Artificial Intelligence (AI) Architectural Governance 

Artificial Intelligence is no longer just a technical discipline—it is an organizational capability that brings together data, models, governance, and decision-making into a unified system. This body of work explores AI not only from the perspective of building machine learning models, but also through the broader lenses of data literacy, system design, and enterprise-scale decision intelligence. The journey begins with foundational insights in *Lessons in A.I. from a Budding Machine Learning Engineer*, where practical experience shapes an understanding of how AI systems are developed in real-world environments. From there, *Data Literacy* emphasizes the importance of understanding data as the core ingredient in any intelligent system.

Using relatable metaphors, the series continues with *Sweet Potato Pie* and *Mixed Fruit*, illustrating how raw ingredients—data, features, and transformations—must be carefully combined to produce meaningful outcomes. This leads into deeper technical exploration in *Getting to the Core – Part I* and *Part II*, where the inner workings of models and feature representations are examined more closely. Building on this foundation, *Finding the Right Recipe* focuses on selecting appropriate algorithms and approaches for specific problems, reinforcing the idea that successful AI systems depend on both art and science. The series then introduces adaptive decision-making through *A Brief Introduction to Reinforcement Learning – Part I* and *Part II*, highlighting how systems can learn from interaction and feedback to improve over time.

As AI systems become embedded in enterprise environments, Architectural Governance, Risk, and Compliance (GRC) becomes essential. Governance is no longer a static checkpoint but an integrated, continuous process within the architecture itself. By embedding fitness functions and automated validation into the development lifecycle, organizations can ensure that AI systems remain reliable, explainable, and aligned with both regulatory requirements and business objectives. This approach transforms governance into a dynamic capability—one that evolves alongside the system while maintaining accountability and trust.

At its core, AI is about decision-making, and this is where Enterprise Decision Management (EDM) plays a critical role. AI models are not isolated artifacts; they are components within larger decision pipelines that influence operations, strategy, and customer outcomes. By combining AI with structured decision frameworks, organizations can move beyond reactive analytics toward proactive and even autonomous systems. When paired with approaches like reinforcement learning, these systems continuously refine their decisions based on feedback, enabling more intelligent and adaptive behavior over time.

Ultimately, AI is not just about building models—it is about building systems that learn, adapt, and make decisions responsibly. By integrating strong data foundations, thoughtful model design, and embedded governance, organizations can unlock the full potential of AI while maintaining control, transparency, and long-term value.


## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Configuration](#configuration)
  - [Environment Variables](#environment-variables)
  - [Secrets Management](#secrets-management)
- [Architecture](#architecture)
  - [System Diagram](#system-diagram)
  - [Data Sources](#data-sources)
    - [Redshift](#redshift)
    - [Neo4j](#neo4j)
- [OHS Incident Report](#ohs-incident-report)
  - [Example Scenario](#example-scenario)
  - [Generated Output](#generated-output)
- [External Resources](#external-resources)
  - [LangChain Docs](https://python.langchain.com/docs/)
  - [AWS Redshift Docs](https://docs.aws.amazon.com/redshift/)
  - [Neo4j Cypher Guide](https://neo4j.com/docs/cypher-refcard/current/)
- [Contributing](#contributing)
- [License](#license)
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [ssh key](https://docs.github.com/en/enterprise/2.15/user/articles/adding-a-new-ssh-key-to-your-github-account)
* [awscli](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html)
* [![Poetry][Poetry.org]][Poetry-url]
* [![Docker][Docker.com]][Docker-url]
* [![Python][Python.org]][Python-url]

Below is the list things you need to use the software and how to install them. Note, these instructions assume you are
using a Mac OS. If you are using Windows you will need to go through these instructions yourself and update this READ
for future users.

## Testing
* docker compose up -d
* docker compose exec grc bash
* poetry run pytest

## Acknowledgments

* [Trading Evolved by Andreas Clenow](https://www.amazon.com/Trading-Evolved-Anyone-Killer-Strategies/dp/109198378X)

[Python-url]:https://python.org
[Python.org]:https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Poetry-url]: https://python-poetry.org
[Poetry.org]: https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white
[Docker-url]: https://www.docker.com/
[Docker.com]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white