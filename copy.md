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
sunriser: a guard for agents that run your infrastructure

## description
sunriser sits between your coding agent and its MCP servers. It hides the tools you deny and logs every call, so you can check later what the agent did.

# Top of the page

## hero (fits 50)
A Continuous-Security Approach for AI SDLC

## hero-sub (fits 60)
Sunriser helps securing systems continuously as models, data, dependencies, and deployment environments evolve

## soon
The source will be public soon.

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

# The five product cards

## products
The five parts of sunriser

## products-sub (fits 60)
Guard is in preview. The other four are still being built.

## card-guard (fits 110)
A proxy that sits in front of any MCP server. It hides the tools you deny and logs every call in a hash chain.

## card-warrant (fits 110)
Gives each agent a short-lived Kubernetes warrant for one role. The agent never holds your real credentials.

## card-hub (fits 110)
A collector you host yourself. It pulls the audit logs from all your machines into one record.

## card-advisories (fits 110)
A list of what to upgrade and why: exploited CVEs, end-of-life versions and risky MCP tools in what you run.

## card-sky (fits 110)
Runs the apps your agents build, straight from a git push. Each deploy runs under a warrant.

# Guard

## guard-sub (fits 60)
The agent can't see denied tools, and every call is logged.

## guard-wrap
Guard sits in front of any MCP server that speaks stdio. It removes the tools you deny from the tool list, so the agent doesn't see them. If the agent calls one anyway, it gets "blocked by policy" back and nothing runs.

## guard-audit
Guard writes each call as one line of JSON: who asked, which tool, whether it was allowed, and how long it took. You can filter the log by tool, server or time.

## guard-verify
Every line includes the hash of the line before it. If someone changes or removes a line, `audit verify` points to the first one.

# The orange block

## sun-1 (fits 27)
One binary on your machine.

## sun-2 (fits 27)
Nothing phones home.

## sun-text (fits 60)
You don't need an account. The log is a file on your disk.

# The log line

## log
Every call is one line of JSON

## log-sub (fits 60)
It records what happened, in lines jq and grep can read.

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

# Warrant

## warrant-sub (fits 60)
The agent works with a warrant instead of your keys.

## warrant-view
Read-only access to one namespace. Every agent starts here.

## warrant-deploy
Can roll out new versions, but only in the namespace it's bound to.

## warrant-operate
For day-two work such as scaling and restarts.

## warrant-as
Guard starts the server under that identity with a short-lived token. Every call in the log shows who it ran as.

# Hub and advisories

## hub-sub (fits 60)
One log for all your machines, and a list of what to upgrade.

## hub-title
Self-hosted collector

## hub
Once agents run on more than one machine, Hub collects their logs into one record. You host it yourself, so the logs stay inside your network.

## advisories-title
What to upgrade and why

## advisories
Advisories checks one list against what you run: CVEs that are being exploited, versions past end-of-life, upgrades known to break things, and MCP tools that are risky to allow. Each finding is a YAML file in a public repo, and anyone can add one.

## out-title
What stays out

## out
There won't be a marketplace or a hosted service. sunriser doesn't score risk and doesn't collect telemetry.

# Sky

## sky-sub (fits 60)
Sky runs the apps your agents ship, under the same rules.

## sky-deploy
Push a repo and a buildpack turns it into a bundle, which then runs on a beam. You don't need a Dockerfile.

## sky-scale
A beam is the unit of compute. You add or remove beams with one command.

## sky-logs
Shows app output together with every deploy, scale and config change. Each change says which agent made it.

## sky-enclave
A private network for apps that must be kept apart from the rest. To deploy into one, an agent needs a warrant bound to that enclave.

# For agents

## agents
Agents can read it too

## agents-sub (fits 60)
The proxy enforces the rules, whatever the prompt says.

## agents-text
An agent can forget a rule in `CLAUDE.md`, but it can't call a tool that isn't in its list. The log is also the agent's memory: it can read back what it did.

## agents-mcp
An MCP server over stdio. Before an agent runs anything new, it can ask what ran against a server last week.

## agents-skill
Tells Claude Code and Cursor what's blocked, so they know before they try.

## agents-commands
Lists every command and flag, for tools that build on sunriser.

## agents-json
With this flag, stdout is one JSON document. Exit code 0 is ok, 1 is your mistake and 2 is the machine's.

# Bottom of the page

## closing (fits 45)
Guard will be the first part to go public.

## closing-sub (fits 60)
Setting it up takes one line in your agent config.

## footer
Open source soon
