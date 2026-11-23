# The words on the sunriser page

Every text on the page has a `##` line with its name. The text sits under it.
Change the text. Leave the `##` lines as they are.

Then commit and push. GitHub builds the page from this file and publishes it.
To look before you push, run `python3 build.py` and open `index.html`.
The `index.html` in the repo may show older text. The build fills in the new text.

- `` `word` `` shows as code. `*word*` shows as highlighted. No other markdown works.
- A line that starts with one `#` is only a divider, like this title.
- "(fits 60)" after a name means about 60 characters fit before the line wraps.

# Browser tab and search result

## title
Sunriser: Secure your ADLC

## description
sunriser sits between your coding agent and its MCP servers. It hides the tools you deny and logs every call, so you can check later what the agent did.

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
Drain node pool b, then restart the api.

## chat-agent
Called *node_management* to drain. It returned *blocked by policy*, so I stopped there. Restarting the api without a drain needs your call.

## chat-ask
Ask your agent anything…

# Setup steps

## step1-title
Give your MCP server a name.

## step1
Keep the MCP server you already run. Put its command in this file, with the tools the agent shouldn't get.

## step2-title
Point your agent at that name.

## step2
That's the only change to the agent's config. You can edit the deny list later without touching it again.

## any-1
the command the client runs

## any-2
no config file? pass it inline

# Why the agent can't skip the rules

## agents
The agent can't skip your rules

## agents-sub (fits 60)
The rules sit outside the agent, where no prompt can reach.

## agents-text
Make the rules external managed, not in .md files.

## agents-mcp
Lets the agent ask sunriser questions, such as what ran on a server last week.

## agents-skill
Tells agents what action they cannot do, so they know in advance.

# The product cards

## products
The four parts of sunriser

## card-guard (fits 110)
Per-tool, per-action control for MCP servers. Denied actions leave the tool list, and every call is logged.

## card-sky (fits 110)
A platform as a service for your apps. Build, Deploy, and Maintain with it.

## card-warrant (fits 110)
A single-purpose, least-privilege identity per agent. It limits the blast radius and holds none of your keys.

## card-hub (fits 110)
A collector you host. It gathers agent telemetry from all your machines and tells you what to upgrade and why.

# Guard

## guard-sub (fits 60)
It protects you from unwanted actions.

## guard-wrap
Guard sits in front of any MCP server that speaks stdio. It removes the tools you deny from the tool list, so the agent doesn't see them. If the agent calls one anyway, it gets "blocked by policy" back and nothing runs.

## guard-audit
Guard writes each call as one line of JSON: who asked, which tool, whether it was allowed, and how long it took. You can filter the log by tool, server or time.

## guard-verify
Every line includes the hash of the line before it. If someone changes or removes a line, `audit verify` points to the first one.

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
The name the agent gave in its MCP handshake.

## field-decision
Either allowed or blocked, according to your deny list.

## field-agent
The pid of the process that started the wrap. All servers from one agent session share it.

## field-prev
The hash of the previous line, which chains the log together.

## field-head
Printed by `verify`. Save it where the agent can't reach it, then compare it the next time you verify.

# Sky

## sky-sub (fits 60)
Simplified way to ship, scale, and monitor your apps on any Kubernetes cluster securely.

## sky-deploy
Builds your app with a buildpack, pushes the image and runs it on your Kubernetes cluster. You don't need a Dockerfile or YAML.

## sky-scale
Sets how many copies of each process run.

## sky-logs
Shows the app's logs. When a pod can't run, Sky records an incident on the app.
# Warrant

## warrant-sub (fits 60)
Agent should have their own pass ticket to do something.

## warrant-view
Read-only access to one namespace. Every agent starts here.

## warrant-deploy
Can roll out new versions, but only in the namespace it's bound to.

## warrant-operate
For day-two work such as scaling and restarts.

## warrant-as
Guard starts the server under that identity with a short-lived token. Every call in the log shows who it ran as.

# Hub

## hub-sub (fits 60)
Your help to upgrade your systems.

## hub-title
Self-hosted collector

## hub
Once agents run on more than one machine, Hub collects their logs into one record. You host it yourself, so the logs stay inside your network.

## advisories-title
What to upgrade and why

## advisories
Hub checks one list against what you run: CVEs that are being exploited, versions past end-of-life, upgrades known to break things, and MCP tools that are risky to allow. Each finding is a YAML file in a public repo, and anyone can add one.

## out-title
What stays out

## out
There won't be a marketplace or a hosted service. sunriser doesn't score risk and doesn't collect telemetry.

# Bottom of the page

## footer
Open source soon
