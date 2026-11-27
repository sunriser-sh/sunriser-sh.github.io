# The words on the sunriser page

Every text on the page has a `##` line with its name. The text sits under it.
Change the text. Leave the `##` lines as they are.

Then commit and push. GitHub builds the page from this file and publishes it.
To look before you push, run `python3 build.py`, then `python3 -m http.server`.
Open http://localhost:8000. The pages in the repo may show older text. The build fills in the new text.

- `` `word` `` shows as code. `*word*` shows as highlighted. No other markdown works.
- A line that starts with one `#` is only a divider, like this title.
- "(fits 60)" after a name means about 60 characters fit before the line wraps.

# Sunriser page: browser tab and search result

## title
Sunriser: Secure your ADLC

## description
A Continuous-Security Approach for AI SDLC. Sunriser helps secure systems continuously as models, data, dependencies, and deployment environments evolve.

# Top of the page

## hero (fits 30)
A Continuous-Security Approach for AI SDLC

## hero-sub (fits 30)
Sunriser helps secure systems continuously as models, data, dependencies, and deployment environments evolve

## soon
The source will be public soon.

## hero-credit (shows when the pointer is over the picture)
Claude Monet, Impression, Sunrise, 1872

# The chat next to the terminal

## chat-user
Open a PR for the login fix, then merge it.

## chat-agent
The PR is open. I called *merge_pull_request*. It returned *blocked by policy*, so I stopped there. Merging needs your call.

## chat-ask
Ask your agent anything…

# Setup steps

## step1-title
Put sunriser in front of your agent's MCP servers and CLI tools

## adopt-1
Claude Code, Cursor, Pi, Claude Desktop, Windsurf and VS Code.

## adopt-2
Wrap your agent with sunriser.

## any-2
inline config

## cli-1 (the CLI tools tab)
Claude Code: gh, kubectl, terraform and every other shell command go through guard.

## cli-2
The same for pi.

## step2-title
Choose preset rules or custom rules

## preset-1
apply the ruleset

## custom-1
block tools by name

## custom-2
or only when its arguments match

## custom-3
ask what the rules would do with one call

## allow-1 (the Allow list tab)
only these tools get through, new ones stay blocked

## clirules-1 (the CLI rules tab)
block shell commands by pattern

# Why the agent can't skip the rules

## agents
Rules enforced outside your agent

## agents-sub (fits 60)
Deterministic checks on every tool call

## agents-text
Make the rules external managed, not in .md files.

## agents-mcp
Lets agents read the rules and the audit log.

## agents-skill
Tells agents what action they cannot do, so they know in advance.

# The product cards

## products
The three parts of sunriser

## card-guard (fits 110)
Action Guardrails for your MCP servers and CLI tools. Blocks unneeded agent actions and audits every call.

## card-warrant (fits 110)
Least-privilege identity for each agent. Short-lived access that limits the blast radius.

## card-hub (fits 110)
Self-hosted collector for your agent telemetry. Tells you what to upgrade and why.

# Guard

## guard-sub (fits 60)
Action Guardrails to automated prevention by blocking unneeded agent actions

## trace-1 (first line of the timeline heading)
One agent run.

## trace-2 (second line)
Every tool call visible.

## trace-text
See what your agent tried, what ran, and where policy stepped in before it reached your systems.

## trace-title (the line above the timeline)
Every action passes through policy

## guard-wrap
Guard wraps your MCP servers and hooks your agent's shell.

## guard-audit
Guard audits every tool call your agents make, and every rule change, even one made by hand.

## guard-verify
Guard verifies your log chain has not been tampered with. Seal it with your SSH key so a rewrite shows.

# The orange block

## sun-1 (fits 31)
One binary that keeps your

## sun-2 (fits 31)
AI SDLC secure as models evolve

## sun-text
Controllable and auditable.

# The log line

## log
Every action is audited

## log-sub (fits 60)
A searchable log chain records who did what and when.

## field-client
The name the agent reports for itself.

## field-decision
Allowed or blocked by your rules.

## field-agent
The agent process that started the call.

## field-prev
The hash of the previous line. It chains the log.

## field-head
Printed by `verify`. Keep it away from your agent and check it next time with `verify --head`.

# Warrant

## warrant-sub (fits 60)
Agent should have their own pass ticket to do something.

## warrant-view
Read-only access to one namespace. Every agent starts here.

## warrant-deploy
Roll out new versions in one namespace.

## warrant-operate
Day-two operations: scaling and restarts.

## warrant-as
Guard runs your MCP server under a warrant. Every call is audited with its identity.

# Hub

## hub-sub (fits 60)
Your help to upgrade your systems.

## hub-title
Self-hosted collector

## hub
Collects audit logs from all your machines into one record. Self-hosted, so your logs stay in your network.

## advisories-title
What to upgrade and why

## advisories
Checks your systems for exploited CVEs, end-of-life versions, breaking upgrades, and risky MCP tools. Advisories are YAML files in a public repo, open to anyone.

## out-title
What stays out

## out
Sunriser is not a marketplace or a hosted service. It does not score risk or collect your telemetry.

# Nightstar page

## title-nightstar
Nightstar: ship your apps on any Kubernetes cluster

## description-nightstar
PaaS solution for Kubernetes

## nightstar-sub (fits 60)
PaaS solution for Kubernetes

## nightstar-deploy
Ship your app to your Kubernetes cluster without a Dockerfile or YAML.

## nightstar-scale
Scale each process of your app.

## nightstar-logs
Monitor your app with logs and incidents.

## ns-step1-title
Install the CLI

## ns-step1-note
The installer opens with the first release.

## ns-step2-title
Deploy your first app

## ns-deploy-1
In any app folder with a Procfile. Detects the stack and writes the config.

## ns-deploy-2
Creates a local cluster, builds your app, and waits until it runs.

## ns-deploy-3
See it in the browser.

# Every page: bottom

## footer
Open source soon
