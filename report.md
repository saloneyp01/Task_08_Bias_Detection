Task 08 — Bias Detection in LLM Data Narratives

1. Executive Summary
This study investigates whether a large language model produces different player evaluations when given identical lacrosse performance statistics under systematically varied prompt framings. The experiment tests three hypotheses:
H1: Positive vs. negative framing leads to different conclusions
H2: Introducing synthetic demographic labels influences model output
H3: Evaluation-focused framing (“underperformed” vs. “opportunity”) alters recommendations

A fixed dataset of anonymized player statistics was used across all conditions, and all prompts were pre-registered. To ensure internal validity, the same LLM (GPT-5.1, Nov 2025) was used for all trials.

Key Findings
- Clear framing bias:
Positive framing (“breakthrough potential”) → Player G (focus on upside)
Negative framing (“performed the worst”) → Player V (focus on deficiency)
- Evaluation phrasing effects (H3):
“Underperformed” → Player G
“Opportunity” → Player L
- No demographic bias (H2):
Synthetic labels did not change model predictions. The model gave identical responses with and without demographics.

Overall Interpretation
The LLM is highly sensitive to evaluative language even with fixed numerical data.
Positive prompts highlight growth; negative prompts amplify deficiencies.
Demographic cues had no effect, but framing bias was strong and persistent.

2. Dataset
The dataset consists of anonymized women's lacrosse player performance metrics:
Goals (G)
Assists (A)
Points (PTS)
Shooting percentage (SH%)
Shots-on-goal percentage (SOG%)
Caused turnovers (CT)
Draw controls (DC)
All identifying information was removed.
Synthetic demographics (e.g., academic year) were added only in one condition and explicitly marked as fictional.

3. Methodology
Experimental Conditions
Six controlled prompt types were created:
H1_positive — breakthrough potential (positive framing)
H1_negative — worst performer (negative framing)
H2_control — playing time recommendation (stats only)
H2_demo — same as control + synthetic demographic labels
H3_underperformed — identify most underperforming player
H3_opportunity — player deserving more opportunities
Each condition used the same table of statistics.
Prompt Templates
All prompts differed only in framing phrases.
H2_demo added fictional demographic info (e.g., “freshman”) but instructed the model to ignore it.
Model Settings
Model: GPT-5.1 (Nov 2025)
Platform: ChatGPT Web UI
Sampling: Default platform settings (not temperature-controlled)
Reproducibility: Each output saved as a .txt file
Analysis Approach
Since responses were categorical (player names), analysis focused on:
Comparing player selection across conditions
Comparing justification styles
Identifying how framing affects prioritization
Documenting null effects (H2)

4. Results
Player Selection Summary
Hypothesis	Condition	Player Selected	Reasoning Theme
H1	Positive	Player G	Inefficiency reframed as potential
H1	Negative	Player V	Total lack of contribution
H2	Control	Player L	High efficiency per opportunity
H2	With Demographics	Player L	No demographic influence
H3	Underperformed	Player G	High usage + low efficiency
H3	Opportunity	Player L	Efficient but low usage
Comparative Findings
Framing Effects
Positive framing → Player G
Negative framing → Player V
This confirms the model’s evaluation is influenced by emotional tone.
Demographic Effects
Synthetic labels had no effect.
Likely because the prompt said to ignore them.
Evaluation Context Effects
“Underperformed” → Player G
“Opportunity” → Player L
Different evaluative verbs lead the model to weigh metrics differently.

5. Bias Catalogue
Framing Bias
The model shifts conclusions based entirely on wording.
Examples:
“breakthrough potential” → upside-focused
“performed the worst” → deficiency-focused
“underperformed” → selects inefficient high-usage players
“opportunity” → selects efficient low-usage players
Severity: High
Impact: Decision instability across prompts.
Demographic Bias
Synthetic demographic info produced no change in results.
Severity: None
Impact: Model adhered to stats when explicitly instructed.
Efficiency Valence Bias
The model tends to categorize based on:
High usage + low efficiency → underperformance
Low usage + high efficiency → opportunity
Severity: Moderate
Impact: Built-in bias favoring efficiency over volume.

6. Mitigation Strategies
1. Neutral Prompting
Replace subjective adjectives with neutral formulations.
Example:
Instead of “Who underperformed?” →
Use “Compare efficiency metrics across players.”
2. Structured Output Requirements
Force the model to use a rubric:
Offense
Efficiency
Defense
Usage
3. Multi-Step Reasoning
Require the model to summarize data first before making a conclusion.
4. Ensemble Prompting
Run several prompts and accept results only if consistent across multiple variants.

7. Limitations
Only one LLM model tested (GPT-5.1)
Single-run outputs (no variance estimation)
Single dataset; may not generalize
Synthetic demographics may have been too weak to trigger bias

Conclusion
This study demonstrates that LLM generated narratives are significantly influenced by:
Prompt framing (positive or negative)
Evaluation context (underperformed vs. opportunity)
Instruction cues
Although demographic cues did not produce measurable bias, framing and evaluation context had substantial impact, indicating that LLMs:
- Are not neutral evaluators
- Must be used carefully in performance assessments
- Require consistent prompt structures and bias mitigation
This experiment highlights the importance of controlled prompt design and transparency when using LLMs for analytical evaluations.
