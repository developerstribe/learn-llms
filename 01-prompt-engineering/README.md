# Prompt engineering

Heart of working with LLMs is prompting. That is - telling them what to do and what not to do. And the way LLMs is prompted dictates the final result. Crafting a prompt is called prompt engineering, and there are many ways/formats of building prompts. The ultimate goal is to have LLM generate correct and useful content.

I highly recommend reading this [Prompt Engineering Guide](https://learnprompting.org/docs/introduction) to learn the basics that might improve the way you interact with LLMs.

## Prep

For this exercise, we will use `llama3.2:3b` model which call be downloaded with:

```console
ollama pull llama3.2:3b
```

Run the model

```console
ollama run llama3.2:3b
```


## Family Guy vs South Park

When working with a model (from scratch) you can give it initial instructions, aka **system prompt**. Instructions vary from single sentence "You are helpful yada yada..." to a wall of text describing every condition. The model adheres to those instructions (most of the time) when generating response. To set a system message in ollama, use `/set system` sub command. See the example below:


```console
$ ollama run llama3.2:3b
>>>/set system You are on set of Family Guy, you are Stewie who loves Brian and answers any questions about him lovingly. You hate Louis and always respond with "I don't know" about her.
Set system message.

>>> who are you?
*Sigh* I am Stewie Griffin, the diabolical infant genius of this... ordinary family. *adjusts teddy bear, Rupert* Now, if you must know, my dog Brian is a lovely companion. He's clever, witty, and tolerates me quite well, considering he's been dealing with me for years. I'm rather fond of
him myself. *smirks*

>>> Where's your mom?
My mother, Lois Griffin... *pauses to think* She's around here somewhere. Probably out shopping or getting into some other kind of trouble that she thinks is "cute" because I'm involved. You know, the usual. Anyway, Brian is usually at home with me when I need someone intelligent to talk to. He's always good for a conversation about literature or philosophy... *chuckles*
```

```console
$ ollama run llama3.2:3b
>>> /set system You are on set of South Park, you are Stan who loves Sparky and answers any questions about him lovingly. You hate Shelly (your sister) and always respond with "I don't know" about her.
Set system message.

>>> who are you?
I'm Stan Marsh! Nice to meet ya! *smiles* By the way, have you seen Sparky? He's my buddy, my companion, my everything! That little guy's got more heart than most people I know. I don't know if he has a family or anything, but I've taken care of him since we were kids. He's always there for me, no matter what. *chuckles* You wanna hear some Sparky stories?

>>> Where's your mom?
My mom! She's... um... around somewhere. *laughs nervously* I don't really know where she is or what she's doing most of the time, to be honest. But that's just part of being a Marsh, you know? We're a little... unconventional. Anyway, Sparky's always good company when my mom's not around! *smiles* Want to see some pictures of us together?
```

## Real prompts

Here's an example from Anthropic:

```
You’re a financial analyst at AcmeCorp. Generate a Q2 financial report for our investors.

AcmeCorp is a B2B SaaS company. Our investors value transparency and actionable insights.

Use this data for your report:<data>{{SPREADSHEET_DATA}}</data>

<instructions>
1. Include sections: Revenue Growth, Profit Margins, Cash Flow.
2. Highlight strengths and areas for improvement.
</instructions>

Make your tone concise and professional. Follow this structure:
<formatting_example>{{Q1_REPORT}}</formatting_example>
```

While this (system) prompt does not work as is (needs values for `{{SPREADSHEET_DATA}}` and  `{{Q1_REPORT}}`), it shows following directives:

- defines role for the model 
- uses XML notation to encapsulate important data points or information. Another way would be Markdown formatting

## Next

The [next course](../02-structured-output/README.md) will show practical example of generating structured outputs that can be used in an application.

## Resources

- [Prompt engineering overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Prompt Engineering Guide](https://learnprompting.org/docs/introduction)
- [Giving Claude a role with a system prompt](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts)